from tkinter import filedialog
from tkinter import messagebox
import moviepy.editor
from tkinter import *

root = Tk() # app constructor
root.title("Video Editor") #title
root.geometry("400x600")
root.configure(bg='#856ff8')

sLabel = Label(root,text="Select the Video you want to edit") #first label
sLabel.pack()

def browse():
    global vPath
    vPath = filedialog.askopenfilename() #browse file path
    vLabel = Label(root, text=vPath,bg="cyan", width= 40) #print video path
    vLabel.pack()
lButton = Button(root, text="Browse...", command=browse) #browsing button to activate browse function
lButton.pack()

#video to audio function

def toAudio():
    sVideo = moviepy.editor.VideoFileClip(vPath) #start editing video
    sAudio = sVideo.audio #change to audio
    newPath = vPath.split(".") #split the video extension from the video name
    newPath = newPath[0] #take path without the extension
    sAudio.write_audiofile(rf"{newPath}.mp3") #create the audio file in the same path as the video
    messagebox.showinfo("Finished","Changed file to mp3 audio file") #message box

    #video to Gif function
def toGIF():
        sVideo = moviepy.editor.VideoFileClip(vPath)
        newPath = vPath.split(".")
        newPath = newPath[0]
        sVideo.write_audiofile(rf"{newPath}.mp3") #create the audio file in the same path as the video
        messagebox.showinfo("Finished","Changed file to mp3 audio file") #message box

lButton = Button(root, text="Convert to Audio", command=toAudio) #button to apply te toAudio function
lButton.pack()

lButton = Button(root, text="Convert to GIF", command=toGIF) #button to apply te toAudio function
lButton.pack()

root.mainloop()

