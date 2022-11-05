import toee, ctrl_behaviour, utils_item, utils_obj, const_toee, factions_zmod, utils_npc, const_animate
import const_proto_armor, const_proto_weapon, const_proto_food, const_proto_cloth, const_proto_containers, const_proto_list_weapons, const_proto_list_scrolls, const_proto_list_cloth
import debug, rumor_control
import const_proto_npc, module_quests, module_globals, module_consts
import py14764_npc_portal

MODULE_SCRIPT_ID = 6610

def san_start_combat(attachee, triggerer): return ctrl_behaviour.san_start_combat(attachee, triggerer)
def san_enter_combat(attachee, triggerer): return ctrl_behaviour.san_enter_combat(attachee, triggerer)
def san_end_combat(attachee, triggerer): return ctrl_behaviour.san_end_combat(attachee, triggerer)
def san_exit_combat(attachee, triggerer): return ctrl_behaviour.san_exit_combat(attachee, triggerer)
def san_will_kos(attachee, triggerer): return ctrl_behaviour.san_will_kos(attachee, triggerer)
def san_dialog(attachee, triggerer): return ctrl_behaviour.san_dialog(attachee, triggerer)
def san_heartbeat(attachee, triggerer): return 0 if attachee.object_flags_get() & toee.OF_OFF else ctrl_behaviour.san_heartbeat(attachee, triggerer)
def san_wield_off(attachee, triggerer): return ctrl_behaviour.san_wield_off(attachee, triggerer)
def gc(npc): return ctrl_behaviour.get_ctrl(npc.id)

class PortalRoad1ToCitadelLv1(py14764_npc_portal.CtrlPortalLaddersUp):
	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		super(PortalRoad1ToCitadelLv1, self).after_created(npc)
		utils_npc.npc_description_set_new(npc, 'Stairwell')
		return

	@classmethod
	def get_dialog_line_cls(cls, npc): return 100

	@classmethod
	def get_dialog_script_id_cls(cls, npc): return MODULE_SCRIPT_ID

	def get_dest_location(self): return module_consts.CITADEL_LV1_ENTRY_COORDS_START

	def get_dest_map(self): return module_consts.MAP_ID_CITADEL_LV1

	def get_dest_travel_time_s(self): return module_consts.TRAVEL_TIME_ROAD1_TO_CITADEL

	def can_travel_road_to_citadel(self, npc): return True

	def travel_road_to_citadel(self, npc): 
		self.do_travel(npc)
		return

class PortalCitadelLv1ToRoad1(py14764_npc_portal.CtrlPortalLaddersUp):
	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		super(PortalCitadelLv1ToRoad1, self).after_created(npc)
		utils_npc.npc_description_set_new(npc, 'Stairwell')
		return

	@classmethod
	def get_dialog_line_cls(cls, npc): return 200

	@classmethod
	def get_dialog_script_id_cls(cls, npc): return MODULE_SCRIPT_ID

	def get_dest_location(self): return module_consts.ROAD1_ENTRY_COORDS_NEAR_LEDGE

	def get_dest_map(self): return module_consts.MAP_ID_ROAD1

	def get_dest_travel_time_s(self): return module_consts.TRAVEL_TIME_ROAD1_TO_CITADEL

	def can_travel_citadel_to_road1(self, npc): return True

	def travel_citadel_to_road1(self, npc): 
		self.do_travel(npc)
		return

class PortalRoad1ToVillage(py14764_npc_portal.CtrlPortalOutImmediate):
	def get_dest_location(self): return module_consts.VILLAGE_ENTRY_COORDS_ROAD_SOUTH

	def get_dest_map(self): return module_consts.MAP_ID_VILLAGE

	def get_dest_travel_time_s(self): return module_consts.TRAVEL_TIME_VILLAGE_TO_ROAD1
