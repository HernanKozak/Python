import copy
import random
# Consider using the modules imported above.

class Hat:  
  def __init__(self, blue=0, red=0, yellow=0, striped=0, orange=0, black=0, pink=0, green=0, test=0):
    self.contents= []
    for i in range(0,red):
      self.contents.append("red")
    for i in range(0,blue):
      self.contents.append("blue")
    for i in range(0,yellow):
      self.contents.append("yellow")
    for i in range(0,striped):
      self.contents.append("striped")
    for i in range(0,orange):
      self.contents.append("orange")
    for i in range(0,black):
      self.contents.append("black")
    for i in range(0,pink):
      self.contents.append("pink")
    for i in range(0,green):
      self.contents.append("green")
    for i in range(0,test):
      self.contents.append("test")

  def draw (self, number):
    if (number>=len(self.contents)):
      return self.contents
    contents2 = copy.deepcopy(self.contents)
    response = []
    for i in range(0, number):
      out = random.randint(0, len(self.contents)-1)
      response.append(self.contents.pop(out))
    return response
  
      
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  colours = expected_balls.keys()
  succesfulExp = 0
  for i in range(0,num_experiments):
    hatCopy = copy.deepcopy(hat)
    result = hatCopy.draw(num_balls_drawn)
    worked = True
    for colour in colours:
      amount = expected_balls[colour]
      count = 0
      for ball in result:
        if(ball == colour):
          count+=1
      if(count<amount):
        worked = False
        break
    if(worked):
      succesfulExp+=1
  return (succesfulExp/num_experiments)
  
    