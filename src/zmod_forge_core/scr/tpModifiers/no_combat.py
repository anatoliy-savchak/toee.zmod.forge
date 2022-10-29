import toee, templeplus.pymod, tpdp, debug

###################################################

def GetConditionName():
	return "No_Combat"

print("Registering " + GetConditionName())
###################################################

def OnQueryReturnTrue(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Query)
	
	evt_obj.return_val = 1
	return 0

def OnQueryReturnFalse(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Query)
	
	evt_obj.return_val = 0
	return 0

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 2) #
modObj.AddHook(toee.ET_OnD20Query, toee.EK_Q_EnterCombat, OnQueryReturnFalse, ())
