stack = []

def push():
    element = input(("Enter the elements : "))

    stack.append(element)

    print(stack)


def pop_element():
    if not stack:
        print("Stack is empty")

    else:
        e = stack.pop()
        print("removed element : ", e)
        print(stack)


while True:
            print("Select : ")
            print("1.Push")
            print("2.Pop")
            print("3.Quite")

            choice = int(input())

            if choice == 1:
                push()

            elif choice == 2:
                pop_element()

            elif choice == 3:
                print("Quiting......")
                break

            else:
                print("Please enter valid input")