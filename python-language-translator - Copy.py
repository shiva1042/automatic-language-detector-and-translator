from tkinter import *
from tkinter import ttk
from winsound import PlaySound
from googletrans import Translator , LANGUAGES
import speech_recognition as sr
from gtts import gTTS
import os

root = Tk()
root.geometry('1080x400')
root.resizable(0,0)
root.title("Language Translator")
root.config(bg = 'yellow')



dic=('kannada','kn','telugu','te','hindi','hi','english','en')
  



#heading
Label(root, text = "Audio Mediator", font = "arial 20 bold", bg='blue').pack()
#Label(root,text ="iiitA", font = 'arial 20 bold', bg ='blue' , width = '20').pack(side = 'bottom')



#INPUT AND OUTPUT TEXT WIDGET
#Label(root,text ="Input text", font = 'arial 13 bold', bg ='white smoke').place(x=200,y=60)
Input_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady=5, width = 60)
Input_text.place(x=30,y = 100)


#Label(root,text ="Output text", font = 'arial 13 bold', bg ='white smoke').place(x=780,y=60)
Output_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady= 5, width =60)
Output_text.place(x = 600 , y = 100)
 


##################
"""
language = list({'kannada','telugu','hindi','english'})

src_lang = ttk.Combobox(root, values= language, width =22)
src_lang.place(x=20,y=60)
src_lang.set('choose input language')

dest_lang = ttk.Combobox(root, values= language, width =22)
dest_lang.place(x=890,y=60)
dest_lang.set('choose output language')
"""
########################################  Define function #######

def Record():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Talk")
        r.adjust_for_ambient_noise(source) #reduce noise
        audio_text = r.listen(source)
        print("Time over, thanks")
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    
    try:
        # using google speech recognition
        text = r.recognize_google(audio_text)
        return text
    except:
         print("Sorry, I did not get that")

###################

def detect():
    trans=Translator()
    stext=Record()
    ulang=trans.translate(text=stext)
    return ulang.src
       
#####################
u_1_lang=""
u_2_lang=""
def u_1_detect():
    global u_1_lang
    u_1_lang+=detect()
    print(u_1_lang)
def u_2_detect():
    global u_2_lang
    u_2_lang+=detect()
    print(u_2_lang)

##########################

def c_trans(s,d):
    translator = Translator()
    stext = Record()
    stranslate=translator.translate(text= stext,src=s,dest=d)
    return stranslate.text


########################
def u_1_trans():
    trans_text=c_trans(u_1_lang,u_2_lang)
    Output_text.delete(1.0, END)
    Output_text.insert(END, trans_text)
    #text=translated.text
    
    speak = gTTS(text=trans_text, lang=u_2_lang, slow= False)
 
            # Using save() method to save the translated
            # speech in capture_voice.mp3
    speak.save("captured_voice.mp3")    
             
            # Using OS module to run the translated voice.
    os.system("start captured_voice.mp3")

######################################################
def u_2_trans():
    trans_text=c_trans(u_2_lang,u_1_lang)
    Input_text.delete(1.0, END)
    Input_text.insert(END, trans_text)
    #text=translated.text
    
    speak = gTTS(text=trans_text, lang=u_1_lang, slow= False)
 
            # Using save() method to save the translated
            # speech in capture_voice.mp3
    speak.save("captured_voice.mp3")    
             
            # Using OS module to run the translated voice.
    os.system("start captured_voice.mp3")


###########################################################

def Translate():
    translator = Translator()
    stext = Record()
    stranslate=translator.translate(text= stext)
    translated=translator.translate(text= stext ,  dest = dest_lang.get())
    Input_text.delete(1.0, END)
    Input_text.insert(END, stranslate.src)
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)
    text=translated.text
    to_lang=dic[dic.index(dest_lang.get())+1]
    speak = gTTS(text=text, lang=to_lang, slow= False)
 
            # Using save() method to save the translated
            # speech in capture_voice.mp3
    speak.save("captured_voice.mp3")    
             
            # Using OS module to run the translated voice.
    os.system("start captured_voice.mp3")
   #PlaySound('captured_voice.mp3')   
#######################################


#################################


##########
user1_btn = Button(root, text = 'user-1 detect',font = 'arial 12 bold',pady = 5,command = u_1_detect , bg = 'royal blue1', activebackground = 'sky blue')
user1_btn.place(x = 20, y = 60)

user2_btn = Button(root, text = 'user-2 detect',font = 'arial 12 bold',pady = 5,command = u_2_detect , bg = 'royal blue1', activebackground = 'sky blue')
user2_btn.place(x = 600, y = 60)

#################
trans_btn = Button(root, text = 'user_1_translate',font = 'arial 12 bold',pady = 5,command = u_1_trans , bg = 'royal blue1', activebackground = 'sky blue')
trans_btn.place(x = 160, y = 60)


trans_btn = Button(root, text = 'user_2_translate',font = 'arial 12 bold',pady = 5,command = u_2_trans , bg = 'royal blue1', activebackground = 'sky blue')
trans_btn.place(x = 750, y = 60)
##########  Translate Button ########
#record_btn = Button(root, text = 'record',font = 'arial 12 bold',pady = 5,command = Record , bg = 'royal blue1', activebackground = 'sky blue')
#record_btn.place(x=250, y=100)
"""""
trans_btn = Button(root, text = 'Translate',font = 'arial 12 bold',pady = 5,command = Translate , bg = 'royal blue1', activebackground = 'sky blue')
trans_btn.place(x = 490, y = 180)
"""""

root.mainloop()

