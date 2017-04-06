# coding: utf-8
import json
from people import People


class CruelWord:
    init_population = 1000  # init population
    max_population = 1000000  # population to emit a disaster
    lifetime = 10000  # nature die days for a people
    people_table = {}  # record all the people

    def __init__(self, config_file=''):
        if config_file:
            with open(config_file, 'r') as reader:
                json_data = json.load(reader)
                self.init_population = json_data['init_population']
                self.max_population = json_data['max_population']
                self.lifetime = json_data['lifetime']
        else:
            pass

    def run(self):
        pass

    def log(self):
        pass

    def disaster(self):
        pass


if __name__ == '__main__':
    new_word = CruelWord()
    new_word.run()
