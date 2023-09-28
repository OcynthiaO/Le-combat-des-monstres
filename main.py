import random
force_adversaire = random.randint(1, 5)
force_adversaire_Boss = random.randint(1, 16)
force_joueur= random.randint(1,12)
niveau_vie = 20

def adversaire(int):
    print('Vous tombez face à face avec un adversaire de difficulté :'+str(force_adversaire))


def choix (int):
    global nombre
    nombre=int(input('Que voulez-vous faire?: \n'
                      '1- Combattre cet adversaire\n'
                      '2- Contourner cet adversaire et aller ouvrir une autre\n'
                      '3- Afficher les règles du jeu\n'
                      '4- Quitter la partie\n'))



adversaire(int)
choix(int)
while True:
    if nombre == 1:
        print("Combattre cet adversaire")

    elif nombre == 2:
        niveau_vie-=1
        print('Niveau de vie de l’usager: '+str(niveau_vie))
        adversaire(int)
        choix(int)

    elif nombre == 3:
        print('''règles:
Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.
Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.
Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire. 
Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.
La partie se termine lorsque les points de vie de l’usager tombent sous 0.
L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.
''')
        adversaire(int)
        choix(int)
    elif nombre == 4:
        print("Merci et au revoir...")
        break
    else:
        print("Erreur")
        break