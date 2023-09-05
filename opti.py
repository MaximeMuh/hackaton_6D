from pulp import *
d1=[0,10,10,50,50,70,40,20,30,20,20,20,40]
d2=[120,220,120,620,650,650,650,100,150,520,510,500]
s0=0
p0=40

c=[0,0,0,0,0,0,20,0,0,0,0,20]
x=[1,1,1,1,1,1,-1,1,1,1,1,1]

p=[40,40,40,40,40,40,20,20,20,20,20,40]
##
def f2(c,d,x):
    i=0
    for k in range(len(c)):
        i+=c[k]
    i*=50

    u=0
    for j in range(1,13):


        u+=j*(prod_mois_k(12-j+1,x,c)-d[12-j+1])

    u*=20
    u+=i
    return u


def prod_mois_k(k,x,c):
    v=40
    for i in range(0,k):
        v+=x[i]*c[i]
    return v



##

def f(p,d):
    p.insert(0,p0)

    I=0

    for i in range(12):
        I+=p[i+1]-p[i]
    I*=50

    I+=20*12*s0
    u=0
    for i in range (1,13):
        u+=i*(p[12-i+1]-d[12-i+1])

    u*=20
    I+=u
    return I


##p=LpVariable('p',0,LpList)

p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12=LpVariable('p1',lowBound=0,cat=LpInteger),LpVariable('p2',lowBound=0,cat=LpInteger),LpVariable('p3',lowBound=0,cat=LpInteger),LpVariable('p4',lowBound=0,cat=LpInteger),LpVariable('p5',lowBound=0,cat=LpInteger),LpVariable('p6',lowBound=0,cat=LpInteger),LpVariable('p7',lowBound=0,cat=LpInteger),LpVariable('p8',lowBound=0,cat=LpInteger),LpVariable('p9',lowBound=0,cat=LpInteger),LpVariable('p10',lowBound=0,cat=LpInteger),LpVariable('p11',lowBound=0,cat=LpInteger),LpVariable('p12',lowBound=0,cat=LpInteger)
p=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12]


x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12=LpVariable('x1',lowBound=-1,cat=LpInteger),LpVariable('x2',lowBound=-1,cat=LpInteger),LpVariable('x3',lowBound=-1,cat=LpInteger),LpVariable('x4',lowBound=-1,cat=LpInteger),LpVariable('x5',lowBound=-1,cat=LpInteger),LpVariable('x6',lowBound=-1,cat=LpInteger),LpVariable('x7',lowBound=-1,cat=LpInteger),LpVariable('x8',lowBound=-1,cat=LpInteger),LpVariable('x9',lowBound=-1,cat=LpInteger),LpVariable('x10',lowBound=-1,cat=LpInteger),LpVariable('x11',lowBound=-1,cat=LpInteger),LpVariable('x12',lowBound=-1,cat=LpInteger)
x=[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12]


probleme=LpProblem(name='productions',sense=LpMinimize)

for i in range(1,13):
    u=0
    for j in range(1,i+1):
        u+=prod_mois_k(j,x,c)-d1[j]
    u+=s0
    probleme+=(u>=0)
for i in range(12):
    probleme+=(x[i==1 or x[i]==-1)
probleme+=f2(p,d1,x)


probleme.solve()
print(f'{p1.value()}',f'{p2.value()}',f'{p3.value()}',f'{p4.value()}',f'{p5.value()}',f'{p6.value()}',f'{p7.value()}',f'{p8.value()}',f'{p9.value()}',f'{p10.value()}',f'{p11.value()}',f'{p12.value()}')

print(f'le coût minimal est  de {f(p,d1)}')



##

x = LpVariable("x", lowBound=0, cat=LpInteger)
# Nombre de petites voitures produites
y = LpVariable("y", lowBound=0, cat=LpInteger)



probleme = LpProblem(name='chiffre_affaires', sense=LpMaximize)

probleme += (x+y == 400)
probleme += (2*x+y <= 600)
probleme += 16000*x +10000*y

solvere = PULP_CBC_CMD(timeLimit=20, msg=True)
probleme.solve()


print(f"x = {x.value()}")
print(f"y = {y.value()}")
