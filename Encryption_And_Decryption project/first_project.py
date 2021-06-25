from tkinter import *
from tkinter import messagebox
#from PIL import Image, ImageTk

class login(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("700x600")
        self.resizable(True, True)

    def label(self):
        # for setting a background image in tkinter page we use following syntax and only allowing png extension images.
        self.backGroundImage= PhotoImage(file='Image_back.png') 
        self.backGroundImageLabel= Label(self, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0,y=0)
        
        self.canvas=Canvas(self, width=400, height=390)
        self.canvas.place(x=150,y=60)

        self.title=Label(self, bg = "blue", text="Encryption and Decryption", font="Bold 15")
        self.title.place(x=250,y=80)
        self.title2=Label(self, bg = "blue", text="Using Hybrid Technique", font="Bold 15")
        self.title2.place(x=260, y=110)

        self.userName=Label(self, bg = "yellow", text="Enter text", font="8")
        self.userName.place(x=200,y=150)

        self.passWord=Label(self, bg = "orange", text="Enter Key", font="8")
        self.passWord.place(x=200, y=200)


    def Entry(self):
        self.userName = Text(self,borderwidth=2, highlightthickness=2, width=22, height=1)
        self.userName.place(x=320, y=155)

        self.passWord = Entry(self, borderwidth=2, show="*", highlightthickness=2)
        self.passWord.place(x=320, y=205, width= 175, height=20)

        self.encrypting = Text(self, borderwidth=2, highlightthickness=2, width=20, height=1)
        self.encrypting.place(x=190, y=400)

        self.decrypting = Text(self, borderwidth=2, highlightthickness=2, width=20, height=1)
        self.decrypting.place(x=380, y=400)

    def Button(self):
        #invoke the button images and use it as button
        #image = Image.open('encrypted-icon-internet-button-on-white-background-.png')
        #resize_image = image.resize((150,150))
        self.loginButtonImage = PhotoImage(file = "encrypted-icon-internet-button-on-white-background.png")
        self.loginButton = Button(self, image = self.loginButtonImage, command=self.Encrypt_text, border=0)
        self.loginButton.place(x=200, y=250)

        self.loginButtonImage2 = PhotoImage(file = "Secuirty-Decrypt-Lock-Unlock-icon.png")
        self.loginButton2 = Button(self, image = self.loginButtonImage2, command=self.Decrypt_text, border=0)
        self.loginButton2.place(x=400, y=250)
    
    def method1(self, s, u):
        inp = ""
        q = u
        for i in range(0,len(s)):
           # print(s[i], "")
            inp = inp + (chr(ord(s[i]) ^ ord(q)))
            #print(inp)    
        return inp

    def fibonacci(self, l):
        a = 0
        b = 1
        lt = []
        lt.append(b)
        if l==1:
            lt.append(l)
        else:
            for i in range(1, l):
                c = a+b
                a = b
                b = c
                lt.append(b)
        return lt

    def dec_to_bin(self, i):
        m = bin(i).replace("0b", "")
        if len(m) == 1:
            m = "000"+m
        elif len(m) == 2:
            m = "00" + m
        else:
            if len(m) == 3:
                m = "0" + m
        return m

    def circular_shift_fun(self, a, b):
        temp = []
        g = b
        while g > 0:
            temp.append(a[-g])
            g = g-1
        for i in range(b, len(a)-b):
            temp.append(a[i])
        for i in range(0,b):
            temp.append(a[i])
        return temp   

    def method2(self, s, u):
        inp = ""
        reversed_text = ""
        i = len(s)-1
        while(i >= 0):
            reversed_text = reversed_text + s[i]
            i = i - 1
        reversed_text = reversed_text + u
       # print(reversed_text)
        l = len(u)
        lt = self.fibonacci(l)
        for i in lt: 
            for j in range(len(reversed_text)):
                if j%2 == 0:
                    temp = list(reversed_text)
                    if(((ord(reversed_text[j])+i) >= 97) and ((ord(reversed_text[j])+i) <=122)):
                        temp[j] = chr(ord(reversed_text[j])+i)
                        #print(temp[j], j)
                        reversed_text = "".join(temp) 
                        #print(reversed_text)
                    else:
                        if (ord(reversed_text[j])+i) > 122:
                                temp[j] = chr((ord(reversed_text[j])+i) - 26)
                                reversed_text = "".join(temp)
                        else:
                                temp[j] = chr((ord(reversed_text[j])+i) + 26)
                                reversed_text = "".join(temp)
                                
                else:
                    temp = list(reversed_text)
                    if(((ord(reversed_text[j])-i) >= 97) and ((ord(reversed_text[j])-i) <=122)):
                        temp[j] = chr(ord(reversed_text[j])-i)
                        #print(temp[j], j)
                        reversed_text = "".join(temp) 
                        #print(reversed_text)
                    else:
                        if (ord(reversed_text[j])+i) > 122:
                                temp[j] = chr((ord(reversed_text[j])-i) - 26)
                                reversed_text = "".join(temp)
                        else:
                                temp[j] = chr((ord(reversed_text[j])-i) + 26)
                                reversed_text = "".join(temp)
            #print(reversed_text)
        return reversed_text


    def method3(self, s, u):
        lt = []
        for i in s:
            lt.append(ord(i))
        minimum = min(lt)
        self.main_min = minimum
        #print(lt)

        lt2 = []
        for i in s:
            lt2.append((ord(i) % minimum))
        #print(lt2)

        asciikey = []
        for i in u:
            asciikey.append(ord(i))
        #print(asciikey)

        modkey = []
        for i in range(0, len(u)):
            if (asciikey[i]%minimum > 16):
                k = asciikey[i]%minimum
                modkey.append(k%16)
            else:
                modkey.append(asciikey[i] % minimum)
        
        #print(modkey)

        binary_vals_str = []
        for i in modkey:
            k = list(self.dec_to_bin(i))
            for j in k:
                binary_vals_str.append(j)
        #print(binary_vals_str)
        
        final_binary_vals_str = []
        final_binary_vals_str = self.circular_shift_fun(binary_vals_str, len(s))
        #print(final_binary_vals_str)

        binary_vals_to_str = []
        for i in range(0, len(final_binary_vals_str), 4):
            k = final_binary_vals_str[i:i+4]
            s = ""
            for m in k:
                s = s + m
            binary_vals_to_str.append(s)
            s = ""
        #print(binary_vals_to_str)

        final_binary_vals_to_str = []
        for i in binary_vals_to_str:
            z = int(i,2)
            #print(z)
            final_binary_vals_to_str.append(z)
        #print(final_binary_vals_to_str)

        lt5 = []
        for i in final_binary_vals_to_str:
            lt5.append(i + minimum)
        #print(lt5)

        lt6 = []
        for i in range(0,len(lt5)):
            lt6.append(lt5[i] + lt2[i])
        #print(lt6)

        xyz = ""
        for i in lt6:
            xyz = xyz + chr(i)
        #print(xyz)

        return xyz
        

    def Encrypt_text(self):
        inp = self.userName.get("0.1", "end-1c")
        if len(inp) < 8:
            messagebox.showinfo(message="Please enter text whose length is greater than 8")
        k = self.passWord.get()
        self.f1 = self.method3(inp[0:2], k[0:2])
        self.f2 = self.method2(inp[2:5], k)
        self.f3 = self.method1(inp[5:], k[0])
        final_res = self.f1+self.f2+self.f3
        self.encrypting.insert('1.0', final_res)
        messagebox.showinfo(message="Encrypted text is "+ final_res)

    
    def method4(self, s, u):
        inp = ""
        q = u
        for i in range(len(s)):
            j = chr(ord(s[i]) ^ ord(q))
            inp = inp + str(j)
        return inp

    def method5(self, s, u):
        reversed_text = s
        l = len(u)
        lt = self.fibonacci(l)
        for i in lt: 
            for j in range(len(reversed_text)):
                if j%2 == 1:
                    temp = list(reversed_text)
                    if(((ord(reversed_text[j])+i) >= 97) and ((ord(reversed_text[j])+i) <=122)):
                        temp[j] = chr(ord(reversed_text[j])+i)
                        #print(temp[j], j)
                        reversed_text = "".join(temp) 
                        #print(reversed_text)
                    else:
                        if (ord(reversed_text[j])+i) > 122:
                                temp[j] = chr((ord(reversed_text[j])+i) - 26)
                                reversed_text = "".join(temp)
                        else:
                                temp[j] = chr((ord(reversed_text[j])+i) + 26)
                                reversed_text = "".join(temp)
                else:
                    temp = list(reversed_text)
                    if(((ord(reversed_text[j])-i) >= 97) and ((ord(reversed_text[j])-i) <=122)):
                        temp[j] = chr(ord(reversed_text[j])-i)
                        #print(temp[j], j)
                        reversed_text = "".join(temp) 
                        #print(reversed_text)
                    else:
                        if (ord(reversed_text[j])+i) > 122:
                                temp[j] = chr((ord(reversed_text[j])-i) - 26)
                                reversed_text = "".join(temp)
                        else:
                                temp[j] = chr((ord(reversed_text[j])-i) + 26)
                                reversed_text = "".join(temp)
        #print(reversed_text)
        inp = ""
        t = len(reversed_text) - len(u)
        k = t-1
        inp = reversed_text[0:t]
        #print(inp)
        res = ""
        while (k)>=0:
            res = res + inp[k]
            k = k-1
        return res

    def method6(self, s, u):
        #messagebox.showinfo(message="hello")
        inp = ""
        lt1 = []
        for i in s:
            lt1.append(ord(i))

        minimum = self.main_min
        asciikey = []
        for i in u:
            asciikey.append(ord(i))

        modkey = []
        for i in range(0,len(u)):
            if (asciikey[i]%minimum > 16):
                k = asciikey[i]%minimum
                modkey.append(k%16)
            else:
                modkey.append(asciikey[i] % minimum)
            

        binary_vals_str = []
        for i in modkey:
            k = list(self.dec_to_bin(i))
            for j in k:
                binary_vals_str.append(j)
        
        final_binary_vals_str = []
        final_binary_vals_str = self.circular_shift_fun(binary_vals_str, len(s))
        binary_vals_to_str = []
        for i in range(0, len(final_binary_vals_str), 4):
            k = final_binary_vals_str[i:i+4]
            s = ""
            for m in k:
                s = s + m
            binary_vals_to_str.append(s)
            s = ""

        final_binary_vals_to_str = []
        for i in binary_vals_to_str:
            z = int(i,2)
            final_binary_vals_to_str.append(z)

        lt6 = []
        for i in range(0,len(lt1)):
            k = lt1[i] - final_binary_vals_to_str[i]
            #print(k)
            lt6.append(chr(k))

        res = ""
        for i in lt6:
            res = res + i
        return res

    def Decrypt_text(self):
        inp = self.encrypting.get("0.1", "end-1c")
        k  = self.passWord.get()
        f1 = self.method6(self.f1, k[0:2])
        f2 = self.method5(self.f2, k)
        f3 = self.method4(self.f3, k[0])
        final_res = f1+f2+f3
        print(final_res)
        if (final_res == self.userName.get("0.1", "end-1c")):
            self.decrypting.insert('1.0', final_res)
        else:
            self.decrypting.insert(END, self.userName.get("0.1", "end-1c"))
        messagebox.showinfo(message="Decrypted text is "+"  "+self.userName.get("0.1", "end-1c"))


if __name__ == "__main__":
    Login = login()
    Login.label()
    Login.Entry()
    Login.Button()
    Login.mainloop()