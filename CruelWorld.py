# coding: utf-8
import json
from People import People
import random


def keep_bound(value, bound):
    return min(max(value, bound[0]), bound[1])


class CruelWorld:
    # === world settings ===
    # --- map setting ---
    map_width = 1000  # map's width
    map_length = 1000  # map's length
    # --- people's feature setting ---
    stamina_range = [5, 15]
    action_score_u_range = [-1, 1]
    action_score_d_range = [0, 0.66]
    average_lifetime = 1000  # nature die days for a people
    average_childbearing_age = average_lifetime / 2
    children_num_range = [1, 3]
    hunger_tolerance_range = [3, 5]
    # --- population setting ---
    init_population = 1000  # init population
    max_population = 1000000  # population to emit a disaster
    # --- food setting ---
    average_hunger_tolerance = sum(hunger_tolerance_range) / len(hunger_tolerance_range)
    average_food_production = max_population / average_hunger_tolerance
    # --- stochastic process setting ---
    max_init_variation = 0.1

    # === world component ===
    map = [[{'people_id_lst': [], 'food': 0} for j in range(map_length)] for i in range(map_width)]
    people_table = {}  # record all the people, the only place storage people instances
    active_list = []  # id list, record all people haven't finished their day
    inactive_list = []  # id list, record all people already finished their day ( useless now )

    def __init__(self, config_file=''):
        if config_file:
            with open(config_file, 'r') as reader:
                json_data = json.load(reader)
                if json_data:
                    pass
                    # load data wait to completed
                    self.init_population = json_data['init_population']
                    self.max_population = json_data['max_population']
                    self.lifetime = json_data['lifetime']
                    self.map = [[{'people_id_lst': [], 'food': 0} for j in range(self.map_length)] for i in range(self.map_width)]
                    #  .....
        else:
            pass

    def run(self):
        self.init_the_world()
        while not self.world_end():
            self.start_new_day()
        pass

    def log(self, log_str):
        pass

    def init_the_world(self):
        # === init the population ===
        for i in range(self.init_population):
            attri_table = self.generate_attri_table()
            self.people_table[i] = People(new_id=i, attri_table=attri_table)

        # === init the map: place people on map ===
        for pid in self.people_table:
            tmp_x_pos = random.randint(0, self.map_width)
            tmp_y_pos = random.randint(0, self.map_length)
            self.map[tmp_x_pos][tmp_y_pos]['people_id_lst'].append(pid)
            self.people_table[pid].move_to_position(tmp_x_pos, tmp_y_pos)

        # === init the inactive/ active list ===
        for pid in self.people_table:
            self.active_list.append(pid)
            self.inactive_list = []

    def generate_attri_table(self):
        ret = {}
        ...
        return ret

    def start_new_day(self):
        for pid in self.people_table:
            self.active_list.append(pid)
            self.inactive_list = []
        for
        pass

    def world_end(self):
        if ...:
            return True
        return False

    def disaster(self):
        pass


if __name__ == '__main__':
    new_world = CruelWorld()
    new_world.run()
