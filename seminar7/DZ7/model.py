

def init(a,b): 
    global x 
    global y
    x = a
    y = b


def searchind(x,y):
    
    for i in x : 
     if y in i: 
       print(i)
       
    else:
      if y not in i:
          with open('lection_1/seminar7/base.txt', 'a') as data:
            data.write(f' ,{y}')
           
      
  
       
    
