import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
from tkinter import messagebox
from tkinter import filedialog as tkFileDialog
from pathlib import Path
import sys


def config():
    ### 関数定義 ###
    # フォルダ選択を押下した場合の処理
    def select_file_default_folder():
        #dir = 'C:\\'
        dir = Path(sys.argv[0]).parent.absolute()
        fld = tkFileDialog.askdirectory(initialdir = dir)
        entry_default_folder.delete(0, tk.END)
        entry_default_folder.insert(0, fld)
        root.attributes('-topmost', True)    ### 強制的に前面に表示させる
        root.attributes('-topmost', False)
    # 環境設定にて登録を押下した際の処理
    def commit_setting():
        dbname = "outlook.db"
        connection = sqlite3.connect(dbname)
        c = connection.cursor()
        c.execute("""
                  UPDATE default_folder SET folder='{}';
        """.format(entry_default_folder.get()))
        connection.commit()
        connection.close()
        messagebox.showinfo('終了', '設定を登録いたしました')
        root.attributes('-topmost', True)    ### 強制的に前面に表示させる
        root.attributes('-topmost', False)
    # 終了を押下した場合の処理
    def button_exit():
        root.destroy()

    ### sqlite3接続設定 ###

    # データベースを接続
    dbname = "outlook.db"
    connection = sqlite3.connect(dbname)
    c = connection.cursor()
    c.execute("SELECT * FROM default_folder")
    df = c.fetchone()
    connection.close()

    ### GUI画面の作成 ###

    # メインウィンドウの設定
    root = tk.Tk()
    root.title("環境設定")
    root.geometry("500x100")

    ### 設定の登録と終了ボタン ###

    # メインフレームの作成と設置
    frame_top = tk.Frame(root,bd=2,relief="ridge")
    frame_top.pack(fill="x")
    # 各種ウィジェットの作成
    button_register = ttk.Button(frame_top,text="登録", command=commit_setting)
    button_exit = ttk.Button(frame_top,text="終了", command=button_exit)
    # 各種ウィジェットの設置
    button_register.pack(side="left")
    button_exit.pack(side="right")

    ### 各種環境設定項目 ###

    # メインフレームの作成と設置
    frame_setting = tk.Frame(root, relief="ridge")
    frame_setting.pack(side="left")
    # 各種ウィジェットの作成
    label_default_folder = ttk.Label(frame_setting, text="デフォルトフォルダ設定：", width=20)
    entry_default_folder = ttk.Entry(frame_setting, justify="left", width=40)
    button_default_folder = ttk.Button(frame_setting, text="フォルダ選択", command=select_file_default_folder)
    # 各種ウィジェットの設置
    label_default_folder.grid(row=0, column=0, padx=10, pady=2)
    entry_default_folder.grid(row=0, column=1, sticky=tk.W + tk.E, padx=2, pady=2)
    button_default_folder.grid(row=0, column=2, sticky=tk.W + tk.E, padx=2, pady=2)
    # 初期値の入力
    entry_default_folder.insert(0, df[0])

    root.mainloop()

### 直接起動時の内容 ###
# ----------------------------------------------
if __name__ == '__main__':
    config()