import random
import tkinter as tk

def kop_of_munt():
    venster = tk.Tk()
    venster.title("heads or tails cheater")

    vraag = tk.Label(venster, text="enter a number from one 1 to 100 to set the chance of heads")
    vraag.pack()

    invoer = tk.Entry(venster)
    invoer.pack()

    uitkomst = tk.Label(venster)
    uitkomst.pack()


    def verstuur():
        kans_kop = int(invoer.get())
        keuze = random.choices(
            ["heads", "tails"], weights=[kans_kop, 100 - kans_kop]
        )
        uitkomst.config(text=f"result: {keuze}.")


    knop = tk.Button(venster, text="Verstuur", command=verstuur)
    knop.pack()

    venster.mainloop()
