import pandas as pd
import elevenlabs
import speech_recognition as sr
from tkinter import *
from PIL import Image, ImageTk

elevenlabs.set_api_key("3c0661f85eb009878971e0f40c128366")

def speech_to_text():
  recognizer = sr.Recognizer()
  with sr.Microphone() as source:
    print("Speak something...")
    recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
    #listening the voice
    audio = recognizer.listen(source)

  try:
    #recognizing speech
    print("Recognizing speech...")
    text = recognizer.recognize_google(audio, language='ta-IN')
    print("You said:", text)
    #Passing the output as Argument
    searching(text)
    return text
  #couldn't listen properly then show them an msg
  except sr.UnknownValueError:
    print("Sorry, could not understand audio.")
    return None
  except sr.RequestError as e:
    print("Error occurred; {0}".format(e))
    return None


def searching(text):
  #Reading File
  df = pd.read_csv("D:\pythonFlask\Thirukural\Thirukural.csv")

  #Slicing Kural from Dataframe
  verses = df['Verse']

  #Dictionary to store first word of every Kural
  first_dict = {}
  for i in range(len(verses)):

    #Variable to store the first word
    word = ''
    for j in range(len(verses.iloc[i])):

      #Each word in Kural is separated by /t so we use that as delimiter
      if verses.iloc[i][j] == '\t':
        #Storing the index and the first word of Kural
        first_dict[i] = word
        break

      else:
        #Taking the word character by character
        word = word + verses.iloc[i][j]
  kural_dict= {}

  #Searching which word mactches with the speech recognized text  
  for i in range(len(first_dict)):
    if text == first_dict[i]:
      #Kural found at index i

      #use dict to separate the line for kural
      new_x = []

      kural = str(verses.iloc[i])

      x = kural.split('\t\t\t')
      line1 = str(x[0])
      line2 = str(x[1])
      line1 = line1.replace('\t', ' ')
      line2 = line2.replace('\t', ' ')
      new_x.append(line1)
      new_x.append(line2)
      kural_dict[0] = new_x
      print(kural_dict[0][0],"\n",kural_dict[0][1])

      display(kural_dict[0][0], kural_dict[0][1])
      text_to_speech(verses.iloc[i])


def text_to_speech(TamilText):
  audio = elevenlabs.generate(
    text=TamilText,
    voice="Thomas",
    model='eleven_multilingual_v2'
    )
  elevenlabs.play(audio)

def display(TamilText, tamil):
  l1 = Label(root, text=TamilText).place(x= 180,y=100 )
  l2 = Label(root, text=tamil).place(x= 180,y=120 )
  root.after(3000, lambda: (l1.__format__, l2.__format__))
# create root window
root = Tk()

# root window title and dimension 
root.title("Thirukkural App")
root.geometry("450x400")
 
# Open image path
image = Image.open("D:\pythonFlask\Thirukural\mic.jpg") 

image = image.resize((50, 50))  # resize image
photo = ImageTk.PhotoImage(image)

image2 = Image.open("D:\pythonFlask\Thirukural\Thiruvalluvar.jpg")
image2 = image2.resize((150,200))
photo2 = ImageTk.PhotoImage(image2)

image3 = ImageTk.PhotoImage(Image.open("D:\pythonFlask\Thirukural\TiruBG.jpg"))
label = Label(root, image = image3).place(x=0,y=0)
# creating button
wlecome = Label(root, text = "Speech Recoginition").place(x=150,y=10)
btn = Button(root, image=photo, command = speech_to_text).place(x=200,y=240)
#thiruvalluvar image
Label(root, image=photo2).place(x=10,y=100)
# running the main loop
root.resizable(0,0)
root.mainloop()

