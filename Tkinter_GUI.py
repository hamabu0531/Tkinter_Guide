import tkinter as tk
import ctypes

# 直接実行かの判定
if __name__ == "__main__":
    # 解像度調整
    ctypes.windll.shcore.SetProcessDpiAwareness(1)

    root = tk.Tk()
    root.title("Tkinter_GUI")
    root.geometry("800x600")  # ウィンドウサイズ

    # Canvasを作成し、その上にFrameを配置する
    canvas = tk.Canvas(root)
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    all_title = tk.Label(scrollable_frame, text="Tkinterのウィジェットの使い方例", font=(24))
    all_title.pack(pady=(0, 20))

    label_title = tk.Label(scrollable_frame, text="<Label>")
    label_title.pack()

    # Label(文字列, 画像等の表示)
    label1 = tk.Label(scrollable_frame, text="labelによる文字列")
    label1.pack()
    label2 = tk.Label(scrollable_frame, text="縁どり", relief="ridge")
    label2.pack()
    label3 = tk.Label(scrollable_frame, text="色の変更", fg="red", bg="cyan")
    label3.pack(pady=(0, 20))

    button_title = tk.Label(scrollable_frame, text="<Button>")
    button_title.pack()

    # Button(ボタンの表示)
    button1 = tk.Button(scrollable_frame, text="色変更", bg="green", command=None)
    button1.pack()
    button2 = tk.Button(scrollable_frame, text="大きさ変更", width=15, bg="pink", command=None)
    button2.pack()
    button3 = tk.Button(scrollable_frame, text="縁どり", width=15, fg="white", bg="blue", relief="solid", command=None)
    button3.pack(pady=(0, 20))

    frame_title = tk.Label(scrollable_frame, text="<Frame>")
    frame_title.pack()

    # Frame(一連のまとまり. ここではlabelとentryをまとめている)
    frame = tk.Frame(scrollable_frame, relief="ridge", bd=3, padx=5, pady=5)
    label = tk.Label(frame, relief="groove", width=15, bg="lightblue", text="下のbuttonとセット")
    label.pack()
    f_button = tk.Button(frame, width=15, text="button")
    f_button.pack()
    frame.pack(pady=(0, 20))

    entry_title = tk.Label(scrollable_frame, text="<Entry>")
    entry_title.pack()

    # entry(文字の入力欄)
    entry1 = tk.Entry(scrollable_frame)
    entry1.pack()

    # こんなこともできる
    var = tk.StringVar(scrollable_frame)
    entry_label = tk.Label(scrollable_frame, width=15, bg="pink", textvariable=var)
    entry_label.pack()
    entry2 = tk.Entry(scrollable_frame, textvariable=var)
    entry2.pack(pady=(0, 20))

    spinbox_title = tk.Label(scrollable_frame, text="<Spinbox>")
    spinbox_title.pack()

    # spinbox(値の増減に使える)
    spinbox1 = tk.Spinbox(scrollable_frame, from_=-5, to=5, increment=1, state="readonly", width=15)
    spinbox1.pack()
    spinbox2 = tk.Spinbox(scrollable_frame, from_=-10, to=10, increment=2, state="normal", width=15)
    spinbox2.pack(pady=(0, 20))

    toplevel_title = tk.Label(scrollable_frame, text="<Toplevel>\nサブウィンドウを見てね")
    toplevel_title.pack()

    # Toplevel(サブウィンドウの表示に使える)
    toplevel1 = tk.Toplevel(scrollable_frame)
    toplevel1.title("sub")
    sub_label = tk.Label(toplevel1, text="これはToplevelによって作られたサブウィンドウ")
    sub_label.pack(pady=(0, 20))

    listbox_label = tk.Label(scrollable_frame, text="<Listbox>")
    listbox_label.pack()

    def get_selected(event):
        n = listbox1.curselection()
        list_label["text"] = values[n[0]]
    items = {"English": "Hello",
             "中文": "你好",
             "한국어": "안녕하세요",
             "日本語": "こんにちは"}
    values = list(items.values())

    # Listbox(一覧表示)
    list_label = tk.Label(scrollable_frame, text="select item", width=15, bg="yellow")
    list_label.pack()
    listbox1 = tk.Listbox(scrollable_frame)
    for item in items.keys():
        listbox1.insert(tk.END, item)
    listbox1.bind("<<ListboxSelect>>", get_selected)
    listbox1.pack(pady=(0, 20))

    checkbutton_label = tk.Label(scrollable_frame, text="<Checkbutton>")
    checkbutton_label.pack()

    # Checkbutton(on.offできるボタン)
    checkbutton1 = tk.Checkbutton(scrollable_frame, text="check1")
    checkbutton2 = tk.Checkbutton(scrollable_frame, text="check2")
    checkbutton3 = tk.Checkbutton(scrollable_frame, text="check3")
    checkbutton1.pack()
    checkbutton2.pack()
    checkbutton3.pack(pady=(0, 20))

    radiobutton_label = tk.Label(scrollable_frame, text="<Radiobutton>")
    radiobutton_label.pack()
    selected_option = tk.IntVar(value=1)

    # Radiobutton(1つだけonにできるボタン)
    radiobutton1 = tk.Radiobutton(scrollable_frame, text="Option1", variable=selected_option, value=1)
    radiobutton2 = tk.Radiobutton(scrollable_frame, text="Option2", variable=selected_option, value=2)
    radiobutton1.pack()
    radiobutton2.pack(pady=(0, 20))

    # CanvasとScrollbarを配置
    canvas.pack(side="left", fill="y", expand=True)
    scrollbar.pack(side="right", fill="y")

    root.mainloop()
