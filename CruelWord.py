# coding: utf-8
import json
from people import People


class CruelWord:

    # map setting
    map_w = 1000  # map's width
    map_l = 1000  # map's length
    map = [[{'people_id_lst': [], 'food':0} for j in range(map_l)] for i in range(map_w)]

    # people's feature
    stamina_range = [5, 15]
    action_score_u_range = [-1, 1]
    action_score_d_range = [0, 0.66]
    average_lifetime = 1000  # nature die days for a people

    # population setting
    init_population = 1000  # init population
    max_population = 1000000  # population to emit a disaster
    people_table = {}  # record all the people

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
                    self.map = [[{'people_id_lst': [], 'food': 0} for j in range(self.map_l)] for i in range(self.map_w)]
                    #  .....
        else:
            pass

    def run(self):
        self.init_the_word()
        pass

    def log(self, log_str):
        pass

    def init_the_word(self):
        # init the population
        for i in range(self.init_population):
            tmp_p = People(new_id=i)
        # init the map, place people on map
        # init the inactive/ active list
        pass

    def disaster(self):
        pass


if __name__ == '__main__':
    new_word = CruelWord()
    new_word.run()
