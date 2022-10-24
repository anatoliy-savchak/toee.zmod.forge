import toee, debug, ctrl_daemon, ctrl_daemon2, utils_toee, utils_storage, utils_obj, utils_item, const_proto_weapon, const_proto_armor, const_toee
import ctrl_behaviour, py06122_cormyr_prompter, factions_zmod, const_proto_scrolls, const_proto_wands, utils_npc
import module_consts, const_proto_sceneries, utils_locks, utils_toee, const_animate
import py14710_smith, py14711_smith_wife, py14712_wizard, py14713_priest, py06601_village_populace, py06602_village_npc

VILLAGE_DAEMON_SCRIPT_ID = 6600
VILLAGE_DAEMON_ID = "G_777CFFCC_1864_4C4D_B05F_ECE4C6EF4B18"

def san_new_map(attachee, triggerer):
	return ctrl_daemon2.do_san_new_map(attachee, triggerer, module_consts.MAP_ID_VILLAGE, CtrlVillage)

def san_first_heartbeat(attachee, triggerer):
	return ctrl_daemon2.do_san_first_heartbeat(attachee, triggerer, module_consts.MAP_ID_VILLAGE, CtrlVillage)

def san_heartbeat(attachee, triggerer):
	return ctrl_daemon2.do_san_heartbeat(attachee, triggerer, module_consts.MAP_ID_VILLAGE, cs())

def san_dying(attachee, triggerer):
	return ctrl_daemon2.do_san_dying(attachee, triggerer, module_consts.MAP_ID_VILLAGE, cs())

def san_destroy(attachee, triggerer):
	_cs = cs()
	if _cs:
		return _cs.do_san_destroy(attachee, triggerer)
	return

def san_use(attachee, triggerer):
	return ctrl_daemon2.do_san_use(attachee, triggerer, module_consts.MAP_ID_VILLAGE, cs())

def cs():
	o = utils_storage.obj_storage_by_id(VILLAGE_DAEMON_ID)
	if (not o): return None
	if (CtrlVillage.get_name() in o.data):
		result = o.data[CtrlVillage.get_name()]
	else: return None
	assert isinstance(result, CtrlVillage)
	return result

class CtrlVillage(ctrl_daemon2.CtrlDaemon2):
	def created(self, npc):
		self.init_daemon2_fields(module_consts.MAP_ID_VILLAGE, VILLAGE_DAEMON_SCRIPT_ID, "village")
		super(CtrlVillage, self).created(npc)
		return

	def place_encounters_initial(self):
		#self.generate_animals()
		self.generate_wanderers()
		#self.place_merchants()
		#self.place_tavern()
		self.generate_people()
		self.spawn_walkers()

		return

	# Sleep interface
	def can_sleep(self):
		return toee.SLEEP_PASS_TIME_ONLY

	def generate_animals(self):
		# there are problems, skip for now
		delay_base = 1*1000
		npc, ctrl = self.create_npc_at(utils_obj.sec2loc(474, 456), py06601_village_populace.CtrlVillageAnimalPig, const_toee.rotation_1100_oclock, "animals", "pig1", None, 0, 1)
		if (npc):
			if (1):
				waypoints = list()
				waypoints.append(utils_npc.Waypoint(474, 456, const_toee.rotation_1100_oclock, 1000 * toee.game.random_range(1, 10), utils_npc.WaypointFlag.Delay))
				waypoints.append(utils_npc.Waypoint(474, 461, const_toee.rotation_0500_oclock, 1000 * toee.game.random_range(1, 10)+delay_base, utils_npc.WaypointFlag.Delay))
				waypoints.append(utils_npc.Waypoint(479, 456, const_toee.rotation_0900_oclock, 1000 * toee.game.random_range(1, 10)+delay_base, utils_npc.WaypointFlag.Delay))
				waypoints.append(utils_npc.Waypoint(479, 461, const_toee.rotation_0600_oclock, 1000 * toee.game.random_range(1, 10)+delay_base, utils_npc.WaypointFlag.Delay))
				npc.npc_waypoints_set(waypoints)
				npc.npc_flag_set(toee.ONF_WAYPOINTS_DAY)
				npc.npc_flag_set(toee.ONF_WANDERS)
				npc.npc_flag_set(toee.ONF_WANDERS_IN_DARK)
			else:
				npc.npc_flag_set(toee.ONF_WANDERS)
				npc.move(utils_obj.sec2loc(479, 461))
				
		npc, ctrl = self.create_npc_at(utils_obj.sec2loc(475, 456), py06601_village_populace.CtrlVillageAnimalPig, const_toee.rotation_1100_oclock, "animals", "pig2", None, 0, 1)
		if (npc):
			if (1):
				waypoints = list()
				waypoints.append(utils_npc.Waypoint(475, 456, const_toee.rotation_1100_oclock, 1000 * toee.game.random_range(1, 10), utils_npc.WaypointFlag.Delay))
				waypoints.append(utils_npc.Waypoint(479, 461, const_toee.rotation_0600_oclock, 1000 * toee.game.random_range(1, 10)+delay_base, utils_npc.WaypointFlag.Delay))
				waypoints.append(utils_npc.Waypoint(474, 461, const_toee.rotation_0500_oclock, 1000 * toee.game.random_range(1, 10)+delay_base, utils_npc.WaypointFlag.Delay))
				waypoints.append(utils_npc.Waypoint(479, 456, const_toee.rotation_0900_oclock, 1000 * toee.game.random_range(1, 10)+delay_base, utils_npc.WaypointFlag.Delay))
				npc.npc_waypoints_set(waypoints)
				npc.npc_flag_set(toee.ONF_WAYPOINTS_DAY)
				npc.npc_flag_set(toee.ONF_WANDERS)
				npc.npc_flag_set(toee.ONF_WANDERS_IN_DARK)
			else:
				npc.npc_flag_set(toee.ONF_WANDERS)

		npc, ctrl = self.create_npc_at(utils_obj.sec2loc(476, 456), py06601_village_populace.CtrlVillageAnimalPig, const_toee.rotation_1100_oclock, "animals", "pig3", None, 0, 1)
		if (npc):
			if (1):
				waypoints = list()
				waypoints.append(utils_npc.Waypoint(476, 456, const_toee.rotation_1100_oclock, 1000 * toee.game.random_range(1, 10), utils_npc.WaypointFlag.Delay))
				waypoints.append(utils_npc.Waypoint(474, 461, const_toee.rotation_0500_oclock, 1000 * toee.game.random_range(1, 10)+delay_base, utils_npc.WaypointFlag.Delay))
				waypoints.append(utils_npc.Waypoint(479, 461, const_toee.rotation_0600_oclock, 1000 * toee.game.random_range(1, 10)+delay_base, utils_npc.WaypointFlag.Delay))
				waypoints.append(utils_npc.Waypoint(479, 456, const_toee.rotation_0900_oclock, 1000 * toee.game.random_range(1, 10)+delay_base, utils_npc.WaypointFlag.Delay))
				npc.npc_waypoints_set(waypoints)
				npc.npc_flag_set(toee.ONF_WAYPOINTS_DAY)
				npc.npc_flag_set(toee.ONF_WANDERS)
				npc.npc_flag_set(toee.ONF_WANDERS_IN_DARK)
			else:
				npc.npc_flag_set(toee.ONF_WANDERS)
		return

	def generate_wanderers(self):
		for num in range(1, 10):
			x, y = py06601_village_populace.VillagePlaces.get_random_sqare_place()
			npc, ctrl = self.create_npc_at(utils_obj.sec2loc(x, y), py06601_village_populace.CtrlVillageRandomWanderer, const_toee.ROT02, "wanderers", "person{}".format(num), None, 0, 1)
			ctrl.make_day_route(npc)
			print('obj_f_speed_walk: {} for {}'.format(npc.obj_get_float(toee.obj_f_speed_walk), npc))
			npc.obj_set_float(toee.obj_f_speed_walk, 0.5)
			print('obj_f_speed_walk CHECK: {} vs {} for {}'.format(npc.obj_get_int(toee.obj_f_speed_walk), npc.obj_get_float(toee.obj_f_speed_walk), npc))
			
			# import py06600_daemon_village, const_animate
			# py06600_daemon_village.cs().monsters.values()[0].get_npc().obj_set_float(toee.obj_f_speed_walk, 0.6)
			# npc = py06600_daemon_village.cs().monsters.values()[0].get_npc() 
			#npc.anim_goal_use_object(OBJ_HANDLE_NULL, 40, npc.location, 0)
			# npc.anim_goal_use_object(npc, 40, npc.location, 0)
			# npc.anim_goal_use_object(game.leader, 51, game.leader.location, 0) -- rotate
			# anim_goal_interrupt
			# npc.anim_goal_use_object(game.leader, 26, game.leader.location, 0)
			# npc.anim_goal_animate(64) = drop down
			# npc.anim_goal_animate(64 + const_animate.NormalAnimType.SkillSearch) # 112
			# wpn = game.obj_create(4036, npc.location, 0, 0)
			# npc.item_wield(wpn, item_wear_weapon_primary)
			# npc.turn_towards(game.leader)
			# wpn = npc.item_worn_at(item_wear_weapon_primary)
			# npc.anim_goal_animate(const_animate.WeaponAnim.RightAttack3)
			
			break
		return

	def generate_people(self):
		npc, ctrl = self.create_npc_at(utils_obj.sec2loc(483, 498), py06601_village_populace.CtrlVillageManCustomerWeaponPicker, const_toee.ROT05, "wanderers", "person_customer_01", None, 0, 1)

		npc2, ctrl = self.create_npc_at(utils_obj.sec2loc(483, 500), py06601_village_populace.CtrlVillageManRandom, const_toee.ROT11, "wanderers", "person_customer_02", None, 0, 1)
		npc.obj_set_obj(toee.obj_f_last_hit_by, npc2)
		
		return

	def place_tavern(self):
		kerowyn, kerowyn_ctrl = self.create_npc_at(utils_obj.sec2loc(492, 461), py06602_village_npc.CtrlKerowyn, const_toee.ROT02, "main", "kerowyn", None, 0, 1)

		bodyguard, bodyguard_ctrl = self.create_npc_at(utils_obj.sec2loc(493, 460), py06602_village_npc.CtrlKerowynBodyguard, const_toee.ROT02, "main", "bodyguard", None, 0, 1)
		if bodyguard:
			bodyguard.obj_set_obj(toee.obj_f_npc_leader, kerowyn)
			bodyguard.turn_towards(kerowyn)
		return

	def place_merchants(self):
		self.create_npc_at(utils_obj.sec2loc(478, 508), py14710_smith.CtrlVillageSmith, const_toee.ROT09, "merchant", "smith", None, 0, 1)
		self.create_npc_at(utils_obj.sec2loc(476, 505), py14711_smith_wife.CtrlVillageSmithWife, const_toee.ROT08, "merchant", "smith_wife", None, 0, 1)
		self.create_npc_at(utils_obj.sec2loc(503, 477), py14712_wizard.CtrlVillageWizard, const_toee.ROT02, "merchant", "wizard", None, 0, 1)
		self.create_npc_at(utils_obj.sec2loc(494, 506), py14713_priest.CtrlVillagePriest, const_toee.ROT11, "merchant", "priest", None, 0, 1)
		return

	def do_san_use(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		print("village san_use id: {}, nameid: {}".format(attachee.id, attachee.name))

		#san_use id: P_000001D4_000001FE_00000000_00001392, nameid: 1814
		if attachee.id == 'P_000001D3_000001FE_00000000_00001392':
			toee.game.fade_and_teleport(
				module_consts.TRAVEL_TIME_VILLAGE_TO_ROAD1, 0, 0, 
				module_consts.MAP_ID_ROAD1, 
				module_consts.ROAD1_ENTRY_COORDS_NORTH[0], 
				module_consts.ROAD1_ENTRY_COORDS_NORTH[1]
				)

		return toee.RUN_DEFAULT

	def do_san_destroy(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		print("do_san_destroy attachee: {}".format(attachee))
		objStorage = utils_storage.obj_remove_storage_by_id(attachee.id)
		ctrl = ctrl_behaviour.get_ctrl_from_objstorage(objStorage)
		if ctrl:
			nn = None
			id = attachee.id
			for n, m in self.monsters.iteritems():
				if m.id == id:
					nn = n
					break
			if nn:
				del self.monsters[nn]
			
			if isinstance(ctrl, py06601_village_populace.CtrlVillageRandomRunOffAtWoman):
				self.spawn_walkers()
		return toee.RUN_DEFAULT

	def spawn_walkers(self):
		# walking couple 
		npc, ctrl = self.create_npc_at(utils_obj.sec2loc(505, 471), py06601_village_populace.CtrlVillageRandomRunOffAt, const_toee.ROT02, "wanderers", "person_walking_01", None, 0, 1)
		#ctrl.near_loc = (492, 469) debug
		ctrl.near_loc = (467, 507)
		if (1):
			waypoints = list()
			waypoints.append(utils_npc.Waypoint(500, 470, const_toee.ROT02))
			waypoints.append(utils_npc.Waypoint(472, 467, const_toee.ROT03))
			waypoints.append(utils_npc.Waypoint(464, 474, const_toee.ROT05))
			waypoints.append(utils_npc.Waypoint(465, 490, const_toee.ROT05))
			waypoints.append(utils_npc.Waypoint(467, 507, const_toee.ROT05, 5000, utils_npc.WaypointFlag.Delay | utils_npc.WaypointFlag.Animate, 64 + const_animate.NormalAnimType.Examine))
			npc.npc_waypoints_set(waypoints)
			npc.npc_flag_set(toee.ONF_WAYPOINTS_DAY)
			npc.npc_flag_set(toee.ONF_WANDERS)
			npc.npc_flag_set(toee.ONF_WANDERS_IN_DARK)
			npc.obj_set_float(toee.obj_f_speed_walk, 0.6)
			npc.scripts[const_toee.sn_destroy] = VILLAGE_DAEMON_SCRIPT_ID

		if (1):
			npc, ctrl = self.create_npc_at(utils_obj.sec2loc(505, 471), py06601_village_populace.CtrlVillageRandomRunOffAtWoman, const_toee.ROT02, "wanderers", "person_walking_02", None, 0, 1)
			ctrl.near_loc = (467, 507)
			if (1):
				waypoints = list()
				waypoints.append(utils_npc.Waypoint(500, 470+2, const_toee.ROT02))
				waypoints.append(utils_npc.Waypoint(472, 467+2, const_toee.ROT03, 1000, utils_npc.WaypointFlag.Delay))
				waypoints.append(utils_npc.Waypoint(464+2, 474, const_toee.ROT05, 1000, utils_npc.WaypointFlag.Delay))
				waypoints.append(utils_npc.Waypoint(465+2, 490, const_toee.ROT05))
				waypoints.append(utils_npc.Waypoint(467+2, 507, const_toee.ROT05, 5000, utils_npc.WaypointFlag.Delay | utils_npc.WaypointFlag.Animate, 64 + const_animate.NormalAnimType.Examine))
				npc.npc_waypoints_set(waypoints)
				npc.npc_flag_set(toee.ONF_WAYPOINTS_DAY)
				npc.npc_flag_set(toee.ONF_WANDERS)
				npc.npc_flag_set(toee.ONF_WANDERS_IN_DARK)
				npc.obj_set_float(toee.obj_f_speed_walk, 0.6)
				npc.scripts[const_toee.sn_destroy] = VILLAGE_DAEMON_SCRIPT_ID
		return
