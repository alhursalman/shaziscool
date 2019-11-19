print ("Hello and welcome to the calculator!")
x=0
ansa = input ("Would you like to do a calculation?(yes/no)" )
if ansa.lower() ==("y") or ("yes"):
    x+=1
while x == 1:
    oppboy = input ("Which operation would you like? (Inputs are add, subtract, multiply, divide) Answer:")
    if oppboy == ("add"):
        fn = float(input("First number: "))
        sn = float(input("Second number: "))
        print("Your answer is", fn+sn, ".")
        dodobird = input("Another calculation? (y/n):")
        if dodobird!=("y"):
            print ("ok maybe next time :+L")
            x+=1
    elif oppboy == ("multiply"):
        fn = float(input("First number: "))
        sn = float(input("Second number: "))
        print("Your answer is", fn*sn, ".")
        dodobird = input("Another calculation? (y/n):")
        if dodobird!=("y"):
             print ("ok maybe next time ;(")           
             x+=1
    elif oppboy == ("subtract"):
        fn = float(input("First number: "))
        sn = float(input("Second number: "))
        print("Your answer is", fn-sn, ".")
        dodobird = input("Another calculation? (y/n):")
        if dodobird!=("y"):
            print ("ok maybe next time :-c")
            x+=1
    elif oppboy == ("divide"):
        fn = float(input("First number: "))
        sn = float(input("Second number: "))
        print("Your answer is", fn/sn, ".")
        dodobird = input("Another calculation? (y/n):")
        if dodobird!=("y"):
            print ("ok maybe next time :/")
            x+=1
    else:
        print("That's not an operation.")