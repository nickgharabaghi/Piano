# use tkinter for a gui
# uses winsound to play saved audio files containing different notes
import tkinter as tk
import winsound as ws

# note that the sound files must be sotred in the current working directory
def play_A():
    ws.PlaySound("A_note.wav", ws.SND_FILENAME|ws.SND_ASYNC)

def play_B():
    ws.PlaySound("B_note.wav", ws.SND_FILENAME|ws.SND_ASYNC)

def play_D():
    ws.PlaySound("D_note.wav", ws.SND_FILENAME|ws.SND_ASYNC)

def play_E():
    ws.PlaySound("E_note.wav", ws.SND_FILENAME|ws.SND_ASYNC)

def play_F():
    ws.PlaySound("F_note.wav", ws.SND_FILENAME|ws.SND_ASYNC)

def play_G():
    ws.PlaySound("G_note.wav", ws.SND_FILENAME|ws.SND_ASYNC)

def play_low_C():
    ws.PlaySound("Low_C_note.wav", ws.SND_FILENAME|ws.SND_ASYNC)

def play_high_C():
    ws.PlaySound("High_C_note.wav", ws.SND_FILENAME|ws.SND_ASYNC)

def piano_setup():
    root = tk.Tk()
    root.configure(background = "black")
    root.title("Piano")
    frame = tk.Frame(root)
    frame.pack()

    low_C_button = tk.Button(frame, text = "C", command = play_low_C, padx = 40, pady = 100)
    low_C_button.pack(side = tk.LEFT)
    low_C_button.configure(background = "white")

    D_button = tk.Button(frame, text = "D", command = play_D, padx = 40, pady = 100)
    D_button.pack(side = tk.LEFT)
    D_button.configure(background = "white")

    E_button = tk.Button(frame, text = "E", command = play_E, padx = 40, pady = 100)
    E_button.pack(side = tk.LEFT)
    E_button.configure(background = "white")

    F_button = tk.Button(frame, text = "F", command = play_F, padx = 40, pady = 100)
    F_button.pack(side = tk.LEFT)
    F_button.configure(background = "white")

    G_button = tk.Button(frame, text = "G", command = play_G, padx = 40, pady = 100)
    G_button.pack(side = tk.LEFT)
    G_button.configure(background = "white")

    A_button = tk.Button(frame, text = "A", command = play_A, padx = 40, pady = 100)
    A_button.pack(side = tk.LEFT)
    A_button.configure(background = "white")

    high_C_button = tk.Button(frame, text = "C", command = play_high_C, padx = 40, pady = 100)
    high_C_button.pack(side = tk.RIGHT)
    high_C_button.configure(background = "white")

    B_button = tk.Button(frame, text = "B", command = play_B, padx = 40, pady = 100)
    B_button.pack(side = tk.RIGHT)
    B_button.configure(background = "white")

    root.mainloop()


piano_setup()