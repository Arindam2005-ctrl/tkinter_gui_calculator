from tkinter import *
import math
button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]
right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]
rows_len=len(button_values)
column_len=len(button_values[0])
window=Tk()
window.title("Calculator")
window.resizable(False,False)
frame=Frame(window)
label=Label(frame, text="0",bg="Black",fg="White",font=("Arial",30),anchor=E,width=column_len)
label.grid(row=0,column=0, columnspan=column_len, sticky="WE")
for row in range(rows_len):
    for column in range(column_len):
        value=button_values[row][column]
        buttons=Button(frame,text=value,font=("Arial",25),width=column_len,height=1,command=lambda value=value:my_fun(value))
        buttons.grid (row=row+1,column=column)
        if value in top_symbols:
            buttons.config(bg="orange",fg="black")
        elif value in right_symbols:
            buttons.config(bg="black",fg="white")      
        else:
            buttons.config(bg="grey",fg="black")
frame.pack()
A=0
operator=None
B= None
def clear_all():
    global A,B,operator
    A=0
    operator=None
    B=0
def remove_points(num):
    if num % 1==0:
        num=int(num)
    return str(num)
def my_fun(value):
    global A, B, operator, label, right_symbols, top_symbols
    if value in top_symbols:
        if value=="AC":
            label["text"]="0"
            clear_all()
        elif value=="+/-":
            result=float(label["text"])*(-1)
            label["text"]=remove_points(result)
        else:
            result=float(label["text"])/100
            label["text"]=remove_points(result)
    elif value in right_symbols:
        if value== "=":
            if A is not None and operator is not None:
                B= label["text"]
                numA=float(A)
                numB=float(B)
                if operator =="+":
                    label["text"]= remove_points(numA+numB)
                elif operator =="-":
                    label["text"]=remove_points(numA-numB)
                elif operator=="×":
                    label["text"]=remove_points(numA*numB)
                elif operator=="÷":
                    label["text"]= remove_points(numA/numB)
                clear_all()
        elif value in ["÷", "×", "-", "+"]:
            if operator is None:
                A=label["text"]
                label["text"]="0"
                B="0"
            operator=value
    elif value=="√":
        numA=float(label["text"])
        result=math.sqrt(numA)
        label["text"]=remove_points(result)
    else:
        if value==".":
            if value not in label["text"]:
                label["text"]+=value
        else:
            if label["text"]== "0":
                label["text"]= value
            else:
                label["text"]+=value

window.update()
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
window_x=int((screen_width/2)-(window_width/2))
window_y=int((screen_height/2)-(window_height/2))
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
window.mainloop()


