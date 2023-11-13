# 20230689 박소망

import os
import random

# 화면을 클리어하는 함수
def clear_screen():
    os.system('cls')
    return


# string 변수를 파라미터로 받아 "x"라면 " "을 리턴하고, 아니라면 파라미터를 그대로 리턴한다
def x_to_blank(s):
    if s == "x":
        return "  "
    return f"{s:2d}"


# 현재까지 얻은 점수 리스트를 파라미터로 전달받아 점수판을 출력하는 함수입니다
def print_score_board(score_list):
    global total

    # player_error나 com_error가 True라면 1~6까지 카테고리가 다 채워지지 않은 것이다
    player_error = False
    com_error = False
    player_bonus = ""
    com_bonus = ""
    sub_total = [0, 0]     # first element is sub total of player, second element is sub total of computer
    for i in range(6):
        try:
            sub_total[0] += score_list[i][0]
        except:
            player_error = True
        try:
            sub_total[1] += score_list[i][1]
        except:
            com_error = True

    total = [sub_total[0], sub_total[1]]         # first element is total of player, second element is total of computer
    for j in range(6, 12):
        try:
            total[0] += score_list[j][0]
        except:
            pass
        try:
            total[1] += score_list[j][1]
        except:
            pass
    
    # sub_total이 다 채워졌다면 63 이상인지 아닌지 확인
    if not player_error:
        if sub_total[0] >= 63:
            player_bonus = "35"
        else:
            player_bonus = "0"
        total[0] += int(player_bonus)
    if not com_error: 
        if sub_total[1] >= 63:
            com_bonus = "35"
        else:
            com_bonus = "0"
        total[1] += int(com_bonus)

    # score board를 화면에 출력한다
    print(f"""┌─────────────────────┬─────────────────────┐
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
│ +35 bonus: {player_bonus:2s}       │ +35 bonus: {com_bonus:2s}       │
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


# 파일명을 string으로 받아 score_list를 반환하는 함수
def load_file2list(filename):
    score_list = ["x" for i in range(12)]

    # 파일을 열어 읽는다
    with open(filename, "r") as fr:
        for l in fr:
            a, b, c = l.split()
            a = a[:-1]
            try:
                score_list[category2int[a]] = [b, c]
            except:
                score_list.append([b, c])
    return score_list        


# score_list와 int2category를 파라미터로 받아, score_list를 파일로 저장해주는 함수
def save_list2file(score_list, int2category):
    file_name = input("Game paused. Enter the filename to save: ")
                    
    with open(file_name, "w") as fw:
        for i in range(12):
            fw.write(f"{int2category[i]}: {score_list[i][0]} {score_list[i][1]}\n")
    
    print("File saved.\n")


# score_list를 파라미터로 받아, 유효한 값들을 가지고 있는지 판단하여 True/False를 반환하는 함수
def check_error(score_list):
    
    # score_list에 있는 값들을 'x'가 아니라면 int 타입으로 변경해 준다
    for i in range(len(score_list)):
        for j in range(2):
            if score_list[i][j] != 'x':
                try:
                    score_list[i][j] = int(score_list[i][j])
                except:
                    return True
                
    # score_list의 길이가 12가 아니라면 error
    if len(score_list) != 12:
        return True
   
    # 1번째부터 6번째 요소까지 유효한지 확인
    for i in range(1, 7):
        for j in range(2):
            if score_list[i-1][j] == "x":
                continue
            if score_list[i-1][j] not in [0, i, i*2, i*3, i*4, i*5] and score_list[i-1][j] != -1: 
                return True

    # 카테고리 C에 대하여 오류 확인
    if score_list[6][0] == "x":
        pass
    elif score_list[6][0] < 5 or score_list[6][0] > 30:   # c
        return True

    if score_list[6][1] == "x":
        pass
    elif score_list[6][1] < 5 or score_list[6][1] > 30:
        return True

    for k in range(2):
        # 카테고리 4k에 대하여 오류 확인
        if score_list[7][k] == "x":
            pass
        elif (score_list[7][k] < 5 or score_list[7][k] > 30) and score_list[7][k] != 0:   # 4K
            return True
        
        # 카테고리 FH에 대하여 오류 확인
        if score_list[8][k] == "x":
            pass
        elif (score_list[8][k] < 5 or score_list[8][k] > 30)and score_list[8][k] != 0:   # FH
            return True
        
        # 카테고리 SS에 대하여 오류 확인
        if score_list[9][k] == "x":
            pass
        elif score_list[9][k] != 0 and score_list[9][k] != 15: # SS
            return True
        
        # 카테고리 LS에 대하여 오류 확인
        if score_list[10][k] == "x":
            pass
        elif score_list[10][k] != 0 and score_list[10][k] != 30: # LS
            return True
        
        # 카테고리 Y에 대하여 오류 확인
        if score_list[11][k] == "x":
            pass
        elif score_list[11][k] != 0 and score_list[11][k] != 50: # Y
            return True

    return False
    
    
# dice_set과 reroll_indices를 파라미터로 받아 주사위를 돌리고 dice_set을 반환한다
def roll_dice(dice_set=[], reroll_indices=[]):
    for e in reroll_indices:
        try:
            dice_set[e-1] = random.randint(1, 6)
        except:
            pass
    return dice_set


# dice_set과 sel 파라미터를 바탕으로 점수를 계산, 반환한다
def calc_score(dice_set, sel):
    sorted_dice_set = sorted(dice_set)

    # 각 숫자가 나온 주사위 눈의 총합을 반환
    if sel == "1":
        return sorted_dice_set.count(1)*1
    if sel == "2":
        return sorted_dice_set.count(2)*2
    if sel == "3":
        return sorted_dice_set.count(3)*3
    if sel == "4":
        return sorted_dice_set.count(4)*4
    if sel == "5":
        return sorted_dice_set.count(5)*5
    if sel == "6":
        return sorted_dice_set.count(6)*6
    
    # 모든 주사위의 합을 반환
    if sel == "C":
        return sum(sorted_dice_set)
    
    # 조건을 만족한다면 모든 주사위의 합을 반환
    if sel == "4K":
        for i in range(1, 7):
            if sorted_dice_set.count(i) >= 4:
                return sum(dice_set)
        else:
            return 0
        
    # 조건을 만족한다면 모든 주사위의 합을 반환
    if sel == "FH":
        if sorted_dice_set[0] == sorted_dice_set[1] and sorted_dice_set[2] == sorted_dice_set[3] == sorted_dice_set[4]:
            return sum(dice_set)
        if sorted_dice_set[0] == sorted_dice_set[1] == sorted_dice_set[2] and sorted_dice_set[3] == sorted_dice_set[4]:
            return sum(sorted_dice_set)
        return 0
    
    # 조건을 만족한다면 15를 반환
    if sel == "SS":
        s = set(sorted_dice_set)
        sorted_dice_set = list(s)
        if len(sorted_dice_set) < 4:
            return 0
        for i in range(len(sorted_dice_set)-1):
            if sorted_dice_set[i] != sorted_dice_set[i+1] - 1:
                return 0
        else:
            return 15
        
    # 조건을 만족한다면 30을 반환    
    if sel== "LS":
        for i in range(4):
            if sorted_dice_set[i] != sorted_dice_set[i+1] - 1:
                return 0
        else:
            return 30
        
     # 조건을 만족한다면 50을 반환
    if sel == "Y":
        result = all(e == sorted_dice_set[0] for e in sorted_dice_set)
        if result:
            return 50
        return 0
        

# 컴퓨터의 동작을 경절하는 함수
def computer_pattern(dice_set, score_list):
    sel = ""
    max_score = 0
    result = []
    sel_left = 0 

    # 모든 카테고리에 대해서, 만약 아직 값이 없다면 calc_score 함수를 이용하여 점수를 계산하고
    # 가장 높은 점수를 가진 카테고리가 무엇인지 찾는다
    for i in range(len(score_list)):
        if score_list[i][1] == "x":
            sel_left += 1
            score = calc_score(dice_set, int2category[i])
            #print(int2category[i], score)
            if int2category[i] == "C" and score < 20:
                continue
            if score >= max_score:
                max_score = score
                sel = int2category[i]
    
    # 카테고리가 1~6이라면, 그 숫자가 아닌 다른 숫자가 나온 모든 주사위들의 인덱스를 result에 넣어 반환한다.
    if sel in ["1", "2", "3", "4", "5", "6"]:
        for i in range(5):
            if dice_set[i] != int(sel):
                result.append(i+1)
        return sel, result
    
    # 모든 카테고리에 대해서 점수가 0이라면, 모든 주사위를 다시 굴린다
    if max_score == 0:
        result = [1, 2, 3, 4, 5]
    
    # 카테고리가 "4K", "FH", "SS", "LS", "Y" 중 하나라면 빈 리스트 또는 [1, 2, 3, 4, 5]을 반환한다
    if sel in ["4K", "FH", "SS", "LS", "Y"]: 
        return sel, result
    
    # 만약 하나 남은 카테고리가 C이고 20 이하라면 C를 카테고리로 다시 설정해준다.
    if sel_left == 1 and score_list[6][1] == "x":
        sel = "C"

    # 카테고리가 "C"일 때는 3이한 주사위를 모두 굴린다
    if sel == "C":
        if max_score == 0:
            result = []
        for i in range(5):
            if dice_set[i] <= 3:
                result.append(i+1)
        return sel, result
    

# score_list를 파라미터로 받아 게임을 실행하는 함수
def start_game(score_list):
    global total
    player_category = {key:False for key in category_list}
    
    # score_list를 읽어 몇 번째 라운드인지 확인한다
    round = 1
    for l in score_list:
        if l[0] == "x":
            continue
        round += 1
    
    player_deck = []
    com_deck = []
    print("\nStarting a game...")
    print_score_board(score_list)

    # 12라운드까지 게임을 진행한다
    while round <= 12:
        # 플레이어 턴
        print(f"[Player's Turn ({round}/12)]")

        # roll_dice를 통해 player_deck을 초기화 해준다
        player_deck = roll_dice([0, 0, 0, 0, 0], [1, 2, 3, 4, 5])
        print(f"Roll: {player_deck}")

        roll_cnt = 2

        # 최대 2번까지 더 주사위를 돌릴 수 있다
        while roll_cnt > 0:
            user_input = input("Which dice to reroll (1~5)? ")

            # 만약 플레이어가 'Q'를 입력했다면 파일을 저장하고 게임 실행을 종료한다
            if user_input.upper() == "Q":
                save_list2file(score_list, int2category)
                return
            
            # 올바른 인덱스들이 들어온다면, 그 인덱스들만 다시 돌린다
            try: 
                reroll_indices = list(map(int, user_input.split()))
                
                
                # 만약 reroll_indices에 있는 모든 정수들이 1~5 범위에 있지 않으면 엔터를 친 것과 같은 효과를 낸다
                for e in reroll_indices:
                    if e in [1, 2, 3, 4, 5]:
                        break
                else:
                    reroll_indices = []

                # 엔터를 쳐서 아무것도 들어오지 않았을 때
                if reroll_indices == []:
                    break

                player_deck = roll_dice(player_deck, reroll_indices)
                print(f"Roll: {player_deck}")
                roll_cnt -= 1
            except:
                print("Wrong input!")
        
        print(f"\nSorted Roll: {sorted(player_deck)}")
        
        # 플레이어 주사위를 다 돌렸다면, 카테고리를 입력 받는다. 
        category = input("Choose a category: ")
        while True:
            if category.upper() == "Q":
                save_list2file(score_list, int2category)
                return
            category = category.upper()
            try:
                if player_category[category] == False:
                    player_category[category] = True
                    break
                print("Wrong Input!")
                category = input("Choose a category: ")
            except:
                print("Wrong Input!")
                category = input("Choose a category: ")

        # 플레이어의 주사위들과 플레이어가 선택한 카테고리를 바탕으로 점수를 계산한다. 
        score = calc_score(player_deck, category)
        category = category2int[category]

        # score_list에 점수를 업데이트 해준다
        score_list[category][0] = score
        print()
        print_score_board(score_list)
        
        
        # 컴퓨터 턴
        print(f"[Computer's Turn ({round}/12)]")
        com_deck = roll_dice([0, 0, 0, 0, 0], [1, 2, 3, 4, 5])
        print(f"Roll: {com_deck}")

        category = ""
        roll_cnt = 2

        # 최대 2번까지 더 주사위를 돌려준다
        while roll_cnt > 0:
            # 점수판에서 채워지지 않은 칸의 5개의 주사위로 만들 수 있는 점수를 모두 계산한다
            category, reroll_indices = computer_pattern(com_deck, score_list)
            
            # 다시 돌려야할 인덱스들을 확인 해준다
            if reroll_indices == []:                                    # 다시 돌릴 인덱스가 없는 경우
                print(f"Which dice to reroll (1~5)? ")
                print(f"Roll: {com_deck}")
                break
            else:                                                       # 다시 돌릴 인덱스가 있는 경우
                print(f"Which dice to reroll (1~5)? ", end="")
                for e in reroll_indices:
                    print(e, end=" ")

                com_deck = roll_dice(com_deck, reroll_indices)
                print(f"\nRoll: {com_deck}")
                roll_cnt -= 1

        # 최종적으로 얻은 com_deck을 출력하고, computer_pattern() 함수를 다시 돌려 최종적으로 선택할 카테고리를 결정한다
        print(f"\nSorted Roll: {sorted(com_deck)}")
        category, reroll_indices = computer_pattern(com_deck, score_list)
        print(f"Choose a category: {category}")
        score_list[category2int[category]][1] = calc_score(com_deck, category)
        print_score_board(score_list)
        
        round += 1
        input("Press Enter to continue...")
        clear_screen()
    
    # 12 라운드가 끝나고 승패를 출력한다
    print("<Final Score Board>")
    print_score_board(score_list)
    if total[0] > total[1]:
        print("You win!")
    elif total[0] < total[1]:
        print("You lose!")
    else:
        print("Draw")
    input("\nPress Enter to continue...")


if __name__ == "__main__":

    category_list = ["1", "2", "3", "4", "5", "6", "C", "4K", "FH", "SS", "LS", "Y"]
    # 카테고리에서 int로 변환할 때 사용하는 딕셔너리
    category2int = {value:key for key, value in enumerate(category_list)}
    # int에서 카테고리로 변환할 때 사용하는 딕셔너리
    int2category = {key:value for key, value in enumerate(category_list)}

    game = True
    
    # 메인 게임 실행을 위한 while loop
    while game:
        # score_list 초기화 및 변수 선엄
        score_list = [["x", "x"] for i in range(12)]
        total = [0, 0]
        
        print("[Yacht Dice]")
        print("----------------------------------")
        print("1. New Game 2. Load Game 3. Exit")
        print("----------------------------------")

        # 플레이어가 3을 입력해서 exit하기 전까지 실행
        while True:

            # 플레이어한테 menu를 입력받아 int가 아니라면 다시 입력 받는다
            try:
                menu = int(input("Select a menu: "))
            except:
                print("Wrong Input!\n")
                continue
            
            if menu == 1:                                       # menu가 1이면 게임 실행
                start_game(score_list)
                break
            elif menu == 2:                                     # menu가 2이면 파일 로드
                filename = ""

                # 플레이어가 유효한 파일을 입력할 때까지 입력을 받는다
                while True:
                    filename = input("Enter filename to load: ")

                    # 파일이 존재하는지 여부를 판단
                    if not os.path.isfile(filename):
                        print("File does not exist.")
                        continue
                    score_list = load_file2list(filename)

                    # check_error 함수를 통해 파일 내용이 유효한지 판단
                    if check_error(score_list):
                        print("Invalid file content.")
                        continue
                    break

                # 파일에서 전달 받은 score_list를 바탕으로 게임을 실행
                start_game(score_list)
                break
            elif menu == 3:                                     # menu가 3이면 프로그램 종료
                print("Program ended. Bye!")
                game = False
                break
            else:
                print("Wrong Input!\n")
    