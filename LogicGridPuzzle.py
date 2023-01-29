class LogicGridPuzzle:
    def __init__(self, problem):
        self.problem = problem

    def add_variables(self, variables, domain):
        self.problem.addVariables(variables, domain)

    def add_constraints(self, constraint_variables):
        for c_v in constraint_variables:
            self.problem.addConstraint(c_v['constraint'], c_v['variables'])

    def get_solution(self):
        return self.problem.getSolution()

    def get_solutions(self):
        return self.problem.getSolutions()

    def get_solutions_count(self):
        return len(self.problem.getSolutions())