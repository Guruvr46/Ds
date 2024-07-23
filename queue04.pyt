queue = []

def enqueue():

   element = input("Enter the elements ")
   queue.append(element)

   print(element, " is added to queue!")


def dequeue():
   if not queue:
      print("Queue is empty")

   else:
      e = queue.pop()
      print("Removed elements are " , e)


def display():
   print(queue)


while True:
   print("Enter \n1.Enqueue \n2.Dequeue \n3.Print \n4.Quit")

   i = int(input())

   if i == 1:
      enqueue()

   elif i == 2:
      dequeue()

   elif i == 3:
      display()

   elif i == 4:
      print("Quitting....")
      break
   
   else:
      print("please enter  valid number")