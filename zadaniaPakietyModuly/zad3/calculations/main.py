import deposit_calculation

starting_amount = float(input("Kwota wpłaty na lokatę (w PLN): "))
percentage = float(input("Oprocentowanie lokaty: "))
period = int(input("Na ile lat lokata: "))

ending_amount = deposit_calculation.deposit_value(starting_amount, percentage, period)
print(f"Po {period} latach wartość Twojej lokaty wyniesie: {ending_amount}")