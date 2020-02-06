import random
import time
import tkinter as tk
import tkinter.messagebox
import webbrowser
from tkinter import *
from tkinter.ttk import *

from PIL import ImageTk


class mainWIN():
    def __init__(self, master):
        self.screenMain = master
        self.screenMain.resizable(0, 0)
        self.screenMain.iconphoto(False, tkinter.PhotoImage(file='icon temp/info.png'))
        self.screenMain.protocol("WM_DELETE_WINDOW", exit)
        self.screenMain.title("INFO 101")
        self.run = False
        self.windowHeight= int(self.screenMain.winfo_reqheight())
        self.windowWidth= int(self.screenMain.winfo_reqwidth())
        self.positionRight = int(self.screenMain.winfo_screenwidth() / 2 - (self.windowWidth / 2))
        self.positionDown = int(self.screenMain.winfo_screenheight() / 2 - (self.windowHeight / 2))
        self.screenMain.geometry(f"250x420+{self.positionRight}+{self.positionDown}")
        style = Style()
        style.configure('W.TButton', font=('Comic sans ms', 8, 'normal', 'italic'), foreground='black')
        style1 = 'W.TButton'
        self.time = tkinter.StringVar(self.screenMain)

        # log out
        logOut = Button(self.screenMain, text='Log Out', command=self.log_out, style=style1)
        logOut.place(relx=0.55, rely=0.45, height=50, width=70, anchor='nw')

        # about me
        aboutMe = Button(self.screenMain, text="About Me", command=self.about_me, style=style1)
        aboutMe.place(relx=0.45, rely=0.45, height=50, width=70, anchor='ne')

        # news
        News = Button(self.screenMain, text="News", command=self.newsScreen, style=style1)
        News.place(relx=0.45, rely=0.35, height=50, width=70, anchor='se')

        # weather
        Weather = Button(self.screenMain, text="Weather", command=self.weatherScreen, style=style1)
        Weather.place(relx=0.55, rely=0.35, height=50, width=70, anchor='sw')

        # Label ID
        self.greet = tkinter.StringVar(self.screenMain)
        self.greeting = Label(self.screenMain, text='Welcome ', font=("impact", 18, "italic"), foreground="blue",
                              textvariable=self.greet)
        self.greeting.place(rely=0.7, relx=0.25, height=30, width=400)
        self.greeting.after(1, self.welcomeTxt)
        Label(self.screenMain, text='ID: ', font=("impact", 15, "italic")).place(rely=0.85, relx=0.14)
        self.text = tkinter.StringVar(self.screenMain)
        id_label = Label(text='TEST123456', font=("Lucida Console", 15, "bold"), foreground="white", background="grey",
                         textvariable=self.text)
        id_label.place(rely=0.86, relx=0.25)
        self.text.set(self.ID_label())

        # time
        style.configure('NuclearReactor.TButton', font=('Arial Narrow', 14, 'bold', 'italic'), foreground='#A0B2C6')
        style2 = 'NuclearReactor.TButton'
        self.timelbl = Button(self.screenMain, text='00:00:00 AMPM', textvariable=self.time, style=style2,
                              command=self.azanTime)
        self.timelbl.place(rely=0.05, relx=0.1, height=50, width=100)
        self.timelbl.after(1, self.updateTime)

        # Social Media
        app_button = Button(self.screenMain, text="Social Media", command=self.socialMedia, style=style1)
        app_button.place(relx=0.56, rely=0.17, height=50, width=80, anchor='sw')

    # the moving word
    def updateTime(self):
        string = time.strftime('%H:%M:%S %p')
        self.time.set(string)
        self.timelbl.after(1000, self.updateTime)

    def welcomeTxt(self):
        greeting = ['welcome', 'hey', 'bonjour', 'assalam', 'heyyo', 'hai', 'salam', 'wasap!', "Kon'nichiwa",
                    'S̄wạs̄dī', 'Vaṇakkam',
                    'marhabaan', 'cześć', 'привет', '问候', '안녕', 'こんにちは', 'سلام', 'good day']
        self.greet.set(random.choice(greeting))
        self.greeting.after(random.randint(3000, 8000), self.welcomeTxt)

    # main button and ID called
    def about_me(self):
        print("about me")
        self.screen1 = Toplevel(self.screenMain)
        self.screen1.iconphoto(False, tkinter.PhotoImage(file='icon temp/info.png'))
        self.screen1.resizable(0, 0)
        self.screen1.title("About ME")

        self.screen1.geometry(f"400x400+{self.positionRight}+{self.positionDown}")
        style = Style()
        style.configure('W.TButton', font=('Comic sans ms', 8, 'normal', 'italic'), foreground='black')
        style1 = 'W.TButton'

        # exit button
        exit_button = Button(self.screen1, text="EXIT", command=self.screen1.destroy, style=style1)
        exit_button.place(relx=0.8, rely=0.85, height=30, width=70, anchor='nw')

        # comment button
        comment_button = Button(self.screen1, text="Comment", command=print("comment"), style=style1)
        comment_button.place(relx=0.8, rely=0.85, height=30, width=70, anchor='ne')

        # label
        text = """My name is Muhammad Helmi Bin Rozain,
    I'm 18 years old.
    I like cat and coding yeshhh. Im new in coding
    this is the try of gui program.
    Do follow my ig:@neko.helmii
    and twitter:@helmimiow
    also FB:Muhammad Helmi Rozain"""

        version = "info 101 v1.01 beta release"

        Label(self.screen1, text=text, font=("Calibri", 15, "italic"), foreground="white", background="grey").place(
            anchor='center', rely=0.5, relx=0.5)
        Label(self.screen1, text=version, font=("Calibri", 15, "italic"), foreground="white", background="grey").place(
            anchor='s', rely=0.1, relx=0.2)

    def ID_label(self):
        print("ID called")
        temp = open('temp', 'r')
        Id = temp.readline()
        temp.close()
        return str(Id)

    def log_out(self):
        self.destroy = self.screenMain.destroy()

    def socialMedia(self):
        self.screen2 = Toplevel(self.screenMain)
        print("social media")
        self.screen2.iconphoto(False, tkinter.PhotoImage(file='icon temp/info.png'))
        self.screen2.title("Social Media")
        self.screen2.geometry("200x200")
        self.screen2.resizable(0, 0)

        def openURL(url):
            webbrowser.open(url)

        Label(self.screen2, text="My Social Media", background="#D4AF37",
              font=('comic sans ms', 12, 'bold', 'italic')).pack()
        Label(self.screen2, text="Follow me ya", background="#D4AF37",
              font=('comic sans ms', 12, 'bold', 'italic')).place(anchor='s', rely=0.8, relx=0.5)

        # FB
        fb_url = 'https://www.facebook.com/JENARALZEROZED?ref=bookmarks'
        fb_ico = ImageTk.PhotoImage(master=self.screen2, file='icon temp/fb.png', width=10, height=10)
        self.fb_button = Button(self.screen2, image=fb_ico, command=lambda url=fb_url: openURL(url))
        self.fb_button.image = fb_ico
        self.fb_button.place(anchor='e', relx=0.5, rely=0.3)

        # Insta
        insta_url = 'https://www.instagram.com/neko.helmii/'
        insta_ico = ImageTk.PhotoImage(master=self.screen2, file='icon temp/ig.png', width=10, height=10)
        self.insta_button = Button(self.screen2, image=insta_ico, command=lambda url=insta_url: openURL(url))
        self.insta_button.image = insta_ico
        self.insta_button.place(anchor='w', relx=0.5, rely=0.3)

        # Twitter
        twit_url = 'https://twitter.com/helmimiow'
        twit_ico = ImageTk.PhotoImage(master=self.screen2, file='icon temp/twitter.png', width=10, height=10)
        self.insta_button = Button(self.screen2, image=twit_ico, command=lambda url=twit_url: openURL(url))
        self.insta_button.image = twit_ico
        self.insta_button.place(anchor='w', relx=0.5, rely=0.5)

        # github
        git_url = 'https://github.com/zerozedsc'
        git_ico = ImageTk.PhotoImage(master=self.screen2, file='icon temp/GitHub.png', width=10, height=10)
        self.insta_button = Button(self.screen2, image=git_ico, command=lambda url=git_url: openURL(url))
        self.insta_button.image = git_ico
        self.insta_button.place(anchor='e', relx=0.5, rely=0.5)

    def news(self):
        print("news")

    def weather(self):
        print("weather")

    # prayerTime Button Function
    def azanTime(self):
        tkinter.messagebox.showinfo("WAKTU AZAN", "ONLY SHOW PRAYER TIME IN MALAYSIA")
        print("show azan time")
        self.azan_screen = Toplevel(self.screenMain)
        self.azan_screen.resizable(0, 0)
        self.azan_screen.geometry(f"500x500+{self.positionRight}+{self.positionDown}")
        self.azan_screen.title('WAKTU AZAN')
        self.azan_screen.iconphoto(False, tkinter.PhotoImage(file='icon temp/info.png'))
        style = Style()
        style.configure('Fun.TButton', font=('Comic sans ms', 10, 'bold'))
        self.style1 = 'Fun.TButton'


        # background
        bg_img = ImageTk.PhotoImage(master=self.azan_screen, file='API/azanWindow/al-quran.jpg')
        bg = Label(self.azan_screen, image=bg_img)
        bg.image = bg_img
        bg.place(x=0, y=0, relwidth=1, relheight=1)

        # state
        negeri = ['Kelantan', "Terengganu", "Sabah", "Sarawak", "Selangor", "Pahang", "Kedah", "Perlis", "Johor",
                  "Perak", "Pulau Pinang", "Wilayah Persekutuan", "Melaka", "Negeri Sembilan"]
        negeri.sort()

        # call district in state
        self.state_read = tk.StringVar()
        self.state_box = Combobox(self.azan_screen, values=negeri, font=('Calibri', 12, 'bold'),
                                  textvariable=self.state_read, state='readonly')
        self.state_box.place(relx=0.5, rely=0.05, anchor='center', width=135)
        self.state_box.bind('<<ComboboxSelected>>', self.district_box)
        Label(self.azan_screen, text='Negeri', font=('roboto', 12, 'bold', 'italic')).place(relx=0.26, rely=0.05,anchor='w')
        Button(self.azan_screen, text='exit', style=self.style1, command=self.azan_screen.destroy).place(relx=0.8,rely=0.93)

    def district_box(self, null):     # calling district_comboBox
        self.district_read = tk.StringVar()
        self.district_box = Combobox(self.azan_screen, textvariable=self.district_read, values=self.state(negeri=self.state_read.get()), font=('Calibri', 12, 'bold'))  # show value in district_comboBox
        self.district_box.place(relx=0.5, rely=0.15, anchor='center', width=135)
        self.district_box.bind('<<ComboboxSelected>>', self.showTime)
        Label(self.azan_screen, text='zon', font=('roboto', 12, 'bold', 'italic')).place(relx=0.3, rely=0.15,anchor='w')
        Button(self.azan_screen, text='?', command=self.helpAzan, style=self.style1).place(relx=0.65, rely=0.15, anchor='w', width=30)

    def showTime(self, null):
        self.adjustAzanTime(self.district_read.get())

    def helpAzan(self):
        self.helpAzanWin = Toplevel(self.screenMain)
        self.helpAzanWin.geometry(f"620x450")
        self.helpAzanWin.resizable(0,0)
        self.helpAzanWin.iconphoto(False, tkinter.PhotoImage(file='icon temp/info.png'))
        self.helpAzanWin.title("HELP")

        helpText = open('API/azanWindow/hint.txt', 'r')
        helpRead = helpText.read()

        # Label(self.helpAzanWin, text=helpRead).place(x=0, y=0, relwidth=1, relheight=1)
        scrollbar = Scrollbar(self.helpAzanWin)
        scrollbar.place(relx=0.95, height=400)
        self.outputArea = Text(self.helpAzanWin, height=26, width=100)
        self.outputArea.insert(END ,helpRead)
        self.outputArea.config(state='disabled', yscrollcommand=scrollbar.set)
        self.outputArea.place(x=0, y=0, relwidth=1, relheight=1)

    def state(self, negeri ='Wilayah Persekutuan') : # district value
        self.azan_screen.update()
        daerah = str(negeri).lower()
        district_list = ['empty']
        if daerah == 'wilayah persekutuan':
            district_list.remove('empty')
            wilayah = ['WLY01', 'WLY02']
            for i in wilayah:
                district_list.append(i)
        elif daerah == 'kelantan':
            district_list.remove('empty')
            kelantan = ['KTN01', 'KTN03']
            for i in kelantan:
                district_list.append(i)
        elif daerah == 'johor':
            district_list.remove('empty')
            johor = ['JHR01', 'JHR02', 'JHR03', 'JHR04']
            for i in johor:
                district_list.append(i)
        elif daerah == 'kedah':
            district_list.remove('empty')
            kedah = ['KDH01', 'KDH02', 'KDH03', 'KDH04', 'KDH05', 'KDH06', 'KDH07']
            for i in kedah:
                district_list.append(i)
        elif daerah == 'melaka':
            district_list.remove('empty')
            district_list.append('MLK01')
        elif daerah == 'negeri sembilan':
            district_list.remove('empty')
            nogori = ['NGS01', 'NGS02']
            for i in nogori:
                district_list.append(i)
        elif daerah == 'pahang':
            district_list.remove('empty')
            pahang = ['PHG01', 'PHG02', 'PHG03', 'PHG04', 'PHG05', 'PHG06']
            for i in pahang:
                district_list.append(i)
        elif daerah == 'perak':
            district_list.remove('empty')
            perak = ['PRK01', 'PRK02', 'PRK03', 'PRK04', 'PRK05', 'PRK06', 'PRK07']
            for i in perak:
                district_list.append(i)
        elif daerah == 'perlis':
            district_list.remove('empty')
            district_list.append('PLS01')
        elif daerah == 'pulau pinang':
            district_list.remove('empty')
            district_list.append('PNG01')
        elif daerah == 'sabah':
            district_list.remove('empty')
            sabah = ['SBH01', 'SBH02', 'SBH03', 'SBH04', 'SBH05', 'SBH06', 'SBH07', 'SBH08', 'SBH09']
            for i in sabah:
                district_list.append(i)
        elif daerah == 'sarawak':
            district_list.remove('empty')
            sarawak = ['SWK01', 'SWK02',  'SWK03', 'SWK04', 'SWK05', 'SWK06', 'SWK07', 'SWK08', 'SWK09']
            for i in sarawak:
                district_list.append(i)
        elif daerah == 'selangor':
            district_list.remove('empty')
            selangor = ['SGR01', 'SGR02', 'SGR03']
            for i in selangor:
                district_list.append(i)
        elif daerah == 'terengganu':
            district_list.remove('empty')
            terengganu = ['TRG01', 'TRG02', 'TRG03', 'TRG04']
            for i in terengganu:
                district_list.append(i)
        else:
            district_list.sort()

        return district_list

    def adjustAzanTime(self, zone='WLY01'):
        from API.azanWindow.azan_api import azanApi
        azanCall = azanApi(zone)
        imsak = azanCall.solatTime('imsak')
        subuh = azanCall.solatTime('subuh')
        syuruk = azanCall.solatTime('syuruk')
        zuhur = azanCall.solatTime('zuhur')
        asar = azanCall.solatTime('asar')
        maghrib = azanCall.solatTime('maghrib')
        isyak = azanCall.solatTime('isyak')
        self.showAzanTime(imsak, subuh, syuruk, zuhur, asar, maghrib, isyak)

    def showAzanTime(self, imsak='0:00 A.M', subuh='0:00 A.M', syuruk='0:00 A.M', zuhur='0:00 P.M', asar='0:00 P.M', maghrib='0:00 P.M', isyak='0:00 P.M'):
        Label(self.azan_screen, text='WAKTU AZAN', font=('Roboto', 18, 'bold', 'italic'), foreground='#FCC201', background='#A0B2C6').place(relx=0.345, rely=0.3)

        # imsak label
        Label(self.azan_screen, text='Imsak:', font=('Roboto', 18, 'bold', 'italic'), foreground='dark green', background='#A0B2C6').place(relx=0.1, rely=0.5, anchor='center')
        self.getImsak = Label(self.azan_screen, text=imsak, font=('NEC', 18), foreground='red', background='dark blue')
        self.getImsak.place(relx=0.32, rely=0.5, anchor='center')

        # subuh Label
        Label(self.azan_screen, text='Subuh:', font=('Roboto', 18, 'bold', 'italic'), foreground='dark green',
              background='#A0B2C6').place(relx=0.1, rely=0.6, anchor='center')
        self.getSubuh = Label(self.azan_screen, text=subuh, font=('NEC', 18), foreground='red',
                              background='dark blue')
        self.getSubuh.place(relx=0.32, rely=0.6, anchor='center')

        # Syuruk Label
        Label(self.azan_screen, text='Syuruk:', font=('Roboto', 18, 'bold', 'italic'), foreground='dark green',
              background='#A0B2C6').place(relx=0.1, rely=0.7, anchor='center')
        self.getSyuruk = Label(self.azan_screen, text=syuruk, font=('NEC', 18), foreground='red',
                              background='dark blue')
        self.getSyuruk.place(relx=0.32, rely=0.7, anchor='center')

        # Zuhur Label
        Label(self.azan_screen, text='Zuhur:', font=('Roboto', 18, 'bold', 'italic'), foreground='dark green',
              background='#A0B2C6').place(relx=0.1, rely=0.8, anchor='center')
        self.getZuhur = Label(self.azan_screen, text=zuhur, font=('NEC', 18), foreground='red',
                              background='dark blue')
        self.getZuhur.place(relx=0.32, rely=0.8, anchor='center')

        # Asar Label
        Label(self.azan_screen, text='Asar:', font=('Roboto', 18, 'bold', 'italic'), foreground='dark green',
              background='#A0B2C6').place(relx=0.6, rely=0.5, anchor='center')
        self.getAsar = Label(self.azan_screen, text=asar, font=('NEC', 18), foreground='red',
                              background='dark blue')
        self.getAsar.place(relx=0.8, rely=0.5, anchor='center')

        # Maghrib Label
        Label(self.azan_screen, text='Maghrib:', font=('Roboto', 18, 'bold', 'italic'), foreground='dark green',
              background='#A0B2C6').place(relx=0.56, rely=0.6, anchor='center')
        self.getMaghrib = Label(self.azan_screen, text=maghrib, font=('NEC', 18), foreground='red',
                             background='dark blue')
        self.getMaghrib.place(relx=0.8, rely=0.6, anchor='center')

        # Isyak Label
        Label(self.azan_screen, text='Isyak:', font=('Roboto', 18, 'bold', 'italic'), foreground='dark green',
              background='#A0B2C6').place(relx=0.6, rely=0.7, anchor='center')
        self.getIsyak = Label(self.azan_screen, text=isyak, font=('NEC', 18), foreground='red',
                             background='dark blue')
        self.getIsyak.place(relx=0.8, rely=0.7, anchor='center')

    # weather Button Function
    def weatherScreen(self):
        tkinter.messagebox.showinfo('WEATHER', 'THE CITIES IN MALAYSIA ONLY')
        self.weather = Toplevel(self.screenMain)
        self.weather.resizable(0,0)
        self.weather.geometry(f"450x400")
        self.weather.title('Weather')
        self.weather.iconphoto(False, tkinter.PhotoImage(file='icon temp/info.png'))

        style =Style()
        style.configure('W.TButton', font=('Comic sans ms', 8, 'normal', 'italic'), foreground='black')
        style1 = 'W.TButton'

        C = tk.Canvas(self.weather, height=400, width=450)
        background_image = tk.PhotoImage(master=self.weather,file='API/weatherWindow/background.png')
        background_label = tk.Label(self.weather, background='gold', image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        C.pack()

        frame = tk.Frame(self.weather, bg='blue', bd=5)
        frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
        # frame_window = C.create_window(100, 40, window=frame)

        self.textbox = tk.Entry(frame, font=('comic sans ms',12 , 'bold', 'italic'))
        self.textbox.place(relwidth=0.65, relheight=1)
        submit = tk.Button(frame, text='Get Weather', font=('comic sans ms', 10, 'italic'), command=self.getWeather)
        submit.place(relx=0.7, relheight=1, relwidth=0.3)

        lower_frame = tk.Frame(self.weather, bg='#42c2f4', bd=10)
        lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

        bg_color = 'white'
        self._results = tk.StringVar()
        self.results = tk.Label(lower_frame,text='Welcome to Weather App ',anchor='nw', justify='left', bd=4, textvariable=self._results)
        self.results.config(font=('good times rg',11, 'italic'), bg=bg_color)
        self.results.place(relwidth=1, relheight=1)

        weather_icon = tk.Canvas(self.results, bg=bg_color, bd=0, highlightthickness=0)
        weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

    def getWeather(self):
        from API.weatherWindow.weather_api import weather
        print("get weather")
        weather = weather(self.textbox.get())
        self._results.set(weather.format_response(weather.weather_json))

    # news Button Function
    def newsScreen(self):
        self.news = Toplevel(self.screenMain)
        self.news.geometry(f"650x650+{self.positionRight}+{self.positionDown}")
        self.news.title("News")
        self.news.resizable(0,0)
        self.news.iconphoto(False, tkinter.PhotoImage(file='icon temp/info.png'))

        #background
        background_image = tk.PhotoImage(master=self.news, file='API/newsWindow/news.png')
        background_label = tk.Label(self.news, background='gold', image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        frame = tk.Frame(self.news, bg='blue', bd=5)
        frame.place(relx=0.5, rely=0.08, relwidth=0.75, relheight=0.05, anchor='n')
        # frame_window = C.create_window(100, 40, window=frame)

        Label(self.news, text='TOP 5 NEWS', font=('impact', 25, 'bold'), foreground='grey', background='gold').pack()

        self.newsbox = tk.Entry(frame, font=('comic sans ms', 12, 'bold', 'italic'))
        self.newsbox.place(relwidth=0.65, relheight=1)
        submit = tk.Button(frame, text='Search', font=('comic sans ms', 10, 'italic'), command=self.getNews)
        submit.place(relx=0.7, relheight=1, relwidth=0.3)
        Button(self.news, text='Exit', command=self.news.destroy).place(relx=0.86, rely=0.95)

    def getNews(self):
        from API.newsWindow.news_api import news
        news = news(self.newsbox.get())
        self.news1 = Label(self.news, text=news.news1(), font=('roboto', 12, 'bold'), background='#C7C6C1')
        self.news1.place(relx=0, rely=0.16)

        self.news2 = Label(self.news, text=news.news2(), font=('roboto', 12, 'bold'), background='#C7C6C1')
        self.news2.place(relx=0, rely=0.3)

        self.news3 = Label(self.news, text=news.news3(), font=('robot', 12, 'bold'), background='#C7C6C1')
        self.news3.place(relx=0., rely=0.44)

        self.news4 = Label(self.news, text=news.news4(), font=('roboto', 12, 'bold'), background='#C7C6C1')
        self.news4.place(relx=0, rely=0.6)

        self.news5 = Label(self.news, text=news.news5(), font=('robot', 12, 'bold'), background='#C7C6C1')
        self.news5.place(relx=0., rely=0.74)



