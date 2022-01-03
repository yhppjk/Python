from tkinter import *
from PIL import Image,ImageTk
from queue import Queue


def img_open(shape, path):
    img = Image.open(path)
    img = img.resize((shape[0] - 5, shape[1]), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    return img

class frame1(object):
    def __init__(self, window, shape, locate, name, color, checked_num):
        self.tw_window = Frame(window, width=shape[0], height=shape[1],
                                bg=color)
        self.tw_window.place(x=locate[0], y=locate[1], anchor=NW)
        self.tw_window.propagate(0)

        self.label = Label(self.tw_window,
#                     text=name,
                    text=str(name+str("checked_num:%d" % checked_num)),
                    fg='red')
        self.label.place(x=int(shape[0]/2), y=int(shape[1]/2))

class TabWidgetFrame(object):
    def __init__(self):
        self.checked = False

class TabWidgetButton(object):
    def __init__(self, window, shape, locate, name):
        self.img_0 = img_open((shape[0], shape[1]), "img/button_label_0.png")
        self.img_1 = img_open((shape[0], shape[1]), "img/button_label_1.png")
        self.tw_button = Label(window, width=shape[0], height=shape[1],
                                image=self.img_1,
                                padx = 0, pady = 0,
                                text=name, fg='red', compound=CENTER)
        self.tw_button.grid(row=locate[0], column=locate[1])
        self.tw_button.propagate(0)

        self.checked = False

class WindowFrame(object):
    def __init__(self, window, shape, locate, window_list):
        self.num = len(window_list)
        self.checked_num = 0
        self.window_list = window_list

        for i in range(self.num-1,-1,-1):
            tw_window = frame1(window, shape, locate,
                                    self.window_list[i].name,
                                    self.window_list[i].color,
                                    self.checked_num)
            self.window_list[i].frame = tw_window


class ButtonFrame(object):
    def __init__(self, window, shape, locate, color, window_list):
        self.num = len(window_list)
        self.checked_num = 0

        button_shape = (int(shape[0]/self.num), shape[1])

        wnd = Frame(window, width=shape[0], height=shape[1], bg=color)
        wnd.place(x=locate[0], y=locate[1])
        wnd.propagate(0)

        self.tw_button_list = []
        for i in range(self.num):
            locate = (0, i)
            tw_button = TabWidgetButton(wnd, button_shape , locate, window_list[i].name)
            tw_button.tw_button.bind("<Button-1>",lambda event, n=i:
                                                self.button_label_func(event, n))
            if i == self.checked_num:
                tw_button.checked = True
                tw_button.tw_button.config(image=tw_button.img_0)
                tw_button.tw_button.image = tw_button.img_0
            self.tw_button_list.append(tw_button)

    def button_label_func(self, event, n):
        print("%d -- status%d" % (n, self.tw_button_list[n].checked), event)
        if self.tw_button_list[n].checked:
            print("alreddy checked")
            pass
        else:
            for i in range(self.num):
                if i == n:
                    self.tw_button_list[i].checked = True
                    self.tw_button_list[i].tw_button.config(image=self.tw_button_list[i].img_0)
                    self.tw_button_list[i].tw_button.image = self.tw_button_list[i].img_0
                else:
                    self.tw_button_list[i].checked = False
                    self.tw_button_list[i].tw_button.config(image=self.tw_button_list[i].img_1)
                    self.tw_button_list[i].tw_button.image = self.tw_button_list[i].img_1
        self.checked_num = n
        return self.checked_num


class TabWidget(object):
    def __init__(self, window, shape, window_list):
        self.num = len(window_list)
        self.window = window
        self.shape = shape
        self.window_list = window_list

        button_frame_shape = (shape[0], 30)
        self.window_frame_shape = (shape[0], shape[1] - button_frame_shape[1])
        button_frame_locate = (0, 0)
        self.window_frame_locate = (0, button_frame_shape[1])

        self.button_frame = ButtonFrame(window, button_frame_shape,
                                    button_frame_locate, 'blue',
                                    window_list)

        self.window_frame = WindowFrame(window, self.window_frame_shape,
                                    self.window_frame_locate,
                                    self.window_list)
    def tw_update(self):
        self.window_frame.checked_num = self.button_frame.checked_num
        for i in range(self.num):
            if i == self.window_frame.checked_num:
                if self.latest_checked_num != self.window_frame.checked_num:
                    self.latest_checked_num = self.window_frame.checked_num
                    self.window_frame.window_list[i].frame = frame1(self.window,
                                        self.window_frame_shape,
                                        self.window_frame_locate,
                                        self.window_list[i].name,
                                        self.window_list[i].color,
                                        self.window_frame.checked_num)
                    self.window_frame.window_list[i].checked = True
            else:
                self.window_frame.window_list[i].checked = False
                self.window_frame.window_list[i].frame.tw_window.destroy()
        self.window_list = self.window_frame.window_list

class WindowType(object):
    def __init__(self):
        self.name = ''
        self.color = ''
        self.frame = None
        self.checked = False

class Tkinter(object):
        #definition of top-level window
    def __init__(self, shape):
        self.wnd = Tk()
        self.wnd.title("attribute interface")
        self.wnd.geometry(str(str(shape[0])+'x'+str(shape[1])))
        self.wnd.resizable(width=False,height=False)

        window_list = []
        window = WindowType()
        window.name = 'wangxy'
        window.color = 'blue'
        window.frame = None
        window_list.append(window)

        window = WindowType()
        window.name = 'shidanfang'
        window.color = 'red'
        window.frame = None
        window_list.append(window)

        window = WindowType()
        window.name = 'wangyifei'
        window.color = 'yellow'
        window.frame = None
        window_list.append(window)

        window = WindowType()
        window.name = 'zhangww'
        window.color = 'green'
        window.frame = None
        window_list.append(window)

        self.tabwidget = TabWidget(self.wnd, shape, window_list)

    def tk_update(self):
        self.tabwidget.tw_update()
        self.wnd.update()


def main():
    tk_root = Tkinter((800,600))

    while True:
        tk_root.tk_update()

    tk_root.wnd.mainloop()



if __name__ == "__main__":
    main()
