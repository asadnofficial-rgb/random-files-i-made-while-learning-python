is_citizen = True
age = 12
if  is_citizen and age >= 18:
    print("you can vote")
elif not is_citizen and age >= 18:
    print("you are not citizen")
elif not is_citizen and age < 18:
    print("you are not a citizen nor old enough")
else:
    print("you are not  old enough")