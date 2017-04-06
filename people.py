# coding: utf-8
class People:
    pid = 0  # identify the single
    stamina = 10  # value determines the action times
    age_value = 0  # value represent for the people's age
    language_value = 0  # value influence the speaking style of the people: kind, neutral, negative
    aggressive_value = 0  # value influence the action decision: leave, attack
    memory_table = {}  # value record the all the people met before, and the impression

    def __init__(self, new_id, setting=None):
        """
        random init the personal attribution,or inherit from parent, or set by a dict
        """
        self.pid = new_id
        if setting:
            if isinstance(setting, People):
                self.inherit(setting)
            pass
        else:
            # random init
            pass

    def inherit(self, parent):
        # slightly change parent's attribute and save value for new baby
        pass

    def move_a_step(self):
        pass

    def collect_food(self):
        pass

    def action(self):
        pass

    def reaction(self):
        pass

    def die(self):
        pass


if __name__ == '__main__':
    print 'People defined here'
