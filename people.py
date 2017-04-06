# coding: utf-8
class People:
    id = 0  # identify the single
    active_value = 0  # value determines the action times
    age_value = 0  # value represent for the people's age
    language_value = 0  # value influence the speaking style of the people: kind, neutral, negative
    aggressive_value = 0  # value influence the action decision: leave, attack
    familiar_table = {}  # value record the all the people met before, and the impression

    def __init__(self, parent=None):
        """
        random init the personal attribution
        """
        if parent:
            pass
        else:
            pass

    def talk(self):
        pass

    def response(self):
        pass

    def act(self):
        pass

    def die(self):
        pass


if __name__ == '__main__':
    print 'People defined here'
