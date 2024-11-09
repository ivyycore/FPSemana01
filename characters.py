#Nome das personagens

name1=str(input())
atq1=int(input())
def1=int(input())

name2=str(input())
atq2=int(input())
def2=int(input())

name3=str(input())
atq3=int(input())
def3=int(input())


p1=[name1,(atq1,def1)]
p2=[name2,(atq2,def2)]
p3=[name3,(atq3,def3)]
plist=[p1,p2,p3]

print(plist)

if (atq1 < atq3 and atq2 < atq3):
    print("Ataque "+name3+" "+str(atq3))
elif (atq2 < atq1 and atq3 < atq1):
    print("Ataque "+name1+" "+str(atq1))
elif (atq1 < atq2 and atq3 < atq2):
    print("Ataque "+name2+" "+str(atq2))

if (def1 < def3 and def2 < def3):
    print("Defesa "+name3+" "+str(def3))
elif (def2 < def1 and def3 < def1):
    print("Defesa "+name1+" "+str(def1))
elif (def1 < def2 and def3 < def2):
    print("Ataque "+name2+" "+str(def2))



