import toee, templeplus.pymod, debug, sys, tpdp, traceback, debugg, const_animate

###################################################

def GetConditionName():
	return "ThrowGN"

print("Registering " + GetConditionName())
#debugg.breakp('')
###################################################

def OnD20PythonActionPerform(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Action)
	try:
		evt_obj.d20a.flags |= toee.D20CAF_RANGED
		grenade = attachee.item_worn_at(toee.item_wear_weapon_primary)
		#evt_obj.d20a.to_hit_processing()
		is_critical = 1 if evt_obj.d20a.flags & toee.D20CAF_CRITICAL else 0
		animated = attachee.anim_goal_animate(const_animate.WeaponAnim.RightThrow)
		#animated = attachee.anim_goal_use_object(evt_obj.d20a.target, const_animate.AG_THROW_ITEM, evt_obj.d20a.loc.get_location(), 1)
		#print('attachee.anim_goal_use_object({}, {}, {}, 1) = {}'.format(evt_obj.d20a.target, const_animate.AG_THROW_ITEM, evt_obj.d20a.loc.get_location(), animated))
		#animated = attachee.anim_goal_push_attack(evt_obj.d20a.target, toee.game.random_range(0, 2), is_critical, 0)
		#animated = attachee.anim_goal_animate(const_animate.WeaponAnim.RightThrow)
		if animated:
			evt_obj.d20a.anim_id = attachee.anim_goal_get_new_id()
			#print('evt_obj.d20a.anim_id = {}'.format(evt_obj.d20a.anim_id))
			evt_obj.d20a.flags |= toee.D20CAF_NEED_ANIM_COMPLETED

		toee.game.timevent_add(_throw_item, (attachee, evt_obj.d20a, grenade), 500, 1) # 1000 = 1 second
	except Exception, e:
		print "OnD20PythonActionPerform:"
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60		
		debugg.breakp("error")
	return 0

def _throw_item(attachee, d20a, thrown_item):
	loc_or_obj = d20a.target
	if not loc_or_obj:
		loc_or_obj = d20a.loc
	projectileProto = thrown_item.get_weapon_projectile_proto()
	projectileHandle = d20a.create_projectile_and_throw(projectileProto, loc_or_obj)
	projectileHandle.obj_set_float(toee.obj_f_offset_z, 60.0)
	if d20a.projectile_append(projectileHandle, thrown_item):
		attachee.apply_projectile_particles(projectileHandle, d20a.flags)
		d20a.flags |= toee.D20CAF_NEED_PROJECTILE_HIT
	return

def OnD20PythonActionFrame(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Action)
	try:
		# _throw_item(attachee, evt_obj.d20a)
		# moved to post call due to better animation
		pass
	except Exception, e:
		print "OnD20PythonActionFrame error:"
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60		
		debugg.breakp("error")
	return 0

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 2) # 
modObj.AddHook(toee.ET_OnD20PythonActionPerform, 3023, OnD20PythonActionPerform, ())
modObj.AddHook(toee.ET_OnD20PythonActionFrame, 3023, OnD20PythonActionFrame, ())


