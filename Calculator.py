from tkinter import *

win = Tk()  # Create a window
win.title("Meghna's Calculator")  
win.geometry("300x334")  # Size of Window
win.resizable(0, 0)  # This prevents the window from resizing itself



def click_button(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def clear_button():
    global expression
    expression = ""
    input_text.set("")

def equal_button():
    global expression
    result = str(eval(expression)) 
    input_text.set(result)
    expression = ""

expression = ""

input_text = StringVar()

# Create a frame for input
input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=TOP)

# input field inside the 'Frame'
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)  

frame_btn = Frame(win, width=312, height=272.5, bg="pink")
frame_btn.pack()

# 1st row of buttons
clear = Button(frame_btn, text="C", fg="green", width=32, height=3, bd=0, bg="yellow", command=lambda: clear_button()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide = Button(frame_btn, text="/", fg="green", width=10, height=3, bd=0, bg="yellow",  command=lambda: click_button("/")).grid(row=0, column=3, padx=1, pady=1)

# 2nd row of buttons
seven = Button(frame_btn, text="7", fg="green", width=10, height=3, bd=0, bg="black", command=lambda: click_button(7)).grid(row=1, column=0, padx=1, pady=1)
eight = Button(frame_btn, text="8", fg="green", width=10, height=3, bd=0, bg="black",  command=lambda: click_button(8)).grid(row=1, column=1, padx=1, pady=1)
nine = Button(frame_btn, text="9", fg="green", width=10, height=3, bd=0, bg="black",  command=lambda: click_button(9)).grid(row=1, column=2, padx=1, pady=1)
multiply = Button(frame_btn, text="*", fg="green", width=10, height=3, bd=0, bg="yellow",  command=lambda: click_button("*")).grid(row=1, column=3, padx=1, pady=1)

# 3rd row of buttons
four = Button(frame_btn, text="4", fg="white", width=10, height=3, bd=0, bg="black",  command=lambda: click_button(4)).grid(row=2, column=0, padx=1, pady=1)
five = Button(frame_btn, text="5", fg="white", width=10, height=3, bd=0, bg="black", command=lambda: click_button(5)).grid(row=2, column=1, padx=1, pady=1)
six = Button(frame_btn, text="6", fg="white", width=10, height=3, bd=0, bg="black",  command=lambda: click_button(6)).grid(row=2, column=2, padx=1, pady=1)
minus = Button(frame_btn, text="-", fg="white", width=10, height=3, bd=0, bg="yellow",  command=lambda: click_button("-")).grid(row=2, column=3, padx=1, pady=1)

# 4th row of buttons
one = Button(frame_btn, text="1", fg="white", width=10, height=3, bd=0, bg="black", command=lambda: click_button(1)).grid(row=3, column=0, padx=1, pady=1)
two = Button(frame_btn, text="2", fg="white", width=10, height=3, bd=0, bg="black",  command=lambda: click_button(2)).grid(row=3, column=1, padx=1, pady=1)
three = Button(frame_btn, text="3", fg="white", width=10, height=3, bd=0, bg="black",  command=lambda: click_button(3)).grid(row=3, column=2, padx=1, pady=1)
plus = Button(frame_btn, text="+", fg="white", width=10, height=3, bd=0, bg="yellow", command=lambda: click_button("+")).grid(row=3, column=3, padx=1, pady=1)

# 5th row of buttons
zero = Button(frame_btn, text="0", fg="white", width=21, height=3, bd=0, bg="black",  command=lambda: click_button(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
point = Button(frame_btn, text=".", fg="white", width=10, height=3, bd=0, bg="yellow",  command=lambda: click_button(".")).grid(row=4, column=2, padx=1, pady=1)
equals = Button(frame_btn, text="=", fg="white", width=10, height=3, bd=0, bg="yellow",  command=lambda: equal_button()).grid(row=4, column=3, padx=1, pady=1)
win.mainloop()

