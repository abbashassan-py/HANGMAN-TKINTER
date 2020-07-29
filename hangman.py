import tkinter as tk
import random
from tkinter import *
from tkinter import messagebox

#startGame Window
root1= Tk()
root1.wm_title("HANGMAN")
root1.minsize(200,100)
root1.geometry("300x80")
#for icon
root1.iconphoto(False, tk.PhotoImage(file='hangm.ico'))

label = Label(root1)
label.pack()
e = Entry(root1, width=30)
e.insert(0, "Enter your name ")
e.pack()

benter = Button(root1, text="Start Game", width=9, overrelief='groove',cursor="hand2", command= lambda:root1.destroy())
benter.pack()
root1.mainloop()

score = 0
run = True
hint = 0
revealed = None

# main
while run:
    root = Tk()
    e = tk.Entry(root)
    root.geometry('905x700')
    root.title('HANGMAN')
    root.config(bg='#E7FFFF')
    root.maxsize(width=920,height=700)
    root.iconphoto(False, tk.PhotoImage(file='hangm.ico'))

    count = 0
    win_count = 0

    # choosing word
    index = random.randint(0, 853)
    file = open('words.txt', 'r')
    l = file.readlines()
    selected_word = l[index].strip('\n')

    # creation  dashes
    x = 250
    for i in range(0, len(selected_word)):
        x += 60
        exec('d{}=Label(root,text="_",bg="#E7FFFF",font=("arial",40))'.format(i))
        exec('d{}.place(x={},y={})'.format(i, x, 450))

    # letters
    al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']
    for let in al:
        exec('{}=PhotoImage(file="{}.png")'.format(let, let))

    # hang man
    h123 = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7']
    for hangman in h123:
        exec('{}=PhotoImage(file="{}.png")'.format(hangman, hangman))

    # letters placement
    button = [['b1', 'a', 0, 595], ['b2', 'b', 70, 595], ['b3', 'c', 140, 595], ['b4', 'd', 210, 595],
              ['b5', 'e', 280, 595], ['b6', 'f', 350, 595], ['b7', 'g', 420, 595], ['b8', 'h', 490, 595],
              ['b9', 'i', 560, 595], ['b10', 'j', 630, 595], ['b11', 'k', 700, 595], ['b12', 'l', 770, 595],
              ['b13', 'm', 840, 595], ['b14', 'n', 0, 645], ['b15', 'o', 70, 645], ['b16', 'p', 140, 645],
              ['b17', 'q', 210, 645], ['b18', 'r', 280, 645], ['b19', 's', 350, 645], ['b20', 't', 420, 645],
              ['b21', 'u', 490, 645], ['b22', 'v', 560, 645], ['b23', 'w', 630, 645], ['b24', 'x', 700, 645],
              ['b25', 'y', 770, 645], ['b26', 'z', 840, 645]]

    for q1 in button:
        exec(
            '{}=Button(root,bd=0,command=lambda:check("{}","{}"),cursor="mouse",bg="#E7FFFF",activebackground="#E7FFFF",font=10,image={})'.format(
                q1[0], q1[1], q1[0], q1[1]))
        exec('{}.place(x={},y={})'.format(q1[0], q1[2], q1[3]))

    # hangman placement
    han = [['c1', 'h1'], ['c2', 'h2'], ['c3', 'h3'], ['c4', 'h4'], ['c5', 'h5'], ['c6', 'h6'], ['c7', 'h7']]
    for p1 in han:
        exec('{}=Label(root,bg="#E7FFFF",image={})'.format(p1[0], p1[1]))

    # placement of first hangman image
    c1.place(x=300, y=- 50)


    # exit
    def close():
        global run
        answer = messagebox.askyesno('ALERT', 'YOU WANT TO EXIT THE GAME?')
        if answer == True:
            run = False
            root.destroy()
    e1 = PhotoImage(file='exit.png')
    ex = Button(root, bd=0, command=close, bg="#E7FFFF",cursor="mouse", activebackground="#E7FFFF", font=10, image=e1)
    ex.place(x=770, y=10)
    s2 = 'SCORE:' + str(score)
    s1 = Label(root, text=s2, bg="#E7FFFF", font=("arial", 25))
    s1.place(x=10, y=10)
    #replay
    def replay():
        global run
        answer = messagebox.askyesno('ALERT', 'YOU WANT TO RESTART THE GAME?')
        if answer == True:
            run = True
            root.destroy()
    e2 = PhotoImage(file='replay.png')
    ey = Button(root, bd=0, command=replay, bg="#E7FFFF", cursor='mouse', activebackground="#E7FFFF", font=10, image=e2)
    ey.place(x=770, y=65)

       #hint
    def show_hint():
        global hint
        answer = messagebox.askyesno('HINT',"DO YOU WANT TO CHOOSE HINT ?")
        if answer == True:
            root2=Tk()
            root2.title=('HINT')
            root2.geometry('300x100')
            label = Label(root2, text="the hidden word contains the letter/letters::     " + selected_word[2:6]).pack()
            btn=Button(root2, text="OK", width=9, overrelief='groove',cursor="hand2",activebackground="Green",command=root2.destroy)
            btn.pack()

    e3 = PhotoImage(file='hint.png')
    ez = Button(root, bd=0, command=show_hint, bg="#E7FFFF", cursor='mouse', activebackground="#E7FFFF", font=10, image=e3)
    ez.place(x=765, y=110)

    # button press check function
    def check(letter, button):
        global count, win_count, run, score
        exec('{}.destroy()'.format(button))
        if letter in selected_word:
            for i in range(0, len(selected_word)):
                if selected_word[i] == letter:
                    win_count += 1
                    exec('d{}.config(text="{}")'.format(i, letter.upper()))
            if win_count == len(selected_word):
                score += 1
                answer = tk.messagebox.showinfo("Winnerx2-Chicken-Dinner", "You WIN! The word was " + selected_word + "!")
                ans = messagebox.askyesno('WANT TO PLAY AGAIN?')
                if ans == True:
                    run = True
                    root.destroy()
                else:
                    run = False
                    root.destroy()
        else:
            count += 1
            exec('c{}.destroy()'.format(count))
            exec('c{}.place(x={},y={})'.format(count + 1, 300, -50))
            if count == 6:
                answer = tk.messagebox.showinfo("TRY AGAIN", "You LOST! The word was " + selected_word +  "!")
                ans = messagebox.askyesno('GAME OVER', 'YOU LOST!\nWANT TO PLAY AGAIN?')
                if ans == True:
                    run = True
                    score = 0
                    root.destroy()
                else:
                    run = False
                    root.destroy()


    root.mainloop()
