from enum import Enum

class UnitAction(Enum):

	ACTION_UNIT_DRAW  = 0
	ACTION_UNIT_SEED = 1
	ACTION_UNIT_EAT = 2
	ACTION_UNIT_PUNISH = 3
	ACTION_GO_FORWARD = 4
	ACTION_EAT = 5
	ACTION_EAT_BACKWARDS = 6
	ACTION_UNIT_NONE = 16