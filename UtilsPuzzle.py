from constraint import *
from operator import itemgetter
from itertools import groupby


class UtilsBreedPuzzle:
    def __init__(self):
        # variables for the puzzle
        self.names = ['Beany', 'Cheetah', 'Thor', 'Suzie']
        self.breeds = ['Boxer', 'Collie', 'Shepherd', 'Terrier']
        self.bests = ['Plank', 'Poles', 'Tire', 'Tunnel']

        # domain of variables for the puzzle
        self.rankings = [1, 2, 3, 4]

    def get_variables(self):
        return self.names + self.breeds + self.bests

    def get_domain(self):
        return self.rankings

    def not_constraint(self, v1, v2):
        return v1 != v2

    def is_constraint(self, v1, v2):
        return v1 == v2

    def one_after_constraint(self, v1, v2):
        return v1 - v2 == 1

    def get_alldifferent_constraints(self):
        builtin_constraint_variables = []

        builtin_constraint_variables.append({'constraint': AllDifferentConstraint(), 'variables': self.names})
        builtin_constraint_variables.append({'constraint': AllDifferentConstraint(), 'variables': self.breeds})
        builtin_constraint_variables.append({'constraint': AllDifferentConstraint(), 'variables': self.bests})

        return builtin_constraint_variables

    def get_problem_constraints(self):
        constraint_variables = []

        ''' 
            7. Suzie is not a Shepherd and Beany doesn’t like the tunnel
            domain value of suzie and shepherd should not be equal
            domain value of beany and tunnel should not be equal 
        '''
        constraint_variables.append({'constraint': self.not_constraint, 'variables': ['Beany', 'Tunnel']})
        constraint_variables.append({'constraint': self.not_constraint, 'variables': ['Suzie', 'Shepherd']})

        ''' 
            4. Thor doesn’t like the plank and didn’t come 2nd
            domain value of thor and domain value of plank should not be equal
            domain value of thor should not be 2 as thor didn't come 2nd
        '''
        constraint_variables.append({'constraint': self.not_constraint, 'variables': ['Thor', 'Plank']})
        constraint_variables.append({'constraint': lambda cr1: cr1 != 2, 'variables': ['Thor']})

        ''' 
            3. Cheetah and the dog who loves the poles were 1st and 3rd
            domain value of cheetah is 1 as Cheetah came 1st
            domain value of the dog who love poles is 3
            domain value of cheetah and pole should not be equal as cheetah and dog love poles are different
        '''
        constraint_variables.append({'constraint': lambda cr1: cr1 == 1, 'variables': ['Cheetah']})
        constraint_variables.append({'constraint': lambda cr1: cr1 == 3, 'variables': ['Poles']})
        constraint_variables.append({'constraint': self.not_constraint, 'variables': ['Cheetah', 'Poles']})

        ''' 
            5. Cheetah either loves the tunnel or she came 4th
            since cheetah came 1st according to clue 3, cheetah loves tunnel
        '''
        constraint_variables.append({'constraint': self.is_constraint, 'variables': ['Cheetah', 'Tunnel']})

        ''' 
            1. Only the winning dog has the same initial letter in name and breed
            since cheetah is 1st, breed of cheetah should start with c which is collie
            all the other combinations should be ruled out - beany, boxer | thor, terrier | suzie, shepherd
        '''
        constraint_variables.append({'constraint': self.is_constraint, 'variables': ['Cheetah', 'Collie']})
        constraint_variables.append({'constraint': self.not_constraint, 'variables': ['Beany', 'Boxer']})
        constraint_variables.append({'constraint': self.not_constraint, 'variables': ['Thor', 'Terrier']})
        constraint_variables.append({'constraint': self.not_constraint, 'variables': ['Suzie', 'Shepherd']})

        '''
            6. The dog who loves the plank came 1 position after the dog who loves the poles
            difference between domain values of plank and pole should be 1
        '''
        constraint_variables.append({'constraint': self.one_after_constraint, 'variables': ['Plank', 'Poles']})

        '''
            2. The Boxer ranked 1 position after the Shepherd. None of them likes the tunnel, nor jumping through the tire
            difference between domain value of boxer and shepherd should be 1
            domain value of boxer and tunnel, tire should not be equal
            domain value of shepherd and tunnel, tire should not be equal
        '''
        constraint_variables.append({'constraint': self.not_constraint, 'variables': ['Boxer', 'Tunnel']})
        constraint_variables.append({'constraint': self.not_constraint, 'variables': ['Boxer', 'Tire']})
        constraint_variables.append({'constraint': self.not_constraint, 'variables': ['Shepherd', 'Tunnel']})
        constraint_variables.append({'constraint': self.not_constraint, 'variables': ['Shepherd', 'Tire']})
        constraint_variables.append({'constraint': self.one_after_constraint, 'variables': ['Boxer', 'Shepherd']})

        return constraint_variables

    def print_solution(self, solution):
        grouped = groupby((sorted(solution.items(), key=itemgetter(1))), key=itemgetter(1))

        sol = {}
        for key, group in grouped:
            items = [None] * (len(self.names) - 1)
            name = None
            for g in dict(group).keys():
                if g in self.breeds:
                    items[0] = g
                elif g in self.bests:
                    items[1] = g
                else:
                    name = g
            items[2] = key
            sol[name] = items

        print("{:<12s}{:<12s}{:<12s}{:<12s}".format("Name", "Breed", "Best", "Ranking"))

        for key in sol:
            print("{:<12s}{:<12s}{:<12s}{:<12d}".format(key, sol[key][0], sol[key][1], sol[key][2]))