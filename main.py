from random import randint
from time import clock_gettime
from json import loads, dumps

incorrect_q = [] #list of incorrectly answered questions
xa = [] #list of incorrect answers
ca = [] #list of correct answers
qn = [] #list of question numbers
op = ["+","-","*","/"] #math operations
tm=clock_gettime(1) #reset timer

def timer(n): #returns the time since the program has been started
  return round((clock_gettime(1)-tm)*n)/n
  
def ask_question(n1,n2,o,i): #asks a math question
  if o==3: 
    n1=n2*n1
    n2+=n2==0 #to prevent asking 0/0
  a=int(input(i+": "+str(n1)+str(op[o])+str(n2)+"=")) #user's answer
  if eval(str(n1)+str(op[o])+str(n2))!=a:
      incorrect_q.append(str(n1)+str(op[o])+str(n2))
      xa.append(a)
      ca.append(eval(str(n1)+str(op[o])+str(n2)))
      qn.append(i)

def lb(gm,time):
	if len(incorrect_q)==0:
		if input("Would you like to add your score to the leaderboard? (yes/no): ")=="yes":
			un=input("enter a username: ")
			l=open("l_"+str(gm)+".json","r")
			l=loads(l.read())
			l.append([time, un])
			l.sort(key=lambda e:e[0])
			w=open("l_"+str(gm)+".json","w")
			w.write(dumps(l))
			w.close()
			print("Heres the top 5 on the leaderboard:")
			for i in range(5 if 5<=len(l) else len(l)):
				print(str(i+1)+":",l[i][1],"-",l[i][0])    

def result(gm):
  time=timer(1000)
  print("Your time:",time)
  print("You got",len(incorrect_q),"question(s) wrong.")
  for i in range(len(incorrect_q)):
    print(str(qn[i])+":", incorrect_q[i])
    print("Your answer:", xa[i])
    print("Correct answer:",ca[i])
  print()
  lb(gm,time)    
  if input("Do you want to play again? (yes/no): ")=="yes": game(int(input("Enter 1-4 depending on how difficult you want the test to be: ")))
  else: print("Thanks for playing!")
  
def game(game_mode):
  global incorrect_q, xa, ca, qn, tm
  tm=clock_gettime(1) #reset timer
  incorrect_q = [] #list of incorrectly answered questions
  xa = [] #list of incorrect answers
  ca = [] #list of correct answers
  qn = [] #list of question numbers
  if game_mode==1: #easy mode
    for i in range(3):
      ask_question(randint(-5,5),randint(-5,5),randint(0,2),str(i+1))
  elif game_mode==2: #normal mode
    for i in range(5): 
      ask_question(randint(-9,9),randint(-9,9),randint(0,3),str(i+1))
  elif game_mode==3: #hard mode
    for i in range(10):
      ask_question(randint(-19,19),randint(-19,19),randint(0,3),str(i+1))
  elif game_mode==4: #extreme mode
    for i in range(20):
      ask_question(randint(-49,49),randint(-49,49),randint( 0,3),str(i+1))    
  result(game_mode)

print("Try to answer the following math questions as fast as you can.")
game(int(input("Enter 1-4 depending on how difficult you want the test to be: ")))
