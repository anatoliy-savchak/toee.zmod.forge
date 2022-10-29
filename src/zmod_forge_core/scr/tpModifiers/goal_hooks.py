import toee, templeplus.pymod, tpdp, debug

###################################################

def GetConditionName():
	return "GoalHooks"

print("Registering " + GetConditionName())
###################################################

def GoalResetToIdleAnim(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Query)
	
	import ctrl_behaviour
	ctrl = ctrl_behaviour.get_ctrl(attachee.id)
	if ctrl and 'GoalResetToIdleAnim' in dir(ctrl):
		ctrl.GoalResetToIdleAnim(attachee, evt_obj.data1, evt_obj.data2)
	return 0

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 6) # reserved
modObj.AddHook(toee.ET_OnD20PythonSignal, "GoalResetToIdleAnim", GoalResetToIdleAnim, ())
