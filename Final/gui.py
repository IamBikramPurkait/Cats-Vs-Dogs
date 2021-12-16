import tensorflow as tf
import cv2
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import filedialog

filename = ''


def upload_action():
    global img
    filename = filedialog.askopenfilename()
    img = Image.open(filename)
    img = img.resize((300, 300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    image_lbl.config(image=img)

    # prediction.set(filename)

    def prepare(image):
        IMG_SIZE = 70
        img_array = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
        new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
        return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

    model = tf.keras.models.load_model("64x3-CNN.model")

    prediction = model.predict([prepare(filename)])
    print(prediction)  # will be a list in a list.
    print(CATEGORIES[int(prediction[0][0])])


window = Tk()


CATEGORIES = ["Dog", "Cat"]


window.geometry('600x500')
window.resizable(False, False)

Font_tuple = ("Comic Sans MS", 20, "bold")

title_frm = Frame(window)
title_frm.pack()


main_title = Label(title_frm, text='Predict Cat vs Dog', font=Font_tuple,
                   background="yellow", foreground="blue")
main_title.pack()

body_frm = Frame()
body_frm.pack(pady=20)


upload_btn = Button(body_frm, text='UPLOAD', command=lambda: upload_action())
upload_btn.pack()


global image_button
image_lbl = Label(body_frm)
image_lbl.pack(pady=20)


# prediction.set('Image Uploaded')

prediction_frm = Frame()
prediction_frm.pack(side=BOTTOM, fill=BOTH)
prediction = StringVar()
prediction_text = Label(
    prediction_frm, textvariable=prediction, font=Font_tuple)
prediction_text.pack()


window.mainloop()
