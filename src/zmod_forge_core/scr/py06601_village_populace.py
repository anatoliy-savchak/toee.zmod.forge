import toee, ctrl_behaviour, utils_item, utils_obj, const_toee, factions_zmod, utils_npc, const_animate
import const_proto_armor, const_proto_weapon, const_proto_food, const_proto_cloth, const_proto_containers, const_proto_list_weapons, const_proto_list_scrolls, const_proto_list_cloth
import random, debug, math

MODULE_SCRIPT_ID = 6601

def san_start_combat(attachee, triggerer):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(triggerer, toee.PyObjHandle)
	ctrl = ctrl_behaviour.CtrlBehaviour.get_from_obj(attachee)
	if (ctrl):
		return ctrl.start_combat(attachee, triggerer)
	return toee.RUN_DEFAULT

def san_dialog(attachee, triggerer):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(triggerer, toee.PyObjHandle)
	ctrl = ctrl_behaviour.CtrlBehaviour.get_from_obj(attachee)
	if (ctrl):
		return ctrl.dialog(attachee, triggerer)
	return toee.RUN_DEFAULT

def san_heartbeat(attachee, triggerer):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(triggerer, toee.PyObjHandle)
	ctrl = ctrl_behaviour.CtrlBehaviour.get_from_obj(attachee)
	if (ctrl):
		#print("heartbeat {}".format(attachee))
		return ctrl.heartbeat(attachee, triggerer)
	else: 
		print("ctrl not found for {}".format(attachee))
	return toee.RUN_DEFAULT

class CtrlVillagePersonRandom(ctrl_behaviour.CtrlBehaviour):
	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		#npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		npc.faction_add(factions_zmod.FACTION_NEUTRAL_NPC)
		utils_item.item_clear_all(npc)

		self.make_up(npc)
		self.dress_up(npc)
		return

	def make_up(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		gender = npc.obj_get_int(toee.obj_f_critter_gender)
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		if (gender == toee.gender_female):
			hairStyle.style = const_toee.hair_styles_human_woman[toee.game.random_range(0, len(const_toee.hair_styles_human_woman)-1)]
		else: hairStyle.style = const_toee.hair_styles_human_gentleman[toee.game.random_range(0, len(const_toee.hair_styles_human_gentleman)-1)]
		hairStyle.color = const_toee.hair_colors_human[toee.game.random_range(0, len(const_toee.hair_colors_human)-1)]
		hairStyle.update_npc(npc)

		# need to recheck
		if (1):
			height = 100
			if (gender == toee.gender_female):
				height = int(160/180*100 - 20 + toee.game.random_range(1, 20))
			else:
				height = int(100 - 20 + toee.game.random_range(1, 20))
			npc.obj_set_int(toee.obj_f_critter_height, height)
		return

	def dress_up(self, npc):
		# create inventory
		robe = toee.game.random_range(const_proto_cloth.PROTO_CLOTH_GARB_VILLAGER_BLUE, const_proto_cloth.PROTO_CLOTH_GARB_VILLAGER_RED)
		if (robe):
			utils_item.item_create_in_inventory(robe, npc, 1, 1)
		if (npc.obj_get_int(toee.obj_f_critter_gender) == toee.gender_male):
			cloak = const_proto_list_cloth.PROTO_CLOTH_CLOAKS[toee.game.random_range(0, len(const_proto_list_cloth.PROTO_CLOTH_CLOAKS)-1)]
			if (cloak):
				utils_item.item_create_in_inventory(cloak, npc, 1, 1)
				utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_CIRCLET_HOODLESS, npc, 1, 1)
		utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_BLACK, npc, 1, 1)
		npc.item_wield_best_all()
		return

class CtrlVillageManRandom(CtrlVillagePersonRandom):
	@classmethod
	def get_proto_id(cls):
		return 14702

class CtrlVillageWomanRandom(CtrlVillagePersonRandom):
	@classmethod
	def get_proto_id(cls):
		return 14703

class CtrlVillageAnimal(ctrl_behaviour.CtrlBehaviour):
	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		utils_obj.obj_scripts_clear(npc)
		utils_item.item_clear_all(npc)
		npc.faction_add(factions_zmod.FACTION_WILDERNESS_INDIFFERENT)
		return

class CtrlVillageAnimalPig(CtrlVillageAnimal):
	@classmethod
	def get_proto_id(cls):
		return 14368

class CtrlVillageAnimalChecken(CtrlVillageAnimal):
	@classmethod
	def get_proto_id(cls):
		return 14362

class CtrlVillageAnimalFarmDog(CtrlVillageAnimal):
	@classmethod
	def get_proto_id(cls):
		return 14048

class VillagePlaces:
	TAVERN_PORCH = (488, 466) # 10 ft before entrance
	TAVERN_DOORSTEP = (488, 463) # 0 ft before entrance
	TAVERN_ENTRY = (488, 461) # 5 ft after entrance
	BORDER_WEST_ENTRY = (505, 472) # 5 ft after west (of tavern) border
	VILLAGE_SQUARE_WEST_ENTRANCE = (492, 470) # 5 ft after far west (of fontain)
	VILLAGE_SQUARE_NORTH_ENTRANCE = (469, 464) # 5 ft after far north (of fontain)
	VILLAGE_SQUARE_SOUTH_ENTRANCE = (469, 497) # 5 ft after far south (of fontain)
	VILLAGE_SQUARE_CORNER_WEST_NORTH = (492, 464)
	VILLAGE_SQUARE_CORNER_WEST_SOUTH = (493, 389)
	VILLAGE_SQUARE_CORNER_EAST_NORTH = (465, 464)
	VILLAGE_SQUARE_CORNER_EAST_SOUTH = (465, 491)
	CHURCH_PORCH = (494, 487) # 10 ft before entrance
	CHURCH_DOORSTEP = (494, 490) # 0 ft before entrance
	CHURCH_ENTRY = (493, 492) # 5 ft after entrance
	CHURCH_CORNER_WEST_NORTH = (498, 491) 
	CHURCH_CORNER_EAST_NORTH = (490, 491) 
	CHURCH_CORNER_AISLE_WEST_SOUTH = (498, 501) 
	CHURCH_CORNER_AISLE_EAST_SOUTH = (490, 501) 
	CHURCH_TRANSEPT_CENTER = (495, 502)

	GENERAL_STORE_PORCH = (479, 493) # 10 ft before entrance
	GENERAL_STORE_DOORSTEP = (479, 496) # 0 ft before entrance
	GENERAL_STORE_ENTRY = (479, 498) # 5 ft after entrance
	GENERAL_STORE_STAND_1 = (483, 498)
	GENERAL_STORE_STAND_2 = (476, 499)
	GENERAL_STORE_STAND_3 = (483, 501)
	GENERAL_STORE_BEFORE_COUNTER = (478, 504)

	@staticmethod
	def scene_church_prey(wp, num):
		assert isinstance(wp, list)
		assert isinstance(num, int)
		wp.append(utils_npc.Waypoint(VillagePlaces.CHURCH_PORCH[0], VillagePlaces.CHURCH_PORCH[1], const_toee.rotation_0500_oclock, 0))
		wp.append(utils_npc.Waypoint(VillagePlaces.CHURCH_TRANSEPT_CENTER[0], VillagePlaces.CHURCH_TRANSEPT_CENTER[1], const_toee.rotation_0500_oclock, 5000, utils_npc.WaypointFlag.Delay | utils_npc.WaypointFlag.Animate \
			, 32 + const_animate.NormalAnimType.Conceal, 32 + const_animate.NormalAnimType.ConcealIdle, 32 + const_animate.NormalAnimType.Unconceal))

		x, y = VillagePlaces.get_random_church_stand()
		wp.append(utils_npc.Waypoint(x, y, const_toee.rotation_0500_oclock, 5000, utils_npc.WaypointFlag.Delay | utils_npc.WaypointFlag.Animate | utils_npc.WaypointFlag.FixedRotation \
			, 32 + const_animate.NormalAnimType.Examine, 32 + const_animate.NormalAnimType.FeatTrack))
		return

	@staticmethod
	def get_random_store_stand():
		r = toee.game.random_range(1, 3)
		if (r == 2): return VillagePlaces.GENERAL_STORE_STAND_2
		if (r == 3): return VillagePlaces.GENERAL_STORE_STAND_3
		return VillagePlaces.GENERAL_STORE_STAND_1

	@staticmethod
	def get_random_church_stand():
		x = VillagePlaces.CHURCH_CORNER_AISLE_EAST_SOUTH[0] - 1 + toee.game.random_range(1, VillagePlaces.CHURCH_CORNER_AISLE_WEST_SOUTH[0] - VillagePlaces.CHURCH_CORNER_AISLE_EAST_SOUTH[0])
		y = VillagePlaces.CHURCH_CORNER_EAST_NORTH[1] - 1 + toee.game.random_range(1, VillagePlaces.CHURCH_CORNER_AISLE_EAST_SOUTH[1] - VillagePlaces.CHURCH_CORNER_EAST_NORTH[1])
		return x, y

	@staticmethod
	def scene_general_store(wp, num):
		assert isinstance(wp, list)
		assert isinstance(num, int)
		wp.append(utils_npc.Waypoint(VillagePlaces.GENERAL_STORE_PORCH[0], VillagePlaces.GENERAL_STORE_PORCH[1], const_toee.rotation_0500_oclock, 0))
		stand_count_to_examine = toee.game.random_range(1, 10)
		#stand_count_to_examine = 3
		for i in range(1, stand_count_to_examine):
			stand_coords = VillagePlaces.get_random_store_stand()
			wp.append(utils_npc.Waypoint(stand_coords[0], stand_coords[1], const_toee.rotation_0500_oclock, 1000, utils_npc.WaypointFlag.Delay | utils_npc.WaypointFlag.Animate | utils_npc.WaypointFlag.FixedRotation \
				, 32 + const_animate.NormalAnimType.Examine))

		wp.append(utils_npc.Waypoint(VillagePlaces.GENERAL_STORE_BEFORE_COUNTER[0], VillagePlaces.GENERAL_STORE_BEFORE_COUNTER[1], const_toee.rotation_0500_oclock, 1000, utils_npc.WaypointFlag.Delay | utils_npc.WaypointFlag.Animate | utils_npc.WaypointFlag.FixedRotation \
			, 32 + const_animate.NormalAnimType.Picklock))
		return

	@staticmethod
	def scene_wander_square(wp, num):
		assert isinstance(wp, list)
		assert isinstance(num, int)
		for i in range(0, toee.game.random_range(5, 10)):
			stand_coords = VillagePlaces.get_random_sqare_place()
			wp.append(utils_npc.Waypoint(stand_coords[0], stand_coords[1], const_toee.rotation_0500_oclock, 5000 * toee.game.random_range(1, 10), utils_npc.WaypointFlag.Delay | utils_npc.WaypointFlag.Animate \
				, 32 + const_animate.NormalAnimType.Examine))
		return

	@staticmethod
	def get_random_sqare_place():
		x = VillagePlaces.VILLAGE_SQUARE_CORNER_EAST_NORTH[0] - 1 + toee.game.random_range(1, VillagePlaces.VILLAGE_SQUARE_CORNER_WEST_NORTH[0] - VillagePlaces.VILLAGE_SQUARE_CORNER_EAST_SOUTH[0])
		y = VillagePlaces.VILLAGE_SQUARE_CORNER_WEST_NORTH[1] - 1 + toee.game.random_range(1, VillagePlaces.VILLAGE_SQUARE_CORNER_EAST_SOUTH[1] - VillagePlaces.VILLAGE_SQUARE_CORNER_WEST_NORTH[1])
		if (x >= 473 and x <= 478 and y >= 477 and y <= 482):
			return VillagePlaces.get_random_sqare_place()
		return x, y

class CtrlVillageRandomWanderer(CtrlVillagePersonRandom):

	def make_day_route(self, npc):
		crowd_place = self.get_var("crowd_place")
		waypoints = list()
		if (not crowd_place is None):
			waypoints.append(utils_npc.Waypoint(crowd_place[0], crowd_place[1], const_toee.rotation_0500_oclock, 1000 * toee.game.random_range(1, 10), utils_npc.WaypointFlag.Delay | utils_npc.WaypointFlag.FixedRotation))
		else:
			self.make_interest_route(waypoints)

		npc.npc_waypoints_set(waypoints)
		npc.npc_flag_set(toee.ONF_WAYPOINTS_DAY)
		npc.npc_flag_unset(toee.ONF_WAYPOINTS_NIGHT)
		return

	def make_interest_route(self, waypoints):
		#attachee.obj_set_int(toee.obj_f_npc_waypoint_current, 0)
		x, y = VillagePlaces.get_random_sqare_place()
		waypoints.append(utils_npc.Waypoint(x, y, const_toee.rotation_1100_oclock, 1000 * toee.game.random_range(1, 10), utils_npc.WaypointFlag.Delay))

		#VillagePlaces.scene_wander_square(waypoints, 1)
		steps = list(range(3))
		steps_random = random.sample(steps, len(steps))
		for step in steps_random:
			if (step == 0):
				#VillagePlaces.scene_wander_square(waypoints, 1)
				pass
			elif (step == 1):
				VillagePlaces.scene_church_prey(waypoints, 1)
			elif (step == 2):
				VillagePlaces.scene_general_store(waypoints, 1)
		return

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		super(CtrlVillageRandomWanderer, self).after_created(npc)
		npc.scripts[const_toee.sn_heartbeat] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		return

	@classmethod
	def get_proto_id(cls):
		if (toee.game.random_range(0, 1)): return 14702 # man
		return 14703 # woman

	@staticmethod
	def find_manwoman_in_radius(npc, radius_ft, except_self):
		assert isinstance(npc, toee.PyObjHandle)
		result = list()
		for obj in toee.game.obj_list_range(npc.location, radius_ft, toee.OLC_NPC):
			if (except_self and obj == npc): continue
			if (obj.proto in (14703, 14702)):
				result.append(obj)
		return result

	def talked_to(self, triggerer, talk_to, message):
		return

	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		#debug.breakp("")
		attachee.anim_goal_interrupt()
		#if (attachee.npc_flags_get() & toee.ONF_WAYPOINTS_DAY):
		#	attachee.npc_flag_unset(toee.ONF_WAYPOINTS_DAY)
		#	attachee.npc_flag_unset(toee.ONF_WAYPOINTS_NIGHT)
		#	attachee.obj_set_int(toee.obj_f_npc_waypoint_current, 0)
		#	attachee.npc_waypoints_set(list())
		#else:
		#	self.make_day_route(attachee)
		return toee.RUN_DEFAULT

class CtrlVillageRandomWandererPious(CtrlVillageRandomWanderer):
	def make_interest_route(self, waypoints):
		
		x, y = VillagePlaces.get_random_sqare_place()
		waypoints.append(utils_npc.Waypoint(x, y, const_toee.rotation_1100_oclock, 1000 * toee.game.random_range(1, 10), utils_npc.WaypointFlag.Delay))

		subgroup_num = self.get_var("subgroup_num", 0)

		# first go to pre sermon chat
		if (subgroup_num <= 3):
			place_no = subgroup_num % 8
			place = (497, 487)
			rotation = const_toee.rotation_0500_oclock
			if (place_no <= 1):
				place = (498, 485)
				rotation = const_toee.rotation_0500_oclock
			elif (place_no <= 2):
				place = (496, 485)
				rotation = const_toee.rotation_0500_oclock
			elif (place_no <= 3):
				place = (494, 485)
				rotation = const_toee.rotation_0500_oclock
			elif (place_no <= 4):
				place = (494, 487)
				rotation = const_toee.rotation_0900_oclock
			elif (place_no <= 5):
				place = (494, 489)
				rotation = const_toee.rotation_0900_oclock
			elif (place_no <= 6):
				place = (496, 488)
				rotation = const_toee.rotation_0900_oclock
			elif (place_no <= 7):
				place = (498, 488)
				rotation = const_toee.rotation_0300_oclock
			elif (place_no <= 8):
				place = (498, 486)
				rotation = const_toee.rotation_0300_oclock
			waypoints.append(utils_npc.Waypoint(place[0], place[1], rotation, 1000 * toee.game.random_range(1, 10), utils_npc.WaypointFlag.Delay| utils_npc.WaypointFlag.FixedRotation))
			waypoints.append(utils_npc.Waypoint(place[0], place[1], const_toee.rotation_0500_oclock, 1000 * toee.game.random_range(1, 10), utils_npc.WaypointFlag.Delay))
			waypoints.append(utils_npc.Waypoint(place[0], place[1], const_toee.rotation_0500_oclock, 1000 * toee.game.random_range(1, 10), utils_npc.WaypointFlag.Delay))
			waypoints.append(utils_npc.Waypoint(place[0], place[1], const_toee.rotation_0500_oclock, 1000 * toee.game.random_range(1, 10), utils_npc.WaypointFlag.Delay))
		else:
			waypoints.append(utils_npc.Waypoint(497, 487, const_toee.rotation_0500_oclock, 0))

		# then go to the church to pray
		if (1):
			place_no = subgroup_num % 9
			place = (495, 499)
			if (place_no <= 1):
				place = (498, 500)
			elif (place_no <= 2):
				place = (498, 492)
			elif (place_no <= 3):
				place = (497, 494)
			elif (place_no <= 4):
				place = (491, 500)
			elif (place_no <= 5):
				place = (498, 496)
			elif (place_no <= 6):
				place = (491, 492)
			elif (place_no <= 7):
				place = (491, 494)
			elif (place_no <= 8):
				place = (492, 497)
			waypoints.append(utils_npc.Waypoint(place[0], place[1], const_toee.rotation_0500_oclock, 1000 * toee.game.random_range(1, 10), utils_npc.WaypointFlag.Delay | utils_npc.WaypointFlag.Animate | utils_npc.WaypointFlag.FixedRotation \
			, 32 + const_animate.NormalAnimType.FeatTrack))
			waypoints.append(utils_npc.Waypoint(place[0], place[1], const_toee.rotation_0500_oclock, 1000 * toee.game.random_range(1, 10), utils_npc.WaypointFlag.Delay | utils_npc.WaypointFlag.Animate | utils_npc.WaypointFlag.FixedRotation \
			, 32 + const_animate.NormalAnimType.FeatTrack))
			waypoints.append(utils_npc.Waypoint(place[0], place[1], const_toee.rotation_0500_oclock, 1000 * toee.game.random_range(1, 10), utils_npc.WaypointFlag.Delay | utils_npc.WaypointFlag.Animate | utils_npc.WaypointFlag.FixedRotation \
			, 32 + const_animate.NormalAnimType.FeatTrack))
			waypoints.append(utils_npc.Waypoint(place[0], place[1], const_toee.rotation_0500_oclock, 1000 * toee.game.random_range(1, 10), utils_npc.WaypointFlag.Delay | utils_npc.WaypointFlag.Animate | utils_npc.WaypointFlag.FixedRotation \
			, 32 + const_animate.NormalAnimType.FeatTrack))

		# then go to post sermon chat
		if (subgroup_num <= 3):
			place_no = subgroup_num % 8
			place = (497, 487)
			if (place_no <= 1):
				place = (498, 485)
			elif (place_no <= 2):
				place = (496, 485)
			elif (place_no <= 3):
				place = (494, 485)
			elif (place_no <= 4):
				place = (494, 487)
			elif (place_no <= 5):
				place = (494, 489)
			elif (place_no <= 6):
				place = (496, 488)
			elif (place_no <= 7):
				place = (498, 488)
			elif (place_no <= 8):
				place = (498, 486)
			waypoints.append(utils_npc.Waypoint(place[0], place[1], const_toee.rotation_0500_oclock, 1000 * toee.game.random_range(1, 10), utils_npc.WaypointFlag.Delay))
			waypoints.append(utils_npc.Waypoint(place[0], place[1], const_toee.rotation_0500_oclock, 1000 * toee.game.random_range(1, 10), utils_npc.WaypointFlag.Delay))
			waypoints.append(utils_npc.Waypoint(place[0], place[1], const_toee.rotation_0500_oclock, 1000 * toee.game.random_range(1, 10), utils_npc.WaypointFlag.Delay))
			waypoints.append(utils_npc.Waypoint(place[0], place[1], const_toee.rotation_0500_oclock, 1000 * toee.game.random_range(1, 10), utils_npc.WaypointFlag.Delay))
		return

	@classmethod
	def get_proto_id(cls):
		return 14702 # man

	def heartbeat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		if (self.get_var("subgroup_num", 0) <= 3):
			self.cooldown_all()
			init_talk_cooldown = self.get_var("init_talk_cooldown", 6)
			#print("init_talk_cooldown: {} for {}".format(init_talk_cooldown, attachee))

			if (init_talk_cooldown == 0):
				wpc = attachee.obj_get_int(toee.obj_f_npc_waypoint_current)
				if (wpc > 1 and wpc <= 4):
					near_list = CtrlVillageRandomWanderer.find_manwoman_in_radius(attachee, 10, 1)
					if (near_list):
						idx = toee.game.random_range(0, len(near_list)-1)
						talk_to = near_list[idx]
						if (talk_to):
							attachee.turn_towards(talk_to)
							message = "Glory to Pelor!"
							attachee.float_text_line(message, toee.tf_yellow)
							self.vars["init_talk_cooldown"] = 5
							for obj in near_list:
								cobj = ctrl_behaviour.get_ctrl(obj.id)
								if (not cobj): continue
								if (cobj is CtrlVillageRandomWanderer): continue
								assert isinstance(cobj, CtrlVillageRandomWanderer)
								cobj.talked_to(attachee, talk_to, message)
					elif (wpc > 5):
						self.vars["init_talk_cooldown"] = 5

		return toee.RUN_DEFAULT

	def talked_to(self, triggerer, talk_to, message):
		npc = self.npc_get()
		if (not npc): return
		if (message == "Glory to Pelor!"):
			message = "Praise him"
			npc.float_text_line(message, toee.tf_light_blue)
			self.vars["init_talk_cooldown"] = -1
		return

	def time_hour_passed(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		if (npc.object_flags_get() & OF_OFF and toee.game.is_daytime()):
			npc.object_flag_unset(OF_OFF)
			npc.anim_goal_interrupt()
			self.vars["init_talk_cooldown"] = 5
			self.make_day_route(npc)
			print("Turned on: {}".format(npc))

		if (not (npc.object_flags_get() & OF_OFF) and not toee.game.is_daytime()):
			npc.object_flag_set(OF_OFF)
			print("Turned off: {}".format(npc))
		return


class CtrlVillageRandomWandererPiousWoman(CtrlVillageRandomWandererPious):
	@classmethod
	def get_proto_id(cls):
		return 14703

class Scene:
	TEXT_COLOR_NORMAL = toee.tf_yellow

	def do_after_created(self, npc):
		self.scene_stage_next = '0'
		self.scene_stage_heartbeats_left = 0
		self.scene_item_id1 = ''
		self.scene_item_proto1 = 0
		return

	def run_scenes(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		if self.scene_stage_heartbeats_left > 0:
			self.scene_stage_heartbeats_left += -1
			return

		result = None
		if self.scene_stage_next:
			print('Playing scene: {} for {}'.format(self.scene_stage_next, npc))
			scene_func = None
			try:
				scene_func = getattr(self, 'scene_' + self.scene_stage_next)
			except AttributeError:
				print('Scene not found: {}'.format(self.scene_stage_next))
				self.scene_stage_next = ''
				pass
			if scene_func:
				sc = self.scene_stage_next
				self.scene_stage_next = ''
				result = scene_func(npc, sc)

		return result

	def set_next_scene(self, next_name, after_heartbeats):
		self.scene_stage_next = next_name
		self.scene_stage_heartbeats_left = after_heartbeats
		return

	def talk_normal(self, npc, text):
		npc.float_text_line(text, toee.tf_yellow)
		return

	def talk_excited(self, npc, text):
		npc.float_text_line(text, toee.tf_white)
		return

	def talk_mocking(self, npc, text):
		npc.float_text_line(text, toee.tf_green)
		return

	def is_play_viable(self, npc):
		# only if near 30 ft and is visible
		near = False
		for pc in toee.game.party:
			if pc.distance_to(npc) < 9*5:
				near = True
				break
		return near
		# unfortunately both can_see and can_sense is related to PC view diraction
		if near:
			can_see = False
			for pc in toee.game.party:
				if pc.can_see(npc):
					can_see = True
					break

			return can_see
		return False

class SceneVillageManCustomerWeaponPicker(Scene):
	def do_after_created(self, npc):
		Scene.do_after_created(self, npc)
		self.weapons = None
		return

	def check_weapons(self):
		if not self.weapons:
			#self.weapons = [const_proto_weapon.PROTO_LONGSWORD, const_proto_weapon.PROTO_BATTLEAXE, const_proto_weapon.PROTO_RAPIER, const_proto_weapon.PROTO_WEAPON_WARHAMMER]
			self.weapons = const_proto_list_weapons.PROTOS_WEAPON_ALL[:]
		return

	def scene_0(self, npc, scene_name):
		self.set_next_scene('look_initial', 2)
		return

	def scene_look_initial(self, npc, scene_name):
		self.scene_look(npc, scene_name)
		return

	def scene_look(self, npc, scene_name):
		text = 'Hey, take a look at that!' if scene_name == 'look_initial' else "What's that now?"
		self.talk_excited(npc, text)

		if not self.weapons:
			self.check_weapons()

		if self.scene_item_proto1 in self.weapons:
			self.weapons.remove(self.scene_item_proto1)

		if not self.weapons:
			self.check_weapons()

		if self.scene_item_id1:
			wpn = toee.game.get_obj_by_id(self.scene_item_id1)
			if wpn:
				wpn.destroy()

		self.scene_item_proto1 = self.weapons[toee.game.random_range(0, len(self.weapons)-1)]
		self.weapons.remove(self.scene_item_proto1)

		wpn = toee.game.obj_create(self.scene_item_proto1, npc.location)
		wpn.move(npc.location, 0, 25)
		wpn.item_flag_set(toee.OIF_NO_NPC_PICKUP) 
		wpn.item_flag_set(OIF_STOLEN)
		wpn.item_flag_set(OIF_WONT_SELL)
		wpn.item_flag_set(OIF_NO_PICKPOCKET)
		self.scene_item_id1 = wpn.id
		npc.anim_goal_animate(64 + const_animate.NormalAnimType.Examine)

		self.set_next_scene('announce_pickup', 2)
		return

	def scene_announce_pickup(self, npc, scene_name):
		self.talk_normal(npc, 'Let me try it.')
		self.set_next_scene('pickup_animation', 2)
		return

	def scene_pickup_animation(self, npc, scene_name):
		npc.anim_goal_animate(64 + const_animate.NormalAnimType.SkillDisableDevice)
		self.set_next_scene('pickup', 2)
		return

	def scene_pickup(self, npc, scene_name):
		wpn = toee.game.get_obj_by_id(self.scene_item_id1)
		if wpn:
			npc.item_wield(wpn, toee.item_wear_weapon_primary)
		self.set_next_scene('try', 2)
		return

	def scene_try(self, npc, scene_name):
		npc.anim_goal_animate(const_animate.WeaponAnim.RightAttack)
		self.set_next_scene('boast', 4)
		return

	def scene_boast(self, npc, scene_name):
		assert isinstance(npc, toee.PyObjHandle)
		self.talk_excited(npc, 'Pretty cool, right?')

		baddy = npc.obj_get_obj(toee.obj_f_last_hit_by)
		if baddy:
			self.set_next_scene('baddy_mocking', 4)
		else:
			self.set_next_scene('giveup', 6)
		return

	def scene_baddy_mocking(self, npc, scene_name):
		assert isinstance(npc, toee.PyObjHandle)
		baddy = npc.obj_get_obj(toee.obj_f_last_hit_by)
		if baddy:
			self.talk_mocking(baddy, 'You look like idiot.')
			#baddy.anim_goal_animate(64)
			self.set_next_scene('giveup', 6)
		return

	def scene_giveup(self, npc, scene_name):
		self.talk_normal(npc, 'All right, screw it.')
		wpn = npc.item_worn_at(toee.item_wear_weapon_primary)
		if wpn:
			npc.anim_goal_animate(64 + const_animate.NormalAnimType.SkillDisableDevice)
			wpn.destroy()
		self.set_next_scene('look', 10)
		return

class CtrlVillageManCustomerWeaponPicker(CtrlVillageManRandom, SceneVillageManCustomerWeaponPicker):
	
	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		super(CtrlVillageManCustomerWeaponPicker, self).after_created(npc)
		npc.scripts[const_toee.sn_heartbeat] = MODULE_SCRIPT_ID
		self.do_after_created(npc)
		return

	def heartbeat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		if self.is_play_viable(attachee):
			self.run_scenes(attachee)
		return

class CtrlVillageRandomRunOffAt(CtrlVillageManRandom):
	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		super(CtrlVillageRandomRunOffAt, self).after_created(npc)
		self.near_loc = (0, 0)
		self.near_threshhold = 2
		self.is_running_off = False
		npc.scripts[const_toee.sn_heartbeat] = MODULE_SCRIPT_ID
		return

	def heartbeat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		if self.is_running_off:
			attachee.destroy()
			return

		if self.near_loc and self.near_loc[0]:
			loc = utils_obj.loc2sec(attachee.location)
			matched = (math.fabs(loc[0] - self.near_loc[0]) <= self.near_threshhold)\
				and (math.fabs(loc[1] - self.near_loc[1]) <= self.near_threshhold)
			if matched:
				#print('NEAR LOC DESTROYING {}'.format(attachee))
				attachee.runoff(attachee.location)
				#attachee.scripts[const_toee.sn_heartbeat] = 0
				self.is_running_off = True
		return toee.RUN_DEFAULT

	@classmethod
	def get_proto_id(cls):
		return 14702

class CtrlVillageRandomRunOffAtWoman(CtrlVillageRandomRunOffAt):
	@classmethod
	def get_proto_id(cls):
		return 14703

class SceneVillageBoyWithDog(Scene):
	def do_after_created(self, npc):
		Scene.do_after_created(self, npc)
		self.thrown_id = None
		self.throw_to_loc = 0
		return

	def scene_0(self, npc, scene_name):
		self.set_next_scene('init', 1)
		return

	def scene_init(self, npc, scene_name):
		#dog = npc.obj_get_obj(toee.obj_f_npc_who_hit_me_last)
		#if dog: npc.turn_towards(dog)
		self.talk_normal(npc, "You are good boy, aren't ya Scratchy!")
		self.set_next_scene('throw', 2)
		return

	def scene_throw(self, npc, scene_name):
		assert isinstance(npc, toee.PyObjHandle)
		#stone = toee.game.obj_create(4647, npc.location)
		thrown = toee.game.get_obj_by_id(self.thrown_id) if self.thrown_id else toee.game.obj_create(4628, npc.location)
		npc.item_wield(thrown, toee.item_wear_weapon_primary)
		self.thrown_id = thrown.id
		#dog = npc.obj_get_obj(toee.obj_f_npc_who_hit_me_last)
		#npc.anim_goal_use_object(dog, const_animate.AG_THROW_ITEM, utils_obj.sec2loc(480, 475), 0)
		#npc.anim_goal_use_object(dog, const_animate.AG_THROW_ITEM, dog.location, 1)
		#npc.anim_goal_animate(const_animate.WeaponAnim.RightThrow)
		#decoy = toee.game.obj_create(14304, utils_obj.sec2loc(480, 475))
		#decoy.object_flag_set(toee.OF_DONTDRAW)
		#decoy.npc_flag_unset(toee.ONF_KOS)
		#decoy.npc_flag_set(toee.ONF_NO_ATTACK)
		#npc.action_perform(toee.D20A_THROW_GRENADE, decoy, decoy.location)
		#utils_obj.obj_timed_destroy(decoy, 100, 1)
		#decoy.ai_stop_attacking()
		#npc.action_perform(toee.D20A_PYTHON_ACTION, dog, utils_obj.sec2loc(482, 475), 3023)
		thrown_loc = utils_npc.loc_near_random(self.throw_to_loc, True)
		npc.action_perform(3023, toee.OBJ_HANDLE_NULL, thrown_loc)
		#npc.action_perform(toee.D20A_THROW_GRENADE, dog, dog.location)
		self.set_next_scene('fetch', 2)
		return

	def scene_fetch(self, npc, scene_name):
		assert isinstance(npc, toee.PyObjHandle)
		self.talk_normal(npc, "Fetch!")
		if self.thrown_id:
			dog = npc.obj_get_obj(toee.obj_f_npc_who_hit_me_last)
			if dog:
				dog_ctrl = ctrl_behaviour.get_ctrl(dog.id)
				if dog_ctrl:
					dog_ctrl.fetch_item_id = self.thrown_id
					dog_ctrl.set_next_scene('fetch', 1)
		niece = npc.obj_get_obj(toee.obj_f_npc_combat_focus)
		if niece:
			thrown = toee.game.get_obj_by_id(self.thrown_id)
			if thrown:
				niece.turn_towards(thrown)
		return

class CtrlVillageBoyDogOwner(CtrlVillagePersonRandom, SceneVillageBoyWithDog):
	@classmethod
	def get_proto_id(cls):
		return 14704

	def dress_up(self, npc):
		# create inventory
		robe = const_proto_cloth.PROTO_CLOTH_GARB_VILLAGER_BLUE
		if (robe):
			utils_item.item_create_in_inventory(robe, npc, 1, 1)
		utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BROWN, npc, 1, 1)
		npc.item_wield_best_all()
		npc.npc_flag_unset(toee.ONF_NO_ATTACK)
		return

	def make_up(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_blonde
		hairStyle.update_npc(npc)
		return

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		super(CtrlVillageBoyDogOwner, self).after_created(npc)
		npc.scripts[const_toee.sn_heartbeat] = MODULE_SCRIPT_ID
		npc.condition_add("ThrowGN")
		npc.condition_add("No_Combat")
		self.do_after_created(npc)
		return

	def heartbeat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		if self.is_play_viable(attachee):
			self.run_scenes(attachee)
		return


class CtrlVillageBoyDog(CtrlVillageAnimal, Scene):
	@classmethod
	def get_proto_id(cls):
		return 14048

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		super(CtrlVillageBoyDog, self).after_created(npc)
		npc.scripts[const_toee.sn_heartbeat] = MODULE_SCRIPT_ID
		npc.condition_add("GoalHooks")

		self.do_after_created(npc)
		self.fetch_item_id = None
		self.anim_id_pick_up = 0
		self.anim_id_bring = 0
		return

	def heartbeat(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		if self.is_play_viable(attachee):
			self.run_scenes(attachee)
		return
	
	def GoalResetToIdleAnim(self, npc, unique_action_id, unique_id):
		#debug.breakp('GoalResetToIdleAnim')
		if self.anim_id_pick_up == unique_action_id:
			self.anim_id_pick_up = -1
			self.set_next_scene('fetch_pick_up', 1)
		elif self.anim_id_bring == unique_action_id:
			self.anim_id_pick_up = -1
			self.set_next_scene('fetch_give', 1)
		return

	def scene_fetch(self, npc, scene_name):
		assert isinstance(npc, toee.PyObjHandle)
		self.set_next_scene('fetch_go', 1)
		return

	def scene_fetch_go(self, npc, scene_name):
		assert isinstance(npc, toee.PyObjHandle)
		if self.fetch_item_id:
			thrown = toee.game.get_obj_by_id(self.fetch_item_id)
			if thrown:
				npc.anim_goal_use_object(thrown, const_animate.AG_RUN_NEAR_OBJ, thrown.location, 0)
				self.anim_id_pick_up = npc.anim_goal_get_new_id()
				print('dog anim_id_pick_up: {}'.format(self.anim_id_pick_up))
				self.set_next_scene('fetch_go_fix', 5)
				niece = npc.leader_get().obj_get_obj(toee.obj_f_npc_combat_focus)
				if niece:
					niece.anim_goal_use_object(npc, const_animate.AG_ANIMATE_STUNNED, npc.location, 0)
		
		return

	def scene_fetch_go_fix(self, npc, scene_name):
		assert isinstance(npc, toee.PyObjHandle)
		if self.fetch_item_id:
			thrown = toee.game.get_obj_by_id(self.fetch_item_id)
			if thrown:
				self.anim_id_pick_up = -1
				npc.anim_goal_interrupt()
				self.set_next_scene('fetch_pick_up', 1)
		
		return

	def scene_fetch_pick_up(self, npc, scene_name):
		assert isinstance(npc, toee.PyObjHandle)
		if self.fetch_item_id:
			thrown = toee.game.get_obj_by_id(self.fetch_item_id)
			if thrown:
				npc.anim_goal_use_object(thrown, const_animate.AG_ATTEMPT_USE_SKILL_ON, thrown.location, 0)
				npc.item_get(thrown)
				self.set_next_scene('fetch_bring', 1)
			boy = npc.leader_get()
			if boy:
				niece = boy.obj_get_obj(toee.obj_f_npc_combat_focus)
				if niece:
					niece.turn_towards(npc)
		
		return

	def scene_fetch_bring(self, npc, scene_name):
		assert isinstance(npc, toee.PyObjHandle)
		if self.fetch_item_id:
			thrown = toee.game.get_obj_by_id(self.fetch_item_id)
			if thrown:
				boy = npc.leader_get()
				if boy:
					#npc.anim_goal_use_object(boy, const_animate.AG_RUN_NEAR_OBJ, boy.location, 0)
					loc = utils_npc.npc_find_path_to_target(npc, boy)[0]
					npc.anim_goal_use_object(toee.OBJ_HANDLE_NULL, const_animate.AG_RUN_TO_TILE, loc, 0)
					self.anim_id_bring = npc.anim_goal_get_new_id()
					print('dog anim_id_bring: {}'.format(self.anim_id_bring))
					self.set_next_scene('fetch_bring_fix', 4)
					niece = boy.obj_get_obj(toee.obj_f_npc_combat_focus)
					if niece:
						niece.anim_goal_interrupt()
						niece.turn_towards(boy)
		
		return

	def scene_fetch_bring_fix(self, npc, scene_name):
		assert isinstance(npc, toee.PyObjHandle)
		if self.fetch_item_id:
			thrown = toee.game.get_obj_by_id(self.fetch_item_id)
			if thrown:
				boy = npc.leader_get()
				if boy:
					npc.anim_goal_interrupt()
					npc.anim_goal_use_object(boy, const_animate.AG_RUN_TO_TILE, utils_obj.sec2loc(472, 475), 0)
					self.anim_id_bring = npc.anim_goal_get_new_id()
					print('dog anim_id_bring fixed: {}'.format(self.anim_id_bring))
		return
		
	def scene_fetch_give(self, npc, scene_name):
		assert isinstance(npc, toee.PyObjHandle)
		if self.fetch_item_id:
			thrown = toee.game.get_obj_by_id(self.fetch_item_id)
			if thrown:
				boy = npc.leader_get()
				if boy:
					npc.turn_towards(boy)
					boy.item_get(thrown)
					boy.item_wield(thrown, toee.item_wear_weapon_primary)
					boy.anim_goal_use_object(npc, const_animate.AG_ATTEMPT_USE_SKILL_ON, npc.location, 0)
					boy_ctrl = ctrl_behaviour.get_ctrl(boy.id)
					if boy_ctrl:
						boy_ctrl.set_next_scene('init', 5)
					niece = boy.obj_get_obj(toee.obj_f_npc_combat_focus)
					if niece:
						niece.anim_goal_interrupt()
						niece.turn_towards(npc)
		return

class CtrlVillageGirl(CtrlVillagePersonRandom, SceneVillageBoyWithDog):
	@classmethod
	def get_proto_id(cls):
		return 14705
