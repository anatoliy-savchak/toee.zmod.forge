import toee, debug, ctrl_daemon, ctrl_daemon2, utils_toee, utils_storage, utils_obj, utils_item, const_proto_weapon, const_proto_armor, const_toee
import ctrl_behaviour, py06122_cormyr_prompter, factions_zmod, const_proto_scrolls, const_proto_wands, utils_npc
import module_consts, const_proto_sceneries, utils_locks, utils_toee
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

def san_use(attachee, triggerer):
	return ctrl_daemon2.do_san_use(attachee, triggerer, module_consts.MAP_ID_VILLAGE, cs())

def cs():
	o = utils_storage.obj_storage_by_id(VILLAGE_DAEMON_SCRIPT_ID)
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
		#self.generate_wanderers()
		self.place_merchants()
		self.place_tavern()

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
		return

	def place_tavern(self):
		self.create_npc_at(utils_obj.sec2loc(492, 461), py06602_village_npc.CtrlKerowyn, const_toee.ROT02, "main", "kerowyn", None, 0, 1)
		return

	def place_merchants(self):
		self.create_npc_at(utils_obj.sec2loc(478, 508), py14710_smith.CtrlVillageSmith, const_toee.ROT09, "merchant", "smith", None, 0, 1)
		self.create_npc_at(utils_obj.sec2loc(476, 505), py14711_smith_wife.CtrlVillageSmithWife, const_toee.ROT08, "merchant", "smith_wife", None, 0, 1)
		self.create_npc_at(utils_obj.sec2loc(503, 477), py14712_wizard.CtrlVillageWizard, const_toee.ROT02, "merchant", "wizard", None, 0, 1)
		self.create_npc_at(utils_obj.sec2loc(494, 506), py14713_priest.CtrlVillagePriest, const_toee.ROT11, "merchant", "priest", None, 0, 1)
		return