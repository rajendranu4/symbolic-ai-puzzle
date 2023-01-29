from LogicGridPuzzle import *
from UtilsPuzzle import *


if __name__ == '__main__':
    problem = Problem()
    puzzle = LogicGridPuzzle(problem)
    utils = UtilsBreedPuzzle()

    variables = utils.get_variables()
    domain = utils.get_domain()

    # variables are names, breeds and bests, domain is their ranking
    puzzle.add_variables(variables, domain)

    '''
       applying alldifferentconstraints to the problem since value of every variable is different
       ex. breed of each dog is different and no two dogs are from same breed
    '''
    alldifferent_constraints = utils.get_alldifferent_constraints()
    puzzle.add_constraints(alldifferent_constraints)

    print("Number of solutions after applying AllDifferentConstraint to the problem: {}".format(
        puzzle.get_solutions_count()))

    problem_constraints = utils.get_problem_constraints()
    puzzle.add_constraints(problem_constraints)

    print("\nNumber of solutions after applying all given constraints to the problem: {}".format(
        puzzle.get_solutions_count()))

    solution = puzzle.get_solution()
    # print(solution)

    print("\nSolution:\n")
    utils.print_solution(solution)