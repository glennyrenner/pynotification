from tkinter import Tk, Label, PhotoImage

class Notification:
    deltatime = 5
    frames = 1
    chars_per_line = 30

    def __init__(self, text, image=None, time=1):
        '''
        Parameters:
        text: Text to print out
        image: Optional, image to show
        time: default = 1 second, time till fade
        '''
        self.text = text
        self.image = image
        self._time = time*1000
        self.target_frames = self._time/self.deltatime
        
    def Show(self):
        self.root = Tk()
        x = self.root.winfo_screenwidth() - 340
        y = self.root.winfo_screenheight() - 170
        self.root.geometry("320x100+{}+{}".format(x, y))
        self.root.attributes("-alpha", .9)
        self.root.attributes("-topmost", 1)
        self.root.config(bg='black')
        self.root.overrideredirect(True)
        self.root.after(self._time, self._animate)

        if self.image != None:
            self.img = PhotoImage(file=self.image)
            self.icon = Label(image=self.img, bg='black')
            self.icon.pack(side='left', padx=5, pady=6)

        self.label = Label(self.root, text=self.text, font="Calibri 14", bg='black', fg='white', justify='left')
        self.label.pack(side='left', padx= 5, pady=6, fill='both')

        self.root.mainloop()

    def _animate(self):
        if self.frames == self.target_frames:
            self.root.destroy()
            self.root.quit()
            return
        dy = self.root.winfo_y() - 1
        self.root.geometry("+{}+{}".format(self.root.winfo_x(), dy))
        alpha = .9 / self.frames 
        self.root.attributes("-alpha", alpha)
        self.frames += 1
        self.root.after(self.deltatime, self._animate)
