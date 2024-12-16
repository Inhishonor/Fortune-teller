
def main():
    #Ask what the name and age is.
    name = input("What is your first name? ")
    print("Welcome to the Fortune Teller of Doom!!!")
    age = input("What is your age? ")
    #Print Name
    print("Hello "+ name + ".")
    x = len(name)
    #Determine Message
    if x < 4 or x == 4:
        print(ds)
    elif x > 4 and x < 7:
        y = float(age)
        if y < 10:
            print(ud)
        elif y > 10 and y < 20:
            print(ss)
        elif y > 20 and y < 50:
            print(sc)
        elif y > 50 and y < 100:
            print(ni)
        else:
            print(ys)
    else:
        nn = input("Pick a new number between 1 and 100. ")
        z = float(nn)
        if z < 50:
            print("You will walk into the mouth of a Volcano while tap-dancing!")
        else:
            print("While you are brushing your teeth you will be carried away by faries!")

if __name__ == '__main__':
	main()
