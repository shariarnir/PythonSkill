'''
words = ["Hello","world","!"]
print(words[0])
print(words[1])
print(words[2])

my_list = []
print(my_list)

number = 1
my_numbers = [number,2,3]
things = ["Numbers",0,my_numbers,4.56]

print(things[0])
print(things[1])
print(things[2])
print(things[2][2])
print(things[3])

str = "Hello World"
print(str[6])

my_numbers = [1,2,3,5]
my_numbers[3] = 4
print(my_numbers)

first_list = [1,2,3]
print(first_list + [4,5,6])
print(first_list * 3)

fruits = ["apple","orange","pineapple","grape",5]
print("orange" in fruits)
print("rice" in fruits)
print("apple" in fruits)
print(5 in fruits)

print("orange" not in fruits)
print(not "rice" in fruits)

nums = [1,2,3]
nums.append(4)
print(nums)

words = ["A","C"]
index = 1
words.insert(index,"B")
index_2 = 2
words.insert(index_2,"D")
words.insert(3,"E")
print(words)


letters = ['p','q','r','s','p','u']
print(letters.index('r'))
print(letters.index('p'))
#print(letters.index('z'))

print(letters.count('p'))
'''

nums = [1, 2, 4, 20, 50, 3, 4]
print(max(nums))
print(min(nums))
print(len(nums))


my_numbers = list(range(10))
print(my_numbers)
numbers = list(range(5,20,5))
print(numbers)
