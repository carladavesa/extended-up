from unified_planning.shortcuts import *

n = 5
lower_bound = 0
upper_bound = 4
instance = [3,4,2,1,0]

# ------------------------------------------------ Problem -------------------------------------------------------------

pancake_problem = Problem('pancake_problem')

pancake = Fluent('pancake', ArrayType(n, IntType(lower_bound, upper_bound)))
pancake_problem.add_fluent(pancake, default_initial_value=lower_bound)
pancake_problem.set_initial_value(pancake, instance)

flip = InstantaneousAction('flip', f=IntType(1, n-1))
f = flip.parameter('f')
b = RangeVariable('b', 0, f)
flip.add_effect(pancake[b], pancake[f - b], forall=[b])
pancake_problem.add_action(flip)

for i in range(n):
    pancake_problem.add_goal(Equals(pancake[i], i))

costs: Dict[Action, Expression] = {
    flip: Int(1),
}
pancake_problem.add_quality_metric(MinimizeActionCosts(costs))