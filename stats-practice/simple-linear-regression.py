#!/usr/local/bin/python3

# Simple Linear Regression Formula Maker

class Simple_Linear_Regression:
  ''' will create the simple linear regression formula  '''
  ''' enter two lists and it create b0 and b1 coefficients '''
  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.b1 = self.find_b1()
    self.b0 = self.find_b0()
  
  # Find B1
  def find_b1(self):
    x_tmp = []
    x_tmp_den = []
    y_tmp = []
    x_mean = self.find_mean(self.x)
    y_mean = self.find_mean(self.y)

    for i in self.x:
      x_tmp.append(i - x_mean)

    for i in self.y:
      y_tmp.append(i - y_mean)
  
    for i in x_tmp:
      x_tmp_den.append(i * i)

    numerator = self.add(self.mult_num(x_tmp, y_tmp))
    denominator = self.add(x_tmp_den)

    if denominator == 0:
      return 0
    else:
      return numerator / denominator
  
  
  def find_mean(self, lst):
    tmp = 0
    for num in lst:
      tmp += num
  
    return tmp / len(lst) 

  def add(self, lst):
    tmp = 0
    for num in lst:
      tmp += num
  
    return tmp

  def mult_num(self, lst1, lst2):
    tmp = []
    for i in range(len(lst1)):
      tmp.append(lst1[i] * lst2[i])

    return tmp

  # Find B0
  def find_b0(self):
    return self.find_mean(self.y) - self.b1 * self.find_mean(self.x)

  def predict(self):
    next_num = float(input('Please enter a new x data point: '))
    prediction = self.b0 + (self.b1 * next_num)
    print('This should be the next y value: ', prediction)

  def __str__(self):
    return 'Formula: y = {0:.2f} + {1:.2f} * x'.format(self.b0, self.b1)


list1 = input('Enter the list data for column x (separate with commas)): ')
list2 = input('Enter the list data for column y (separate with commas)): ')

def format_list(lst):
  res = []
  for i in lst.split(','):
    res.append(float(i))

  return res

x = format_list(list1)
y = format_list(list2)

coefficients = Simple_Linear_Regression(x,y)

print(coefficients)
coefficients.predict()

