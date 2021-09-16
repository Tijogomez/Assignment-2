import random
game_cache={}
def game():
    rounds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    end = False
    combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    comp_choice=[1,2,3,4,5,6,7,8,9]
    def draw():
        print(rounds[0], rounds[1], rounds[2])
        print(rounds[3], rounds[4], rounds[5])
        print(rounds[6], rounds[7], rounds[8])
        print()

    def player1():
        n = choices()
        if rounds[n] == "X" or rounds[n] == "O":
            print("\nYou can't go there. Try again")
            player1()
        else:
            rounds[n] = "X"

    def comp():
        n = random.choice(comp_choice)
        if rounds[n] == "X" or rounds[n] == "O":
            print("\nYou can't go there. Try again")
            comp()
        else:
            rounds[n] = "O"

    def choices():
        while True:
            while True:
                a = int(input())
                try:
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print("\nThat's not on the board. Try again")
                        continue
                except ValueError:
                    print("\nThat's not a number. Try again")
                    continue

    def board():
        count = 0
        for a in combinations:
            if rounds[a[0]] == rounds[a[1]] == rounds[a[2]] == "X":
                print("Player Wins!\n")
                print("Congratulations!\n")
                rounds[9]=0
                return True
            if rounds[a[0]] == rounds[a[1]] == rounds[a[2]] == "O":
                print("Computer Wins!\n")
                print("Congratulations!\n")
                rounds[9]=1
                return True
        for a in range(9):
            if rounds[a] == "X" or rounds[a] == "O":
                count += 1
            if count == 9:
                print("The game ends in a Tie\n")
                return True

    while not end:
        draw()
        end = board()
        temp=rounds

        if end == True:
            break
        print("Player 1 choose where to place a cross")
        player1()
        print()
        draw()
        end = board()
        if end == True:
            break
        print("Player 2 choose where to place a nought")
        comp()
        print()
    return rounds
i=0
while i<10:
    i+=1
    x=game()
    game_cache[i]=x
round_number=int(input("ENTER THE ROUND :"))
round_number_dec=round_number-1
y=game_cache[round_number]
print(y[0], y[1], y[2])
print(y[3], y[4], y[5])
print(y[6], y[7], y[8])
if(y[9]==0):
    print("PLAYER WON THE ROUND {}",(round_number_dec))
else:
    print("COMPUTER WON THE ROUND {}",(round_number_dec))
