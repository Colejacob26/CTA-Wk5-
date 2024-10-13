#Part 1
print("Part #1")
print()

#Collects amount of years
print("Please enter the number of years:")
yearNum = int(input())

#for print statement(set up)
aList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

#Starting values
#Count is for the amount of months
result = 0
count = 0


for i in range(yearNum):
    #adds 12 months per year
    count += 12
    for j in range(12):
        print("Please enter the rainfall in inches for", aList[j] + ":")
        result += float(input())
        #collects rainfall

#prints results         
print("The number of months:", str(count))

print("The total amount of rainfall is:", str(result) + '"')

print("The average rainfall per month over all periods is:", str(format((result/count),".2f") +'"')) 

print()
print()
print()
#Give space between parts

print("Part #2")
print()

#Default for part 2
books = 0

print("Please enter the number of books purchased this month")
books = int(input())
#Collects amount of books purchased
points = 0

#Test for points earned
if books >= 8:
    points += 60
elif books >= 6:
    points += 30
elif books >= 4:
    points += 15
elif books >= 2:
    points += 5
else:
    points = 0

print("You have been awarded", points, "points")


