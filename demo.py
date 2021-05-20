class Customrs_details:
    class_counter=0

    def __init__(self,name,joining_date,package):
        self.name=name
        self.joining_date=joining_date
        self.package=package
        self.id=Customrs_details.class_counter
        Customrs_details.class_counter+=1
    @classmethod
    def from_input(cls):
        return cls(
            input('name: '),
            input('joining_date: '),
            input('package: '),


        )
    def __str__(self):
        return str(self.__dict__)

u=[]
n=input("enter the no:of data u want to enter: ")
create_range=range(0,int(n))
for i in create_range:
    u.append(Customrs_details.from_input())
with open('id.txt',"w")as myfile:
    for ele in u:
        myfile.write("%s\n" % ele)

f=open("id.txt","r")
print(f.read())




