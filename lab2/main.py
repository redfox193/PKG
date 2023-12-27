from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
from PIL import Image

selected_image_path = ""
diag = 15


def get_folder():
    """
    Prompt the user to select a folder and update the folder_path entry.
    Clears the treeview and initiates scanning of the selected folder.
    """
    filepath = filedialog.askdirectory()
    folder_path.delete(0, END)
    folder_path.insert(INSERT, filepath)
    tree.delete(*tree.get_children())
    scan(filepath)


def scan(folder_path):
    """
    Recursively scan the specified folder for image files and populate the treeview with image information.
    Args:
        folder_path (str): The path to the folder to scan for images.
    """
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(('.jpg', '.gif', '.tif', '.bmp', '.png', '.pcx')):
                tree.insert("", END, values=image_info(os.path.join(root, file)))


def image_info(image_path):
    """
    Retrieve information about an image file.
    Args:
        image_path (str): The path to the image file.

    Returns:
        tuple: A tuple containing image information such as name, size, resolution, color depth, and compression.
    """
    img = Image.open(image_path)
    name = os.path.basename(image_path)
    width, height = img.size
    resolution = (width ** 2 + height ** 2) ** 0.5 / diag
    depth = img.mode
    compression = img.info.get("compression", "N/A")
    return name, f"Size: {width}x{height}", f"Dots/Inch: {resolution:.2f}", f"Color Depth: {depth}", f"Compression: {compression}"


def show_image(event):
    """
    Display the selected image in a separate window when a row in the treeview is clicked.
    Args:
        event: The event object that triggered the function.
    """
    global selected_image_path
    selected_item = tree.item(tree.selection())
    image_name = selected_item['values'][0]
    selected_image_path = os.path.join(folder_path.get(), image_name)
    img = Image.open(selected_image_path)
    img.show()

my_font = ('Comic Sans MS', 12)

root = Tk()
root.title("Image Reader")
root.geometry('860x540')
root.configure(bg='#ccd5ae') 

folder_path = Entry(root, width=70, bg='#fefae0', font=my_font, foreground='#283618')
folder_path.grid(row=0, column=1, padx=10, pady=20, sticky=(W, E))
folder_path.insert(INSERT, "Please, select a folder :)")

# Button creation
btn_folder_path = Button(root, text="-> Browse <-", command=get_folder, width=10, bg='#ffb703', font=my_font, foreground='#fefae0')
btn_folder_path.grid(row=0, column=0, padx=20, pady=20, sticky=(W, E))

# Table creation
columns = ('Name', 'Size', 'Dots/Inch', 'Color Depth', 'Compression')
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.grid(row=1, columnspan=2, sticky=(N, S, W, E))

# Style
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", font=my_font, rowheight=25, background='#fefae0', foreground='#283618')
style.configure("Treeview.Heading", font=my_font, background='#ffb703', foreground='#fefae0')

# Columns
for col in columns:
    tree.heading(col, text=col)
column_widths = [100, 150, 150, 150, 150, 150]
for i, col in enumerate(columns):
    tree.column(f"#{i + 1}", stretch=YES, width=column_widths[i])

scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=1, column=2, sticky=(N, S, W, E))

tree.bind("<<TreeviewSelect>>", show_image)

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()