#Tip Calculator

#Greeting to program
print("Welcome to Tip Calculator!")

#inputs from user
total_bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10,12, or 15? "))
split = int(input("How many people to split the bill? "))



calc_percentage_tip = percentage_tip / 100 * total_bill
calc_total_bill = total_bill + calc_percentage_tip
calc_split = calc_total_bill / split

#final_amount = "{:.2f}".format(calc_split)
print(f"Each person should pay: ${round(calc_split,2):.2f}")
