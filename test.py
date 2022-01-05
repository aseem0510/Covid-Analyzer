import pandas as pd
import matplotlib.pyplot as plt
import time
import random
import math
import heapq
import numpy as np
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


#########################################################################################################################################


df_tc = pd.read_excel(r"data/totconfirmed.xlsx", sheet_name=0)
df_tr = pd.read_excel(r"data/totrecovered.xlsx", sheet_name=0)
df_td = pd.read_excel(r"data/totdeath.xlsx", sheet_name=0)
df_dd = pd.read_excel(r"data/daydeath.xlsx", sheet_name=0)
df_dr = pd.read_excel(r"data/dayrecovered.xlsx", sheet_name=0)
df_dc = pd.read_excel(r"data/dayconfirmed.xlsx", sheet_name=0)

df_histo = pd.DataFrame()

df_histo['june_c'] = [sum(sum(df_dc.loc[i, '6/2/20':'6/30/20']) for i in range(187))]
df_histo['july_c'] = [sum(sum(df_dc.loc[i, '7/1/20':'7/31/20']) for i in range(187))]
df_histo['august_c'] = [sum(sum(df_dc.loc[i, '8/1/20':'8/31/20']) for i in range(187))]
df_histo['september_c'] = [sum(sum(df_dc.loc[i, '9/2/20':'9/23/20']) for i in range(187))]

df_histo['june_d'] = [sum(sum(df_dd.loc[i, '6/2/20':'6/30/20']) for i in range(187))]
df_histo['july_d'] = [sum(sum(df_dd.loc[i, '7/1/20':'7/31/20']) for i in range(187))]
df_histo['august_d'] = [sum(sum(df_dd.loc[i, '8/1/20':'8/31/20']) for i in range(187))]
df_histo['september_d'] = [sum(sum(df_dd.loc[i, '9/2/20':'9/23/20']) for i in range(187))]

df_histo['june_r'] = [sum(sum(df_dr.loc[i, '6/2/20':'6/30/20']) for i in range(187))/10000]
df_histo['july_r'] = [sum(sum(df_dr.loc[i, '7/1/20':'7/31/20']) for i in range(187))/10000]
df_histo['august_r'] = [sum(sum(df_dr.loc[i, '8/1/20':'8/31/20']) for i in range(187))/10000]
df_histo['september_r'] = [sum(sum(df_dr.loc[i, '9/2/20':'9/23/20']) for i in range(187))/10000]


##################################################################################################################################


lst = []


#################################################################################################################################


def detail(cou):

    lst_of_dataset_name = lst
    
    for i in range(187):
        if(df_dd['Country'][i] == cou):
            ind = i
            break

    if cou in lst_of_dataset_name:

        graph = Toplevel()
        graph.title(cou+"'s"+" Analysis")
        graph.geometry("800x550+250+90")
        graph.resizable(False, False)
        graph.grab_set()
        graph.iconbitmap("images/earth.ico")


        photo = PhotoImage(file="images/cases.PNG")
        bg_photo = Label(graph, image=photo)
        bg_photo.place(x=0, y=0, relwidth=1, relheight=1)


        b1 = Button(graph, text="Case Analysis", relief=RIDGE, borderwidth=4, font=("times", 14, "bold"), bg="light blue", activebackground="blue", activeforeground="white", command=lambda: confirmed(ind))
        b1.place(x=150, y=100)

        b2 = Button(graph, text="Case Analysis", relief=RIDGE, borderwidth=4, font=("times", 14, "bold"), bg="light blue", activebackground="blue", activeforeground="white", command=lambda: death(ind))
        b2.place(x=150, y=290)

        b3 = Button(graph, text="Case Analysis", relief=RIDGE, borderwidth=4, font=("times", 14, "bold"), bg="light blue", activebackground="blue", activeforeground="white", command=lambda: recovered(ind))
        b3.place(x=150, y=470)


        la1_text = df_tc.loc[ind, '9/23/20']
        la2_text = math.ceil(df_tc.loc[ind, '9/23/20']/114)
        la3_text = df_td.loc[ind, '9/23/20']
        la4_text = math.ceil(df_td.loc[ind, '9/23/20']/114)
        la5_text = df_tr.loc[ind, '9/23/20']
        la6_text = math.ceil(df_tr.loc[ind, '9/23/20']/114)


        la1 = Label(graph, text= la1_text, font=("times", 14, "bold"), bg="brown", fg="yellow")
        la1.place(x=260, y=15)

        la2 = Label(graph, text=la2_text, font=("times", 14, "bold"), bg="brown", fg="yellow")
        la2.place(x=260, y=55)

        la3 = Label(graph, text=la3_text, font=("times", 14, "bold"), bg="brown", fg="yellow")
        la3.place(x=260, y=200)

        la4 = Label(graph, text=la4_text, font=("times", 14, "bold"), bg="brown", fg="yellow")
        la4.place(x=260, y=240)

        la5 = Label(graph, text=la5_text, font=("times", 14, "bold"), bg="brown", fg="yellow")
        la5.place(x=260, y=385)

        la6 = Label(graph, text=la6_text, font=("times", 14, "bold"), bg="brown", fg="yellow")
        la6.place(x=260, y=425)


        graph.mainloop()


    else:

        show = messagebox.showinfo("Notification", "OOPS! "+cou+" details are not available in our dataset. Please try searching for another country.")



###########################################################################################################################################


def death(ind):
    
    df_dd1 = df_dd.loc[:, '6/2/20':]
    df = pd.DataFrame({'x': range(0, 114), 'y1': df_dd1.iloc[ind, :]})
    plt.plot('x', 'y1', data=df, marker='o', markerfacecolor='red', markersize=8, color='skyblue', linewidth=2)
    plt.title('Death Cases Per Day Analysis')
    plt.xlabel("Number Of Days")
    plt.ylabel("Cases At Particular Date")
    plt.show()


############################################################################################################################################


def recovered(ind):
    
    df_dr1 = df_dr.loc[:, '6/2/20':]
    df = pd.DataFrame({'x': range(0, 114), 'y1': df_dr1.iloc[ind, :]})
    plt.plot('x', 'y1', data=df, marker='o', markerfacecolor='green', markersize=8, color='skyblue', linewidth=2)
    plt.title('Recovered Cases Per Day Analysis')
    plt.xlabel("Number Of Days")
    plt.ylabel("Cases At Particular Date")
    plt.show()


####################################################################################################################################


def confirmed(ind):
    
    df_dc1 = df_dc.loc[:, '6/2/20':]
    df = pd.DataFrame({'x': range(0, 114), 'y1': df_dc1.iloc[ind, :]})
    plt.plot('x', 'y1', data=df, marker='o', markerfacecolor='blue', markersize=8, color='skyblue', linewidth=2)
    plt.title('Confirmed Cases Per Day Analysis')
    plt.xlabel("Number Of Days")
    plt.ylabel("Cases At Particular Date")
    plt.show()
    
    

#####################################################################################################################################


def cou_wise():


    def show_entry_fields():

        cou = countrychoosen.get()

        detail(cou)

    
    for i in range(187):
        lst.append(df_dc['Country'][i])
        

    ll = Label(root, text="Country Name :", font=("times", 15, "bold"), bg="gold2", fg="brown")
    ll.place(x=155, y=210)

    n = StringVar()

    countrychoosen = ttk.Combobox(root, textvariable=n, font=("times", 16))
    countrychoosen.place(x=320, y=210)


    countrychoosen['values'] = lst

    countrychoosen.current()

    ll1 = Button(root, text='Show', font=("times", 11, "bold"), command=show_entry_fields, bg="light grey", relief = RIDGE, borderwidth = 2, width=8)
    ll1.place(x=600, y=210)



######################################################################################################################################


def Tick():

    t_s = time.strftime("%H:%M:%S")
    d_s = time.strftime("%d/%m/%Y")

    clock.config(text="Date- "+d_s+"\n"+"Time- "+t_s)

    clock.after(200, Tick)


####################################################################################################################################


colours = ["red", "green", "blue", "yellow", "pink", "gold2", "red2", "brown", "purple"]


def Labelcol():

    aa = random.choice(colours)
    SliderLabel.config(fg=aa)

    SliderLabel.after(2, Labelcol)


###################################################################################################################################


def TickLabel():

    global count, text

    if count >= len(ss):

        count = 0
        text = ""

        SliderLabel.config(text=text)

    else:

        text = text + ss[count]
        SliderLabel.config(text=text)
        count += 1


    SliderLabel.after(200, TickLabel)



####################################################################################################################################


def about_us():


    top = Toplevel()
    top.title("Group Details")
    top.geometry("800x550+250+90")
    top.config(bg="cyan")
    top.resizable(False, False)
    top.grab_set()


    l1 = Label(top, text = "GROUP MEMBER'S NAME", font = ("times", 16, "bold"), bg = "cyan")
    l1.place(x=100, y=50)

    l1 = Label(top, text="Aseem Ranjan", font=("times", 16, "bold"), bg="cyan", fg="red")
    l1.place(x=150, y=150)

    l1 = Label(top, text="Naveen Rathore", font=("times", 16, "bold"), bg="cyan", fg="red")
    l1.place(x=150, y=250)



    l1 = Label(top, text="ENROLLMENT NUMBER", font=("times", 16, "bold"), bg="cyan")
    l1.place(x=450, y=50)

    l1 = Label(top, text="BT19CSE085", font=("times", 16, "bold"), bg="cyan", fg="purple")
    l1.place(x=500, y=150)

    l1 = Label(top, text="BT19CSE117", font=("times", 16, "bold"), bg="cyan", fg="purple")
    l1.place(x=500, y=250)



##################################################################################################################################


def pie_chart(name, cases):

    meta = name
    values = cases
    distribution = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1)

    fig1, ax = plt.subplots()
    ax.pie(values, explode=distribution, labels=meta, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')
    ax.set_title("Percentage Distribution Of Each Country\n")
    plt.show()


###################################################################################################################################


aa = '6/30/20'
bb = '7/31/20'
cc = '8/31/20'
dd = '9/23/20'


def month(aa):
    
    
    lst, lst1, name, name1, cases, cases1 =[], [], [], [], [], []
    lst = heapq.nlargest(6, df_tc.loc[:, aa])
    lst1 = heapq.nsmallest(6, df_tc.loc[:, aa])

    for j in range(len(lst)):
        for i in range(187):
            if df_tc[aa][i] == lst[j]:
                name.append(df_tc['Country'][i])
                cases.append(df_tc[aa][i])
                break
    
    for j in range(len(lst1)):
        for i in range(187):
            if df_tc[aa][i] == lst1[j]:
                name1.append(df_tc['Country'][i])
                cases1.append(df_tc[aa][i])
                break
    
    
    top = Toplevel()
    if aa == '6/30/20': top.title("June")
    elif aa == '7/31/20': top.title("July")
    elif aa == '8/31/20': top.title("August")
    else: top.title("September")
    top.geometry("800x550+250+90")
    top.resizable(False, False)
    top.grab_set()

    if aa == '6/30/20': photo = PhotoImage(file="images/June_Analysis.png")
    elif aa == '7/31/20': photo = PhotoImage(file="images/July_Analysis.png")
    elif aa == '8/31/20': photo = PhotoImage(file="images/August_Analysis.png")
    else: photo = PhotoImage(file="images/September_Analysis.png")

    bg_photo = Label(top, image=photo)
    bg_photo.place(x=0, y=0, relwidth=1, relheight=1)

    qq1 = name[0]
    qq2 = name[1]
    qq3 = name[2]
    qq4 = name[3]
    qq5 = name[4]
    qq6 = name[5]

    lab1 = Label(top, text=qq1, font=("times", 20, "normal"), bg="brown", fg="yellow")
    lab1.place(x=50, y=160)

    lab2 = Label(top, text=qq2, font=("times", 20, "normal"), bg="brown", fg="yellow")
    lab2.place(x=50, y=210)

    lab3 = Label(top, text=qq3, font=("times", 20, "normal"), bg="brown", fg="yellow")
    lab3.place(x=50, y=260)

    lab4 = Label(top, text=qq4, font=("times", 20, "normal"), bg="brown", fg="yellow")
    lab4.place(x=50, y=310)

    lab5 = Label(top, text=qq5, font=("times", 20, "normal"), bg="brown", fg="yellow")
    lab5.place(x=50, y=360)

    lab6 = Label(top, text=qq6, font=("times", 20, "normal"), bg="brown", fg="yellow")
    lab6.place(x=50, y=410)


    button_1 = Button(top, text="Case Analysis", width=20, relief=RIDGE, borderwidth=4, font=("times", 14, "bold"), bg="light pink", activebackground="green2", activeforeground="white",command=lambda: pie_chart(name,cases))
    button_1.place(x=80, y=480)



    tt1 = name1[0]
    tt2 = name1[1]
    tt3 = name1[2]
    tt4 = name1[3]
    tt5 = name1[4]
    tt6 = name1[5]


    label1 = Label(top, text=tt1, font=("times", 20, "normal"), bg="light green")
    label1.place(x=450, y=160)

    label2 = Label(top, text=tt2, font=("times", 20, "normal"), bg="light green")
    label2.place(x=450, y=210)

    label3 = Label(top, text=tt3, font=("times", 20, "normal"), bg="light green")
    label3.place(x=450, y=260)

    label4 = Label(top, text=tt4, font=("times", 20, "normal"), bg="light green")
    label4.place(x=450, y=310)

    label5 = Label(top, text=tt5, font=("times", 20, "normal"), bg="light green")
    label5.place(x=450, y=360)

    label6 = Label(top, text=tt6, font=("times", 20, "normal"), bg="light green")
    label6.place(x=450, y=410)


    button_2 = Button(top, text="Case Analysis", width=20, command=lambda: pie_chart(name1,cases1), relief=RIDGE, borderwidth=4, font=("times", 14, "bold"), bg="light pink", activebackground="green2", activeforeground="white")
    button_2.place(x=480, y=480)



    button = Button(top, text="Back", command=top.destroy, relief=RIDGE, borderwidth=4 , width=5, bg="gold2", font=("times", 12, "bold"), activebackground="light pink", activeforeground="white")
    button.place(x=740, y=8)


    top.mainloop()



#####################################################################################################################################


def histogram():
    
    cases = [(414.204, 711.462, 785.36, 600.27), (265.23, 500.17, 642.65, 480.288), (129.49, 166.42, 174.42, 117.68)]
    index = np.arange(4)
    wid = 0.25

    plt.bar(index, cases[0], wid, label='Confirmed')
    plt.bar(index + wid, cases[1], wid, label='Recovered')
    plt.bar(index + 2*wid, cases[2], wid, label='Death')

    plt.ylabel('Cases\n')
    plt.title('Cases Per Month Analysis Chart\n')

    plt.xticks(index + wid, ('June', 'July', 'August', 'September'))
    plt.legend(loc='best')
    plt.show()

    
###################################################################################################################################


root = Tk()

root.title("Covid Analizer")
root.config(bg = "gold2")
root.geometry("900x650+200+0")
root.resizable(False, False)


####################################################################################################################################


ss = "Covid-19 Analyzer"
count = 0
text = ""

SliderLabel = Label(root, text=ss, relief=RIDGE, borderwidth=5, font=("chiller", 30, "italic bold"), width=20, bg="cyan")
SliderLabel.place(x=300, y=0)


TickLabel()
Labelcol()



####################################################################################################################################


clock = Label(root, relief=RIDGE, borderwidth=4, font=("times", 14, "bold"), bg="lawn green")
clock.place(x=0, y=0)

Tick()


#####################################################################################################################################


qq = "About Us"

about = Button(root, text=qq, font=("times", 14, "bold"), command=about_us, relief=RIDGE, borderwidth=4, width=9, bg="green2", activebackground="light pink", activeforeground="white")
about.place(x=786, y=8)


####################################################################################################################################


qq = "INDIAN INSTITUTE OF INFORMATION TECHNOLOGY, NAGPUR"

footer = Label(root, text=qq, font=("times", 14, "bold"), bg="lawn green", width=82)
footer.place(x=0, y=622)


#####################################################################################################################################


button1 = Button(root, text="June", command=lambda: month(aa), width=10, relief=RIDGE, borderwidth=4, font=("times", 14, "bold"), bg="light pink", activebackground="green2", activeforeground="white")
button1.place(x=80, y=370)


button2 = Button(root, text="July", command=lambda: month(bb), width=10, relief=RIDGE, borderwidth=4, font=("times", 14, "bold"), bg="light pink", activebackground="green2", activeforeground="white")
button2.place(x=280, y=370)


button3 = Button(root, text="August", command=lambda: month(cc), width=10, relief=RIDGE, borderwidth=4, font=("times", 14, "bold"), bg="light pink", activebackground="green2", activeforeground="white")
button3.place(x=480, y=370)


button4 = Button(root, text="September", command=lambda: month(dd), width=10, relief=RIDGE, borderwidth=4, font=("times", 14, "bold"), bg="light pink", activebackground="green2", activeforeground="white")
button4.place(x=680, y=370)


button5 = Button(root, text="Worldwide Analysis", command=histogram, width=28, relief=RIDGE, borderwidth=4, font=("times", 14, "bold"), bg="light blue", activebackground="blue", activeforeground="white")
button5.place(x=280, y=470)


cou_wise()


#######################################################################################################################################


s = "Search Country wise Data"
l = Label(root, text=s, font=("times", 16, "bold"), bg="gold2")
l.place(x=325, y=130)


s = "Search Month's wise Data"
l = Label(root, text=s, font=("times", 16, "bold"), bg="gold2")
l.place(x=325, y=300)


#######################################################################################################################################


root.mainloop()


######################################################################################################################################



