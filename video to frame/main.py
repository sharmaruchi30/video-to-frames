from curses import window
from tkinter import *
from tkinter import filedialog
import cv2
from PIL import Image
import os
import random
import webbrowser

def get_vid_path ():
    window.filename = filedialog.askopenfilename(initialdir="" , title="Select Video" , filetypes=(("mp4 files" , "*.mp4"),("mkv files","*.mkv"),("avi files","*.avi"),("wmv files","*.wmv"),("mpeg4 files","*.mpeg4"),("all files","*.*")))
    path_ = window.filename
    sel_vid_entry.delete(0,END)
    sel_vid_entry.insert(0,path_)

def get_save_path ():
    window.filename = filedialog.askdirectory()
    path_ = window.filename
    save_vid_entry.delete(0,END)
    save_vid_entry.insert(0,path_)

def convert_to_frames():
    count = 0
    cap = cv2.VideoCapture(sel_vid_entry.get())
    success,image =cap.read()

    print(success)

    while(success):
        success , image = cap.read()

        if not success:
            break

        cv2.imwrite(os.path.join(save_vid_entry.get() , str(count)+'.jpg') , image)

        if cv2.waitKey(10) == 27:
            break
        count+=1
    
    r_img = str(random.randint(0,count))
    
    im = Image.open(save_vid_entry.get() + "\\"+r_img +'.jpg') 
    im.show() 
    
    webbrowser.open(save_vid_entry.get()) 

    save_vid_entry.delete(0,END)
    sel_vid_entry.delete(0,END)


### GUI 
window = Tk()
window.title("Video to Frames")
window.geometry("400x300")
txthead = Label(window,text = "Convert Video to Frames",font =("calibre" , 15 , "normal") )
txthead.place(x = 100, y = 10)

sel_vid_path = Label(window, text="Video Path:" )
sel_vid_path.place(x = 30 , y = 80)

sel_vid_btn = Button(window, text="Open" ,command=get_vid_path)
sel_vid_btn.place(x = 350 , y = 80)

sel_vid_entry = Entry(window, width= 30)
sel_vid_entry.place(x = 150 , y = 80)

save_vid_path = Label(window, text="Saved Frame Path:" )
save_vid_path.place(x = 30 , y = 120)

save_vid_btn = Button(window, text="Open" ,command=get_save_path)
save_vid_btn.place(x = 350 , y = 120)

save_vid_entry = Entry(window, width= 30)
save_vid_entry.place(x = 150 , y = 120)

conv = Button (window , text= "CONVERT", command=convert_to_frames)
conv.place(x = 160 , y = 200)
window.mainloop()
