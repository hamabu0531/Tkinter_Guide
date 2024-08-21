import tkinter as tk
import ctypes
from tkinter import ttk

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

    scale_label = tk.Label(scrollable_frame, text="<Scale>")
    scale_label.pack()
    var2 = tk.IntVar(root)
    s_label = tk.Label(scrollable_frame, textvariable=var2, relief="ridge")
    s_label.pack()

    # Scale(スライドバー)
    scale1 = tk.Scale(scrollable_frame, variable=var2)
    scale1.pack()
    # 横version
    scale2 = tk.Scale(scrollable_frame, variable=var2, orient="horizontal")
    scale2.pack(pady=(0, 20))

    message_label = tk.Label(scrollable_frame, text="<Message>")
    message_label.pack()
    comment = "上がMessageでの表示、下がLabelでの表示です。"

    # Message(複数行表示)
    message = tk.Message(scrollable_frame, relief="raised", aspect=300, text=comment)
    message.pack()
    m_label = tk.Label(scrollable_frame, relief="raised", text=comment)
    m_label.pack(pady=(0, 20))

    canvas_label = tk.Label(scrollable_frame, text="<Canvas>")
    canvas_label.pack()

    # Canvas(図形、画像の表示)
    canvas2 = tk.Canvas(scrollable_frame, height=150)
    canvas2.pack(pady=(0, 20))
    canvas2.create_oval(50, 50, 150, 150, fill="cyan")
    canvas2.create_rectangle(200, 50, 300, 150, fill="red")
    canvas2.create_polygon(310, 150, 400, 50, 450, 150, fill="lightgreen")

    # Menu(上に表示されるメニューバー)
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Open", command=None)
    file_menu.add_command(label="Save", command=None)
    file_menu.add_separator() #区切り線
    file_menu.add_command(label="Exit", command=root.quit)


    # ここから下はttkのimportが必要です

    combo_label = tk.Label(scrollable_frame, text="<Combobox>")
    combo_label.pack()

    # Combobox(広がる選択肢)
    combo_list = ["Morning", "Afternoon", "Night"]
    combobox = ttk.Combobox(scrollable_frame, values=combo_list, state="readonly")
    combobox.pack(pady=(0, 20))

    tree_label = tk.Label(scrollable_frame, text="<Treeview>")
    tree_label.pack()

    # Treeview
    tree = ttk.Treeview(scrollable_frame)
    parent = tree.insert("", "end", text="parent")
    child = tree.insert(parent, "end", text="child")
    child2 = tree.insert(parent, "end", text="child2")
    c2_child = tree.insert(child2, "end", text="c2_child")
    tree.pack(pady=(0, 20))

    progress_label = tk.Label(scrollable_frame, text="<Progressbar>")
    progress_label.pack()
    pb_var = tk.IntVar(scrollable_frame)
    def update_progress():
        if pb_var.get() < 100:
            pb_var.set(pb_var.get()+10)
        else:
            pb_var.set(0)
    def start_progress():
        if cb2["text"] == "start":
            pb2.start(interval=10)
            cb2["text"] = "stop"
        else:
            pb2.stop()
            cb2["text"] = "start"

    # Progressbar(determinate)
    pb1 = ttk.Progressbar(scrollable_frame, maximum=100, variable=pb_var,
                          mode="determinate", orient="horizontal")
    pb1.pack()
    cb1 = tk.Button(scrollable_frame, text="count up",
                    command=update_progress)
    cb1.pack(pady=(0, 20))

    # Progressbar(imdeterminate)
    pb2 = ttk.Progressbar(scrollable_frame, mode="indeterminate", orient="horizontal")
    pb2.pack()
    cb2 = tk.Button(scrollable_frame, text="start", command=start_progress)
    cb2.pack(pady=(0, 20))

    notebook_label = tk.Label(scrollable_frame, text="<Notebook>")
    notebook_label.pack()

    # Notebook
    note = ttk.Notebook(scrollable_frame)
    note_label = tk.Label(scrollable_frame, text="登録完了しました")
    note_text = tk.Entry(scrollable_frame)
    note_button = tk.Button(scrollable_frame, text="登録", command=lambda: note.select(2))
    note.add(note_text, text="入力欄")
    note.add(note_button, text="登録確認")
    note.add(note_label, text="完了", state="hidden")
    note.pack(pady=(0, 20))
    # CanvasとScrollbarを配置
    canvas.pack(side="left", fill="y", expand=True)
    scrollbar.pack(side="right", fill="y")

    root.mainloop()
