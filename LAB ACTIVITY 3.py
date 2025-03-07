#custom function
def check_number(x):
    if x %2 == 0:
        print(x, "is an Even number.")
    else:
        print(x, "is an Odd number")


#main code
num = int(input("Enter a number: "))
check_number(num)

while True:
    a = input("Run again? (yes/no): ")
    if a == "yes":
        num = int(input("Enter a number: "))
        check_number(num)
    else:
        print("Exiting Program.")
        break

