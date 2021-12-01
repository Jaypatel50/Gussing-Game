import random
number = int(input("Enter Number : "))
win = random.randint(0,10)
count = 1

while number != win:
    if number < win:
        print("Too Low")
        count+=1
    else:
        print("Too High")
        count+=1
    number = int(input("Enter Number : ")) 
    if number == win:
        print(f"you got answer in {count} attemps")
        break
