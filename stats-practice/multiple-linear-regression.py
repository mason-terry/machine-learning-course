#!/usr/local/bin/python3

# Multiple Linear Regression

class Multiple_Linear_Regression:
  ''' will create the multiple linear regression formula  '''
  ''' enter three lists and it create b0, b1, and b3 coefficients '''
  def __init__(self,x,y,z):
    self.x = x
    self.y = y
    self.z = z
    self.b1, self.b2 = self.find_b1()
    self.b0 = self.find_b0()
  
  # Find B1
  def find_b1(self):
    x_tmp = []
    x_tmp_den = []
    y_tmp = []
    z_tmp = []
    x_mean = self.find_mean(self.x)
    y_mean = self.find_mean(self.y)
    z_mean = self.find_mean(self.z)

    for i in self.x:
      x_tmp.append(i - x_mean)

    for i in self.y:
      y_tmp.append(i - y_mean)

    for i in self.y:
      z_tmp.append(i - z_mean)
  
    for i in x_tmp:
      x_tmp_den.append(i * i)

    numerator1 = self.add(self.mult_num(x_tmp, z_tmp))
    numerator2 = self.add(self.mult_num(y_tmp, z_tmp))
    denominator = self.add(x_tmp_den)
    tmp_res_1 = numerator1 / denominator
    tmp_res_2 = numerator2 / denominator

    if denominator == 0:
      return 0
    else:
      return tmp_res_1, tmp_res_2,
  
  
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
    tmp_b1 = self.b1 * self.find_mean(self.x)
    tmp_b2 = self.b2 * self.find_mean(self.y)
    tmp_list = [tmp_b1, tmp_b2]
    return self.find_mean(self.y) - self.find_mean(tmp_list)

  def predict(self):
    next_x = float(input('Please enter a new x data point: '))
    next_y = float(input('Please enter a new x data point: '))
    prediction = self.b0 + (self.b1 * next_x) + (self.b2 * next_y)
    print('This should be the next z value: ', prediction)

  def __str__(self):
    return 'Formula: z = {0:.2f} + {1:.2f} * x + {2:.2f} * y'.format(self.b0, self.b1, self.b2)


list1 = input('Enter the list data for column x (separate with commas)): ')
list2 = input('Enter the list data for column y (separate with commas)): ')
list3 = input('Enter the list data for column z (separate with commas)): ')

def format_list(lst):
  res = []
  for i in lst.split(','):
    res.append(float(i))

  return res

x = format_list(list1)
y = format_list(list2)
z = format_list(list3)

coefficients = Multiple_Linear_Regression(x,y,z)

print(coefficients)
coefficients.predict()

