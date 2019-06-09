import multiprocessing
import random
import math
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from absl import app

import os.path

import numpy as np
import pandas as pd


from pysc2.agents import base_agent
from pysc2.env import sc2_env
from pysc2.lib import actions, features, units
from pysc2.lib import features
from custom_buildings import Zerg, Terran, Protoss
from strategys import strategys

from GUI import *

DATA_FILE = 'T_v_P'


# class DataBase:
#     conn = psycopg2.connect(dbname='Qlearning', user='postgress',
#                             password='pssword', host='localhost')
#     cursor = conn.cursor()
#
#     def get_Qtable(self):
#         self.cursor.execute('select "State" ,  "Action", "Value" from public."Value", public."State", public."Action" where fk_action_id = action_id and fk_state_id = state_id')
#         records = self.cursor.fetchall()
#         return records
#     def insert_new_state(self, state_id, state):
#         self.cursor.execute('INSERT INTO public."State"(state_id, "State")VALUES ({}, {}})'.format(state_id, state))
#
#     def update_qtable(self, value_id, action_id, state_id, value):
#         self.cursor.execute('UPDATE public."Value" SET  fk_action_id={}, fk_state_id={}, "Value"={} WHERE public.value_id = {}'.format(action_id,state_id,value, value_id))
#
#     def insert_new_record_into_db(self,value_id, action_id, state_id, value):
#         self.cursor.execute('INSERT INTO public."Value"(value_id, fk_action_id, fk_state_id, "Value") VALUES ({}, {}, {}, {})'.format(value_id,action_id,state_id,value))


class QLearningTable:
    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
        self.actions = actions
        self.lr = learning_rate
        self.gamma = reward_decay
        self.epsilon = e_greedy
        self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64)
        # self.disallowed_actions = {}

    def choose_action(self, observation):
        self.check_state_exist(observation)
        state_action = self.q_table.ix[observation, :]

        if np.random.uniform() < self.epsilon:
            # some actions have the same value
            state_action = state_action.reindex(np.random.permutation(state_action.index))

            action = state_action.idxmax()
        else:
            # choose random action
            action = np.random.choice(state_action.index)


        # state_action = self.q_table.ix[observation, :]
        # state_action = state_action.reindex(np.random.permutation(state_action.index))
        # print(str(state_action.idxmax()) + " max")
        # action = state_action.idxmax()
        return action

    def learn(self, s, a, r, s_):

        if s == s_:
            return

        self.check_state_exist(s_)
        self.check_state_exist(s)

        q_predict = self.q_table.ix[s, a]
        print(q_predict)

        s_rewards = self.q_table.ix[s_, :]

        if s_ != 'terminal':
            q_target = r + self.gamma * s_rewards.max()
        else:
            q_target = r

        self.q_table.ix[s, a] += self.lr * (q_target - q_predict)

    def set_state_value(self, s, a, v):
        self.q_table.ix[s, a] = v

    def check_state_exist(self, state):
        if state not in self.q_table.index:
            # append new state to q table
            self.q_table = self.q_table.append(
                pd.Series([0] * len(self.actions), index=self.q_table.columns, name=state))


class SupportAI(QObject, base_agent.BaseAgent):
    list_of_unic_enemy_buildings = []
    init_list_enemy_buildings = []
    state_list = []
    smart_actions = []
    rl_action = None
    signalSuperDupa = pyqtSignal(str)

    def __init__(self, game_type):
        super(SupportAI, self).__init__()

        self.previous_action = None
        self.previous_state = None
        self.init_smart_action_list(game_type)
        self.qlearn = QLearningTable(actions=list(range(len(self.smart_actions))))

        self.gui = qt_widget
        self.signalSuperDupa.connect(self.gui.handleSuperDupa)

        # self.data_base = DataBase()
        if os.path.isfile(DATA_FILE + '.gz'):
            self.qlearn.q_table = pd.read_pickle(DATA_FILE + '.gz', compression='gzip')
            print(self.qlearn.q_table)

    def init_smart_action_list(self, strategy_type):
        strategy = strategys(strategy_type)
        self.smart_actions = strategy.smart_actions

    def init_state_list(self):
        return np.zeros(45)

    def init_type_list_of_enemy_buildings(self):
        list = []
        for unit in Terran:
            list.append(unit)
        for unit in Protoss:
            list.append(unit)
        for unit in Zerg:
            list.append(unit)
        return list

    def set_unic_buildings_to_list_of_unic_buildings_from_screen_and_generate_new_state(self, obs):
        for unit in obs.observation.feature_units:
            if unit.unit_type not in self.list_of_unic_enemy_buildings and unit.owner != 1 and unit.owner != 16 and unit.unit_type in self.init_list_enemy_buildings:
                self.list_of_unic_enemy_buildings.append(unit.unit_type)
                self.new_state()

    def new_state(self):
        index = self.init_list_enemy_buildings.index(
            self.list_of_unic_enemy_buildings[len(self.list_of_unic_enemy_buildings) - 1])
        self.state_list[index] = 1

    def step(self, obs):
        super(SupportAI, self).step(obs)
        hz = obs.observation.feature_minimap[4].nonzero
        print(hz)

        list_of_showed_actions = []

        if obs.last():
            reward = obs.reward

            self.qlearn.learn(str(self.previous_state), self.previous_action, reward, 'terminal')

            self.qlearn.q_table.to_pickle(DATA_FILE + '.gz', 'gzip')
            self.qlearn.q_table.to_csv(DATA_FILE + '.csv')
            self.previous_action = None
            self.previous_state = None
            self.list_of_unic_enemy_buildings = []

            return actions.FUNCTIONS.no_op()

        if obs.first():
            self.init_list_enemy_buildings = self.init_type_list_of_enemy_buildings()
            self.state_list = self.init_state_list()

        self.set_unic_buildings_to_list_of_unic_buildings_from_screen_and_generate_new_state(obs)

        if self.previous_action is not None:
            self.qlearn.learn(str(self.previous_state), self.previous_action, 0, str(self.state_list))

        if np.any(self.previous_state != self.state_list):
            self.rl_action = self.qlearn.choose_action(str(self.state_list))

            self.previous_state = self.state_list.copy()
            self.previous_action = self.rl_action
            self.signalSuperDupa.emit(self.smart_actions[self.rl_action])

        print(self.smart_actions[self.rl_action] + " do action")
        print(str(self.rl_action) + " do action")
        print(self.list_of_unic_enemy_buildings)
        print(self.state_list)

        return actions.FUNCTIONS.no_op()


def main(unused_argv):
    agent = SupportAI(game_type)

    try:
        while True:
            with sc2_env.SC2Env(
                    map_name="Simple64",
                    players=[sc2_env.Agent(player_race),
                             sc2_env.Bot(enemy_race,
                                         sc2_env.Difficulty.very_easy)],
                    agent_interface_format=features.AgentInterfaceFormat(
                        feature_dimensions=features.Dimensions(screen=86, minimap=86),
                        use_feature_units=True),
                    step_mul=16,
                    game_steps_per_episode=0,
                    visualize=False,
                    realtime=True) as env:

                feats = features.Features(
                    features.AgentInterfaceFormat(
                        feature_dimensions=features.Dimensions(
                            screen=86,
                            minimap=86)))
                action_spec = feats.action_spec()

                agent.setup(env.observation_spec(), env.action_spec())

                timesteps = env.reset()
                agent.reset()

                while True:
                    step_actions = [agent.step(timesteps[0])]
                    feats = features.Features(
                        features.AgentInterfaceFormat(
                            feature_dimensions=features.Dimensions(
                                screen=86,
                                minimap=86)))
                    action_spec = feats.action_spec()
                    if timesteps[0].last():
                        break
                    timesteps = env.step(step_actions)

    except KeyboardInterrupt:
        pass


class sc_thread(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.sig = pyqtSignal()

    def run(self):
        print("sc-thread is started")
        self.run_main()

    def run_main(self):
        app.run(main)

    def __del__(self):
        print("sc-thread is over")



if __name__ == "__main__":

    player_race = sc2_env.Race.terran
    enemy_race = sc2_env.Race.protoss
    game_type = "tvp"

    qt_app = QApplication(sys.argv)
    qt_widget = W()

    sc_therad = sc_thread()
    sc_therad.start()

    # app.run(qt_app.exec_())
    sys.exit((qt_app.exec_()))


    # app.run(main)
