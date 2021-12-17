# Import required Libraries
from tkinter import *
import requests
import cv2

# create tkinter object
root = Tk()

# Set title
root.title("View Image From URL")

# set geomertry
root.geometry("400x160")

# View Image From URL


def view_image():
    # Get Image URL using get() method
    image = requests.get(image_url.get())
    print(image.status_code)
    # Check whether the Image URL is correct or not
    if image.status_code == 200:
        # Use File Handling to download the image
        with open("sample/image.png", 'wb') as image_file:
            image_file.write(image.content)

        image = cv2.imread("image.png")
        cv2.imshow("Image", image)
        cv2.waitKey(0)

        # close the file
        image_file.close()
    else:
        print("Incorrect Image URL")


# Add Labels, Button, and entry box
Label(root, text="View Image From URL",
      font=("Comic Sans MS", 20, "bold")).pack(pady=10)

image_url = Entry(root, width=50, font=("Comic Sans MS", 9))
image_url.pack(pady=10)

Button(root, text="View Image", font=("Comic Sans MS", 10),
       command=view_image).pack(pady=10)

# Execute Tkinter
root.mainloop()
