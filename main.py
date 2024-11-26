import tkinter as tk

calculation = "0"

operators = ["*","+","-","/"]
# numbers = ["0","1","2","3","4","5","6","7","8","9"]

def add_to_calculation(symbol):
    global calculation
    if calculation.startswith("0"):
        calculation = ""
        calculation += str(symbol)
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation,"right")
    else:
        calculation += str(symbol)
        if calculation[-2] in operators and calculation[-1] == calculation[-2]:
            calculation = calculation[:-1]
        elif calculation[-2] in operators and calculation[-1] in operators:
            calculation = calculation[:-2] + str(symbol)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation,"right")






def evaluate_calculation():
    global calculation
    try:
        steps_calculation = calculation + "="
        text_steps.delete(1.0,"end")
        text_steps.insert(1.0,steps_calculation,"right")
        calculation = str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation,"right")
    except:
        clear_field()
        text_result.insert(1.0,"Error","right")

def clear_field():
    global calculation
    calculation = "0"
    text_steps.delete(1.0, "end")
    text_result.delete(1.0,"end")
    text_result.insert(1.0, calculation,"right")


def clear_one_char():
    global calculation
    calculation = calculation[:-1]
    if len(calculation) != 0:
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation,"right")
    else:
        calculation = "0"
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation,"right")



def on_enter(event):
    event.widget.config(bg="lightgray", fg="black")

def on_leave(event):
    event.widget.config(bg="SystemButtonFace", fg="black")


def on_enter_eq(event):
    event.widget.config(bg="#45b6fe", fg="white")

def on_leave_eq(event):
    event.widget.config(bg="blue", fg="white")



root = tk.Tk()
root.geometry("300x300")
root.resizable(False, False)
root.title("Calculator")
root.config(bg="white")

text_steps = tk.Text(root,height=1,width=16,font=("Arial",24))
text_steps.grid(columnspan=5)
text_steps.tag_configure("right", justify="right")


text_result = tk.Text(root,height=1,width=16,font=("Arial",24))
text_result.grid(columnspan=5)
text_result.tag_configure("right", justify="right")
text_result.insert(1.0, calculation,"right")





btn_1 = tk.Button(root,text="1",command=lambda: add_to_calculation(1),width=5,font=("Arial",14))
btn_1.grid(row=2,column=1,pady=2)
btn_1.bind("<Enter>", on_enter)
btn_1.bind("<Leave>", on_leave)
btn_2 = tk.Button(root,text="2",command=lambda: add_to_calculation(2),width=5,font=("Arial",14))
btn_2.grid(row=2,column=2)
btn_2.bind("<Enter>", on_enter)
btn_2.bind("<Leave>", on_leave)
btn_3 = tk.Button(root,text="3",command=lambda: add_to_calculation(3),width=5,font=("Arial",14))
btn_3.grid(row=2,column=3)
btn_3.bind("<Enter>", on_enter)
btn_3.bind("<Leave>", on_leave)
btn_4 = tk.Button(root,text="4",command=lambda: add_to_calculation(4),width=5,font=("Arial",14))
btn_4.grid(row=3,column=1,pady=2)
btn_4.bind("<Enter>", on_enter)
btn_4.bind("<Leave>", on_leave)
btn_5 = tk.Button(root,text="5",command=lambda: add_to_calculation(5),width=5,font=("Arial",14))
btn_5.grid(row=3,column=2)
btn_5.bind("<Enter>", on_enter)
btn_5.bind("<Leave>", on_leave)
btn_6 = tk.Button(root,text="6",command=lambda: add_to_calculation(6),width=5,font=("Arial",14))
btn_6.grid(row=3,column=3)
btn_6.bind("<Enter>", on_enter)
btn_6.bind("<Leave>", on_leave)
btn_7 = tk.Button(root,text="7",command=lambda: add_to_calculation(7),width=5,font=("Arial",14))
btn_7.grid(row=4,column=1,pady=2)
btn_7.bind("<Enter>", on_enter)
btn_7.bind("<Leave>", on_leave)
btn_8 = tk.Button(root,text="8",command=lambda: add_to_calculation(8),width=5,font=("Arial",14))
btn_8.grid(row=4,column=2)
btn_8.bind("<Enter>", on_enter)
btn_8.bind("<Leave>", on_leave)
btn_9 = tk.Button(root,text="9",command=lambda: add_to_calculation(9),width=5,font=("Arial",14))
btn_9.grid(row=4,column=3)
btn_9.bind("<Enter>", on_enter)
btn_9.bind("<Leave>", on_leave)
btn_0 = tk.Button(root,text="0",command=lambda: add_to_calculation(0),width=5,font=("Arial",14))
btn_0.grid(row=5,column=2)
btn_0.bind("<Enter>", on_enter)
btn_0.bind("<Leave>", on_leave)
btn_plus = tk.Button(root,text="+",command=lambda: add_to_calculation("+"),width=5,font=("Arial",14))
btn_plus.grid(row=2,column=4)
btn_plus.bind("<Enter>", on_enter)
btn_plus.bind("<Leave>", on_leave)
btn_minus = tk.Button(root,text="-",command=lambda: add_to_calculation("-"),width=5,font=("Arial",14))
btn_minus.grid(row=3,column=4)
btn_minus.bind("<Enter>", on_enter)
btn_minus.bind("<Leave>", on_leave)
btn_mul = tk.Button(root,text="X",command=lambda: add_to_calculation("*"),width=5,font=("Arial",14))
btn_mul.grid(row=4,column=4)
btn_mul.bind("<Enter>", on_enter)
btn_mul.bind("<Leave>", on_leave)
btn_div = tk.Button(root,text="/",command=lambda: add_to_calculation("/"),width=5,font=("Arial",14))
btn_div.grid(row=5,column=4)
btn_div.bind("<Enter>", on_enter)
btn_div.bind("<Leave>", on_leave)
btn_open = tk.Button(root,text="(",command=lambda: add_to_calculation("("),width=5,font=("Arial",14))
btn_open.grid(row=5,column=1,pady=2)
btn_open.bind("<Enter>", on_enter)
btn_open.bind("<Leave>", on_leave)
btn_close = tk.Button(root,text=")",command=lambda: add_to_calculation(")"),width=5,font=("Arial",14))
btn_close.grid(row=5,column=3)
btn_close.bind("<Enter>", on_enter)
btn_close.bind("<Leave>", on_leave)
btn_clear_one = tk.Button(root,text="<-",command=clear_one_char,width=5,font=("Arial",14))
btn_clear_one.grid(row=6,column=1,pady=2)
btn_clear_one.bind("<Enter>", on_enter)
btn_clear_one.bind("<Leave>", on_leave)
btn_clear_all = tk.Button(root,text="C",command=clear_field,width=5,font=("Arial",14))
btn_clear_all.grid(row=6,column=2)
btn_clear_all.bind("<Enter>", on_enter)
btn_clear_all.bind("<Leave>", on_leave)
btn_decimal = tk.Button(root,text=".",command=lambda: add_to_calculation("."),width=5,font=("Arial",14))
btn_decimal.grid(row=6,column=3)
btn_decimal.bind("<Enter>", on_enter)
btn_decimal.bind("<Leave>", on_leave)
btn_equals = tk.Button(root,text="=",command=evaluate_calculation,bg="blue",fg="white",width=5,font=("Arial",14))
btn_equals.grid(row=6,column=4)
btn_equals.bind("<Enter>", on_enter_eq)
btn_equals.bind("<Leave>", on_leave_eq)




root.mainloop()