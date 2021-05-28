
lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
	ele = int(input())

	lst.append(ele) 

if n % 2 == 0:
    median1=n//2
    median2=n//2-1
    median=(median1 + median2)//2
else:
    median=n//2
print(median)
