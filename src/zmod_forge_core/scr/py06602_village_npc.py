import toee, ctrl_behaviour, utils_item, utils_obj, const_toee, factions_zmod, utils_npc, const_animate
import const_proto_armor, const_proto_weapon, const_proto_food, const_proto_cloth, const_proto_containers, const_proto_list_weapons, const_proto_list_scrolls, const_proto_list_cloth
import debug, rumor_control
import const_proto_npc, module_quests, module_globals

MODULE_SCRIPT_ID = 6602

def san_start_combat(attachee, triggerer): return ctrl_behaviour.san_start_combat(attachee, triggerer)
def san_enter_combat(attachee, triggerer): return ctrl_behaviour.san_enter_combat(attachee, triggerer)
def san_end_combat(attachee, triggerer): return ctrl_behaviour.san_end_combat(attachee, triggerer)
def san_exit_combat(attachee, triggerer): return ctrl_behaviour.san_exit_combat(attachee, triggerer)
def san_will_kos(attachee, triggerer): return ctrl_behaviour.san_will_kos(attachee, triggerer)
def san_dialog(attachee, triggerer): return ctrl_behaviour.san_dialog(attachee, triggerer)
def san_heartbeat(attachee, triggerer): return 0 if attachee.object_flags_get() & toee.OF_OFF else ctrl_behaviour.san_heartbeat(attachee, triggerer)
def san_wield_off(attachee, triggerer): return ctrl_behaviour.san_wield_off(attachee, triggerer)
def gc(npc): return ctrl_behaviour.get_ctrl(npc.id)

class CtrlKerowyn(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_WOMAN

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID

		utils_npc.npc_description_set_new(npc, "Kerowyn Hucrele")

		npc.make_class(const_toee.stat_level_npc_expert, 5)

		npc.obj_set_int(toee.obj_f_critter_portrait, 7370) # Matron_Mathilde_14043
		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_medium
		hairStyle.color = const_toee.hair_color_black
		hairStyle.update_npc(npc)

		npc.object_flag_set(toee.OF_INVULNERABLE)
		npc.npc_flag_set(toee.ONF_NO_ATTACK)

		# create inventory
		utils_item.item_create_in_inventory(self.get_cloth_garb(), npc, 1, 1)
		utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_CIRCLET_HOODLESS, npc, 1, toee.item_wear_helmet)
		utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_BLACK, npc, 1, 1)
		utils_item.item_money_create_in_inventory(npc, 0, 500)
		
		npc.item_wield_best_all()
		utils_npc.npc_generate_hp_avg_first(npc)
		return

	def get_cloth_garb(self): return const_proto_cloth.PROTO_CLOTH_ROBES_GREEN

	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		attachee.turn_towards(triggerer)
		if (not attachee.has_met(triggerer)):
			triggerer.begin_dialog(attachee, 1) # meet and quest
		else: 
			triggerer.begin_dialog(attachee, 50) # after quest given
		return toee.SKIP_DEFAULT

	@classmethod
	def dialog_give_quest(cls, npc, willing):
		assert isinstance(npc, toee.PyObjHandle)
		if willing:
			toee.game.quests[module_quests.QUEST_VILLAGE_HUCRELE].state = toee.qs_accepted
		else: 
			toee.game.quests[module_quests.QUEST_VILLAGE_HUCRELE].state = toee.qs_mentioned
		return

	def get_is_off_at_night(self): return 1

class CtrlKerowynBodyguard(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_DWARF_MAN

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID
		npc.scripts[const_toee.sn_heartbeat] = MODULE_SCRIPT_ID
		#npc.faction_add(factions_zmod.FACTION_NEUTRAL_NPC)

		npc.make_class(const_toee.stat_level_npc_warriror, 4)

		utils_npc.npc_description_set_new(npc, "Bodyguard")

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_black
		hairStyle.update_npc(npc)

		npc.object_flag_set(toee.OF_INVULNERABLE)
		npc.npc_flag_set(toee.ONF_NO_ATTACK)

		# create inventory
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_HALF_PLATE, npc, 1, 1)
		utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_BLACK, npc, 1, 1)
		utils_item.item_create_in_inventory(const_proto_weapon.PROTO_LONGSWORD_MASTERWORK, npc, 1, 1)
		utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_MASTERWORK_STEEL, npc, 1, 1)
		
		npc.item_wield_best_all()
		utils_npc.npc_generate_hp(npc)
		return

	def get_is_off_at_night(self): return 1


class CtrlVillageBarkeeper(ctrl_behaviour.CtrlBehaviourAI):
	@classmethod
	def get_proto_id(cls):
		return 14702

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)
		npc.scripts[const_toee.sn_dialog] = MODULE_SCRIPT_ID

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_medium
		hairStyle.color = const_toee.hair_color_brown
		hairStyle.update_npc(npc)

		new_name_id = toee.game.make_custom_name("Barkeep")
		npc.obj_set_int(toee.obj_f_critter_description_unknown, new_name_id)
		new_name_id = toee.game.make_custom_name("Davis Owensby")
		npc.obj_set_int(const_toee.obj_f_description_correct, new_name_id)

		npc.obj_set_int(toee.obj_f_critter_portrait, 10060) # barkeep_42x37.tga

		npc.object_flag_set(toee.OF_INVULNERABLE)
		npc.npc_flag_set(toee.ONF_NO_ATTACK)

		# create inventory
		utils_item.item_create_in_inventory(self.get_cloth_garb(), npc, 1, 1)
		#utils_item.item_create_in_inventory2(const_proto_cloth.PROTO_CLOTH_CIRCLET_HOODLESS, npc, 1, toee.item_wear_helmet)
		utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_BLACK, npc, 1, 1)
		utils_item.item_money_create_in_inventory(npc, 0, 200)

		npc.item_wield_best_all()
		utils_npc.npc_generate_hp(npc)
		return

	def get_cloth_garb(self): return const_proto_cloth.PROTO_CLOTH_GARB_FARMER_BROWN

	def dialog(self, attachee, triggerer):
		assert isinstance(attachee, toee.PyObjHandle)
		assert isinstance(triggerer, toee.PyObjHandle)

		attachee.turn_towards(triggerer)
		if (not attachee.has_met(triggerer)):
			triggerer.begin_dialog(attachee, 200) 
		else: 
			triggerer.begin_dialog(attachee, 250) # already met
		return toee.SKIP_DEFAULT

	@staticmethod
	def get_rent_price_cp():
		return 2

	def dialog_room_rent(self, pc):
		assert isinstance(pc, toee.PyObjHandle)
		pc.money_adj(-self.get_rent_price_cp())
		toee.game.create_history_freeform('\nYou paid {} cp for the room for 24 hours.\n'.format(self.get_rent_price_cp()))
		toee.game.global_flags[module_globals.GFLAG_REST_ALLOWED] = 1
		toee.game.timeevent_add(CtrlVillageBarkeeper.room_no_longer_available, (), 24*60*60*1000)
		toee.game.sleep_status_update()
		return toee.RUN_DEFAULT

	def dialog_check_room_rent(self, pc):
		assert isinstance(pc, toee.PyObjHandle)
		return pc.money_get() >= self.get_rent_price_cp()
	
	@staticmethod
	def room_no_longer_available():
		print('room_no_longer_available')
		toee.game.global_flags[module_globals.GFLAG_REST_ALLOWED] = 0
		toee.game.sleep_status_update()
		return toee.RUN_DEFAULT
