
import random
import tkinter as tk


def start_spel():
    venster = tk.Tk()
    venster.geometry("400x300")
    venster.title("calculator game gusto")

    vraag = tk.Label(venster)
    vraag.pack()

    invoer = tk.Entry(venster)
    invoer.pack()

    feedback = tk.Label(venster)
    feedback.pack()

    resultaat = 0

    def nieuwe_vraag():
        nonlocal resultaat

        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        soort = random.choice(["+", "-", "*", "/"])
        
        resultaat = round(eval(str(number1) + soort + str(number2)), 1)
        vraag.config(text=f"Wat is {number1} {soort} {number2}?")
        invoer.delete(0, tk.END)
        invoer.focus_set()

    def controleer():
        try:
            
            antwoord = round(float(invoer.get()), 1)
        except ValueError:
            feedback.config(text="enter a valid number.")
            return

        if antwoord == resultaat:
            nieuwe_vraag()
            feedback.config(text=f"Correct! . Here is the next problem.")
        else:
            feedback.config(text="Incorrect! Try again.")

    
    knop = tk.Button(venster, text="Verstuur", command=controleer)
    knop.pack()

    nieuwe_vraag()
    venster.mainloop()


if __name__ == "__main__":
    start_spel()
