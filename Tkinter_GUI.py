import tkinter as tk
import ctypes

#直接実行かの判定
if __name__ == "__main__":
    #解像度調整
    ctypes.windll.shcore.SetProcessDpiAwareness(1)

    root = tk.Tk()
    root.title("Tkinter_GUI")
    root.geometry("800x600") #ウィンドウサイズ
    
    all_title = tk.Label(root, text="Tkinterのウィジェットの使い方例", font=(24))
    all_title.pack(pady=(0, 20))
    label_title = tk.Label(root, text="<Label>")
    label_title.pack()
    
    #Label(文字列, 画像等の表示)
    label1 = tk.Label(root, text="lebelによる文字列")
    label1.pack()
    label2 = tk.Label(root, text="縁どり", relief="ridge")
    label2.pack()
    label3 = tk.Label(root, text="色の変更", fg="red", bg="cyan")
    label3.pack(pady=(0, 20))
    
    button_title = tk.Label(root, text="<Button>")
    button_title.pack()
    
    #Button(ボタンの表示)
    button1 = tk.Button(root, text="色変更",bg="green", command=None)
    button1.pack()
    button2 = tk.Button(root, text="大きさ変更", width=15, bg="pink", command=None)
    button2.pack()
    button3 = tk.Button(root, text="縁どり", width=15, fg="white", bg="blue", relief="solid", command=None)
    button3.pack(pady=(0, 20))
    
    frame_title = tk.Label(root, text="<Frame>")
    frame_title.pack()
    
    #Frame(一連のまとまり. ここではlabelとentryをまとめている)
    frame = tk.Frame(root, relief="ridge", bd=3, padx=5, pady=5)
    label = tk.Label(frame, relief="groove", width=15, bg="lightblue", text="下のbuttonとセット")
    label.pack()
    f_button = tk.Button(frame, width=15, text="button")
    f_button.pack()
    frame.pack(pady=(0, 20))
    
    entry_title = tk.Label(root, text="<Entry>")
    entry_title.pack()
    
    #entry
    
    root.mainloop()