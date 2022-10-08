import toee, debug, ctrl_daemon, ctrl_daemon2, utils_toee, utils_storage, utils_obj, utils_item, const_proto_weapon, const_proto_armor, const_toee
import ctrl_behaviour, py06122_cormyr_prompter, factions_zmod, const_proto_scrolls, const_proto_wands, utils_npc
import module_consts, const_proto_sceneries, utils_locks, py14710_smith, py14711_smith_wife, py14712_wizard, py14713_priest, utils_toee

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
		self.create_npc_at(utils_obj.sec2loc(478, 508), py14710_smith.CtrlVillageSmith, const_toee.ROT09, "merchant", "smith", None, 0, 1)
		self.create_npc_at(utils_obj.sec2loc(476, 505), py14711_smith_wife.CtrlVillageSmithWife, const_toee.ROT08, "merchant", "smith_wife", None, 0, 1)
		self.create_npc_at(utils_obj.sec2loc(503, 477), py14712_wizard.CtrlVillageWizard, const_toee.ROT02, "merchant", "wizard", None, 0, 1)
		self.create_npc_at(utils_obj.sec2loc(494, 506), py14713_priest.CtrlVillagePriest, const_toee.ROT11, "merchant", "priest", None, 0, 1)

		return

	# Sleep interface
	def can_sleep(self):
		return toee.SLEEP_PASS_TIME_ONLY
