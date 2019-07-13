'''
i = 1
while i <= 5 :
    print(i)
    i = i + 1
print("I am priting eventually cause the while loop is done with his job.")

while 1 == 1 :
    print("In the loop")

i = 0
while 1 == 1:
    print(i)
    i = i + 1
    if i >= 5:
        print("Breaking")
        break
print("Finished")

i = 0
while True:
    i += 1
    if i == 2:
        print("Skipping 2")
        continue
    if i == 5:
        print("Breaking")
        break
    print(i)
print("Finished")


fruits = ["Apple","Orange","Pineapple","Grape"]
start_index = 0;
max_index = len(fruits)-1
while start_index <= max_index:
    fruit = fruits[start_index]
    print(fruit + " Juice")

    start_index +=1


fruits = ["Apple","Orange","Pineapple","Grape"]
for fruit in fruits:
    print(fruit + " Juice!")

for i in range(1,10):
    print(i)

for i in range(1,20,2):
    print(i)

for i in range(10, 1, -1):
    print(i)
'''
for letter in "Raju":
    print(letter)
    
