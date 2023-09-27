import random
force_adversaire = random.randint(1, 5)

print('Vous tombez face à face avec un adversaire de difficulté :'+str(force_adversaire))

choix = int(input('Que voulez-vous faire?: \n'
                      '1- Combattre cet adversaire\n'
                      '2- Contourner cet adversaire et aller ouvrir une autre\n'
                      '3- Afficher les règles du jeu\n'
                      '4- Quitter la partie\n'))

while True:
    if choix == 1:
        print("Combattre cet adversaire")
    elif choix == 2:
        print("Contourner cet adversaire et aller ouvrir une autre")
    elif choix == 3:
        print('''Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.
Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.
Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire. 
Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.
La partie se termine lorsque les points de vie de l’usager tombent sous 0.
L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.
''')
        break
    elif choix == 4:
        print("Merci et au revoir...")
        break
    else:
        print("Erreur")
        break