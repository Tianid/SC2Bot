import enum
import numpy as np

class strategys:
    # id = -1
    # action = ""
    enemy_unit_id = []
    smart_actions = []
    def __init__(self,strategy_type):
        if strategy_type == "tvp":
        



            self.smart_actions.append("SCOUT")
            self.smart_actions.append("3 BARACKS, one of them with REACTOR and two of them with TECH LAB")
            self.smart_actions.append("build FACTORY with TECH LAB")
            self.smart_actions.append("build 2 STARPORT with REACTOR")
            self.smart_actions.append("build  STARPORT with TECH LAB")
            self.smart_actions.append("make some GHOSTS and VIKINGS")
            self.smart_actions.append("use SCAN and build STARPORT with TECH LAB then train RAVEN")
            self.smart_actions.append("get ready for photon cannon rush, build BARACKS and BUNKERS, train MARINE")
            self.smart_actions.append("build many VIKINGS")
            self.smart_actions.append("MMM")
            self.smart_actions.append("build 3 FACTORY, train some THORS")



    def scout_action(self):
        self.id = 0
        self.action = "SCOUT"
        self.enemy_unit_id = []

    def T_v_P_action_one(self):
        self.id = 1
        self.action = "3 BARACKS, one of them with REACTOR and two of them with TECH LAB"
        self.enemy_unit_id = [133, 72]

    def T_v_P_action_two(self):
        self.id = 2
        self.action = "build FACTORY with TECH LAB "
        self.enemy_unit_id = [72, 71]

    def T_v_P_action_three(self):
        self.id = 3
        self.action = "build 2 STARPORT with REACTOR"
        self.enemy_unit_id = [72, 71, 67]

    def T_v_P_action_four(self):
        self.id = 4
        self.action = "build  STARPORT with TECH LAB"
        self.enemy_unit_id = [72, 67]

    def T_v_P_action_five(self):
        self.id = 5
        self.action = "make some GHOSTS and VIKINGS"
        self.enemy_unit_id = [133,68,70]
    def T_v_P_action_six(self):
        self.id = 6
        self.action = "use SCAN and build STARPORT with TECH LAB then train RAVEN"
        self.enemy_unit_id = [133,68,69]
    def T_v_P_action_seven(self):
        self.id = 7
        self.action = "get ready for photon cannon rush, build BARACKS and BUNKERS, train MARINE"
        self.enemy_unit_id = [63]
    def T_v_P_action_eight(self):
        self.id = 8
        self.action = "build many VIKINGS"
        self.enemy_unit_id = [133,70,64,67]
    def T_v_P_action_nine(self):
        self.id = 9
        self.action = "MMM"
        self.enemy_unit_id = [133,70,71]
    def T_v_P_action_ten(self):
        self.id = 10
        self.action = "build 3 FACTORY, train some THORS"
        self.enemy_unit_id = [133,67,70,71]
