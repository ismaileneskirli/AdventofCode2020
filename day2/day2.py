from collections import defaultdict
f = open("input.txt","r")
counter = 0
# There are one duplicate passwords in the input file therefore use default dict which allows multiple keys.
dict = defaultdict(list) # key is the password, values are letter, min time, max time.in order
for line in f:
    counter +=1
    password_value = line.split()[0]
    minVal,maxVal = password_value.split("-")
    key = line.split()[2]
    letter = line.split()[1].strip(":")
    #defaultdict doesnt let us append multiple variables at once.
    dict[key].append(letter)
    dict[key].append(minVal)
    dict[key].append(maxVal)

    
valid_password_counter = 0

for key in dict.keys(): #value[0] is letter, value[1] is min number of time, value[2] is max.
    count = key.count(dict[key][0]) #function to count a specific substring in a string.
    #print(count,dict[key][1],dict[key][2])
    if int(dict[key][1]) <= count <= int(dict[key][2]):
        valid_password_counter += 1
        
# How to access elements of dictionary by index. This is what i have learned in this quiz.
# dict_items = dict.items()
# first_two = list(dict_items)[:2] 
# print(first_two)
print(valid_password_counter)
