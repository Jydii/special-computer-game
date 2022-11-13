import random
import tkinter as tk
from tkinter import messagebox as messagebox


class SpecialComputerGame:

    def __init__(self, p_name, p_choice, c_choice, num_ch, ch_num, a, b, player, comp, draw, game_num):
        self.p_name = p_name  # Player name
        self.p_choice = p_choice  # Player's choice
        self.c_choice = c_choice  # Computer's choice in integer
        self.num_ch = num_ch  # Computers choice converted to string
        self.ch_num = ch_num  # players's choice converted to integer
        self.a = a  # String to display winner's condition of win
        self.b = b  # String to display winner
        self.player = player  # Player's score
        self.comp = comp  # Computer's score
        self.draw = draw  # Number of draw's
        self.game_num = game_num  # Game round number

    # Function to start a new game as a new player
    def replay_new(self):
        self.p_name = None  # Setting old name to None so it would ask for a new name
        var_check.set(0)  # Setting variable value of check button to unchecked state
        var.set("n")  # Setting variable value of radio button to "n" which is the  default value
        SpecialComputerGame.run_multiple(self)

    # Function to start a game with the previous players name
    def replay_old(self):
        var_check.set(0)  # Setting variable value of check button to unchecked state
        var.set("n")  # Setting variable value of radio button to "n" which is the  default value
        SpecialComputerGame.run_multiple(self)

    # Function to determine if to start game from the screen asking for name or to just continue with a new round
    def run_multiple(self):
        # Setting scores value to zero so it doesnt display score's from the old tournament
        self.player = 0
        self.comp = 0
        self.draw = 0
        self.game_num = 0
        if self.p_name is None:  # If self.p_name is none it then start from the page asking for name
            SpecialComputerGame.start_game(self)  # Page asking for name and storing it in self

        SpecialComputerGame.r_loop(self, self.p_name)  # function to play game 5 times and display final score

    # Function to start game from asking for name
    def start_game(self):
        # Setting tkinter widget's to ask for name and button to start game
        frame = tk.Frame(root, bg='black')
        label = tk.Label(frame, text="Welcome, Whats your Name ?", font=('Courier', 27), fg='#ededed', bg='#262626')
        name = tk.Entry(frame, font=('Courier', 40), fg='#ededed', bg='#262626', bd=2)
        button = tk.Button(frame, text="Start Game", highlightbackground='#3cf03c', bg='#3cf03c', fg="black",
                           font=('Courier', 27), command=lambda: SpecialComputerGame.r_loop(self, name.get()))
        # Positioning and displaying widgets's
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        label.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=0.1)
        name.place(relx=0.15, rely=0.45, relwidth=0.7, relheight=0.1)
        button.place(relx=0.35, rely=0.60, relwidth=0.3, relheight=0.1)
        root.mainloop()

    # Function to play game 5 times and display final score
    def r_loop(self, name):
        self.p_name = name  # Setting name in self
        self.game_num += 1  # adding 1 to game tournament number for every iteration
        while self.game_num <= 5:  # Running game for 5 times
            b = int(var_check.get())  # Assigning position of check button to b, 1 = checked while 2 = unchecked
            if b == 1:  # If checked button is checked then set the radio button to the last value
                var.set(var.get())
            else:  # If not checked set the value to the default value which is "n"
                var.set("n")
            SpecialComputerGame.first_loop(self)  # Then run the while game number is <= 5
        SpecialComputerGame.final_score(self)  # function to display final score page after the 5'th round

    # Function for computer to make a random selection
    def comp_choice(self):
        my_list = [1, 2, 3, 4, 5]  # Putting all the possible selection in a list
        choice = random.choice(my_list)  # Calling the random library to make a random selection
        self.c_choice = choice  # Assigning the selection to self

    # Function to convert players chosen string to integer
    def ch_to_num(self):
        final = {"rock": 1, "paper": 2, "scissors": 3, "lizard": 4,
                 "spock": 5}  # Creating a dictionary of possible selections
        a = final[str(self.p_choice)]  # Checking the player choice value in integer
        self.ch_num = a  # Assigning the integer to self

    # Function for converting computer chosen number to string
    def num_to_ch(self):
        final = {1: "rock", 2: "paper", 3: "scissors", 4: "lizard",
                 5: "spock"}  # Creating a dictionary of possible selections
        a = final[int(self.c_choice)]  # Checking computer chosen integer value in string
        self.num_ch = str(a)  # Assigning the string to self

    # Function to ask player to make a selection and play
    def first_loop(self):
        # setting Tkinter widget's to display radio buttons for player to make selection and display score's
        frame1 = tk.Frame(root, bg='black')
        label = tk.Label(frame1, text="Welcome " + str(self.p_name), font=('Courier', 40), fg='#ededed', bg='#262626')
        label1 = tk.Label(frame1, text="Tournament " + str(self.game_num), font=('Courier', 27), fg='#ededed',
                          bg='#262626')
        label2 = tk.Label(frame1, text="Choose your weapon here", font=('Courier', 19), fg='#ededed', bg='#262626')
        label3 = tk.Label(frame1, text=str(self.p_name) + "'s Score: " + str(self.player), font=('Courier', 22),
                          fg='#ededed', bg='#262626')
        label4 = tk.Label(frame1, text="Computer's Score: " + str(self.comp), font=('Courier', 20), fg='#ededed',
                          bg='#262626')
        label5 = tk.Label(frame1, text="Draw: " + str(self.draw), font=('Courier', 22), fg='#ededed', bg='#262626')
        label6 = tk.Label(frame1, bg='#303030')
        label7 = tk.Label(frame1, bg='#303030')
        label8 = tk.Label(frame1, bg='#303030')
        label9 = tk.Label(frame1, bg='#303030')
        button = tk.Button(frame1, text="PLAY", highlightbackground='#3cf03c', bg='#3cf03c', font=('Courier', 27))

        # *** EXTRA FEATURE to display error if nothing is selected *** #
        c = str(var.get())  # Getting the value of the radiobutton
        if c != "n":  # If the value is not "n" which is a invisible default radio button
            button["command"] = lambda: SpecialComputerGame.score_page(
                self)  # Make the command of the button be the funtion to load score page
        else:
            button["command"] = lambda: SpecialComputerGame.show_error()  # Else show error window

        # Positioning and displaying the widget's
        frame1.place(relx=0, rely=0, relwidth=1, relheight=1)
        label.place(relx=0.1, rely=0.05, relwidth=0.7, relheight=0.1)
        label1.place(relx=0.35, rely=0.18, relwidth=0.25, relheight=0.05)
        label2.place(relx=0.05, rely=0.3, relwidth=0.45, relheight=0.05)
        label3.place(relx=0.58, rely=0.35, relwidth=0.4, relheight=0.05)
        label4.place(relx=0.58, rely=0.45, relwidth=0.4, relheight=0.05)
        label5.place(relx=0.58, rely=0.55, relwidth=0.4, relheight=0.05)
        label6.place(relx=0.53, rely=0.28, relwidth=0.03, relheight=0.6)
        label7.place(relx=0.05, rely=0.37, relwidth=0.48, relheight=0.01)
        label8.place(relx=0.53, rely=0.32, relwidth=0.48, relheight=0.01)
        label9.place(relx=0.53, rely=0.62, relwidth=0.48, relheight=0.01)
        button.place(relx=0.7, rely=0.9, relwidth=0.3, relheight=0.1)

        # Setting, displaying and positioning the radio button widget's
        r0 = tk.Radiobutton(root, text="Nothing", variable=var, value="n", fg='#ededed', bg='#262626',
                            font=('Courier', 20), command=lambda: SpecialComputerGame.select(self))
        r0.place(relx=0.1, rely=0.4, relwidth=0.0, relheight=0.0)

        r1 = tk.Radiobutton(root, text="Rock", variable=var, value="rock", fg='#ededed', bg='#262626',
                            font=('Courier', 20), command=lambda: SpecialComputerGame.select(self))
        r1.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.08)

        r2 = tk.Radiobutton(root, text="Paper", variable=var, value="paper", fg='#ededed', bg='#262626',
                            font=('Courier', 20), command=lambda: SpecialComputerGame.select(self))
        r2.place(relx=0.1, rely=0.5, relwidth=0.3, relheight=0.08)

        r3 = tk.Radiobutton(root, text="Scissors", variable=var, value="scissors", fg='#ededed', bg='#262626',
                            font=('Courier', 20), command=lambda: SpecialComputerGame.select(self))
        r3.place(relx=0.1, rely=0.6, relwidth=0.3, relheight=0.08)

        r4 = tk.Radiobutton(root, text="Lizard", variable=var, fg='#ededed', bg='#262626', value="lizard",
                            command=lambda: SpecialComputerGame.select(self), font=('Courier', 20))
        r4.place(relx=0.1, rely=0.7, relwidth=0.3, relheight=0.08)

        r5 = tk.Radiobutton(root, text="Spock", variable=var, fg='#ededed', bg='#262626', value="spock",
                            command=lambda: SpecialComputerGame.select(self), font=('Courier', 20))
        r5.place(relx=0.1, rely=0.8, relwidth=0.3, relheight=0.08)

        root.mainloop()

    # *** EXTRA FEATURE that lets a player to choose to remember last selection and Function that runs when a radio button is selected
    def select(self):
        # Setting the checkbutton for player to choose weather to remember last selection or not
        check_1 = tk.Checkbutton(root, text="Remember my selection", variable=var_check, onvalue=1, offvalue=0,
                                 height=5, width=20, fg='#ededed', bg='#262626')
        a = var.get()  # Assigning the value of the check button to a
        # Displaying the value of the radio button selected
        label3 = tk.Label(root, text="You selected " + str(a), font=('Courier', 18), fg='#ededed', bg='#262626')

        button = tk.Button(root, text="PLAY", highlightbackground='#3cf03c', bg='#3cf03c', font=('Courier', 27),
                           command=lambda: SpecialComputerGame.score_page(self))
        # Positioning and displaying the tkinter widget's
        label3.place(relx=0.58, rely=0.7, relwidth=0.4, relheight=0.06)
        button.place(relx=0.7, rely=0.9, relwidth=0.3, relheight=0.1)
        check_1.place(relx=0.1, rely=0.9, relwidth=0.275, relheight=0.03)

    # Function to display error window using tkinter messagebox
    @staticmethod
    def show_error():
        messagebox.showerror("error", "You didn't make any selection!!!")
        root.mainloop()

    # Function to show round result
    def score_page(self):
        p_c = var.get()  # Getting players Choice from radio button
        SpecialComputerGame.comp_choice(self)  # Getting computer's choice
        self.p_choice = p_c  # Storing players choice in self
        SpecialComputerGame.result(self)  # Comparing the player and computer's choice to get winner
        SpecialComputerGame.num_to_ch(self)  # Calling function to convert computer choice to string
        winner = self.b  # Assigning the value of self.b which would either player, computer or draw to variable winner
        g = winner[0]  # Assigning the first later of the string to variable g
        # Comparing the variable g to know the winner so the score can be increased by 1
        if g == "p":
            self.player += 1

        elif g == "D":
            self.draw += 1
        else:
            self.comp += 1
        # Creating the tkinter widget's to display the result's page per round
        frame = tk.Frame(root, bg='black')
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        label = tk.Label(frame, text="Tournament " + str(self.game_num) + " Result ", font=('Courier', 30), fg='#ededed',
                         bg='#262626')
        label1 = tk.Label(frame, text=str(self.p_name) + " Chose: " + self.p_choice, font=('Courier', 20), fg='#ededed',
                          bg='#262626')
        label2 = tk.Label(frame, text="Computer Chose: " + self.num_ch, font=('Courier', 20), fg='#ededed',
                          bg='#262626')
        label3 = tk.Label(frame, text=self.a, font=('Courier', 20), fg='#ededed', bg='#262626')
        label4 = tk.Label(frame, text=str(self.p_name) + "'s score: " + str(self.player), font=('Courier', 20),
                          fg='#ededed',
                          bg='#262626')
        label5 = tk.Label(frame, text="Computer Score: " + str(self.comp), font=('Courier', 20), fg='#ededed',
                          bg='#262626')
        label6 = tk.Label(frame, text="Draw: " + str(self.draw), font=('Courier', 20), fg='#ededed', bg='#262626')
        button = tk.Button(frame, text="NEXT TOURNAMENT", highlightbackground='#3cf03c', bg='#3cf03c', fg="black",
                           font=('Courier', 27), command=lambda: SpecialComputerGame.r_loop(self, self.p_name))
        button1 = tk.Button(frame, text="Quit", font=('Courier', 27), highlightbackground='#f23030', bg='#f23030',
                            fg="black", command=lambda: exit())

        # Changing the text displayed by the button on the fifth round of play
        if self.game_num == 5:
            button["text"] = "FINAL RESULT"

        # Positioning and displaying the tkinter widget's
        label.place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.065)
        label1.place(relx=0.25, rely=0.15, relwidth=0.5, relheight=0.06)
        label2.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.06)
        label3.place(relx=0.05, rely=0.4, relwidth=0.9, relheight=0.09)
        label4.place(relx=0.25, rely=0.6, relwidth=0.5, relheight=0.06)
        label5.place(relx=0.25, rely=0.7, relwidth=0.5, relheight=0.06)
        label6.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.06)
        button.place(relx=0.65, rely=0.9, relwidth=0.35, relheight=0.1)
        button1.place(relx=0, rely=0.9, relwidth=0.3, relheight=0.1)
        root.mainloop()

    # Function comparing the computer choice and the player choice to determine who won and what result to display
    def result(self):
        # Assigning the self to the variables
        p_choice1 = str(self.p_choice)
        SpecialComputerGame.ch_to_num(self)
        p_choice = self.ch_num  # Converting player choice to int to compare with the computer's choice which is an int
        c_choice = self.c_choice
        name = str(self.p_name)

        if p_choice == c_choice:
            # Assigning self.a as the string to be displayed in the score page
            # Assigning self.b as the winner string to add 1 to the score
            self.a = "Draw Because computer and " + name + " both chose " + p_choice1
            self.b = "Draw"

        elif p_choice == 1 and c_choice == 2:
            self.a = "computer wins because paper covers rock"
            self.b = "computer"
        elif p_choice == 1 and c_choice == 3:
            self.a = name + " wins because rock crushes scissors"
            self.b = "player"
        elif p_choice == 1 and c_choice == 4:
            self.a = name + " wins because rock crushes lizard"
            self.b = "player"
        elif p_choice == 1 and c_choice == 5:
            self.a = "computer wins because spock vaporizes rock"
            self.b = "computer"
        elif p_choice == 2 and c_choice == 1:
            self.a = name + " wins because paper covers rock"
            self.b = "player"
        elif p_choice == 2 and c_choice == 3:
            self.a = "computer wins because scissors cuts paper"
            self.b = "computer"
        elif p_choice == 2 and c_choice == 4:
            self.a = "computer wins because lizard eats paper"
            self.b = "computer"
        elif p_choice == 2 and c_choice == 5:
            self.a = name + " wins because paper disproves spock"
            self.b = "player"
        elif p_choice == 3 and c_choice == 1:
            self.a = "computer wins because rock crushess scissors"
            self.b = "computer"
        elif p_choice == 3 and c_choice == 2:
            self.a = name + " wins because scissors cuts paper"
            self.b = "player"
        elif p_choice == 3 and c_choice == 4:
            self.a = name + " wins because scissors decapitates lizard"
            self.b = "player"
        elif p_choice == 3 and c_choice == 5:
            self.a = "computer wins because spock smashes scissors"
            self.b = "computer"
        elif p_choice == 4 and c_choice == 1:
            self.a = "computer wins because rock crushes lizard"
            self.b = "computer"
        elif p_choice == 4 and c_choice == 2:
            self.a = name + " wins because lizard eats paper"
            self.b = "player"
        elif p_choice == 4 and c_choice == 3:
            self.a = "computer wins because scissors decapitates lizard"
            self.b = "computer"
        elif p_choice == 4 and c_choice == 5:
            self.a = name + " wins because lizard poisons spock"
            self.b = "player"
        elif p_choice == 5 and c_choice == 1:
            self.a = name + " wins because spock vaporizes rock"
            self.b = "player"
        elif p_choice == 5 and c_choice == 2:
            self.a = "computer wins because paper disproves spock"
            self.b = "computer"
        elif p_choice == 5 and c_choice == 3:
            self.a = name + " wins because spock smashes scissors"
            self.b = "player"
        elif p_choice == 5 and c_choice == 4:
            self.a = "computer wins because lizard poisons spock"
            self.b = "computer"

    # Function to display final score page
    def final_score(self):
        # Comparing player and computer scores to know who wn the tournament
        if self.player == self.comp:
            a = "*** Draw ***"
        elif self.player > self.comp:
            a = "*** " + str(self.p_name) + " Won ***"
        else:
            a = "*** Computer Won ***"
        # Assigning variable to tkinter widget Check top for more explanation
        frame = tk.Frame(root, bg='black')
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        label = tk.Label(frame, text="Final Score", font=('Courier', 40), fg='#ededed', bg='#262626')
        label1 = tk.Label(frame, text=str(self.p_name) + "'s score: " + str(self.player), font=('Courier', 22),
                          fg='#ededed', bg='#262626')
        label2 = tk.Label(frame, text="Computer score: " + str(self.comp), font=('Courier', 22), fg='#ededed',
                          bg='#262626')
        label3 = tk.Label(frame, text="Draw : " + str(self.draw), font=('Courier', 22), fg='#ededed', bg='#262626')
        label4 = tk.Label(frame, text=a, font=('Courier', 40), fg='#ededed', bg='#262626')
        button = tk.Button(frame, text="Play again", font=('Courier', 22), highlightbackground='#3cf03c',
                           fg="black",
                           bg='#3cf03c', command=lambda: SpecialComputerGame.final_page(self))
        button1 = tk.Button(frame, text="Quit", font=('Courier', 22), highlightbackground='#f23030', bg='#f23030',
                            fg="black", command=lambda: exit())
        # Positioning and displaying the tkinter widgets
        label.place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.1)
        label1.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.06)
        label2.place(relx=0.25, rely=0.3, relwidth=0.5, relheight=0.06)
        label3.place(relx=0.25, rely=0.4, relwidth=0.5, relheight=0.06)
        label4.place(relx=0.15, rely=0.5, relwidth=0.7, relheight=0.1)
        button.place(relx=0.7, rely=0.9, relwidth=0.3, relheight=0.1)
        button1.place(relx=0, rely=0.9, relwidth=0.3, relheight=0.1)
        root.mainloop()

    # *** ONE OF THE EXTRA feature's added: askes if you'd want to play as new player or to continue as old player ***
    def final_page(self):
        # Assigning variable to tkinter widget to ask if you want to continue playing as old player or new player
        frame = tk.Frame(root, bg='black')
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        button = tk.Button(frame, text="Continue playing as " + str(self.p_name), font=('Courier', 18),
                           highlightbackground='#3cf03c', bg='#3cf03c', fg="black",
                           command=lambda: SpecialComputerGame.replay_old(self))
        button1 = tk.Button(frame, text="Start as New Player", font=('Modern', 20),
                            highlightbackground='#4192f0', bg='#4192f0',
                            fg="black", command=lambda: SpecialComputerGame.replay_new(self))
        # placing and displaying
        button.place(relx=0, rely=0.4, relwidth=0.45, relheight=0.1)
        button1.place(relx=0.55, rely=0.4, relwidth=0.5, relheight=0.1)
        root.mainloop()


# Running the app cause __name__ == "__main__"
if __name__ == "__main__":
    HEIGHT = 500  # Setting the height of the window
    WIDTH = 650  # Setting the width of the window
    root = tk.Tk()
    root.title("SpecialComputerGame")  # Setting the name of the window
    var = tk.StringVar()  # setting the variable for the radio button and the value is a string
    var_check = tk.IntVar()  # setting the variable for the check button and the value is a integer
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)  # setting the application main window
    canvas.pack()  # Positioning and displaying the widget
    pos_x = int(root.winfo_screenwidth() / 2 - WIDTH / 2)  # ---
    pos_y = int(
        root.winfo_screenheight() / 2 - HEIGHT / 2)  # Setting and positioning the window to the center of the screen
    root.geometry("+{}+{}".format(pos_x, pos_y))  # ---
    # Running the app
    SpecialComputerGame.replay_new(SpecialComputerGame)
