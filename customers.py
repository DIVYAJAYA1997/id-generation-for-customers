from uuid import uuid4
class Customrs_details:
    def __init__(self,name,joining_date,package):
        self.name=name
        self.joining_date=joining_date
        self.package=package
        self.uid=uuid4().hex
    def __str__(self):
        return str(self.__dict__)
    @classmethod
    def from_input(cls):
        return cls(
            input('name: '),
            input('joining_date: '),
            input('package: '),

        )
u=[]
n=input("enter the no:of data u want to enter: ")
create_range=range(0,int(n))
for i in create_range:
    u.append(Customrs_details.from_input())
with open('id.txt',"w")as myfile:
    for ele in u:
        myfile.write("%s\n" % ele)
f=open("id.txt")
print(f.read())









