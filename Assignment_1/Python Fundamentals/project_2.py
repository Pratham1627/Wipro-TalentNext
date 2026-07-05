# Project 2: Calculate server operating cost.

# Cost per hour
cost_per_hour = 0.51

# Cost per day
cost_per_day = cost_per_hour * 24

# Cost per week
cost_per_week = cost_per_day * 7

# Cost per month (30 days)
cost_per_month = cost_per_day * 30

# Budget available
budget = 918

# Number of days the server can run
days = budget / cost_per_day

print("Cost to operate one server per day: $", round(cost_per_day, 2))
print("Cost to operate one server per week: $", round(cost_per_week, 2))
print("Cost to operate one server per month: $", round(cost_per_month, 2))
print("Number of days one server can operate with $918:", round(days, 2))
