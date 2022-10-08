import toee, debug
import utils_storage, utils_obj, const_toee
import const_animate

def mayor_walk():
	mayor = utils_storage.ca("mayor_uptal").npc_get()
	print(mayor)
	mayor.anim_goal_push_goto(utils_obj.sec2loc(461, 474), 0)
	return

def mayor_walk2():
	mayor = utils_storage.ca("mayor_uptal").npc_get()
	print(mayor)
	#mayor.anim_goal_push_goto(utils_obj.sec2loc(461, 474), 0)
	#mayor.standpoint_set_ex(toee.STANDPOINT_DAY, utils_obj.sec2loc(461, 474))
	mayor.standpoint_set(toee.STANDPOINT_DAY, -1, utils_obj.sec2loc(459, 456), 0, 0, 0)
	return

def mayor_check():
	mayor = utils_storage.ca("mayor_uptal").npc_get()
	assert isinstance(mayor, toee.PyObjHandle)

	has_ONF_WAYPOINTS_DAY = mayor.npc_flags_get() & toee.ONF_WAYPOINTS_DAY
	print("ONF_WAYPOINTS_DAY: {}".format(has_ONF_WAYPOINTS_DAY))
	has_ONF_WAYPOINTS_NIGHT = mayor.npc_flags_get() & toee.ONF_WAYPOINTS_NIGHT
	print("ONF_WAYPOINTS_NIGHT: {}".format(has_ONF_WAYPOINTS_NIGHT))
	return


# import tezts
# tezts.dog_check()
def dog_check():
	dog = None
	for npc in toee.game.obj_list_range(utils_obj.sec2loc(502, 469), 20, toee.OLC_CRITTERS):
		dog = npc
		break

	wp = dog.npc_waypoints_get()
	item1 = wp[0]
	assert isinstance(item1, dict)
	item2 = wp[1]
	assert isinstance(item2, dict)
	for key in item1.iterkeys():
		print("{}: {} = {}".format(key, item1[key], item2[key]))
	#print(wp)
	debug.breakp("")
	return 0

class Waypoint:
	def __init__(self, x, y, rotation, delay, flags = 0, anim1 = 0):
		self.flags = flags
		self.x = x
		self.y = y
		self.off_x = 0
		self.off_y = 0
		self.rotation = rotation
		self.delay = delay
		self.anim1 = anim1
		self.anim2 = 0
		self.anim3 = 0
		self.anim4 = 0
		self.anim5 = 0
		self.anim6 = 0
		self.anim7 = 0
		#self.anim8 = 0
		return

class WaypointFlag:
    FixedRotation = 1
    Delay = 2
    Animate = 4

# import tezts
# tezts.chickwp()

def chickwp():
	chick = toee.game.obj_create(14362, utils_obj.sec2loc(492, 469))
	waypoints = list()
	waypoints.append(Waypoint(490, 467, const_toee.rotation_0000_oclock, 1000))
	waypoints.append(Waypoint(488, 469, const_toee.rotation_0300_oclock, 1000))
	waypoints.append(Waypoint(493, 471, const_toee.rotation_0300_oclock, 1000))
	chick.npc_waypoints_set(waypoints)
	return

# import tezts
# tezts.hu1()
def hu1():
	npc = toee.game.obj_create(14702, utils_obj.sec2loc(491, 466))
	npc.npc_flag_unset(toee.ONF_KOS)
	waypoints = list()
	d = 0
	waypoints.append(Waypoint(491-d, 466, const_toee.rotation_0000_oclock, 500, WaypointFlag.Delay, 0))
	d += 2
	waypoints.append(Waypoint(491-d, 466, const_toee.rotation_0300_oclock, 1000, WaypointFlag.Delay | WaypointFlag.Animate, 32 + const_animate.NormalAnimType.Falldown))
	d += 2
	waypoints.append(Waypoint(491-d, 466, const_toee.rotation_0300_oclock, 1000, WaypointFlag.Delay | WaypointFlag.Animate, 32 + const_animate.NormalAnimType.Death))
	d += 2
	waypoints.append(Waypoint(491-d, 466, const_toee.rotation_0300_oclock, 1000, WaypointFlag.Delay | WaypointFlag.Animate, 32 + const_animate.NormalAnimType.Death2))
	d += 2
	waypoints.append(Waypoint(491-d, 466, const_toee.rotation_0300_oclock, 1000, WaypointFlag.Delay | WaypointFlag.Animate, 32 + const_animate.NormalAnimType.Death3))
	d += 2
	waypoints.append(Waypoint(491-d, 466, const_toee.rotation_0300_oclock, 1000, WaypointFlag.Delay | WaypointFlag.Animate, 32 + const_animate.NormalAnimType.SkillBarbarianRage))
	d += 2
	waypoints.append(Waypoint(491-d, 466, const_toee.rotation_0300_oclock, 1000, WaypointFlag.Delay | WaypointFlag.Animate, 32 + const_animate.NormalAnimType.Conceal))
	d += 2
	waypoints.append(Waypoint(491-d, 466, const_toee.rotation_0300_oclock, 1000, WaypointFlag.Delay | WaypointFlag.Animate, 32 + const_animate.NormalAnimType.FeatTrack))
	d += 2
	waypoints.append(Waypoint(491-d, 466, const_toee.rotation_0300_oclock, 1000, WaypointFlag.Delay | WaypointFlag.Animate, 32 + const_animate.NormalAnimType.Trip))
	d += 2
	waypoints.append(Waypoint(491-d, 466, const_toee.rotation_0300_oclock, 1000, WaypointFlag.Delay | WaypointFlag.Animate, 32 + const_animate.NormalAnimType.Examine))
	d += 2
	waypoints.append(Waypoint(491-d, 466, const_toee.rotation_0300_oclock, 1000, WaypointFlag.Delay | WaypointFlag.Animate, 32 + const_animate.NormalAnimType.Flurry))
	d += 2
	waypoints.append(Waypoint(491-d, 466, const_toee.rotation_0300_oclock, 1000, WaypointFlag.Delay | WaypointFlag.Animate, 32 + const_animate.NormalAnimType.Kistrike))
	d += 2
	waypoints.append(Waypoint(491-d, 466, const_toee.rotation_0300_oclock, 1000, WaypointFlag.Delay | WaypointFlag.Animate, 32 + const_animate.NormalAnimType.Throw2))
	d = 2
	waypoints.append(Waypoint(491-d, 466, const_toee.rotation_0300_oclock, 1000, WaypointFlag.Delay | WaypointFlag.Animate, 32 + const_animate.NormalAnimType.AbjurationCasting))
	d += 2
	waypoints.append(Waypoint(491-d, 466, const_toee.rotation_0300_oclock, 1000, WaypointFlag.Delay | WaypointFlag.Animate, 32 + const_animate.NormalAnimType.DivinationCasting))
	d += 2
	waypoints.append(Waypoint(491-d, 466, const_toee.rotation_0300_oclock, 1000, WaypointFlag.Delay | WaypointFlag.Animate, 32 + const_animate.NormalAnimType.EnchantmentCasting))
	d += 2
	waypoints.append(Waypoint(491-d, 466, const_toee.rotation_0300_oclock, 1000, WaypointFlag.Delay | WaypointFlag.Animate, 32 + const_animate.NormalAnimType.EvocationCasting))
	d += 2
	waypoints.append(Waypoint(491-d, 466, const_toee.rotation_0300_oclock, 1000, WaypointFlag.Delay | WaypointFlag.Animate, 32 + const_animate.NormalAnimType.IllusionCasting))
	d += 2
	waypoints.append(Waypoint(491-d, 466, const_toee.rotation_0300_oclock, 1000, WaypointFlag.Delay | WaypointFlag.Animate, 32 + const_animate.NormalAnimType.NecromancyCasting))
	d += 2
	waypoints.append(Waypoint(491-d, 466, const_toee.rotation_0300_oclock, 1000, WaypointFlag.Delay | WaypointFlag.Animate, 32 + const_animate.NormalAnimType.TransmutationCasting))

	npc.npc_waypoints_set(waypoints)

	waypoints2 = npc.npc_waypoints_get()
	for wp in waypoints2:
		print(wp)

	return

# import tezts
# tezts.pig1()
def pig1():
	npc = toee.game.obj_create(14368, utils_obj.sec2loc(491, 466))
	npc.npc_flag_unset(toee.ONF_KOS)
	waypoints = list()
	d = 0
	waypoints.append(Waypoint(491-d, 466, const_toee.rotation_0000_oclock, 500, WaypointFlag.Delay, 0))
	d += 2
	waypoints.append(Waypoint(491-20, 466, const_toee.rotation_0300_oclock, 1000, WaypointFlag.Delay | WaypointFlag.Animate, const_animate.WeaponAnim.Run))
	d += 2
	waypoints.append(Waypoint(491-d, 466, const_toee.rotation_0300_oclock, 1000, WaypointFlag.Delay | WaypointFlag.Animate, 32 + const_animate.NormalAnimType.Falldown))
	d += 2
	waypoints.append(Waypoint(491-d, 466, const_toee.rotation_0300_oclock, 1000, WaypointFlag.Delay | WaypointFlag.Animate, 32 + const_animate.NormalAnimType.Death))
	d += 2
	waypoints.append(Waypoint(491-d, 466, const_toee.rotation_0300_oclock, 1000, WaypointFlag.Delay | WaypointFlag.Animate, 32 + const_animate.NormalAnimType.Death2))
	d += 2
	waypoints.append(Waypoint(491-d, 466, const_toee.rotation_0300_oclock, 1000, WaypointFlag.Delay | WaypointFlag.Animate, 32 + const_animate.NormalAnimType.Death3))
	d += 2
	waypoints.append(Waypoint(491-d, 466, const_toee.rotation_0300_oclock, 1000, WaypointFlag.Delay | WaypointFlag.Animate, 32 + const_animate.NormalAnimType.SkillBarbarianRage))
	d += 2
	waypoints.append(Waypoint(491-d, 466, const_toee.rotation_0300_oclock, 1000, WaypointFlag.Delay | WaypointFlag.Animate, 32 + const_animate.NormalAnimType.Special1))
	d += 2
	waypoints.append(Waypoint(491-d, 466, const_toee.rotation_0300_oclock, 1000, WaypointFlag.Delay | WaypointFlag.Animate, 32 + const_animate.NormalAnimType.Special2))
	d += 2
	waypoints.append(Waypoint(491-d, 466, const_toee.rotation_0300_oclock, 1000, WaypointFlag.Delay | WaypointFlag.Animate, 32 + const_animate.NormalAnimType.Special3))
	d += 2
	waypoints.append(Waypoint(491-d, 466, const_toee.rotation_0300_oclock, 1000, WaypointFlag.Delay | WaypointFlag.Animate, 32 + const_animate.NormalAnimType.Special4))

	npc.npc_waypoints_set(waypoints)

	waypoints2 = npc.npc_waypoints_get()
	for wp in waypoints2:
		print(wp)

	return

# import tezts
# tezts.hu2()
def hu2():
	npc = toee.game.obj_create(14702, utils_obj.sec2loc(491, 466))
	npc.npc_flag_unset(toee.ONF_KOS)
	waypoints = list()
	d = 0
	waypoints.append(Waypoint(491-d, 466, const_toee.rotation_0000_oclock, 500, WaypointFlag.Delay, 0))
	d += 2
	for i in range(0, 64):
		waypoints.append(Waypoint(491-d, 466, const_toee.rotation_0300_oclock, 1000, WaypointFlag.Delay | WaypointFlag.Animate, 64 + 28 - 32))

	npc.npc_waypoints_set(waypoints)

	waypoints2 = npc.npc_waypoints_get()
	for wp in waypoints2:
		print(wp)

	return