row1=[0]
row2=list()
row3=list()
row4=list()
row5=list()
row1[0]=int(input("Enter first row"))
print("Enter row 2")
for i in range(0,2):
    n=int(input())
    row2.append(n)

print("Enter row 3")
for i in range(0,3):
    n=int(input())
    row3.append(n)

print("Enter row 4")
for i in range(0,4):
    n=int(input())
    row4.append(n)

print("Enter row 5")
for i in range(0,5):
    n=int(input())
    row5.append(n)
    
print("Row 1: ", row1[0],"s =",row1[0])
print("Row 2: " ,row2[0],"s =",row2[0]*2)
print("Row 3: " ,row3[0],"s =",row3[0]*3)
print("Row 4: " ,row4[0],"s =",row4[0]*4)
print("Row 5: " ,row5[0],"s =",row5[0]*5)
