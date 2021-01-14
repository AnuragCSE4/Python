####### Functions Defining ##############
def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def mul(a,b):
    return(a*b)
def div(a,b):
    return(a/b)
def mod(a,b):
    return(a%b)
def pow(a,b):
    return(a**b)
result = 1
while result==1:
    choice = input("""
    Please choose any options from following.
    Press 1 for addition
    Press 2 for subtraction
    Press 3 for multiplication
    Press 4 for Division
    Press 5 for Finding reminder or Modulo [example : 10/3 = 1 (remainder)]
    Press 6 for Power [example : (5)^3 = 5x5x5 = 125]
    Press X for exit
    Enter Your choice : """)
    #print(choice,type(choice))                 # for checking the type of received input.
    if choice.lower() == 'x':
        print("\n#############\tThanks for using !!!\t##################\n")
        break
    else:
        choice = int(choice)
        #print(choice,type(choice))
        if choice < 1 or choice > 6 :
            print("\nPlease choose a valid\n")
        else:
            num1 = int(input(" Enter 1st Number : "))
            num2 = int(input(" Enter 2nd Number : "))
            if choice == 1 : 
            #   add = add(num1,num2)       #If you choose the variable name as the name of the function then it will run only one time.
            # And in next iteration it terminate the execution.
                sum = add(num1, num2)
                print("\tAddition : ",num1," + ", num2, " = ",sum)
            elif choice == 2 :
                subtract = sub(num1,num2)
                print("\tSubtraction : ",num1," - ", num2, " = ",subtract)
            elif choice == 3 :
                multi = mul(num1,num2)
                print("\tMultiplication : ",num1," x ", num2, " = ",multi)
            elif choice == 4 :
                division = div(num1,num2)
                print("\tDivision : ",num1," / ", num2, " = ",division)
            elif choice == 5 :
                modulo = mod(num1,num2)
                print("\tModulo : ",num1," % ", num2, " = ",modulo,"remainder")
            elif choice == 6 :
                power = pow(num1,num2)
                print("\tPower : ",num1," ^ ", num2, " = ",power)
            else:
                result == 0
    if result != 0:
        while True :
            choice=input("Do you wanna try again ? \nPress Y for Continue \nPress X for Exit \nEnter Your choice : ")
            if choice.lower() == 'x':
                print("\n#############\tThanks for using !!!\t##################\n")
                result=0
                break
            elif choice.lower() == 'y' :
                result=1
                break
            else:
                print("\nPlease choose a valid option from following")
#########################################################################################################################################
################################################# Same Program in optimized way #########################################################
#########################################################################################################################################
'''
def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def mul(a,b):
    return(a*b)
def div(a,b):
    return(a/b)
def mod(a,b):
    return(a%b)
def pow(a,b):
    return(a**b)
result = 1
while result==1:
    # choice = input("Please choose any options from following. \nPress 1 for addition \nPress 2 for subtraction \nPress 3 for multiplication \nPress 4 for Division \nPress 5 for Finding reminder or Modulo [example : 10/3 = 1 (remainder)] \nPress 6 for Power [example : (5)^3 = 5x5x5 = 125] \nPress X for exit \nEnter Your choice : ")
    choice = input("""
    Please choose any options from following.
    Press 1 for addition
    Press 2 for subtraction
    Press 3 for multiplication
    Press 4 for Division
    Press 5 for Finding reminder or Modulo [example : 10/3 = 1 (remainder)]
    Press 6 for Power [example : (5)^3 = 5x5x5 = 125]
    Press X for exit
    Enter Your choice : """)
    if choice.lower() == 'x':
        print("\n#############\tThanks for using !!!\t##################\n")
        break
    else:
        choice = int(choice)
        if choice < 1 or choice > 6 :
            print("\nPlease choose a valid\n")
        else:
            num1 = int(input(" Enter 1st Number : "))
            num2 = int(input(" Enter 2nd Number : "))
            if choice == 1 : 
                print("\tAddition : ",num1," + ", num2, " = ",add(num1,num2))
            elif choice == 2 :
                print("\tSubtraction : ",num1," - ", num2, " = ",sub(num1,num2))
            elif choice == 3 :
                print("\tMultiplication : ",num1," x ", num2, " = ",mul(num1,num2))
            elif choice == 4 :
                print("\tDivision : ",num1," / ", num2, " = ",div(num1,num2))
            elif choice == 5 :
                print("\tModulo : ",num1," % ", num2, " = ",mod(num1,num2),"remainder")
            elif choice == 6 :
                print("\tPower : ",num1," ^ ", num2, " = ",pow(num1,num2))
            else:
                result == 0
    if result != 0:
        while True :
            result=input("Do you wanna try again ? \nPress 1 for Continue \nPress 0 for Exit \nEnter Your choice : ")
            result=int(result)   #using type casting because user can give any input.
            if result == 0 :
                print("\n#############\tThanks for using !!!\t##################\n")
                break
            elif result == 1 :
                break
            else:
                print("\nPlease choose a valid option from the following")

'''