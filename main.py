import random

playHp = 20
victoryCurrent = 0
victoryTotal = 0
lossTotal = 0
fightTotal = 0
monsterTotal= 0

def printStatus():
    print("=============================")
    print("Adversaire:"+ str(monsterTotal))
    print("Force de l’adversaire: "+str(monsterDmg))
    print("Niveau de vie de l’usager：" + str(playHp))
    print("Combat " + str(fightTotal)+": "+ str(victoryTotal)+" victoire vs "+ str(lossTotal)+" défaite")
    print("=============================")

while playHp <= 0:
    if victoryCurrent >= 3:
        print("BOSS...")
        monsterDmg = random.randint(2,12
        print("Vous tombez face à face avec un adversaire de difficulté:" + str(monsterDmg))
        monsterTotal += 1
        printStatus()
        victoryTotal += 1
        victoryCurrent = 0
        if choice == "1":
            playDmg = random.randint(3, 6)
            print("Lancer du dé：" + str(playDmg))
            if monsterDmg < playDmg:
                print("Dernier combat = gagner")
                print("")
                playHp = playHp + monsterDmg
                fightTotal += 1
                victoryTotal += 1
                victoryCurrent += 1
            else:
                print("Dernier combat = défaite")
                print("")
                playHp = playHp - monsterDmg
                fightTotal += 1
                lossTotal += 1

    else:
        monsterDmg = random.randint(1,5 )
        print("Vous tombez face à face avec un adversaire de difficulté:" + str(monsterDmg))
        monsterTotal += 1
        printStatus()
        choice = input('''Que voulez-vous faire ?
1- Combattre cet adversaire
2- Contourner cet adversaire et aller ouvrir une autre porte
3- Afficher les règles du jeu
4- Quitter la partie
                        ''')
        if choice == "1":
            playDmg = random.randint(1, 6)
            print("Lancer du dé：" + str(playDmg))
            if monsterDmg < playDmg:
                print("Dernier combat = gagner")
                print("")
                playHp = playHp + monsterDmg
                fightTotal += 1
                victoryTotal += 1
                victoryCurrent += 1
            else:
                print("Dernier combat = défaite")
                print("")
                playHp = playHp - monsterDmg
                fightTotal += 1
                lossTotal += 1


        elif choice == "2":
            playHp = playHp - 1


        elif choice == "3":
            print("=============================")
            print('''Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  
Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.
Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.
Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.

La partie se termine lorsque les points de vie de l’usager tombent sous 0.

L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.
''')
            print("=============================")

        elif choice == "4":
            print("Merci et au revoir...")
            break

print("La partie est terminée, vous avez vaincu "+str(victoryTotal)+" nombre_victoires monstre(s)")
print("Exiting the program...")

#if playHp <= 0:
    #print(La partie est terminée, vous avez vaincu "+str(victoryTotal)+" nombre_victoires monstre(s)")
    #print("Exiting the program...")
    #break
