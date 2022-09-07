# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random
#intializing screen
wn = trtl.Screen()
#importing images
applegoated = "applegoated.gif"
wn.addshape(applegoated)
peargoated = "peargoated.gif"
wn.addshape(peargoated)
kiwigoated = "kiwigoated.gif"
wn.addshape(kiwigoated)
orangegoated = "orangegoated.gif"
wn.addshape(orangegoated)
starFishgoated = "starFishgoated.gif"
wn.addshape(starFishgoated)
bgcolorgoated = input("Your favorite color?")
wn.bgcolor(bgcolorgoated)
name = input("Your name:")
#-----game configuration----
#intialzing images and setting them in the shape of fruits
apple = trtl.Turtle()
apple.shape(applegoated)
pear = trtl.Turtle()
pear.shape(peargoated)
orange = trtl.Turtle()
orange.shape(orangegoated)
kiwi = trtl.Turtle()
kiwi.shape(kiwigoated)
starFish = trtl.Turtle()
starFish.shape(starFishgoated)
 
#intializing score and timer variables 
score = 0
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000
timer_up = False
fruitSpeed = [1,2,3,4,5,6,7,13,15,9,17]
iteration = 0
x=0
lives = 3
#-----initialize turtle-----

#intializing score writer turtle 
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(-230,170)
score_writer.hideturtle()
counter = trtl.Turtle()
counter.penup()
counter.goto(110,90)
counter.pendown()
counter.hideturtle()
 
 

 
 
 
 
 
#-----game functions--------
#randomizing the posistions of the fruit in the start
def fruitPosistion():
   global x
   x = random.randint(-400,400)
   y = 150
   a = x-240
   b = x - 480
   c = x - 720
   d = x - 960
   e = x + 240
   f = x + 480
   g = x + 720
   h = x + 960
   apple.penup()
   apple.goto(x,y)
   apple.pendown()
   if(x<= 60 and x>=-60):
      pear.penup()
      pear.goto(a,y)
      pear.pendown()
      orange.penup()
      orange.goto(b,y)
      orange.pendown()
      kiwi.penup()
      kiwi.goto(c,y)
      kiwi.pendown()
      starFish.penup()
      starFish.goto(d,y)
      starFish.pendown()
   if(x>60):
      pear.penup()
      pear.goto(a,y)
      pear.pendown()
      orange.penup()
      orange.goto(b,y)
      orange.pendown()
      kiwi.penup()
      kiwi.goto(c,y)
      kiwi.pendown()
      starFish.penup()
      starFish.goto(d,y)
      starFish.pendown()
   if(x<-60):
      pear.penup()
      pear.goto(e,y)
      pear.pendown()
      orange.penup()
      orange.goto(f,y)
      orange.pendown()
      kiwi.penup()
      kiwi.goto(g,y)
      kiwi.pendown()
      starFish.penup()
      starFish.goto(h,y)
      starFish.pendown()

 
 #the fruit falling
def fruitFalling():
  #setting random distances for fruits, so they go at different speeds, making game more challenging
 appleDistance = random.randint(0,10)
 pearDistance = random.randint(0,10)
 orangeDistance = random.randint(0,10)
 kiwiDistance = random.randint(0,10)
 starFishDistance = random.randint(0,10)
 global iteration
 apple.setheading(270)
 pear.setheading(270)
 orange.setheading(270)
 kiwi.setheading(270)
 starFish.setheading(270)
 #movement of the turtles downwards
 while(iteration < 10):
  
   apple.penup()
   apple.forward(fruitSpeed[appleDistance])
   apple.pendown()
   #if the apple reaches the bottom of screen, then it will go back up and call the collision function
   if(apple.ycor() == -200):
     fruitCollisionA()
 
  
   pear.penup()
   pear.forward(fruitSpeed[pearDistance])
   pear.pendown()
   if(pear.ycor()== -200):
     fruitCollisionP()
  
   orange.penup()
   orange.forward(fruitSpeed[orangeDistance])
   orange.pendown()
   if(orange.ycor()==-200):
     fruitCollisionO()
    
 
   kiwi.penup()
   kiwi.forward(fruitSpeed[kiwiDistance])
   kiwi.pendown()
   if(kiwi.ycor()==-200):
     fruitCollisionK()
 
   starFish.penup()
   starFish.forward(fruitSpeed[starFishDistance])
   starFish.pendown()
   if(starFish.ycor()==-200):
     fruitCollisionS()
 #collision function allows you to subtract score and life points when the fruit hits bottom of the screen
def fruitCollisionA():
 global x
 apple.penup()
 apple.goto(x,150)
 apple.pendown()
 subtract_score()
 life()
 
#when the player clicks("slices the fruit"), then the fruit will go back up and the player will get a point
def fruitOnClickA(x,y):
 global appleDistance
 apple.penup()
 appleX=apple.xcor()
 apple.goto(appleX,150)
 apple.pendown()
 update_score()
 appleDistance = random.randint(0,10)


 
def fruitCollisionP():
 
 pear.penup()
 pearX = pear.xcor() 
 pear.goto(pearX,150)
 pear.pendown()
 subtract_score()
 life()
 
    
def fruitOnClickP(x,y):
 global pearDistance
 pear.penup()
 pear.goto(pear.xcor(),150)
 pear.pendown()
 update_score()
 pearDistance = random.randint(0,10)
 

def fruitCollisionO():
 
 orange.penup()
 orangeX = orange.xcor()  
 orange.goto(orangeX,150)
 orange.pendown()
 subtract_score()
 life()

 
    
 
 
def fruitOnClickO(x,y):
 global orangeDistance 
 orange.penup()
 orange.goto(orange.xcor(),150)
 orange.pendown()
 update_score()
 orangeDistance = random.randint(0,10)
 orange.forward(fruitSpeed[orangeDistance])
 
def fruitCollisionK():
 
 kiwi.penup()
 kiwiX = kiwi.xcor()
 kiwi.goto(kiwiX,150)
 kiwi.pendown()
 subtract_score()
 life()
 
    
 
 
def fruitOnClickK(x,y):
 global kiwiDistance 
 kiwi.penup()
 kiwi.goto(kiwi.xcor(),150)
 kiwi.pendown()
 update_score() 
 kiwiDistance = random.randint(0,10)
 kiwi.forward(fruitSpeed[kiwiDistance])
 
def fruitCollisionS():
  
 starFish.penup()
 starFishX = starFish.xcor()
 starFish.goto(starFishX,150)
 starFish.pendown()
 subtract_score()
 life()

 
 
def fruitOnClickS(x,y):
 global starFishDistance
 starFish.penup()
 starFish.goto(starFish.xcor(),150)
 starFish.pendown()
 update_score()  
 starFishDistance = random.randint(0,10)
 starFish.forward(fruitSpeed[starFishDistance])
#this will happen either when the time ends, or when the lives run out
def gameover():
 global score
 kiwi.forward(0)
 pear.forward(0)
 apple.forward(0)
 starFish.forward(0)
 orange.forward(0)
 return name + ":" + score
 
#player has three lives and lives will keep decreasing as turtle hits bottom of the screen
def life():
  global lives
  lives -= 1
  if(lives == 0):
    gameover()
 

#updates score by adding points
def update_score():
  global score
  score += 1
  score_writer.clear()
  score_writer.write(score, font = font_setup)
#updates score by subtracting points 
def subtract_score():
  global score
  score -= 1
  score_writer.clear()
  score_writer.write(score, font = font_setup)
#counts down the timer  
def countdown():
  global timer, timer_up
  counter.clear() 
 #if timer hits zero, than the game is over  
if (timer <= 0):

  counter.write("Time's Up", font=font_setup)
  timer_up = True
  gameover()

  
else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
 
#-----events----------------
#the game starts
wn.ontimer(countdown, counter_interval)
 
apple.onclick(fruitOnClickA)
pear.onclick(fruitOnClickP)
orange.onclick(fruitOnClickO)
kiwi.onclick(fruitOnClickK)
starFish.onclick(fruitOnClickS)
fruitPosistion()
fruitFalling()
fruitCollisionA()
fruitCollisionK()
fruitCollisionP()
fruitCollisionO()
fruitCollisionS()


wn.listen()
 
wn.mainloop()
