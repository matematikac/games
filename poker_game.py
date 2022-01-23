import random # za nasumican izbor karata iz spila

deck=["2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "AH", "JH", "QH", "KH", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "AS", "JS", "QS", "KS", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "AD", "JD", "QD", "KD", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "AC", "JC", "QC", "KC"]
N=2 #broj ruku koje se igraju
card_number_pull=[[]]*N #cuva izvucene brojeve za svaku ruku
card_suit_pull=[[]]*N   #cuva izvucene znakove u ruci

#nasumicno izvlacimo pet karata i razdvajamo broj karte od njenog znaka
k=0
while k<N:
    temp=random.sample(deck, k=5) # nasumican izbor pet karata iz spila bez ponavljanja karata
    temp1=[""]*5
    temp2=[""]*5
    for i in range(len(temp)):
        temp1[i]=temp[i][0:len(temp[i])-1] # uzimamo broj karte
        temp2[i]=temp[i][len(temp[i])-1:len(temp[i])] # uzimamo znak karte
    card_number_pull[k]=temp1
    card_suit_pull[k]=temp2
    k+=1# uslov za izlazak iz while petlje

#utvrdjujemo jacinu ruke
k=0
strength_hand=[0]*N #cuva jacinu ruke, od 1 za najjacu do 10 za najslabiju ruku
mesage=[""]*N       #ostavlja poruku koji je tip ruke
while k<N:
    temp=[""]*5
    temp=card_number_pull[k] # cuva brojeve iz (k+1)ve ruke, koi ce biti sortirani za uporedjivanje za "straight" ili 4 iste, 3 iste
    temp=sorted(temp) # sortirani brojevi izgledaju 10, 2, 3, 4...9, A, J, K, Q
    #ispitujemo da li je ruka boja koristeci funkciju set koja nam od liste pravi listu u kojoj se svaki elemnt nalazi tacno jednom
    if len(set(card_suit_pull[k]))==1:
      if (temp[0]=="10")&(temp[1]=="A")&(temp[2]=="J")&(temp[3]=="K")&(temp[4]=="Q"):
          strength_hand[k]=1
          mesage[k]="Royal Flush"
      elif ((temp[0]=="2")&(temp[1]=="3")&(temp[2]=="4")&(temp[3]=="5")&(temp[4]=="6"))|((temp[0]=="2")&(temp[1]=="3")&(temp[2]=="4")&(temp[3]=="5")&(temp[4]=="A"))|((temp[0]=="3")&(temp[1]=="4")&(temp[2]=="5")&(temp[3]=="6")&(temp[4]=="7"))|((temp[0]=="4")&(temp[1]=="5")&(temp[2]=="6")&(temp[3]=="7")&(temp[4]=="8"))|((temp[0]=="5")&(temp[1]=="6")&(temp[2]=="7")&(temp[3]=="8")&(temp[4]=="9"))|((temp[0]=="10")&(temp[1]=="6")&(temp[2]=="7")&(temp[3]=="8")&(temp[4]=="9"))|((temp[0]=="10")&(temp[1]=="7")&(temp[2]=="8")&(temp[3]=="9")&(temp[4]=="A"))|((temp[0]=="10")&(temp[1]=="8")&(temp[2]=="9")&(temp[3]=="A")&(temp[4]=="J"))|((temp[0]=="10")&(temp[1]=="9")&(temp[2]=="A")&(temp[3]=="J")&(temp[4]=="Q")):
          strength_hand[k]=2
          mesage[k]="Straight Flush"
      else:
          strength_hand[k]=5
          mesage[k]="Flush"
    #ispitujemo da li je ruka poker ili full hause
    if len(set(card_number_pull[k]))==2:
      if ((temp[0]==temp[1])&(temp[1]==temp[2])&(temp[2]==temp[3]))|((temp[1]==temp[2])&(temp[2]==temp[3])&(temp[3]==temp[4])):
        strength_hand[k]=3
        mesage[k]="Four of a Kind"
      else:
        strength_hand[k]=4
        mesage[k]="Full House"
    #da li je ruka triling ili dva para
    if len(set(card_number_pull[k]))==3:
      if ((temp[0]==temp[1])&(temp[1]==temp[2]))|((temp[1]==temp[2])&(temp[2]==temp[3]))|((temp[2]==temp[3])&(temp[3]==temp[4])):
        strength_hand[k]=7
        mesage[k]="Three of a Kind"
      else:
        strength_hand[k]=8
        mesage[k]="Two Pair"
    #da li je ruka par
    if len(set(card_number_pull[k]))==4:
        strength_hand[k]=9
        mesage[k]="One Pair"
    #da li je ruka niz ili najveca karta
    if (len(set(card_number_pull[k]))==5)&(len(set(card_suit_pull[k]))!=1):
      if ((temp[0]=="2")&(temp[1]=="3")&(temp[2]=="4")&(temp[3]=="5")&(temp[4]=="6"))|((temp[0]=="2")&(temp[1]=="3")&(temp[2]=="4")&(temp[3]=="5")&(temp[4]=="A"))|((temp[0]=="3")&(temp[1]=="4")&(temp[2]=="5")&(temp[3]=="6")&(temp[4]=="7"))|((temp[0]=="4")&(temp[1]=="5")&(temp[2]=="6")&(temp[3]=="7")&(temp[4]=="8"))|((temp[0]=="5")&(temp[1]=="6")&(temp[2]=="7")&(temp[3]=="8")&(temp[4]=="9"))|((temp[0]=="10")&(temp[1]=="6")&(temp[2]=="7")&(temp[3]=="8")&(temp[4]=="9"))|((temp[0]=="10")&(temp[1]=="7")&(temp[2]=="8")&(temp[3]=="9")&(temp[4]=="A"))|((temp[0]=="10")&(temp[1]=="8")&(temp[2]=="9")&(temp[3]=="A")&(temp[4]=="J"))|((temp[0]=="10")&(temp[1]=="9")&(temp[2]=="A")&(temp[3]=="J")&(temp[4]=="Q"))|((temp[0]=="10")&(temp[1]=="A")&(temp[2]=="J")&(temp[3]=="K")&(temp[4]=="Q")):
        strength_hand[k]=6
        mesage[k]="Straight"
      else:
        strength_hand[k]=10
        mesage[k]="High Card"
    k+=1# uslov za izlazak iz while petlje
#pronalazimo najacu ruku\ruke tako sto trazimo minimum niza strenght_hend
Min=11
for i in range(len(strength_hand)):
    if strength_hand[i]<=Min:
        Min=strength_hand[i]
# pronalazimo u kojoj ruci\rukama se pojavio minimum
position=0 #pozicija minimuma (najjace ruke)
fr=0       #koliko puta se najjaca ruka javila
for i in range(len(strength_hand)):
    if strength_hand[i]<=Min:
        position=i
        fr+= 1
#ispisujemo rezultat
k=0
while k<N:
    temp=[""]*5
    temp1=[""]*5
    temp2=[""]*5
    temp1=card_number_pull[k]
    temp2=card_suit_pull[k]
#pravimo od broja i znaka ponovo jednu kartu i na taj nacin dobijamo ruku
    for i in range(5):
        temp[i]=temp1[i]+temp2[i]
    print ('\n',"Hand",k+1,":",' '.join(temp),'\n',"Hand",k+1,"type:",mesage[k])
#ako se najaca ruka pojavila samo jednom ispisujemo da je pobedila
    if (k==position)&(fr==1):
        print("","Winerr")
    k+=1# uslov za izlazak iz while petlje
#ukoliko je bilo vise najjacih ruku ispisujemo da je nereseno
if fr!=1:
    print ('\n',"Draw")