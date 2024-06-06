import cv2
import numpy as np
from tkinter import filedialog

class PhotoEditor:
    def __init__(self):
        self.cv_img = None
        self.face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        self.hat_img = cv2.imread('kisspng-asian-conical-hat-cowboy-flickr-clothing-cowboy-hat-5a702b8d27bff9.6863105815173006211628.png', cv2.IMREAD_UNCHANGED)
        self.mustache_img = cv2.imread('biyik1.png', cv2.IMREAD_UNCHANGED)
        self.interface = None

    def resmi_al(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if len(file_path) > 0:
            self.cv_img = cv2.imread(file_path)
            if self.cv_img is not None:
                max_width = 800
                height, width = self.cv_img.shape[:2]
                if width > max_width:
                    scaling_factor = max_width / width
                    new_width = max_width
                    new_height = int(height * scaling_factor)
                    self.cv_img = cv2.resize(self.cv_img, (new_width, new_height))
                self.interface.resmi_panele_yukle(self.cv_img.copy())
            else:
                print("Dosya okunamadı.")

    def cilEkle(self):
        if self.cv_img is None:
            return

        cv_img_copy = self.cv_img.copy()

        gray = cv2.cvtColor(cv_img_copy, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 6, minSize=(30, 30))

        for (x, y, w, h) in faces:
            face_center_x = x + w // 2
            face_center_y = y + h // 2

            nose_x_min = x + w // 3
            nose_x_max = x + 2 * w // 3

            cheek_y_min = face_center_y
            cheek_y_max = y + h
 
            for _ in range(20):
                cx = np.random.randint(nose_x_min, nose_x_max)
                cy = np.random.randint(cheek_y_min - h // 15, face_center_y + h // 15)
                cv2.circle(cv_img_copy, (cx, cy), 1, (110, 79, 50), -1)

        self.interface.resmi_panele_yukle(cv_img_copy)

    def bıyık_sapkaEkle(self):
        if self.cv_img is None:
            return

        cv_img_copy = self.cv_img.copy()

        gray = cv2.cvtColor(cv_img_copy, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 6, minSize=(30, 30))

        for (x, y, w, h) in faces:
            # Şapka ekle
            hat_resized = cv2.resize(self.hat_img, (w, int(h / 2)))
            if hat_resized.shape[2] == 4:
                for i in range(hat_resized.shape[0]):
                    for j in range(hat_resized.shape[1]):
                        if hat_resized[i, j, 3] != 0:
                            cv_img_copy[y + i - int(h / 2), x + j] = hat_resized[i, j, :-1]
            else:
                for i in range(hat_resized.shape[0]):
                    for j in range(hat_resized.shape[1]):
                        cv_img_copy[y + i - int(h / 2), x + j] = hat_resized[i, j]

            
            mustache_width = w
            mustache_height = int(h / 3)
            mustache_resized = cv2.resize(self.mustache_img, (mustache_width, mustache_height))
            mustache_y = y + int(2 * h / 3) - int(mustache_height / 2)
            mustache_x = x
            if mustache_resized.shape[2] == 4:
                for i in range(mustache_resized.shape[0]):
                    for j in range(mustache_resized.shape[1]):
                        if mustache_resized[i, j, 3] != 0:
                            cv_img_copy[mustache_y + i, mustache_x + j] = mustache_resized[i, j, :-1]
            else:
                for i in range(mustache_resized.shape[0]):
                    for j in range(mustache_resized.shape[1]):
                        cv_img_copy[mustache_y + i, mustache_x + j] = mustache_resized[i, j]

        self.interface.resmi_panele_yukle(cv_img_copy)

