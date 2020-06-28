# Your code goes here
import math

for i in range(1, 1000):
    if i >= 10:
        a = math.floor((i/100)) 
        b = math.floor(((i-a*100)/10))
        c = i-b*10-a*100
        print(a,b,c)        
        if a != 1 and a != 7 and b != 1 and b != 7 and c != 1 and c != 7:
            if a+b+c <= 10:
                print(i)      
                if i >= 100 and (a+b)%2 == 1:
                    print(i)      
                    if b == 4 and c == 3:
                        mystery_number = i
                elif b+c%2 == 1:
                    if b == 4 and c == 2:
                        mystery_number = i

print(f'Le nombre mystère est le : {mystery_number}')
