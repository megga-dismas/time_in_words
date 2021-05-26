from time import localtime
import tkinter as tk
from tkinter import Tk, Label, PhotoImage

tim = localtime()

def timeInWords(h, m):
    # Write your code here
    assert(1<=h<=12)
    hm = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
          11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'quarter', 16: 'sixteen', 17: 'seventeen',
          18: 'eighteen', 19: 'nineteen', 20: 'twenty', 21: 'twenty one', 22: 'twenty two', 23: 'twenty three',
          24: 'twenty four', 25: 'twenty five', 26: 'twenty six', 27: 'twenty seven', 28: 'twenty eight', 29: 'twenty nine'
         }

    if m==0:
        return "{} o' clock.".format(hm[h]).capitalize()
    elif m==1 or m==59:
        if m==1:
            return "{} minute past {}.".format(hm[m],hm[h])
        else:
            return "{} minute past {}.".format(hm[m],hm[h+1] if h+1<=12 else hm[(h+1)%12]).capitalize()
    elif m==15 or m==45:
        text = "quarter past {}.".format(hm[h]) if m==15 else "quarter to {}".format(hm[h+1] if h+1<=12 else hm[(h+1)%12])
        return text.capitalize()
    elif m==30:
        return "half past {}.".format(hm[h]).capitalize()
    elif m>30:
        return "{} minutes to {}.".format(hm[60-m], hm[h+1] if (h+1)<=12 else hm[(h+1)%12]).capitalize()
    else:
        return "{} minutes past {}.".format(hm[m],hm[h]).capitalize()

# def call_time():
#     h = tim.tm_hour
#     m = tim.tm_min
#     return h,m




if __name__=="__main__":
    main_window = Tk()
    #main_window.state("zoomed")
    main_window.title("Time in words")
    photo = PhotoImage(file="logo.png")
    main_window.iconphoto(False,photo)

    #time configurations
    h = str(tim.tm_hour) if tim.tm_hour>=10 else '0'+str(tim.tm_hour)
    m = str(tim.tm_min) if tim.tm_min>=10 else '0'+str(tim.tm_min)

    Label(text=h+':'+m, font=("Times New Roman bold",50)).pack()
    Label(text=timeInWords(int(h),int(m)), bg="Yellow", fg="Blue",font=("Times New Roman bold",50)).pack()
    main_window.mainloop()
