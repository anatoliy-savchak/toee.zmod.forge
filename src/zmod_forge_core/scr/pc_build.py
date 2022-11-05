import toee, debug
import utils_item, const_proto_weapon, const_proto_armor, const_proto_cloth, const_proto_scrolls, utils_npc

# import pc_build
# pc_build.forge_a1()
def forge_a1():
	# 1: barbarian
	# 2: dwarf cleric longsword
	# 3: sorc
	# 4: wizard from rogue

	# fighter tank
	pc = toee.game.party[0]
	if (pc):
		utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_WEAPON_GREATAXE, pc)
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_ARMOR_BREASTPLATE, pc)
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_SHIELD_BUCKLER, pc)
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_BOOTS_SILVER_PLATE_BOOTS, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)
		pc.item_wield_best_all()

	# cleric
	pc = toee.game.party[1]
	if (pc):
		utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_LONGSWORD, pc)
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_SHIELD_SMALL_WOODEN, pc)
		utils_item.item_create_in_inventory_buy(const_proto_armor.PROTO_ARMOR_BANDED_MAIL, pc)
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_BOOTS_GILDED_BOOTS, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)
		pc.item_wield_best_all()

	# sorc
	pc = toee.game.party[3]
	if (pc):
		utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_WEAPON_CROSSBOW_LIGHT, pc)
		item = utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_BOLT_QUIVER, pc)
		if (item):
			item.obj_set_int(toee.obj_f_ammo_quantity, 50)
		
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_BOOTS_MONK, pc)
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_MONK_OUTFIT, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)

		#utils_item.item_create_in_inventory_buy(const_proto_scrolls.PROTO_SCROLL_OF_ENLARGE_PERSON, pc)
		
		pc.item_wield_best_all()

	# wizard
	pc = toee.game.party[2]
	if (pc):
		utils_item.item_create_in_inventory_buy(const_proto_weapon.PROTO_WEAPON_CROSSBOW_LIGHT, pc)
		item = utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_BOLT_QUIVER, pc)
		if (item):
			item.obj_set_int(toee.obj_f_ammo_quantity, 50)
		
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_GARB_NOBLE_PURPLE, pc)
		utils_item.item_create_in_inventory_buy(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, pc)
		utils_item.item_clear_by_proto(pc, const_proto_cloth.PROTO_CLOTH_GARB_BROWN)

		#utils_item.item_create_in_inventory_buy(const_proto_scrolls.PROTO_SCROLL_OF_ENLARGE_PERSON, pc)
		
		pc.item_wield_best_all()

	return
