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
        self.current_round = 1
        self.round_instances = {}

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

    def start_match(self):
        self.fighter1 = self.entry_fighter1.get()
        self.fighter2 = self.entry_fighter2.get()

        self.round_instances[1] = Round(self.master, self.fighter1, self.fighter2, self.SCard1, self.SCard2, self.next_round)
        self.round_instances[1].start_round()

    def next_round(self):
        self.current_round += 1
        if self.current_round <= 15:
            if self.current_round == 15:
                self.round_instances[self.current_round] = Round(self.master, self.fighter1, self.fighter2, self.SCard1, self.SCard2, self.display_results)
                self.round_instances[self.current_round].start_round()
            else:
                self.round_instances[self.current_round] = Round(self.master, self.fighter1, self.fighter2, self.SCard1, self.SCard2, self.next_round)
                self.round_instances[self.current_round].start_round()
        else:
            messagebox.showinfo("End of Rounds", "All rounds completed.")
            self.display_results()

    def display_results(self):
        self.results = Results(self.master, self.fighter1, self.fighter2, self.SCard1, self.SCard2)

class Round:
    def __init__(self, master, fighter1, fighter2, SCard1, SCard2, next_round_callback):
        self.master = master
        self.fighter1 = fighter1
        self.fighter2 = fighter2
        self.SCard1 = SCard1
        self.SCard2 = SCard2
        self.next_round_callback = next_round_callback
        self.round_number = None

        self.create_widgets()

    def create_widgets(self):
        self.round_number = len(self.SCard1) // 1 + 1

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

        continue_button = tk.Button(self.master, text="Continue", command=self.submit_scores)
        continue_button.grid(row=7, column=1)

    def submit_scores(self):
        round_score1 = int(self.entry_fighter1.get())
        round_score2 = int(self.entry_fighter2.get())

        self.SCard1.append(round_score1)
        self.SCard2.append(round_score2)

        overall1 = sum(self.SCard1)
        overall2 = sum(self.SCard2)

        print(f"{self.fighter1}: {self.SCard1} - Total: {overall1}")
        print(f"{self.fighter2}: {self.SCard2} - Total: {overall2}")

        self.next_round_callback()

    def start_round(self):
        self.round_number = len(self.SCard1) // 2 + 1

class Results:
    def __init__(self, master, fighter1, fighter2, SCard1, SCard2):
        self.master = master
        self.fighter1 = fighter1
        self.fighter2 = fighter2
        self.SCard1 = SCard1
        self.SCard2 = SCard2

        self.show_results()

    def show_results(self):
        tk.Label(self.master, text="Results").grid(row=8, columnspan=2)
        
        overall1 = sum(self.SCard1)
        overall2 = sum(self.SCard2)

        if overall1 > overall2:
            winner = self.fighter1
        elif overall2 > overall1:
            winner = self.fighter2
        else:
            winner = "Draw"

        result_label = tk.Label(self.master, text=f"Winner: {winner}")
        result_label.grid(row=9, columnspan=2)

        tk.Label(self.master, text=f"{self.fighter1}: {self.SCard1} - Total: {overall1}").grid(row=10, columnspan=2)
        tk.Label(self.master, text=f"{self.fighter2}: {self.SCard2} - Total: {overall2}").grid(row=11, columnspan=2)

        finish_button = tk.Button(self.master, text="Finish", command=self.master.quit)
        finish_button.grid(row=12, columnspan=2)

def main():
    root = tk.Tk()
    app = BoxingMatchApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
