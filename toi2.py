row1=list()
row2=list()
row3=list()
row4=list()
row5=list()
row1.append(1)
n=row1[0]
n+=3
for i in range(n,n+2):
    row2.append(i)

n=row2[-1]+3
for i in range(n,n+3):
    row3.append(i)

n=row3[-1]+3
for i in range(n,n+4):
    row4.append(i)

n=row4[-1]+3
for i in range(n,n+5):
    row5.append(i)
    

print(row1)
print(row2)
print(row3)
print(row4)
print(row5)

print("Row 1: ",row1[0])
print("Row 2: ",row2[0]+row2[1])
print("Row 3: ",row3[0]+row3[1]+row3[2])
print("Row 4: ",row4[0]+row4[1]+row4[2]+row4[3])
print("Row 5: ",row5[0]+row5[1]+row5[2]+row5[3]+row5[4])
