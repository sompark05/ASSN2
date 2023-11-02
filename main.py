import os
import random

# 화면을 클리어하는 함수
def clear_screen():
    os.system('cls')
    return


def x_to_blank(s):
    if s == "x":
        return "  "
    return f"{s:2d}"

# 현재까지 얻은 점수 리스트를 파라미터로 전달받아 점수판을 출력하는 함수입니다
def print_score_board(score_list):
    category_list = ["1", "2", "3", "4", "5", "6", "C", "4K", "FH", "SS", "LS", "Y"]
    sub_total = [0, 0]     # first element is sub total of player, second element is sub total of computer
    for i in range(6):
        try:
            sub_total[0] += score_list[i][0]
            sub_total[1] += score_list[i][1]
        except:
            pass

    total = [sub_total[0], sub_total[1]]         # first element is total of player, second element is total of computer
    for j in range(6, 12):
        try:
            total[0] += score_list[j][0]
            total[1] += score_list[j][1]
        except:
            pass

    # print("┌─────────────────────┬─────────────────────┐")
    # print("│        Player       │       Computer      │")
    # print("├─────────────────────┴─────────────────────┤")
    # for i in range(6):
    #     print(f"│ {i+1}:          {x_to_blank(score_list[i][0])}      │ {i+1}:          {x_to_blank(score_list[i][1])}      │")
    # print("├───────────────────────────────────────────┤ ")
    # print(f"│ Sub total: {sub_total[0]:2d}/63    │ Sub total: {sub_total[1]:2d}/63    │")
    # print(f" │ +35 bonus:          │ +35 bonus:          │")
    # print("├───────────────────────────────────────────┤ ")
    # print(f"│ C:          {x_to_blank(score_list[6][0])}      │ C:          {x_to_blank(score_list[6][1])}      │")
    # print("├───────────────────────────────────────────┤ ")
    # for j in range(7, 12):
    #     print(f"│ {category_list[j]}:         {x_to_blank(score_list[j][0])}      │ {category_list[j]}:         {x_to_blank(score_list[j][1])}      │")
    # print("├───────────────────────────────────────────┤ ")
    # print(f"│ Total:     {total[0]:3d}      │ Total:     {total[1]:3d}      │")
    # print("└───────────────────────────────────────────┘")

    print(f"""
┌─────────────────────┬─────────────────────┐
│        Player       │       Computer      │
├─────────────────────┴─────────────────────┤
│ 1:          {x_to_blank(score_list[0][0])}      │ 1:          {x_to_blank(score_list[0][1])}      │
│ 2:          {x_to_blank(score_list[1][0])}      │ 2:          {x_to_blank(score_list[1][1])}      │
│ 3:          {x_to_blank(score_list[2][0])}      │ 3:          {x_to_blank(score_list[2][1])}      │
│ 4:          {x_to_blank(score_list[3][0])}      │ 4:          {x_to_blank(score_list[3][1])}      │
│ 5:          {x_to_blank(score_list[4][0])}      │ 5:          {x_to_blank(score_list[4][1])}      │  
│ 6:          {x_to_blank(score_list[5][0])}      │ 6:          {x_to_blank(score_list[5][1])}      │
├───────────────────────────────────────────┤                     
│ Sub total: {sub_total[0]:2d}/63    │ Sub total: {sub_total[1]:2d}/63    │
│ +35 bonus:          │ +35 bonus:          │
├───────────────────────────────────────────┤                     
│ C:          {x_to_blank(score_list[6][0])}      │ C:          {x_to_blank(score_list[6][1])}      │
├───────────────────────────────────────────┤
│ 4K:         {x_to_blank(score_list[7][0])}      │ 4K:         {x_to_blank(score_list[7][1])}      │
│ FH:         {x_to_blank(score_list[8][0])}      │ FH:         {x_to_blank(score_list[8][1])}      │
│ SS:         {x_to_blank(score_list[9][0])}      │ SS:         {x_to_blank(score_list[9][1])}      │
│ LS:         {x_to_blank(score_list[10][0])}      │ LS:         {x_to_blank(score_list[10][1])}      │
│ Yacht:      {x_to_blank(score_list[11][0])}      │ Yacht:      {x_to_blank(score_list[11][1])}      │
├───────────────────────────────────────────┤
│ Total:     {total[0]:3d}      │ Total:     {total[1]:3d}      │
└───────────────────────────────────────────┘
""")

def load_file2list(filename):
    pass


def check_error(score_list):
    pass


def roll_dice(dice_set=[], reroll_indices=[]):
    for e in reroll_indices:
        try:
            dice_set[e-1] = random.randint(1, 6)
        except:
            pass
    return dice_set

def calc_score(dice_set, sel):
    dice_set = sorted(dice_set)

    if sel == "1":
        return dice_set.count(1)*1
    if sel == "2":
        return dice_set.count(2)*2
    if sel == "3":
        return dice_set.count(3)*3
    if sel == "4":
        return dice_set.count(4)*4
    if sel == "5":
        return dice_set.count(5)*5
    if sel == "6":
        return dice_set.count(6)*6
    if sel == "C":
        return sum(dice_set)
    if sel == "4K":
        for i in range(1, 5):
            if dice_set.count(i) >= 4:
                return sum(dice_set)
        else:
            return 0
    if sel == "FH":
        if dice_set[0] == dice_set[1] and dice_set[2] == dice_set[3] == dice_set[4]:
            return sum(dice_set)
        if dice_set[0] == dice_set[1] == dice_set[2] and dice_set[3] == dice_set[4]:
            return sum(dice_set)
        return 0
    if sel == "SS":
        for i in range(3):
            if dice_set[i] != dice_set[i+1] - 1:
                break
        else:
            return 15
        
        for i in range(1, 4):
            if dice_set[i] != dice_set[i+1] - 1:
                break
        else:
            return 15
        return 0
    if sel== "LS":
        for i in range(5):
            if dice_set[i] != dice_set[i+1] - 1:
                return 0
        else:
            return 30
    if sel == "Y":
        result = all(e == dice_set[0] for e in dice_set)
        if result:
            return 50
        return 0
        


def computer_pattern(dice_set, score_list):
    category_list = ["1", "2", "3", "4", "5", "6", "C", "4K", "FH", "SS", "LS", "Y"]
    int2category = {key:value for key, value in enumerate(category_list)}
    sel = ""
    max_score = 0
    result = []

    for i in range(len(score_list)):
        if score_list[i][1] == "x":
            score = calc_score(dice_set, int2category[i])
            if int2category[i] == "C" and score < 20:
                continue
            if score > max_score:
                max_score = score
                sel = int2category[i]

    if sel in ["4K", "FH", "SS", "LS", "Y"]: 
        return sel, result
    
    if sel == "C":
        for i in range(5):
            if dice_set[i] <= 3:
                result.append(i+1)
        return sel, result
    
    for i in range(5):
        if dice_set[i] != int(sel):
            result.append(i+1)
    return sel, result



def new_game(score_list):
    
    category_list = ["1", "2", "3", "4", "5", "6", "C", "4K", "FH", "SS", "LS", "Y"]
    category2int = {value:key for key, value in enumerate(category_list)}
    player_category = {key:False for key in category_list}
    
    round = 1
    player_deck = []
    com_deck = []
    
    print_score_board(score_list)
    while round <= 12:
        # 플레이어 턴
        print(f"[Player's Turn ({round}/12)]")
        player_deck = roll_dice([0, 0, 0, 0, 0], [1, 2, 3, 4, 5])

        print(f"Roll: {player_deck}")

        roll_cnt = 2

        while roll_cnt > 0:
            try: 
                reroll_indices = list(map(int, input("Which dice to reroll (1~5)? ").split()))
                if reroll_indices == []:
                    break

                player_deck = roll_dice(player_deck, reroll_indices)
                print(f"Roll: {player_deck}")
                roll_cnt -= 1
            except:
                print("Wrong input!")
        

        print(f"\nSorted Roll: {sorted(player_deck)}")
        
        category = input("Choose a category: ").upper()
        while True:
            try:
                if player_category[category] == False:
                    player_category[category] = True
                    break
                print("Wrong Input!")
                category = input("Choose a category: ").upper()
            except:
                print("Wrong Input!")
                category = input("Choose a category: ").upper()

        score = calc_score(player_deck, category)
        category = category2int[category]

        score_list[category][0] = score
        print()
        print_score_board(score_list)
        
        
        # 컴퓨터 턴
        print(f"[Computer's Turn ({round}/12)]")
        com_deck = roll_dice([0, 0, 0, 0, 0], [1, 2, 3, 4, 5])
        print(f"Roll: {com_deck}")

        category = ""
        roll_cnt = 2

        while roll_cnt > 0:
            # 점수판에서 채워지지 않은 칸의 5개의 주사위로 만들 수 있는 점수를 모두 계산한다
            category, reroll_indices = computer_pattern(com_deck, score_list)
            

            if reroll_indices == []: 
                print(f"Which dice to reroll (1~5)? {category}")
                print(f"Roll: {com_deck}")
                break
            else:
                print(f"Which dice to reroll (1~5)? {category} ", end="")
                for e in reroll_indices:
                    print(e, end=" ")

                com_deck = roll_dice(com_deck, reroll_indices)
                print(f"\nRoll: {com_deck}")
                roll_cnt -= 1

        print(f"\nSorted Roll: {com_deck}")
        print(f"Choose a category: {category}")
        score_list[category2int[category]][1] = calc_score(com_deck, category)
        print_score_board(score_list)
        
        round += 1
        input("계속하려면 엔터를 누르세요")
        clear_screen()
        
                
             
                
            

if __name__ == "__main__":
    score_list = [["x", "x"] for i in range(12)]


    print("[Yacht Dice]")
    print("----------------------------------")
    print("1. New Game 2. Load Game 3. Exit")
    print("----------------------------------")
    
    while True:
        menu = int(input("Select a menu: "))

        if menu == 1:
            new_game(score_list)
        elif menu == 2:
            pass
        elif menu == 3:
            print("Program ended. Bye!")
            break
        else:
            print("Wrong Input!")