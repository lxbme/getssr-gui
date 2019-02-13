from tkinter import *
from getssr import *
from getssrfunc import *

root = Tk()
root.title('SSR Getter')
try:
    root.iconbitmap('import.ico')
except:
    pass
pk = Frame(root)
pk.pack(side=TOP,padx=30,pady=25)

welable = Label(pk, text='===SSR自动获取===\n作者：lixiaobai\n源：http://ssr.wangzhan.gq/')
welable.pack(side=TOP)

but = Button(pk,text='立即获取ssr',command=main)
but.pack(pady=5)

mainloop()
