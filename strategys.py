import enum
import numpy as np

class strategys:
    # id = -1
    # action = ""
    enemy_unit_id = []
    smart_actions = []
    def __init__(self,strategy_type):
        if strategy_type == "tvp":
        



            self.smart_actions.append("scout")
            self.smart_actions.append("3 baracks, one of them with reactor and two of them with tech lab")
            self.smart_actions.append("build factory with tech lab")
            self.smart_actions.append("build 2 starport with reactor")
            self.smart_actions.append("build starport tech lab")
    




    def T_v_P_part_one(self):
        self.id = 1
        self.action = "3 baracks, one of them with reactor and two of them with tech lab"
        self.enemy_unit_id = [133, 72]

    def T_v_P_part_two(self):
        self.id = 2
        self.action = "build factory with tech lab "
        self.enemy_unit_id = [72, 71]

    def T_v_P_part_three(self):
        self.id = 3
        self.action = "build 2 starport with reactor"
        self.enemy_unit_id = [72, 71, 67]

    def T_v_P_part_four(self):
        self.id = 4
        self.action = "build  starport tech lab"
        self.enemy_unit_id = [72, 67]