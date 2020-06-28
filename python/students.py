# Your code goes here
import json

if __name__ == "__main__":

    filename = 'students.csv'

    # Ecrivez une fonction permettant de récupérer toutes les lignes
    # du fichier CSV dans une list() `data`
    rows = []
    with open(filename) as my_file:
        for line in my_file:
            rows.append(line)
            
    print(f'\nLe fichier brut contient {len(rows)} lignes')

    # Les étudiants ont chacun un diplôme qui leur est attribué
    # La variable `degrees` contient la liste des diplômes
    degrees = []
    for i in range(0, len(rows)):
        temp = rows[i].split(",")
        rows[i]=  temp
    for i in range(0, len(rows)):
        if len(degrees) == 0:
            degrees.append(rows[i][4])
        present = False
        for x in range(0, len(degrees)):
            if rows[i][4] == degrees[x] and present == False:
                present = True
        if present == False:
            degrees.append(rows[i][4])
            
    print(f'\nLe fichier contient {len(degrees)} diplômes uniques')

    # Donnez, dans un dict, pour chaque diplôme le nombre d'étudiant
    # par catégorie d'utilisateur (student, alumni, ...)
    users_per_degree = {}
    for x in range(0, len(degrees)): # TODO
            users_per_degree[degrees[x]] = 0
    print(users_per_degree)
    for i in range(0, len(rows)):
        for x in range(0, len(degrees)):
            if rows[i][4] == degrees[x]:
                users_per_degree[degrees[x]] = users_per_degree[degrees[x]]+1
    print(f'\nLa répartition des diplômes est la suivante :')
    for degree in users_per_degree.keys():
        print(f' - {degree}, {users_per_degree[degree]} étudiants')

    # Enregistrez le dictionnaire dans un nouveau fichier `degree_count.json`
    # TODO
    savefilename = 'degree_count.json'
    with open(savefilename, 'w') as file:
        file.write(json.dumps(users_per_degree))
    file.close
    print(f'\nFichier `degree_count.json` enregistré !')
