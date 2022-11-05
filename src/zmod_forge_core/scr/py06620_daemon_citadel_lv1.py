import toee, debug, debugg, utils_toee, utils_storage, utils_obj, utils_item, const_toee, ctrl_daemon, ctrl_daemon2
import ctrl_behaviour, py06122_cormyr_prompter, factions_zmod, utils_npc, utils_locks, const_proto_items, const_proto_scrolls, const_proto_rings
import monster_info, module_quests, module_consts, module_globals

DAEMON_SCRIPT_ID = 6611
DAEMON_GID = "G_0621A980_A4D0_4724_949F_B084035AAA6B"

def san_new_map(attachee, triggerer):
	return ctrl_daemon2.do_san_new_map(attachee, triggerer, module_consts.MAP_ID_CITADEL_LV1, CtrlCitadelLv1)

def san_first_heartbeat(attachee, triggerer):
	return ctrl_daemon2.do_san_first_heartbeat(attachee, triggerer, module_consts.MAP_ID_CITADEL_LV1, CtrlCitadelLv1)

def san_heartbeat(attachee, triggerer):
	return ctrl_daemon2.do_san_heartbeat(attachee, triggerer, module_consts.MAP_ID_CITADEL_LV1, cs())

def san_dying(attachee, triggerer):
	return ctrl_daemon2.do_san_dying(attachee, triggerer, module_consts.MAP_ID_CITADEL_LV1, cs())

def san_use(attachee, triggerer):
	return ctrl_daemon2.do_san_use(attachee, triggerer, module_consts.MAP_ID_CITADEL_LV1, cs())

def san_bust(attachee, triggerer):
	return ctrl_daemon2.do_san_bust(attachee, triggerer, module_consts.MAP_ID_CITADEL_LV1, cs())

def cs():
	o = utils_storage.obj_storage_by_id(DAEMON_GID)
	if (not o): 
		return None
	result = o.data.get(CtrlCitadelLv1.get_name())
	assert isinstance(result, CtrlCitadelLv1)
	return result

class CtrlCitadelLv1(ctrl_daemon2.CtrlDaemon2):
	def created(self, npc):
		self.init_daemon2_fields(module_consts.MAP_ID_CITADEL_LV1, DAEMON_SCRIPT_ID, "citadel_lv1")
		super(CtrlCitadelLv1, self).created(npc)
		self.vars["foe_ids"] = list()
		return

	def place_encounters_initial(self):
		self.place_portals()
		self.place_doors()

		#self.place_monsters_r03()
		return

	# Sleep interface
	def can_sleep(self):
		return toee.SLEEP_IMPOSSIBLE

	def create_lib_foe(self, npc_loc, ctrl_class, rot, encounter, code_name, faction = None, no_draw = 1, no_kos = 1, no_move = 0):
		result = self.create_npc_at(npc_loc, ctrl_class, rot, encounter, code_name, faction, no_draw, no_kos, no_move)
		self.vars["foe_ids"].append(result[0].id)
		return result

	def place_portals(self):
		#py06616_orc_fort_encounters.CtrlOrcFortPortalTowersToGroundSE.create_obj_at_loc(utils_obj.sec2loc(489, 488))
		#py06616_orc_fort_encounters.CtrlOrcFortPortalTowersToGroundSW.create_obj_at_loc(utils_obj.sec2loc(498, 469))
		return

	def place_doors(self):
		utils_locks.portal_hook_autodestroy(493, 474, 30)
		return
