
class Project:
    def __init__(self,user_sal) :
        self.sal=user_sal
    def sort_sal(self):
        print("Values before sorting are",self.sal)
        for i in range(1,len(self.sal)):
            j=i-1
            temp=self.sal[i]
            while(j>=0 and self.sal[i]<self.sal[j]):
                self.sal[j+1]=self.sal[j]
                j=j-1
            self.sal[j+1]=temp
        print("Values after sorting",self.sal)
                
#initializing dictionary with user salary values
p1_users_sal={'u1':1500,'u3':3000,'u4':2000}
p2_users_sal={'u5':4500,'u8':1000}
p3_users_sal={'u7':1500,'u6':2000,'u2':4000}

#storing the salary values from dict to string
p1_sal=[]
p2_sal=[]
p3_sal=[]

for key1 in p1_users_sal:
    p1_sal.append(p1_users_sal[key1])  
for key2 in p2_users_sal:
    p2_sal.append(p2_users_sal[key2])  
for key3 in p3_users_sal:
    p3_sal.append(p3_users_sal[key3])  

#creating the instances of the class and passing the strings having salaries
p1=Project(p1_sal)
p2=Project(p2_sal)
p3=Project(p3_sal)

#calling the sort_val() method of the class
p1.sort_sal()
p2.sort_sal()
p3.sort_sal()

#project_dict=dict()


