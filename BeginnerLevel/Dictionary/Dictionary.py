#1. Create a list of your friends names

friends = ['Nishchitha', 'Suman', 'Preethi', 'Chaithra', 'Amulya']

name_lengths = [(name, len(name)) for name in friends]

print(name_lengths)


#2. Program for calculating total expenses and the difference between them

your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

total_your_expense = sum(your_expenses.values())
total_partner_expense = sum(partner_expenses.values())

print(f"Your total expenses:",total_your_expense)
print(f"Your partner's total expenses:",total_partner_expense)

if total_your_expense > total_partner_expense:
    print("You spent more money overall.")
elif total_partner_expense > total_your_expense:
    print("Your partner spent more money overall.")
else:
    print("Both spent the same amount of money overall.")

max_diff = 0
diff_category = ""

for category in your_expenses:
    diff = abs(your_expenses[category] - partner_expenses[category])
    if diff > max_diff:
        max_diff = diff
        diff_category = category

print(f"The biggest spending difference is in '{diff_category}' with a difference of {max_diff}.") 