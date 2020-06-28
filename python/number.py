# Your code goes here
import math

for i in range(1, 1000):
    if i >= 10: #Le nombre est composé de deux chiffres ou plus
        a = math.floor((i/100)) 
        b = math.floor(((i-a*100)/10))
        c = i-b*10-a*100
        print(a,b,c)        
        if a != 1 and a != 7 and b != 1 and b != 7 and c != 1 and c != 7: #Le nombre ne contient pas de 1, ni de 7
            if a+b+c <= 10: #La somme de ses chiffres est inférieure ou égale 10
                print(i)      
                if i >= 100 and (a+b)%2 == 1: #Les deux premiers chiffres donne un nombre impair quand on les additionne et Si il y a plus de 3 nombres 
                    print(i)      
                    if b == 4 and c == 3: #L'avant dernier chiffre est un 4 et Le dernier chiffre est égal au nombre de chiffre composant le nombre (ici 3)
                        mystery_number = i
                elif b+c%2 == 1:
                    if b == 4 and c == 2: #L'avant dernier chiffre est un 4 et Le dernier chiffre est égal au nombre de chiffre composant le nombre (ici 2)
                        mystery_number = i

print(f'Le nombre mystère est le : {mystery_number}')
