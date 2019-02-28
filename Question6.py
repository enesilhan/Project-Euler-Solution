sumSquare = 0
squareSum = 0
n = int(input("Enter a value : "))
for i in range(1,n+1):
    sumSquare += i**2
    squareSum += i
sum = squareSum**2 - sumSquare
print("Difference :",sum)