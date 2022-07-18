while(True):
    print("Press q to quit")
    a=input("Enter a number: ")
    if a=='q' :
        break
    
    try:
        a=int(a)
        if(a>6):
            print("You have entered a number greater than 6")
        elif a==6:
            print("Number is equal to 6")
        else:
            print("You have entered a number less than 6")

    except Exception as e:
        print(f"Only Numbers are allowed Exception : {e}")        

print(" Thanks for playing this game")        
            