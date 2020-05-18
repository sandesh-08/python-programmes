import tkinter
import cv2
import PIL.Image,PIL.ImageTk
from functools import partial
import threading
import time
import imutils
stream=cv2.VideoCapture("clip.mp4")
flag=True
def play(speed):
    print(f"You clicked on play Speed is {speed}")
    global flag

  # Play the video inreverse mode
    frame1=stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1+speed)

    grabbed,frame=stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(134,26,fill="black",font="Times 26 bold",text="Decision Pending")
        flag=not flag





def pending(decision):
    # 1.Display decision pending image
    frame=cv2.cvtColor(cv2.imread("pending.png"),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame= PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    #2.sleep for 1 seconds
    time.sleep(1.5)
    #3.display sponser image
    frame = cv2.cvtColor(cv2.imread("lords2.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    #wait for 1.5 second
    time.sleep(2.5)
    #Display Not out\out image
    if decision=='out':
        decisionImg="out.png"
    else:
        decisionImg="not_out.png"
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

def out():
    thred=threading.Thread(target=pending,args=("out",))
    thred.daemon=1
    thred.start()
    print("Player is Out")
def not_out():
    thred = threading.Thread(target=pending, args=("not out",))
    thred.daemon = 1
    thred.start()
    print("Player is not out")
#width and height of our main screen
SET_WIDTH=650
SET_HEIGHT=368

#tkinter gui starts here
window=tkinter.Tk()
window.title("Abhay third umpire review system kit")
cv_image=cv2.cvtColor(cv2.imread("lords3.png"),cv2.COLOR_BGR2RGB)
canvas=tkinter.Canvas(window,width=SET_WIDTH,height=SET_HEIGHT)
photo=PIL.ImageTk.PhotoImage(image= PIL.Image.fromarray(cv_image))
image_on_canvas=canvas.create_image(0,0,ancho=tkinter.NW,image=photo)
canvas.pack()

#Buttons to control Playback
btn=tkinter.Button(window,text="<<Privous(Fast)",width=50 ,command=partial(play,-25))
btn.pack()
btn=tkinter.Button(window,text="<<Privous(slow)",width=50,command=partial(play,-2))
btn.pack()
btn=tkinter.Button(window,text="Next(Fast)>>",width=50,command=partial(play,25))
btn.pack()
btn=tkinter.Button(window,text="Next(slow)>>",width=50,command=partial(play,2))
btn.pack()
btn=tkinter.Button(window,text="Give Out",width=50,command=out)
btn.pack()
btn=tkinter.Button(window,text="Give Not Out",width=50,command=not_out)
btn.pack()




window.mainloop()