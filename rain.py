file = open('rainfall.csv','r')
newList = []
for line in file:
    number_strings = line.split() 
    numbers = [str(n) for n in number_strings] 
    newList.append(numbers) 
   
print(newList)    