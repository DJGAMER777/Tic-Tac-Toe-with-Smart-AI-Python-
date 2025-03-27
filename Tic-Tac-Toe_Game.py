import random
box = [" " for _ in range(9)]

def print_box():
    print(f" {box[0]} | {box[1]} | {box[2]} ")
    print(f"---|---|---")

    print(f" {box[3]} | {box[4]} | {box[5]} ")
    print(f"---|---|---")
    print(f" {box[6]} | {box[7]} | {box[8]} ")
 
def get_empty_positions(box):
    empty_place = []
    for i in range(len(box)):
        if box[i] == " ":
            empty_place.append(i)
    return empty_place
 
def find_winning_move(player):
    for pos in get_empty_positions(box):
        box[pos] = player
        if Checkwin(player):
            box[pos] = " "
            return pos
        box[pos] = " "
    return None
 
def Checkwin(player):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if box[win[0]]==box[win[1]] == box[win[2]] == player:
            return True
    return False

print_box()
def main():
    move_count = 0
    while move_count < 9 and not Checkwin("X") and not Checkwin("O"):
        try:
            pos = int(input("Player X, position daal (0-8): "))
            if 0 <= pos <= 8 and box[pos] == " ":
                box[pos] = "X"
                move_count += 1
                print_box()
                if Checkwin("X"):
                    print("Player X Jeet Gaya Bhai Congratulations!")
                    break
            else:
                print("Space Full hai ya 0-8 ke beech mein daal Bhai!")
                continue
        except ValueError:
            print("Sahi Number Daal Bhai!")
            continue
        
        empty_positions = get_empty_positions(box)
        if empty_positions:
            win_move = find_winning_move("O")
            if win_move is not None:
                pos = win_move
            else:
                block_move = find_winning_move("X")
                if block_move is not None:
                    pos = block_move    
                else:
                    pos = random.choice(empty_positions)
                    
            print("AI thinking... O ne {pos} pe daala")
            box[pos] = "O"
            move_count += 1
            print_box()
            if Checkwin("O"):
                print("Player O Jeet Gaya Bhai Congratulations!")
                break

    if move_count == 9 and not Checkwin("X") and not Checkwin("O"):
        print("Draw Hogaya bhai!")
        
if __name__ == '__main__':
    main()