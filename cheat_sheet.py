#test project for bill splitter
running_bill = 0
num_of_friends = float(input("How many people are splitting the bill? "))
appetizers = float(input("Cost of appetizers"))
maincourses= float(input("Cost of main courses"))
drinks= float(input("Cost of drinks"))
desserts= float(input("Cost of desserts"))
tips = float(input("If tip was added, add amount here"))
running_bill += appetizers + maincourses + drinks + desserts + tips
final_bill = running_bill / num_of_friends
running_bill = round(running_bill, 2)
each_pays = round(final_bill, 2)
print(f"Your total bill is {running_bill} SAR")
print(f"Each person should pay {each_pays} SAR")