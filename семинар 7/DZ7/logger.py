def get_data():
   with open('lection_1/seminar7/base.txt', 'r') as data: # здесь, если в одной папке, наверное можно просто base.txt
      base = data.read()
      base1 = base.split(',')
      return base1
      
