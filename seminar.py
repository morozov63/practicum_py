
#Задача 1

a = int(input('Введите число от 1 до 7: '))
if a in range(1,6):
 print('Будний день')
elif a in range(6,8):
 print ('Выходной')
else:
 print("Неверное число")

 #Задача 2 Тут я так и не понял, что нужно сделать :-(, 
 # может быть что то в таком духе. После 2го семинара 
 # надеюсь все будет понятно 

X = input('True или False: ')
Y = input('True или False: ')
Z = input('True или False: ')
if not(X or Y or Z) == (not X and not Y and not Z):
    print(1)
else:
    print(0)

    #Задача 3

a = int(input('Введите координату Х: '))
b = int(input('Введите координату Y: '))
if a > 0 and b > 0:
    print (1)
elif a < 0 and b > 0:
    print (2)
elif a < 0 and b < 0:
    print (3)  
elif a > 0 and b < 0:
    print (4)  
else:
    print('X и Y не равны 0!') 

    #Задача 4

a = int(input('Введите число от 1 до 4: '))
if a == 1:
    print( 'X > 0 and Y > 0')
elif a == 2:
    print( 'X < 0 and Y > 0')   
elif a == 3:
    print( 'X < 0 and Y < 0') 
elif a == 4:
    print( 'X > 0 and Y < 0') 
else:
    print('Введите число от 1 до 4: ')

#Задача 5

a = int(input('Введите координату Х1: '))
b = int(input('Введите координату Y1: '))
c = int(input('Введите координату Х2: '))
d = int(input('Введите координату Y2: '))
l = ((c - a)**2 + (d - b)**2) **0.5
print (round (l, 3))
