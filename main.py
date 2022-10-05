#print("This test strat is great.")

import random

guesses_right = 0
#counter for correct guesses before switching strategy
#should be ~ 15 for 75%
bubbles_right = 0
#counter for correct bubbles after switching strategy
g_right_acc = 0
#counter for accumulated correct guesses before switching strategy
b_right_acc = 0
#counter for accumulated correct bubbles after switching strategy


Answers = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0}
#initial dictionary set up for the answer key
Guesses = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0}
#intial dictionary set up for the guesses pre switching strategy
Bubbles = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0}
#initial dictionary set up for the bubbling post switching strategy
roll = 0
#a needed variable for a random roll later


for i in range(100000):
#running the simulation this many times
  guesses_right = 0
  #reset the counter for the number of correct guesses pre switching strategy
  bubbles_right = 0
  #reset the counter for the number of correct bubblies post switching strategy
  for k,v in Answers.items():
  #to set the values in the answer key, going through each value, one by one
    v = random.randrange(1,5)
    #rolling a random nomber between and including 1 and 4
    Answers.update({k:v})
    #updating the dictionary accordingly with each value

  for k, v in Guesses.items():
  #set the values for the guesses
    roll = random.random()
    #This is the implementation of that variable
    #We assume that the student got approximately 75% on their test
    if roll <= .75:
    #thusly if the roll is less than or equal to .75 
      v = Answers[k]
      #update the guess to be identically what is in the answer key
      Guesses.update({k:v})
      #Then update back to the dictionary of the students guesses
      guesses_right += 1
      #and add 1 to the number of correct guesses
    else:
    #If the roll does not fall within the .75
      v = random.randrange(1,5)
      #Roll v to a random number between 1 and 4
      for i in range(1000000):
      #this for loop is to insure that the student does not get an extra point.
      #I feel a little like an old testament god smiting this poor student by doing this, but...
      #this loop will repeat an arbitrarily large number of times until the number rolled is different from the number in the answer key
        if v == Answers[k]:
        #If the new rolled answer is identically the answer in the answer key then
          v = random.randrange(1,5)
          #re roll the answer, and go back to the start of the for loop
        else:
        #If the new rolled answer is not identically the answer in the answer key then
          Guesses.update({k:v})
          #update the dictionary of the students guesses with the new, incorrect answer
          break
          #exit the arbitrarily large for loop, and go back to the initial for loop cycling through the dictionary


  for k,v in Bubbles.items():
  #This is where we implement the students strategy of bubbling the next answer up
   v = Guesses[k]+1
   #The answer given is the answer from the guesses plus 1
   if v == 5:
   #resetting an answer of e (not an option) to a
     v = 1
     #set to a
   if v == Answers[k]:
     #if the value in guesses is identical to the value in the answer key, then
      bubbles_right += 1
      #add 1 to the counter of total correct bubbles
   Bubbles.update({k:v})
   #update the bubble dictionary
 
    
  
  b_right_acc += bubbles_right
  #accumulated bubbles collect all the correct bubbles from this iteration
  #we are collecting to take an average of the number of correct bubbles per test
  g_right_acc += (guesses_right/20)
  #accumulated guesses collect all the correct answers from this round
  #we are dividing by the number of questions on the test becuase we want to know the students average percentage


print("The students average grade before he altered according to the bubbling strategy after 100,000 iterations was:", g_right_acc/(100000))
#We divide the value by the number of iterations to get the average
print ("The students average number of correct answers for the bubbling strategy after 100,000 iterations was:", b_right_acc/100000)
#We divide the value by the number of iterations to get the average