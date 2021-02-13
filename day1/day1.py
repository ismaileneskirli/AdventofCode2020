f = open("input.txt","r")
numbers = []
for line in f:
    line = line.strip("\n")
    numbers.append(int(line))



#Find the two entries that sum to 2020
def find_entries(numbers):
    for i in range(len(numbers)-1):
        for j in range(len(numbers)-i-1):
            if 2020 == numbers[i] + numbers[j+i+1]:
                a = numbers[i]
                b = numbers[j+i+1]
                return a,b
    return 0

print(find_entries(numbers))
x,y = find_entries(numbers)

print(x*y)
            