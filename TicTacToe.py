import numpy as np
board = np.array([["A", "B", "C"],
            ["D", "E", "F"],
            ["G", "H", "I"]])
win = ""
print(board)
for x in range(5):
    p1 = input("Masukkan pilihanmu sesuai huruf yang tertera (Pemain X) : ")
    while p1 not in board or p1 == "X" or p1 == "O":
        print("Tidak valid :)")
        p1 = input("Masukkan pilihanmu sesuai huruf yang tertera (Pemain X) : ")
    z = np.where(board == p1)
    board[z] = "X"
    print(board)
    for a in range(3):
        if board[a,0] == board[a,1] == board[a,2] or board[0,a] == board[1,a] == board[2,a] or board[0,0] == board[1,1] == board[2,2] or board[0,2] == board[1,1] == board[2,0]:
            win = "Pemain 1"
    if win != "":
        break
    if x == 4:
        break
    p2 = input("Masukkan pilihanmu sesuai huruf yang tertera (Pemain O) : ")
    while p2 not in board or p2 == "X" or p2 == "O":
        print("Tidak valid :)")
        p1 = input("Masukkan pilihanmu sesuai huruf yang tertera (Pemain X) : ")
    q = np.where(board == p2)
    board[q] = "O"
    print(board)
    for a in range(3):
        if board[a,0] == board[a,1] == board[a,2] or board[0,a] == board[1,a] == board[2,a] or board[0,0] == board[1,1] == board[2,2] or board[0,2] == board[1,1] == board[2,0]:
            win = "Pemain 2"
    if win != "":
        break

if win == "Pemain 1": 
    print("Selamat, Pemain 1 memenangkan permainan!")
elif win == "Pemain 2":
    print("Selamat, Pemain 2 memenangkan permainan!")
elif win == "":
    print("Permainan Seri!")