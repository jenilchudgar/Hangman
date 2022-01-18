from tkinter import *
from tkinter import messagebox
import requests

root = Tk()
root.title("Hang Man")
root.geometry("1300x650")

global RANDOM_WORD
global STAGE
RANDOM_WORD = ""
STAGE = 1

# Letter Click Function
def letter_click(b:Button):
    global RANDOM_WORD
    letter = str(b["text"]).lower()
    list_word = list(RANDOM_WORD)
    
    if letter in list_word:
        index = list_word.index(letter)
        blank_list[index].config(text=letter)
        list_word.remove(letter)
    else:
        try:
            global STAGE
            STAGE += 1
            hang_man_img.config(image=images[STAGE-1])
        except Exception:
            a = ""
            for e in blank_list:
                a += e["text"]
            if a == RANDOM_WORD:
                messagebox.showinfo("Hangman","You won the Game!")
            messagebox.showerror("Hangman","Game Over!")

def random_word():
    global RANDOM_WORD
    r = requests.get("https://random-word-api.herokuapp.com/word?number=1&swear=0")
    data = r.json()[0]
    RANDOM_WORD = data

# Creating Header
Label(root,text="Hang Man",font=("Pacifico",20)).pack()

# Defining All Hangman Images
images = []

images.append(PhotoImage(file="Hangman Images/h1.png"))
images.append(PhotoImage(file="Hangman Images/h2.png"))
images.append(PhotoImage(file="Hangman Images/h3.png"))
images.append(PhotoImage(file="Hangman Images/h4.png"))
images.append(PhotoImage(file="Hangman Images/h5.png"))
images.append(PhotoImage(file="Hangman Images/h6.png"))
images.append(PhotoImage(file="Hangman Images/h7.png"))

# Hang Man Image to Be Displayed
hang_man_img = Label(root,image=images[0])
hang_man_img.pack()

# Blanks List Frame
blank_list_frame = Label(root)
blank_list_frame.pack()

# Blanks List
blank_list = []
random_word()

# Create Blank Spaces
for i in range(len(RANDOM_WORD)):
    blank_list.append(Label(blank_list_frame,text="__",font=("Calibri",25)))
    blank_list[i].grid(row=0,column=i)

# Alphabets Frame
alphabets_btn_frame = LabelFrame(root,text="Alphabets")
alphabets_btn_frame.pack()

# Alphabets Buttons
alphabets_btns = []
alphabets_images = []

for i in range(0,13):
    alphabets_images.append(PhotoImage(file=f"Letter Images//{chr(i+65)}.png"))
    alphabets_btns.append(Button(alphabets_btn_frame,image=alphabets_images[i],text=f"{chr(i+65)}"))

    alphabets_btns[i].grid(row=0,column=i,padx=5)

for i in range(13,26):
    alphabets_images.append(PhotoImage(file=f"Letter Images//{chr(i+65)}.png"))
    alphabets_btns.append(Button(alphabets_btn_frame,image=alphabets_images[i],text=f"{chr(i+65)}"))

    alphabets_btns[i].grid(row=1,column=i-13,padx=5)

alphabets_btns[0].config(command = lambda: letter_click(alphabets_btns[0]))
alphabets_btns[1].config(command = lambda: letter_click(alphabets_btns[1]))
alphabets_btns[2].config(command = lambda: letter_click(alphabets_btns[2]))
alphabets_btns[3].config(command = lambda: letter_click(alphabets_btns[3]))
alphabets_btns[4].config(command = lambda: letter_click(alphabets_btns[4]))
alphabets_btns[5].config(command = lambda: letter_click(alphabets_btns[5]))
alphabets_btns[6].config(command = lambda: letter_click(alphabets_btns[6]))
alphabets_btns[7].config(command = lambda: letter_click(alphabets_btns[7]))
alphabets_btns[8].config(command = lambda: letter_click(alphabets_btns[8]))
alphabets_btns[9].config(command = lambda: letter_click(alphabets_btns[9]))
alphabets_btns[10].config(command = lambda: letter_click(alphabets_btns[10]))
alphabets_btns[11].config(command = lambda: letter_click(alphabets_btns[11]))
alphabets_btns[12].config(command = lambda: letter_click(alphabets_btns[12]))
alphabets_btns[13].config(command = lambda: letter_click(alphabets_btns[13]))
alphabets_btns[14].config(command = lambda: letter_click(alphabets_btns[14]))
alphabets_btns[15].config(command = lambda: letter_click(alphabets_btns[15]))
alphabets_btns[16].config(command = lambda: letter_click(alphabets_btns[16]))
alphabets_btns[17].config(command = lambda: letter_click(alphabets_btns[17]))
alphabets_btns[18].config(command = lambda: letter_click(alphabets_btns[18]))
alphabets_btns[19].config(command = lambda: letter_click(alphabets_btns[19]))
alphabets_btns[20].config(command = lambda: letter_click(alphabets_btns[20]))
alphabets_btns[21].config(command = lambda: letter_click(alphabets_btns[21]))
alphabets_btns[22].config(command = lambda: letter_click(alphabets_btns[22]))
alphabets_btns[23].config(command = lambda: letter_click(alphabets_btns[23]))
alphabets_btns[24].config(command = lambda: letter_click(alphabets_btns[24]))
alphabets_btns[25].config(command = lambda: letter_click(alphabets_btns[25]))

root.mainloop()