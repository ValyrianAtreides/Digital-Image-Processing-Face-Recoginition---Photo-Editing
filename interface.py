from tkinter import *
from PIL import Image, ImageTk
import cv2

class PhotoEditorInterface:
    def __init__(self, window, photo_editor):
        self.window = window
        self.photo_editor = photo_editor

        self.window.title("SGİ Ödevi")
        self.window.geometry("800x600")
        self.window.configure(bg="#ececec")


        panel_frame = Frame(self.window, borderwidth=2, relief="sunken", bg="#ffffff")
        panel_frame.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        self.panel = Label(panel_frame, bg="#ffffff")
        self.panel.pack(fill="both", expand=True)


        button_frame = Frame(self.window, bg="#ececec")
        button_frame.pack(side="bottom", pady=10)

        Button(button_frame, text="Fotoğraf Yükle", command=self.photo_editor.resmi_al).pack(side="left", padx=10)
        Button(button_frame, text="Çil Ekle", command=self.photo_editor.cilEkle).pack(side="left", padx=10)
        Button(button_frame, text="Şapka ve Bıyık Ekle", command=self.photo_editor.bıyık_sapkaEkle).pack(side="left", padx=10)

    def resmi_panele_yukle(self, cv_img):
        img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        tk_img = ImageTk.PhotoImage(img)

        self.panel.configure(image=tk_img)
        self.panel.image = tk_img