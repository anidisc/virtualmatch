import random as R
from random import shuffle

#definire classe Squadra
class Squadra:
    def __init__(self,nome,id):
        self.nome=nome
        self.id=id
        self.pg=0
        self.punti=0 #punti ottenuti
        self.gf=0 #gol fatti
        self.gs=0 #gol subiti
        self.pareggi=0
        self.vittorie=0
        self.sconfitte=0
        self.difr=0
        self.statoforma=R.randint(20,80)
        #variabile di classe
    over05=0
    over15=0
    over25=0
    over35=0
    altro=0
    goal=0
    nogoal=0

    
    #metodi

    #definisce il risultato di un azione in base ad una percentaule
    def azione(self,percent):
        caso=R.randint(1,100)
        if (percent not in range(1,100)): percent=50
        if (caso<=percent): return True
        else: return False
    #aggiorna risultati statistici

    def update_stat(self,r1,r2):
        #r1 = risultato proprio
        #r2 = risultato avversario
        bonuspa = 2
        bonusvi = 5
        malussc = 10
        self.gf+=r1 #aggiorna numero di gol fatti
        self.gs+=r2 #aggiorna numero di gol subiti
        self.difr=self.gf-self.gs #aggiorna differenza reti
        self.pg+=1 #aggiorna numero partite giocate
        if (r1>0 and r2>0): self.goal+=1
        if r1>0: self.over05+=1
        else: self.nogoal+=1
        if r1>1: self.over15+=1
        if r1>2: self.over25+=1
        if r1>3: self.over35+=1
        if r1>4: self.altro+=1
        if r1==r2:
            self.punti+=1
            self.pareggi+=1
            if self.statoforma+bonuspa <=89: self.statoforma+=bonuspa
        if r1>r2: #la squadra ha vinto
            self.punti+=3
            self.vittorie+=1
            if self.statoforma+bonusvi <=80: self.statoforma+=bonusvi
        if r1<r2: #squadra perde
            self.sconfitte+=1
            if self.statoforma-malussc>=20: self.statoforma-=malussc

def probgol(punti,giocate,casadr,ospitedr,statoforma):
    forma=statoforma
    bonus=0
    if (punti!=0)and(giocate!=0):
        mediapunti=int(punti/giocate)
        if mediapunti==3 : bonus=5
        if mediapunti==2 : bonus=3
        if mediapunti==1 : bonus=1
    return forma+bonus

#creare lista campionato funzione creata da pingumen96
def championship(lista):
    partite = []
    shuffle(lista)
    for i in range(len(lista) - 1):
        giornata = []
        for j in range(round(len(lista) / 2)):
                #print(lista[j], "-", lista[len(lista) - j - 1])
                giornata.append(lista[j])
                giornata.append(lista[len(lista) - j - 1])
                #self.append_function('\t\t<partita>' + lista[j] + "-" + lista[len(lista) - j - 1] + "</partita>\n\t")
        #self.append_function('\t</giornata>\n')
        partite+=giornata
        temp = lista.pop()
        lista.insert(1, temp)
    return partite;


#corpo del programma
nsquadre=20
nazioni=7
cicliar=2


t=[Squadra("Team"+str(i),i) for i in range(nsquadre)]
c=championship(t)
sq_c=[c[i] for i in range(0,len(c),2)]
sq_o=[c[i] for i in range(1,len(c),2)]
#print(s.nome+"-" for s in sq_c)

for team in t:
    print(f"SQ: {team.nome} -  PUNTI:{team.punti}  - G:{team.pg} - V:{team.vittorie} - P:{team.pareggi} - S:{team.sconfitte} - GF:{team.gf} - GS:{team.gs} - DIFR:{team.difr} - SF:{team.statoforma} ")
print("-")

p=0 #contatore partite

for ar in range(1,cicliar+1):
    if cicliar/ar==1:
        temp_sqc=sq_o
        temp_sqo=sq_c
    else:
        temp_sqc=sq_c
        temp_sqo=sq_o
    for tc,tf in zip(temp_sqc,temp_sqo):
        a=1
        p+=1
        match={tc:0,tf:0}
        while a<=nazioni:
            chi=R.choice(list(match))
            bonuscasa=10 if chi==tc else -10
            if chi.azione(probgol(tc.punti,tc.pg,tc.difr,tf.difr,chi.statoforma)+bonuscasa):
                match[chi]+=1
            a+=1
        tc.update_stat(match[tc],match[tf])
        tf.update_stat(match[tf],match[tc])
        # print(f"{tc.nome} vs {tf.nome} = {match[tc]} - {match[tf]}")
        # if p==(nsquadre/2) :
        #     print("-------")
        #     p=0


classifica=sorted(t, key=lambda x: x.punti,reverse=True)
            
for team in classifica:
    print(f"SQ: {team.nome} -  PUNTI:{team.punti}  - G:{team.pg} - V:{team.vittorie} - P:{team.pareggi} - S:{team.sconfitte} - GF:{team.gf} - GS:{team.gs} - DIFR:{team.difr} - SF:{team.statoforma} ")


# classifica=sorted(t, key=lambda x: x.punti,reverse=True)
print("-")            
for team in classifica:
   print(f"{team.nome} - MP: {round((team.punti/team.pg),2)} - MG: {round(team.gf/team.pg,2)} "
         f" - OV0.5:{int(team.over05/team.pg*100)}%"
         f" - OV1.5:{int(team.over15/team.pg*100)}%"
         f" - OV2.5:{int(team.over25/team.pg*100)}%"
         f" - OV3.5:{int(team.over35/team.pg*100)}%"
         f" - ALTRO:{int(team.altro/team.pg*100)}%"
         f" - GG:{int(team.goal/team.pg*100)}%"
         f" - NG:{int(team.nogoal/team.pg*100)}%")



#print(probgol(12,4,9,15))
