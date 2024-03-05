print("give me two numbers to divide.")
print("enter q to quit")
while True:
    first_number=input("\n first_number")
    if first_number=='q':
       break
    second_number = input("\n second_number")
    if second_number=='q':
        break
try:
    answer = int(first_number) / int(second_number)
except ZeroDivisionError:
     print("you cant divide by 0")



