
#Call's fortune's
from fortune import ds, ud, ss, sc, ni, ys, lf, tv, bt
def main():
    #Ask what the name and age is.
    name = input("What is your first name? ")
    print("Welcome to the Fortune Teller of Doom!!!")
    age = input("What is your age? ")
    #Print Name
    print("Hello "+ name + ".")
    nameLength = len(name)
    #Determine Message
    if nameLength < 4 or nameLength == 4:
        print(ds)
    elif nameLength > 4 and nameLength < 7:
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
            print(tv)
    elif nameLength > 7 and nameLength < 11:
        print(lf)
    else:
        nn = input("Pick a new number between 1 and 100. ")
        z = float(nn)
        if z < 50:
            print(ys)
        else:
            print(bt)

if __name__ == '__main__':
    while True: 
        main()
