def get_data():
   with open('base.txt', 'r') as data: 
      base = data.read()
      base1 = base.split(',')
      return base1
      
