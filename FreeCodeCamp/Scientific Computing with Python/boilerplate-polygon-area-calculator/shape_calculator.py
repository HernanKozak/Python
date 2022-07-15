class Rectangle:
  
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.height*self.width

  def get_perimeter(self):
    return (self.height+self.width)*2

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    response=''
    if(self.width>50 or self.height>50):
      return 'Too big for picture.'
    for i in range(0,self.height):
      response+='*'*self.width
      response+='\n'
    return response

  def __str__(self):
    return 'Rectangle(width='+str(self.width)+', height='+str(self.height)+')'

  def get_amount_inside(self, rectangle2):
    amountHor=int(self.width/rectangle2.width)
    amountVer=int(self.height/rectangle2.height)
    if(amountHor == 0 or amountVer == 0):
      return 0
    return amountHor*amountVer

  

class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.height = side

  def set_side(self, side):
    self.width = side
    self.height = side

  def set_width(self, width):
    self.width = width
    self.height = width

  def set_height(self, height):
    self.height = height
    self.width = height

  def __str__(self):
    return 'Square(side='+str(self.width)+')'