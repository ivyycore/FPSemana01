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

matq=max(plist)
mdef=max(plist)

print(plist)
print(matq)
print(mdef)

