import toee, tpactions, tpdp, tpactions, debug, debugg

def GetActionName():
	return "Throw Grenade"

def GetActionDefinitionFlags():
	return toee.D20ADF_Python
	
def GetTargetingClassification():
	return toee.D20TC_CastSpell

def GetActionCostType():
	return toee.D20ACT_Standard_Action

# addToSeqFunc
def AddToSequence(d20action, action_seq, tb_status):
	assert isinstance(d20action, tpdp.D20Action)
	assert isinstance(action_seq, tpactions.ActionSequence)
	assert isinstance(tb_status, tpdp.TurnBasedStatus)

	d20action.flags |= toee.D20CAF_THROWN | toee.D20CAF_RANGED | toee.D20CAF_RANGED | toee.D20CAF_TOUCH_ATTACK
	action_seq.add_action(d20action)
	return toee.AEC_OK

# tgtCheckFunc has none
# actionCheckFunc none

# locCheckFunc via LocationCheckPython is not yet introduced. In ActionCheckThrowGrenade it will check for AEC_TARGET_BLOCKED and D20CAF_COVER
#	

# d20aTriggerCombatCheck
# D20ActionTriggersAoO: if D20ADF_QueryForAoO then query DK_QUE_ActionTriggersAOO OR if D20ADF_TriggersAoO

# performFunc -> ET_OnD20PythonActionPerform. PerformFuncThrowGrenade
#	ToHitProcessing
#	PushAttackAnim

# actionFrameFunc -> ET_OnD20PythonActionFrame, called from PerformOnAnimComplete(obj, animId). ActionFrameThrowGrenade
#	CreateProjectileAndThrow

# projectileHitFunc -> ProjectileHit, called from PerformOnProjectileComplete(projectile, thrower)

def ProjectileHit(d20action, proj, obj2):
	assert isinstance(d20action, tpdp.D20Action)
	assert isinstance(proj, toee.PyObjHandle)
	assert isinstance(obj2, toee.PyObjHandle)
	# proj.destroy() Projectile is destroyed after this call in AnimProjectile_10013470
	#grenade = d20action.performer.item_worn_at(toee.item_wear_weapon_primary)
	grenade = obj2
	#print('grenade: {}'.format(grenade))
	if grenade:
		d20action.performer.item_worn_unwield(toee.item_wear_weapon_primary, 1)
		#print('moving grenade to location {}, {} for {}. OF_OFF: {}'.format(d20action.loc.loc_xy.x, d20action.loc.loc_xy.y, grenade, grenade.object_flags_get() & toee.OF_OFF))
		grenade.move(d20action.loc.get_location(), 0, 0)
	return 1

