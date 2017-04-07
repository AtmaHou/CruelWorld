# coding: utf-8
class People:

    # === innate attribute ===
    pid = 0  # identify the single
    language_value = 0  # value influence the speaking style of the people: kind, neutral, negative
    aggressive_value = 0  # value influence the action decision: leave, attack
    pocket_size = 10  # max number of carried food
    hunger_tolerance = 3  # die days without having food
    life_expectancy = 1000  # average age of death
    action_score_u = 0  # used to generate action & reaction decision
    action_score_d = 0.33  # used to generate action & reaction decision
    observation_ability = 0.5  # used to influence reaction decision

    # === variable attribute ===
    # --- inner part ---
    age = 0  # value represent for the people's age
    hunger = 0
    stamina = 10  # value determines the action times
    # --- environmental part ---
    carried_food = 0
    x_pos = 0  # position on map
    y_pos = 0  # position on map
    memory_table = {}  # value record the all the visited place, interaction + food gained

    # stochastic process setting
    max_genetic_variation = 0.1

    def __init__(self, new_id, attri_table=None):
        """
        random init the personal attribution,or inherit from parent, or set by a dict
        """
        self.pid = new_id
        if attri_table:
            if isinstance(attri_table, People):
                self.inherit(attri_table)
            pass
        else:
            # random init
            pass

    def inherit(self, parent):
        # slightly change parent's attribute and save value for new baby
        pass

    def move_a_step(self):
        pass

    def move_to_position(self, p_x, p_y):
        self.x_pos = p_x
        self.y_pos = p_y

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
