from tkinter import messagebox
import tensorflow as tf
import cv2
from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import filedialog
import requests

filename = ''
CATEGORIES = ["Dog", "Cat"]


# def upload_action():
#     global img
#     filename = filedialog.askopenfilename()
#     img = Image.open(filename)
#     img = img.resize((300, 300), Image.ANTIALIAS)
#     img = ImageTk.PhotoImage(img)
#     image_lbl.config(image=img)


# ------------------------------------------------------------------------------------------------

window = Tk()


window.geometry('600x600')
window.title('Dog vs Cat')
window.resizable(False, False)

Font_tuple = ("Comic Sans MS", 20, "bold")

title_frm = Frame(window)
title_frm.pack()


main_title = Label(title_frm, text='Predict Dog vs Cat by Deep Learning', font=Font_tuple,
                   background="yellow", foreground="blue")
main_title.pack()

# -----------------------------------------------------------------------------------------------------


body_frm = Frame()
body_frm.pack(pady=20)


style = ttk.Style()
style.theme_use('alt')
style.configure('TButton', background='white', foreground='black', font=("Comic Sans MS", 15, "bold"),
                borderwidth=2, focusthickness=3, focuscolor='none')
style.map('TButton', background=[('active', 'red')])

# link_var = StringVar()
# textvariable = link_var,
link_entry = Text(body_frm,
                  font=("Comic Sans MS", 12, "bold"), width=50, height=2, fg="green", relief="solid", padx=5)
link_entry.pack(pady=5)
link_entry.insert(
    "1.0", "Delete this text and Paste the Image address/link here and then press Predict button")

# global img_link
# img_link = link_var.get()
# print(img_link)


# upload_btn = ttk.Button(body_frm, text='UPLOAD',
#                         command=lambda: upload_action())
# upload_btn.pack()


# prediction.set('Image Uploaded')
prediction_var = StringVar()

prediction_frm = Frame()
prediction_frm.pack(side=BOTTOM, fill=BOTH)
prediction_text = Label(
    prediction_frm, textvariable=prediction_var, font=Font_tuple)
prediction_text.pack()

prediction_var.set('Select Dog or Cat image only')


def download_image():
    # Get Image URL using get() method
    image = requests.get(link_entry.get("1.0", END))

    # Check whether the Image URL is correct or not
    if image.status_code == 200:
        # Use File Handling to download the image

        with open("sample/image.jpg", 'wb') as image_file:
            image_file.write(image.content)

        # close the file
        image_file.close()

    global img
    image_address = 'C:/Users/bkrmp/Desktop/Cats Vs Dogs/sample/image.jpg'
    img = Image.open(image_address)
    img = img.resize((300, 300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    image_lbl.config(image=img, borderwidth=2,
                     relief='solid')

    model = tf.keras.models.load_model("64x3-CNN.model")

    def prepare(image):
        IMG_SIZE = 70
        img_array = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
        new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
        return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

    prediction = model.predict([prepare(image_address)])
    prediction_var.set(CATEGORIES[int(prediction[0][0])])


download_image_btn = ttk.Button(
    body_frm, text='Predict', command=download_image)
download_image_btn.pack(pady=5)


image_lbl = Label(body_frm, fg="blue")
image_lbl.pack()


window.mainloop()
