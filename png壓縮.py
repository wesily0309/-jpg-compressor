#import mod
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import json
import time
#--------------------

#轉換日誌紀錄
'''
class file:           #檔案名稱傳入
    def __init__(self,fname):
        self.fname=fname#檔案名稱
    
    def time():
        pass#規劃中(time模組使用)
    
    def rjson(self):#json讀取 
        print(self.fname)
        with open(self.fname,mode="r") as file:
            data=json.load(file)
        return data
    
    def add_record(self):
        #規劃中(json寫入)
        pass
'''


    #選擇匯入檔按
def open_folder():
    global openfile
    openfile=filedialog.askopenfilename()   # 選擇檔案後回傳檔案路徑與名稱
    print(openfile)   
    #
    #選擇匯出資料夾
def out_folder():
    global outfile
    outfile=filedialog.askdirectory()
    print(outfile)

win=tk.Tk()#建立實體物鍵win (啟用視窗)
win.title("圖片壓所器")#標題
win.geometry('300x150')
#設定大小

    #壓縮
def rar():
    global outfile
    outfile=outfile+"\\outimg.jpg"
    img = Image.open(openfile)
    #img.save("outimg",quality=65, subsampling=0)
    img.save(outfile,quality=65, subsampling=0) #原本想這樣   


#按紐選擇圖片
btn=tk.Button(win,text="選擇圖片",width=6,height=2,command=open_folder)
btn.config(bg="skyblue")
btn.pack()

#按紐選擇輸出地
btn2=tk.Button(win,text="選擇輸出地",width=6,height=2,command=out_folder)
btn2.config(bg="skyblue")
btn2.pack()

#按紐
btn3=tk.Button(win,text="壓縮",command=rar)        
btn3.config(bg="skyblue")
btn3.pack()

win.mainloop()#常駐視窗
#要怎麼同時指定路就和檔名 指定路徑沒有指定檔名會錯誤(存檔路徑是filedialog.askdirectory()抓的