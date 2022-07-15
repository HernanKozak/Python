def arithmetic_arranger(problems, showResults=False):
  if(len(problems)> 5):
    return "Error: Too many problems."
  arranged_problems = ''
  firstNums = []
  secondNums = []
  operators = []
  results = []
  size = []
  
  for problem in problems:
    if(problem.find("*")!=-1 or problem.find("/")!=-1):
      return "Error: Operator must be '+' or '-'."
    
    if(problem.find("+")!=-1):
      numbers=problem.split('+')
      num1=numbers[0].replace(' ', '')
      num2=numbers[1].replace(' ', '')
      if(num1.isnumeric()==False or num2.isnumeric()==False):
        return "Error: Numbers must only contain digits."
      size1=len(num1)
      size2=len(num2)
      if(size1>4 or size2>4):
        return "Error: Numbers cannot be more than four digits."
      if(size1 > size2):
        size.append(size1)
      else:
        size.append(size2)
      firstNums.append(num1)
      secondNums.append(num2)
      operators.append('+')
      results.append(int(num1) + int(num2))
    if(problem.find("-")!=-1):
      numbers=problem.split('-')
      num1=numbers[0].replace(' ', '')
      num2=numbers[1].replace(' ', '')
      if(num1.isnumeric()==False or num2.isnumeric()==False):
        return "Error: Numbers must only contain digits."
      size1=len(num1)
      size2=len(num2)
      if(size1>4 or size2>4):
        return "Error: Numbers cannot be more than four digits."
      if(size1 > size2):
        size.append(size1)
      else:
        size.append(size2)
      firstNums.append(num1)
      secondNums.append(num2)
      operators.append('-')
      results.append(int(num1) - int(num2))

  i=0
  isNotFirst=False
  for x in firstNums:
    if(isNotFirst):
      arranged_problems+=' '*4
    arranged_problems+=' '*(size[i]-len(x)+2)
    arranged_problems+=x
    isNotFirst=True
    i+=1
  arranged_problems+='\n'

  i=0
  isNotFirst=False
  for x in secondNums:
    if(isNotFirst):
      arranged_problems+=' '*4
    arranged_problems+=operators[i]
    arranged_problems+=' '*(size[i]-len(x)+1)
    arranged_problems+=x
    isNotFirst=True
    i+=1
  arranged_problems+='\n'

  i=0
  isNotFirst=False
  for x in firstNums:
    if(isNotFirst):
      arranged_problems+=' '*4
    arranged_problems+='-'*(size[i]+2)
    isNotFirst=True
    i+=1

  if(showResults):
    arranged_problems+='\n'
    i=0
    isNotFirst=False
    for x in results:
      if(isNotFirst):
        arranged_problems+=' '*4
      arranged_problems+=' '*(size[i]-len(str(x))+2)
      arranged_problems+=str(x)
      isNotFirst=True
      i+=1
        
  return arranged_problems