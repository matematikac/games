import random #for a random choice of dice number
import statistics #for the calculate of mean and variance

dice = [1, 2, 3, 4, 5, 6]
N=1000000 #number of bets
i=0
betting_hand=[0]*N #this array contains every single bet, for win +1 dollar, for lose -1 dollar
number_of_wins=0   #calculating the number of wins
while i<N:
 #rolling one dice four time in one bet
 roll_1=random.choice(dice)
 roll_2=random.choice(dice)
 roll_3=random.choice(dice)
 roll_4=random.choice(dice)
# condition for win
 if (roll_1==6)|(roll_2==6)|(roll_3==6)|(roll_4==6):
   betting_hand[i]=1
   number_of_wins+=1
 else:
   betting_hand[i]=-1
 i+=1 #condition for while loop
print ("","The number of win bets:", number_of_wins,'\n',"The number of lose bets is:", N-number_of_wins,'\n')
# calculating the mean, the variance and standard deviation for data in betting_hand
Mean=statistics.mean(betting_hand)
Variance=statistics.variance(betting_hand)
Standard_Dev=pow(Variance, 0.5)
print("","The Mean is:",Mean,'\n',"The Variance is:",round(Variance,6),'\n',"The Standard deviation is:",round(Standard_Dev, 6))