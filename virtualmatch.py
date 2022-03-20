import random as r
from tabulate import tabulate

#nuemro di partite
n=100
goals=0
over=0
pari=0
uno=0
due=0
over3=0
zero=0

for i in range(n):
    azioni=7
    squadre={"team1":0,"team2":0}

    while (azioni>0):
        chi=r.choice(list(squadre))
        gol=bool(r.getrandbits(1))
        if gol: squadre[chi]+=1
        azioni-=1  

    #print(f"Squadra1-Squadra2: {squadre['team1']}:{squadre['team2']}")
    if ((squadre['team1']>0) and (squadre['team2']>0)) :
         goals+=1
    if (squadre['team1']+squadre['team2'])>2 :
        over+=1
    if (squadre['team1']==squadre['team2']):
        pari+=1
    if (squadre['team1']>squadre['team2']):
        uno+=1
    if (squadre['team1']<squadre['team2']):
        due+=1
    if (squadre['team1']+squadre['team2']>3):
        over3+=1
    if (squadre['team1']+squadre['team2']==0):
        zero+=1

tab=[[n,goals,goals*100/n,over,over*100/n,pari,pari*100/n,uno,uno*100/n,due,due*100/n,over3,over3*100/n,zero,zero*100/n]]
print("\n SIMULAZIONE *** VIRTUAL MATCH *** \n")
print(tabulate(tab,headers=["N.PARTITE","GOAL","GG %","OV25","OV25 %","X","X %","1","1 %","2","2 %","OV35","OV35 %","0-0","NULL %"],tablefmt="pretty"))

# print(f"su {n} incontri è avvenuto il risultato GOAL ={goals} volte - {(goals*100)/n} %")
# print(f"su {n} incontri è avvenuto il risultato O2.5 ={over} volte - {(over*100)/n} %")
# print(f"su {n} incontri è avvenuto il risultato X ={pari} volte - {(pari*100)/n} %")
# print(f"su {n} incontri è avvenuto il risultato 1 ={uno} volte - {(uno*100)/n} %")
# print(f"su {n} incontri è avvenuto il risultato 2 ={due} volte - {(due*100)/n} %")
# print(f"su {n} incontri è avvenuto il risultato O3.5 ={over3} volte - {(over3*100)/n} %")
# print(f"su {n} incontri è avvenuto il risultato 0-0 ={zero} volte - {(zero*100)/n} %")



