import time  
import tkinter as tk  
  
class PomodoroClock:  
    def __init__(self, master):  
        self.master = master  
        master.title("Pomodoro Clock")  
  
        self.remaining_time = 25 * 60  # 25 minutes in seconds  
        self.break_time = 5 * 60  # 5 minutes in seconds  
        self.is_working = True  
  
        self.time_label = tk.Label(master, text="25:00", font=("Helvetica", 50))  
        self.time_label.pack()  
  
        self.start_button = tk.Button(master, text="Start", command=self.start_timer)  
        self.start_button.pack()  
  
        self.reset_button = tk.Button(master, text="Reset", command=self.reset_timer)  
        self.reset_button.pack()  
  
    def start_timer(self):  
        if self.is_working:  
            self.countdown(self.remaining_time)  
        else:  
            self.countdown(self.break_time)  
  
    def countdown(self, seconds):  
        while seconds > 0:  
            minutes, seconds = divmod(seconds, 60)  
            self.time_label.config(text=f"{int(minutes)}:{int(seconds)}")  
            self.master.update()  
            time.sleep(1)  
            seconds -= 1  
        if self.is_working:  
            self.is_working = False  
            self.time_label.config(text="Break Time!")  
        else:  
            self.is_working = True  
            self.time_label.config(text="Work Time!")  
  
    def reset_timer(self):  
        self.is_working = True  
        self.remaining_time = 25 * 60  # Reset work time to 25 minutes  
        self.break_time = 5 * 60  # Reset break time to 5 minutes  
        self.time_label.config(text="25:00")  
  
root = tk.Tk()  
clock = PomodoroClock(root)  
root.mainloop()
