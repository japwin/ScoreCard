import tkinter as tk
from tkinter import messagebox

class BoxingMatchApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Boxing Match Scoring")
        
        self.fighter1 = ""
        self.fighter2 = ""
        self.SCard1 = []
        self.SCard2 = []
        self.winner = ""
        self.current_round = 1
        self.round_instance = None

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Enter Fighter 1 Name:").grid(row=0, column=0)
        self.entry_fighter1 = tk.Entry(self.master)
        self.entry_fighter1.grid(row=0, column=1)

        tk.Label(self.master, text="Enter Fighter 2 Name:").grid(row=1, column=0)
        self.entry_fighter2 = tk.Entry(self.master)
        self.entry_fighter2.grid(row=1, column=1)

        begin_button = tk.Button(self.master, text="Begin", command=self.start_match)
        begin_button.grid(row=2, columnspan=2)
        self.master.bind('<Return>', lambda event: self.start_match())  # Bind Enter key

    def start_match(self):
        self.fighter1 = self.entry_fighter1.get()
        self.fighter2 = self.entry_fighter2.get()

        self.round_instance = Round(self.master, self.fighter1, self.fighter2, self.SCard1, self.SCard2, self.current_round, self.next_round, self.set_winner)
        self.round_instance.start_round()

    def next_round(self):
        self.current_round += 1
        if self.current_round <= 15:
            self.round_instance.clear_widgets()
            self.round_instance = Round(self.master, self.fighter1, self.fighter2, self.SCard1, self.SCard2, self.current_round, self.next_round, self.set_winner)
            self.round_instance.start_round()
        else:
            self.display_results()

    def set_winner(self, winner):
        self.winner = winner
        self.display_results()

    def display_results(self):
        self.round_instance.clear_widgets()
        self.results = Results(self.master, self.fighter1, self.fighter2, self.SCard1, self.SCard2, self.winner)

class Round:
    def __init__(self, master, fighter1, fighter2, SCard1, SCard2, round_number, next_round_callback, set_winner_callback):
        self.master = master
        self.fighter1 = fighter1
        self.fighter2 = fighter2
        self.SCard1 = SCard1
        self.SCard2 = SCard2
        self.round_number = round_number
        self.next_round_callback = next_round_callback
        self.set_winner_callback = set_winner_callback

    def create_widgets(self):
        tk.Label(self.master, text=f"Round {self.round_number}").grid(row=3, columnspan=2)
        tk.Label(self.master, text=f"{self.fighter1} vs {self.fighter2}").grid(row=4, columnspan=2)

        tk.Label(self.master, text=self.fighter1).grid(row=5, column=0)
        self.entry_fighter1 = tk.Entry(self.master)
        self.entry_fighter1.grid(row=5, column=1)

        tk.Label(self.master, text=self.fighter2).grid(row=6, column=0)
        self.entry_fighter2 = tk.Entry(self.master)
        self.entry_fighter2.grid(row=6, column=1)

        quit_button = tk.Button(self.master, text="Quit", command=self.master.quit)
        quit_button.grid(row=7, column=0)
        self.master.bind('<Return>', lambda event: self.master.quit())  # Bind Enter key to Quit

        continue_button = tk.Button(self.master, text="Continue", command=self.submit_scores)
        continue_button.grid(row=7, column=1)
        self.master.bind('<Return>', lambda event: self.submit_scores())  # Bind Enter key to Continue

        ko_button = tk.Button(self.master, text="KO", command=self.ko)
        ko_button.grid(row=8, column=0)
        self.master.bind('<Return>', lambda event: self.ko())  # Bind Enter key to KO

        no_contest_button = tk.Button(self.master, text="No Contest", command=self.no_contest)
        no_contest_button.grid(row=8, column=1)
        self.master.bind('<Return>', lambda event: self.no_contest())  # Bind Enter key to No Contest

        points_button = tk.Button(self.master, text="Points", command=self.submit_scores)
        points_button.grid(row=8, column=2)
        self.master.bind('<Return>', lambda event: self.submit_scores())  # Bind Enter key to Points

    def submit_scores(self):
        round_score1 = self.entry_fighter1.get()
        round_score2 = self.entry_fighter2.get()

        if round_score1.isdigit() and round_score2.isdigit():
            round_score1 = int(round_score1)
            round_score2 = int(round_score2)
            self.SCard1.append(round_score1)
            self.SCard2.append(round_score2)
        else:
            messagebox.showerror("Invalid Input", "Scores must be integers")
            return

        self.next_round_callback()

    def ko(self):
        self.ko_popup = tk.Toplevel(self.master)
        self.ko_popup.title("KO Winner")

        tk.Label(self.ko_popup, text="Who won by KO?").pack()

        self.ko_winner_choice = tk.StringVar(self.ko_popup)
        self.ko_winner_choice.set(self.fighter1)  # Default choice

        ko_winner_menu = tk.OptionMenu(self.ko_popup, self.ko_winner_choice, self.fighter1, self.fighter2)
        ko_winner_menu.pack()

        ko_confirm_button = tk.Button(self.ko_popup, text="Confirm", command=self.ko_confirm)
        ko_confirm_button.pack()
        self.ko_popup.bind('<Return>', lambda event: self.ko_confirm())  # Bind Enter key to Confirm

    def ko_confirm(self):
        winner = self.ko_winner_choice.get()
        if winner == self.fighter1:
            self.SCard1.append("KO")
            self.SCard2.append("Loss")
        elif winner == self.fighter2:
            self.SCard2.append("KO")
            self.SCard1.append("Loss")

        self.ko_popup.destroy()
        self.set_winner_callback(f"{winner} by KO")

    def no_contest(self):
        self.SCard1.append("No Contest")
        self.SCard2.append("No Contest")
        self.set_winner_callback("No Contest")

    def start_round(self):
        self.create_widgets()

    def clear_widgets(self):
        for widget in self.master.winfo_children():
            widget.grid_forget()

class Results:
    def __init__(self, master, fighter1, fighter2, SCard1, SCard2, winner):
        self.master = master
        self.fighter1 = fighter1
        self.fighter2 = fighter2
        self.SCard1 = SCard1
        self.SCard2 = SCard2
        self.winner = winner

        self.show_results()

    def show_results(self):
        tk.Label(self.master, text="Results").grid(row=0, columnspan=2)
        
        overall1 = sum([score for score in self.SCard1 if isinstance(score, int)])
        overall2 = sum([score for score in self.SCard2 if isinstance(score, int)])

        if self.winner == "":
            if overall1 > overall2:
                self.winner = self.fighter1
            elif overall2 > overall1:
                self.winner = self.fighter2
            else:
                self.winner = "Draw"

        result_label = tk.Label(self.master, text=f"Winner: {self.winner}")
        result_label.grid(row=1, columnspan=2)

        tk.Label(self.master, text=f"{self.fighter1}: {self.SCard1} - Total: {overall1}").grid(row=2, columnspan=2)
        tk.Label(self.master, text=f"{self.fighter2}: {self.SCard2} - Total: {overall2}").grid(row=3, columnspan=2)

        finish_button = tk.Button(self.master, text="Finish", command=self.master.quit)
        finish_button.grid(row=4, columnspan=2)
        self.master.bind('<Return>', lambda event: self.master.quit())  # Bind Enter key to Finish

def main():
    root = tk.Tk()
    app = BoxingMatchApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
