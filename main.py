import random

playHp = 20
victoryCurrent = 0
victoryTotal = 0
lossTotal = 0
fightTotal = 0

def printStatus():
    print("=============================")
    print("Niveau de vie de l’usager ：" + str(playHp))
    print("Combat " + str(fightTotal)+": "+ str(victoryTotal)+" victoire vs "+ str(lossTotal)+" défaite")
    print("=============================")

while True:
    if victoryCurrent >= 3:
        print("打BOSS...")
        fightTotal += 1
        victoryTotal += 1
        victoryCurrent += 1
        victoryCurrent = 0
        print("赢了...")
        continue
    else:
        printStatus()
        monsterDmg = random.randint(1, 5)
        print("Vous tombez face à face avec un adversaire de difficulté:" + str(monsterDmg))
        choice = input('''Que voulez-vous faire ?
1- Combattre cet adversaire
2- Contourner cet adversaire et aller ouvrir une autre porte
3- Afficher les règles du jeu
4- Quitter la partie
                        ''')


        if choice == "1":
            playDmg = random.randint(3, 6)
            print("Lancer du dé：" + str(playDmg))
            if monsterDmg < playDmg:
                print("Dernier combat = gagner")
                playHp = playHp + monsterDmg
                fightTotal += 1
                victoryTotal += 1
                victoryCurrent += 1
            else:
                playHp = playHp - monsterDmg
                fightTotal += 1
                lossTotal += 1
                if playHp <= 0:
                    print("游戏结果")
                    print("Exiting the program...")
                    break

        elif choice == "2":
            monsterDmg = random.randint(1, 6)
            playHp = playHp - 1
            if playHp <= 0:
                print("游戏结果")
                print("Exiting the program...")
                break

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
