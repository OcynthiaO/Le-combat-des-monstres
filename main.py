import random

playHp = 20
victoryCurrent = 0
victoryTotal = 0
lossTotal = 0
fightTotal = 0

def printStatus():
    print("=============================")
    print("当前血量：" + str(playHp))
    print("一共战斗了：" + str(fightTotal))
    print("一共胜利：" + str(victoryTotal))
    print("一共失败：" + str(lossTotal))
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
        monsterDmg = random.randint(1, 1)
        print("当前怪物伤害：" + str(monsterDmg))
        print("选择菜单...")
        choice = input("玩家选择： ").strip()

        if choice == "1":
            playDmg = random.randint(3, 6)
            print("当前玩家伤害：" + str(playDmg))
            if monsterDmg < playDmg:
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
            print("游戏规则")
            print("=============================")

        elif choice == "4":
            print("Exiting the program...")
            break
