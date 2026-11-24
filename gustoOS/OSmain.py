import pygame
import random
from ml import game
from modelgui import spamfilter
from kopmunt_gui import kop_of_munt
from rekenspelgui import start_spel
import tkinter as tk
import csv
import re
venster = tk.Tk()
venster.geometry("400x400")
venster.title("gusto OS")
venster.button = tk.Button(venster, text="painter game", command=lambda: game())
venster.button.pack()
venster.button2 = tk.Button(venster, text="spamfilter", command=lambda: spamfilter())
venster.button2.pack()
venster.button3 = tk.Button(venster, text="heads or tails cheater", command=lambda: kop_of_munt())
venster.button3.pack()
venster.button4 = tk.Button(venster, text="calculator game gusto", command=lambda: start_spel())
venster.button4.pack()
venster.mainloop()


