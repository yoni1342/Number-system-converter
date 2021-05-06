# I spend 6 days to write this my first GUI project. I leared tkinter from scrache and do it. I finshed in jul 02 2020 1:45AM
#define the screen
from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Number System Converter")
# root.iconbitmap(r'letter-m.ico')
root.geometry('500x500')

#define frame 1
frame1 = LabelFrame(root, text = "Welcome to the number sysetem converter, choose converstion types below the list!", padx=100,   pady=10 )
def Button_Okay():
    if click.get() == "Binary to Decimal":
        global Button_convert
        global frame2
        #define Button_Convert function
        def B_to_D():
            l = [int(i) for i in binarry.get()]
            if any(b>1 for b in l) == False:
                l.reverse()
                decimal = 0
                for I, V in enumerate(l):
                    z = V * (2**I)
                    decimal += z
                la = Label(frame2, text = "("+str(binarry.get())+")2 = ("+str(decimal)+")10").pack()
            else:
                messagebox.showerror("error", "you entered wrong value, please enter correct binary numbers in 1 or 0!").pack()
        #define the second frame
        frame2 = LabelFrame(root, text = 'Binary to Decimal ', padx=100,   pady=10)
        #define the info label
        Info = Label(frame2, text = "Enter your Binary number").pack()
        #define the converter button
        Button_convert = Button(frame2, text = 'Convert', command = B_to_D)
        #define the entery
        binarry = Entry(frame2,width = 40,borderwidth = 5 )
        #set the entry
        binarry.pack(padx = 5, pady=20)
        #set the convert button
        Button_convert.pack(anchor = E)
        #set the second frame
        frame2.grid(row=1, column=0,padx=10, pady=50)
    elif click.get() == "Binary to Octal":
        #frame2.grid_forget()
        # define convert_button function
        def B_to_O():
            l = [int(i) for i in binarry.get()]
            if any(b>1 for b in l) == False:
                l.reverse()
                decimal = 0
                for I, V in enumerate(l):
                    z = V * (2**I)
                    decimal += z

                o = []
                while decimal!=0:
                    r= decimal%8
                    o.append(r)
                    decimal //=8
                o.reverse()
                octal = ''
                for i in o:
                    octal += str(i)
                la = Label(frame2, text = "("+str(binarry.get())+")2 = ("+str(octal)+")8").pack()
            else:
                messagebox.showerror("error", "you entered wrong value, please enter correct binary numbers in 1 or 0!").pack()

        #define the second frame
        frame2 = LabelFrame(root, text = "Binary to Octal", padx=100,   pady=10)
        #define the info label
        Info = Label(frame2, text = "Enter your Binary number").pack()
        #define the converter button
        Button_convert = Button(frame2, text = 'Convert', command = B_to_O)
        #define the entery
        binarry = Entry(frame2,width= 40,borderwidth = 5 )
        #set the entry
        binarry.pack(padx = 5, pady=20)
        #set the convert button
        Button_convert.pack(anchor = E)
        #set the second frame
        frame2.grid(row=1, column=0,padx=10, pady=50)
    elif click.get() == "Binary to Hexadecimal":
        #define Binary to Hexadecimal function
        def B_to_H():
            l = [int(i) for i in binarry.get()]
            if any(b>1 for b in l) == False:
                l.reverse()
                decimal = 0
                for I, V in enumerate(l):
                    z = V * (2**I)
                    decimal += z

                o = []
                while decimal!=0:
                    r= decimal%16
                    if r == 10:
                        r = "a"
                    elif r == 11:
                        r = "b"
                    elif r == 12:
                        r = "c"
                    elif r == 13:
                        r = "d"
                    elif r == 14:
                        r = "e"
                    elif r == 15:
                        r = "f"
                    o.append(r)
                    decimal //=16
                o.reverse()
                hexadecimal = ''
                for i in o:
                    hexadecimal += str(i)
                la = Label(frame2, text = "("+str(binarry.get())+")2 = ("+str(hexadecimal)+")16").pack()
            else:
                messagebox.showerror("error", "you entered wrong value, please enter correct binary numbers in 1 or 0!").pack()
        #define the second frame
        frame2 = LabelFrame(root, text = "Binary to Hexadecimal", padx=100,   pady=10)
        #define the info label
        Info = Label(frame2, text = "Enter your Binary number").pack()
        #define the converter button
        Button_convert = Button(frame2, text = 'Convert', command = B_to_H)
        #define the entery
        binarry = Entry(frame2,width= 40,borderwidth = 5 )
        #set the entry
        binarry.pack(padx = 5, pady=20)
        #set the convert button
        Button_convert.pack(anchor = E)
        #set the second frame
        frame2.grid(row=1, column=0,padx=10, pady=50)
    if click.get() == "Decimal to Binary":
        def D_to_B():
            y = [decimal.get()]
            l = []
            while y[0]!=0:
                r= int(y[0])%2
                l.append(r)
                y[0] = int(y[0])//2
            l.reverse()
            binary = ''
            for i in l:
                binary += str(i)
            la = Label(frame2, text = "("+str(decimal.get())+")10 = ("+str(binary)+")2").pack()

        #define the second frame
        frame2 = LabelFrame(root, text = "Decimal to Binary", padx=100,   pady=10)
        #define the info label
        Info = Label(frame2, text = "Enter your Decimal number").pack()
        #define the converter button
        Button_convert = Button(frame2, text = 'Convert', command = D_to_B)
        #define the entery
        decimal = Entry(frame2,width= 40,borderwidth = 5 )
        #set the entry
        decimal.pack(padx = 5, pady=20)
        #set the convert button
        Button_convert.pack(anchor = E)
        #set the second frame
        frame2.grid(row=1, column=0,padx=10, pady=50)
    elif click.get() == "Decimal to Octal":
        def D_to_O():
            y = [decimal.get()]
            l = []
            while y[0]!=0:
                r= int(y[0])%8
                l.append(r)
                y[0] = int(y[0])//8
            l.reverse()
            octal = ''
            for i in l:
                octal += str(i)

            la = Label(frame2, text = "("+str(decimal.get())+")10 = ("+str(octal)+")8").pack()
        #define the second frame
        frame2 = LabelFrame(root, text = "Decimal to Octal", padx=100,   pady=10)
        #define the info label
        Info = Label(frame2, text = "Enter your Decimal number").pack()
        #define the converter button
        Button_convert = Button(frame2, text = 'Convert', command = D_to_O)
        #define the entery
        decimal = Entry(frame2,width= 40,borderwidth = 5 )
        #set the entry
        decimal.pack(padx = 5, pady=20)
        #set the convert button
        Button_convert.pack(anchor = E)
        #set the second frame
        frame2.grid(row=1, column=0,padx=10, pady= 50)
    elif click.get() == "Decimal to Hexadecimal":
        def D_to_H():
            y =[decimal.get()]
            l = []
            while y[0]!=0:
                r= int(y[0])%16
                if r == 10:
                    r = "a"
                elif r == 11:
                    r = "b"
                elif r == 12:
                    r = "c"
                elif r == 13:
                    r = "d"
                elif r == 14:
                    r = "e"
                elif r == 15:
                    r = "f"
                l.append(r)
                y[0] = int(y[0]) //16
            l.reverse()
            hexadecimal = ''
            for i in l:
                hexadecimal += str(i)

            la = Label(frame2, text = "("+str(decimal.get())+")10 = ("+str(hexadecimal)+")16").pack()
        #define the second frame
        frame2 = LabelFrame(root, text = "Decimal to Hexadecimal", padx=100,   pady=10)
        #define the info label
        Info = Label(frame2, text = "Enter your Decimal number").pack()
        #define the converter button
        Button_convert = Button(frame2, text = 'Convert', command = D_to_H)
        #define the entery
        decimal = Entry(frame2,width= 40,borderwidth = 5 )
        #set the entry
        decimal.pack(padx = 5, pady=20)
        #set the convert button
        Button_convert.pack(anchor = E)
        #set the second frame
        frame2.grid(row=1, column=0,padx=10, pady= 50)
    elif click.get() == "Octal to Binary":
        def O_to_B():
            l = [int(i) for i in str(octal.get())]
            l.reverse()
            List = []
            decimal = 0

            f = any(b>=8 for b in l )
            if f == False:
                for i, v in enumerate(l):
                    z = v * (8**i)
                    decimal += z
                int(decimal)
                print(decimal)
            while decimal != 0:
                r = decimal % 2
                List.append(r)
                decimal //= 2
            List.reverse()
            binary = ''
            for h in List:
                binary += str(h)
            la = Label(frame2, text = "("+str(octal.get())+")8 = ("+str(binary)+")2").pack()
            if f == True:
                messagebox.showerror("error", "you entered wrong value, please enter correct octal number!").pack()

        #define the second frame
        frame2 = LabelFrame(root, text = "Octal to Binary", padx=100,   pady=10)
        #define the info label
        Info = Label(frame2, text = "Enter your Octal number").pack()
        #define the converter button
        Button_convert = Button(frame2, text = 'Convert', command = O_to_B)
        #define the entery
        octal = Entry(frame2,width= 40,borderwidth = 5 )
        #set the entry
        octal.pack(padx = 5, pady=20)
        #set the convert button
        Button_convert.pack(anchor = E)
        #set the second frame
        frame2.grid(row=1, column=0,padx=10, pady= 50)
    elif click.get() == "Octal to Decimal":
        def O_to_D():
            l = [int(i) for i in str(octal.get())]
            l.reverse()

            f = any(b>=8 for b in l )
            if f == False:
                decimal = 0
                for i, v in enumerate(l):
                    z = v * (8**i)
                    decimal += z
                la = Label(frame2, text = "("+str(octal.get())+")8 = ("+str(decimal)+")10").pack()
            if f == True:
                messagebox.showerror("error", "you entered wrong value, please enter correct octal number!").pack()
        #define the second frame
        frame2 = LabelFrame(root, text = "Octal to Decimal", padx=100,   pady=10)
        #define the info label
        Info = Label(frame2, text = "Enter your Octal number").pack()
        #define the converter button
        Button_convert = Button(frame2, text = 'Convert', command = O_to_D)
        #define the entery
        octal = Entry(frame2,width= 40,borderwidth = 5 )
        #set the entry
        octal.pack(padx = 5, pady=20)
        #set the convert button
        Button_convert.pack(anchor = E)
        #set the second frame
        frame2.grid(row=1, column=0,padx=10, pady= 50)
    elif click.get() == "Octal to Hexadecimal":
        def O_to_H():
            l = [int(i) for i in str(octal.get())]
            l.reverse()

            f = any(b>=8 for b in l )
            if f == False:
                decimal = 0
                for i, v in enumerate(l):
                    z = v * (8**i)
                    decimal += z
                h = []
                while decimal!=0:
                    r = decimal%16
                    if r == 10:
                        r = "a"
                    elif r == 11:
                        r = "b"
                    elif r == 12:
                        r = "c"
                    elif r == 13:
                        r = "d"
                    elif r == 14:
                        r = "e"
                    elif r == 15:
                        r = "f"
                    h.append(r)
                    decimal //=16
                h.reverse()
                hexadecimal = ''
                for i in h:
                    hexadecimal += str(i)

                la = Label(frame2, text = "("+str(octal.get())+")8 = ("+str(hexadecimal)+")16").pack()
            elif f == True:
                messagebox.showerror("error", "you entered wrong value, please enter correct octal number!").pack()

        #define the second frame
        frame2 = LabelFrame(root, text = "Octal to Hexadecimal", padx=100,   pady=10)
        #define the info label
        Info = Label(frame2, text = "Enter your Octal number").pack()
        #define the converter button
        Button_convert = Button(frame2, text = 'Convert', command = O_to_H)
        #define the entery
        octal = Entry(frame2,width= 40,borderwidth = 5 )
        #set the entry
        octal.pack(padx = 5, pady=20)
        #set the convert button
        Button_convert.pack(anchor = E)
        #set the second frame
        frame2.grid(row=1, column=0,padx=10, pady= 50)
    elif click.get() == "Hexadecimal to Binary":
        def H_to_B():
            l  = [str(i) for i in hexadecimal.get()]
            l.reverse()
            for i in l:
                if i == 'a':
                    x = l.index('a')
                    l.remove('a')
                    l.insert(x, 10)
                elif i == 'b':
                    x = l.index('b')
                    l.remove('b')
                    l.insert(x, 11)
                elif i == 'c':
                    x = l.index('c')
                    l.remove('c')
                    l.insert(x, 12)
                elif i == 'd':
                    x = l.index('d')
                    l.remove('d')
                    l.insert(x, 13)
                elif i == 'e':
                    x = l.index('e')
                    l.remove('e')
                    l.insert(x, 14)
                elif i == 'f':
                    x = l.index('f')
                    l.remove('f')
                    l.insert(x, 15)
            k = [int(i) for i in l]

            decimal = 0
            for I, V in enumerate(k):
                g = V * (16**I)
                decimal += g
            o = []
            while decimal!=0:
                r= decimal%2
                o.append(r)
                decimal //=2
            o.reverse()
            binary = ''
            for i in o:
                binary += str(i)

            la = Label(frame2, text = "("+str(hexadecimal.get())+")16 = ("+str(binary)+")2").pack()
        #define the second frame
        frame2 = LabelFrame(root, text = "Hexadecimal to Binary", padx=100,   pady=10)
        #define the info label
        Info = Label(frame2, text = "Enter your Hexadecimal number").pack()
        #define the converter button
        Button_convert = Button(frame2, text = 'Convert', command = H_to_B)
        #define the entery
        hexadecimal = Entry(frame2,width= 40,borderwidth = 5 )
        #set the entry
        hexadecimal.pack(padx = 5, pady=20)
        #set the convert button
        Button_convert.pack(anchor = E)
        #set the second frame
        frame2.grid(row=1, column=0,padx=10, pady= 50)
    elif click.get() == "Hexadecimal to Decimal":
        def H_to_D():
            l  = [str(i) for i in hexadecimal.get()]
            l.reverse()
            for i in l:
                if i == 'a':
                    x = l.index('a')
                    l.remove('a')
                    l.insert(x, 10)
                elif i == 'b':
                    x = l.index('b')
                    l.remove('b')
                    l.insert(x, 11)
                elif i == 'c':
                    x = l.index('c')
                    l.remove('c')
                    l.insert(x, 12)
                elif i == 'd':
                    x = l.index('d')
                    l.remove('d')
                    l.insert(x, 13)
                elif i == 'e':
                    x = l.index('e')
                    l.remove('e')
                    l.insert(x, 14)
                elif i == 'f':
                    x = l.index('f')
                    l.remove('f')
                    l.insert(x, 15)
            k = [int(i) for i in l]

            decimal = 0
            for I, V in enumerate(k):
                g = V * (16**I)
                decimal += g
            la = Label(frame2, text = "("+str(hexadecimal.get())+")16 = ("+str(decimal)+")10").pack()
        #define the second frame
        frame2 = LabelFrame(root, text = "Hexadecimal to Decimal", padx=100,   pady=10)
        #define the info label
        Info = Label(frame2, text = "Enter your Hexadecimal number").pack()
        #define the converter button
        Button_convert = Button(frame2, text = 'Convert', command = H_to_D)
        #define the entery
        hexadecimal = Entry(frame2,width= 40,borderwidth = 5 )
        #set the entry
        hexadecimal.pack(padx = 5, pady=20)
        #set the convert button
        Button_convert.pack(anchor = E)
        #set the second frame
        frame2.grid(row=1, column=0,padx=10, pady= 50)
    elif click.get() == "Hexadecimal to Octal":
        def H_to_O():
            l  = [str(i) for i in hexadecimal.get()]
            l.reverse()
            for i in l:
                if i == 'a':
                    x = l.index('a')
                    l.remove('a')
                    l.insert(x, 10)
                elif i == 'b':
                    x = l.index('b')
                    l.remove('b')
                    l.insert(x, 11)
                elif i == 'c':
                    x = l.index('c')
                    l.remove('c')
                    l.insert(x, 12)
                elif i == 'd':
                    x = l.index('d')
                    l.remove('d')
                    l.insert(x, 13)
                elif i == 'e':
                    x = l.index('e')
                    l.remove('e')
                    l.insert(x, 14)
                elif i == 'f':
                    x = l.index('f')
                    l.remove('f')
                    l.insert(x, 15)
            k = [int(i) for i in l]

            decimal = 0
            for I, V in enumerate(k):
                g = V * (16**I)
                decimal += g
            o = []
            while decimal!=0:
                r= decimal%8
                o.append(r)
                decimal //=8
            o.reverse()
            octal = ''
            for i in o:
                octal += str(i)

            la = Label(frame2, text = "("+str(hexadecimal.get())+")16 = ("+str(octal)+")8").pack()
        #define the second frame
        frame2 = LabelFrame(root, text = "Hexadecimal to Octal", padx=100,   pady=10)
        #define the info label
        Info = Label(frame2, text = "Enter your Hexadecimal number").pack()
        #define the converter button
        Button_convert = Button(frame2, text = 'Convert', command = H_to_O)
        #define the entery
        hexadecimal = Entry(frame2,width= 40,borderwidth = 5 )
        #set the entry
        hexadecimal.pack(padx = 5, pady=20)
        #set the convert button
        Button_convert.pack(anchor = E)
        #set the second frame
        frame2.grid(row=1, column=0,padx=10, pady= 50)
#define down list
convertion_List = [
    "Binary to Decimal",
    "Binary to Octal",
    "Binary to Hexadecimal",
    "Decimal to Binary",
    "Decimal to Octal",
    "Decimal to Hexadecimal",
    "Octal to Binary",
    "Octal to Decimal",
    "Octal to Hexadecimal",
    "Hexadecimal to Binary",
    "Hexadecimal to Decimal",
    "Hexadecimal to Octal",
]
        #define the variabel and set of the down button
click = StringVar()
click.set("choos the convertion")
down_list = OptionMenu(frame1, click, *convertion_List)

#define okay button

Button_ok = Button(frame1, text = 'OK', command = Button_Okay)

#set frame 1
frame1.grid(row=0, column=0,padx=10, pady=50)
#set down list
down_list.pack()
#set okay button on the frame
Button_ok.pack(anchor = E)



mainloop()
