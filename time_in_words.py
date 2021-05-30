from tkinter import Tk, PhotoImage, Label
from time import localtime
import math
import getpass


#create a function that reads time in words
def timeInWords(h,m):
    hours = {0: 'twelve', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
            10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
            18: 'eighteen', 19: 'nineteen', 20: 'twenty', 21: 'twenty one', 22: 'twenty two', 23: 'twenty three'}
    minutes = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
            10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'quarter', 16: 'sixteen', 17: 'seventeen',
            18: 'eighteen', 19: 'nineteen', 20: 'twenty', 21: 'twenty one', 22: 'twenty two', 23: 'twenty three',24:'twenty four',
            25:'twenty five',26:'twenty six',27:'twenty seven',28:'twenty eight',29:'twenty nine'}

    am_pm = ""
    if 0<=h<=11 or ((h+1)>23 and m>30):
        am_pm = "AM"
    else:
        am_pm = "PM"

    if m==0:
        return "{} o'clock ({}).".format(hours[h],am_pm).capitalize()
    elif m==1 or 60-m==1:
        return  "{} minute past {} ({})".format(minutes[m],hours[h%12], am_pm).capitalize() if m==1 else "{} minute to {} ({}).".format(minutes[60-m],hours[h+1], am_pm).capitalize()
    elif 1<m<30:
        if m==15:
            return "quarter past {} ({}).".format(hours[h%12],am_pm).capitalize()
        else:
            return "{} minutes past {} ({}).".format(minutes[m],hours[h%12],am_pm).capitalize()
    elif m==30:
        return "half past {} ({})".format(hours[h%12],am_pm).capitalize()
    elif 30<m<=59:
        if h+1 > 23:
            hours[h+1]=hours[0]
        if m==45:
            return "{} to {} ({})".format(minutes[60-m],hours[(h+1)%12],am_pm).capitalize()
        else:
            return "{} minutes to {} ({}).".format(minutes[60-m],hours[(h+1)%12],am_pm).capitalize()


    return "This time is not yet configured in your system!"




if __name__=="__main__":

    #create a localtime object
    t = localtime()

    #get computer username
    username = getpass.getuser()

    main_window = Tk()
    main_window.title("Time in words")

    #set customised icon
    photo = PhotoImage(file="logo.png")
    main_window.iconphoto(False,photo)


    #create a label for Time
    h = '0'+str(t.tm_hour) if t.tm_hour<10 else str(t.tm_hour)
    m = '0'+str(t.tm_min) if t.tm_min<10 else str(t.tm_min)
    Label(text=str(h)+':'+str(m), font=("Times New Roman", 50), fg="black").pack()

    #create a label for time in words
    Label(text=timeInWords(t.tm_hour,t.tm_min), font=("Times New Roman",50), bg="yellow", fg="blue").pack()

    #print a welcome message
    Label(text="Hello {}, thank you for using my app!".format(username), font=("Times New Roman",25), fg="Green").pack()

    main_window.mainloop()
