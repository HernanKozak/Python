class Category:

  def __init__(self, catName):
    
    self.categoryName=catName
    self.ledger=[]
    self.balance=0
    
  def check_funds(self, amount):
    if(self.balance >= amount):
      return True
    else:
      return False

  def deposit(self, amount, description=''):
    self.ledger.append({"amount": amount, "description": description})
    self.balance+=amount
    

  def withdraw(self, amount, description=''):
    if(self.check_funds(amount)):
      amount*=-1
      self.balance+=amount
      self.ledger.append({"amount": amount, "description": description})
      return True
    else:
      return False

  def get_balance(self):
    return self.balance

  def transfer(self, amount, destinCategory):
    if(self.check_funds(amount)):
      self.balance-=amount
      self.ledger.append({"amount": (amount*-1), "description": 'Transfer to ' +destinCategory.categoryName})
      destinCategory.deposit(amount, 'Transfer from '+self.categoryName)
      return True
    else:
      return False

  def __str__(self):
    response=''
    stars=30-len(self.categoryName)
    response+='*'*int(stars/2)
    response+=self.categoryName
    if(stars%2==0):
      response+='*'*int(stars/2)
    else:
      response+='*'*int(stars/2+1)
    response+='\n'
    for movement in self.ledger:
      response+=movement["description"][0:23]
      lenDesc=len(movement["description"])
      if(lenDesc<23):
        response+=' '*(23-lenDesc)
      amount="{:.2f}".format(movement["amount"])
      lenNumber=len(amount)
      response+=' '*(7-lenNumber)
      response+=str(amount)
      response+='\n'
    response+='Total: '+str(self.balance)
    return response
 
def create_spend_chart(categories):
  numCategories=len(categories)
  spendings = []
  porcentages = []
  totalSpend = 0
  largestCatName = 0
  
  i=0
  for categorie in categories:
    if(len(categorie.categoryName)>largestCatName):
      largestCatName=len(categorie.categoryName)
    spendings.append(0)
    for movement in categorie.ledger:
      if (movement["amount"]<0):
        amount=(movement["amount"]*-1)
        spendings[i]+=amount
        totalSpend += amount
    i+=1
  
  i=0
  for spent in spendings:
    porcentages.append(0)
    porcentages[i]=(spendings[i]/totalSpend)*100
    i+=1

  response='Percentage spent by category\n'
  
  for i in range(100,0,-10):
    response+=' '*(3-len(str(i)))
    response+=str(i)+'| '
    for por in porcentages:
      if((por/i)>=1):
        response+='o  '
      else:
        response+='   '
    response+='\n'
  
  response+='  0| '
  
  for i in range(0, numCategories):
    response+='o  '
  
  response+='\n'
  
  response+='    '
  response+='-'*(numCategories*3+1)
  response+='\n'

  for i in range(0,largestCatName):
    response+='     '
    for categorie in categories:
      if(i<len(categorie.categoryName)):
        response+=categorie.categoryName[i]+'  '
      else:
        response+='   '
    if(i!=largestCatName-1):
      response+='\n'

  return response
  
    