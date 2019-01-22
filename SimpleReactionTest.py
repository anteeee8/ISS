import random, time
from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master=master
        self.init_window()

    def init_window(self):
        global counter #number of turns
        n=5
        self.pack(fill=BOTH, expand=1)
        self.ready_button = Button(self, text="Ready!", command=self.ready) #initialize the ready button
        self.ready_button.place(relx=0.5, rely=0.5, anchor=CENTER)    #place the ready button
        self.ready_button.config(height=9, width=27, bg="green", fg="white", font=('Arial', 30))   #configure the ready button
        root.bind('<Return>', self.ready)   #calling the func with the return key
        counter+=1  #increase number of turns by 1
        if counter>n :    #if number of turns exceeds n
            self.ready_button.destroy()  # delete the ready button
            self.end_button = Button(self, text=f"Total time = {total_time*1000:.0f} ms", bg="blue", fg="yellow", height=9, width=27, font=('Arial', 30), command=self.end)    #initialize and configure the end button
            self.end_button.place(relx=0.5, rely=0.5, anchor=CENTER) #place the end button
            root.bind('<Return>', self.end)  # calling the func with the return key

    def end(self, key): #key because the bind func passes the return key as an argument
        root.quit()

    def ready(self, key):   #key because the bind func passes the return key as an argument
        self.ready_button.destroy() #delete the ready button
        time.sleep(random.randint(1, 5))    #wait between 1 and 5 seconds
        self.react_button = Button(self, text="React!", command=self.react) #initialize the react button
        self.react_button.place(relx=0.5, rely=0.5, anchor=CENTER)    #place the react button
        self.react_button.config(height=9, width=27, bg="orange", fg="purple", font=('Arial', 30))  #configure the react button
        root.bind('<Return>', self.react)  # calling the func with the return key
        self.start_time=time.time() #start the timer

    def react(self, key):   #key because the bind func passes the return key as an argument
        global total_time   #total accumulated time
        turn_time=time.time()-self.start_time   #time it took to react
        total_time+=turn_time   #update the total time
        self.react_button.destroy()  # delete the react button
        self.init_window()  #go again

counter=0
total_time=0
root = Tk()
root.geometry("800x600")
root.title("Simple reaction test")
app = Window(root)
root.mainloop()
