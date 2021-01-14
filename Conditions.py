age = int(input('Enter your age : '))
if age < 13:
    print("You are a kid ")
elif age <= 18:
    print('You are a Teenager')
elif age >18 and age <= 30:
    print("You are a Yougth")
else:
    print("You are older than 30 year")