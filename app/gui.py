import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox, scrolledtext
import threading
from controller import start_extraction
import os
import sys

# Store file path in a global variable for access in all functions
file_path = ''

def select_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[('Excel Files', '*.xlsx')])
    if file_path:
        # Print the selected file to the console log window
        print(f"Selected File: {file_path}")
        print("You can now start the process ->")
    else:
        print('🟥  No file selected')


def start_process():
    if not file_path:
        messagebox.showinfo("Error", "🟥 Please select an Excel file first.")
        return
    start_thread = threading.Thread(target=start_extraction, args=(file_path,))
    start_thread.start()

def main():
    # Create main window
    root = tk.Tk()
    root.title("Data Extraction App")
    root.geometry("900x800")  # Set a fixed window size
    root.configure(bg='black')  # Set the background color to black

    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Set a background image
    image_path = os.path.join(os.path.dirname(__file__), "bg.png")
    original_image = Image.open(image_path)

    # Resize the image while maintaining the aspect ratio
    aspect_ratio = min(screen_width / original_image.width, screen_height / original_image.height)
    new_width = int(original_image.width * aspect_ratio)
    new_height = int(original_image.height * aspect_ratio)
    resized_image = original_image.resize((new_width, new_height), Image.LANCZOS)

    # Create a PhotoImage from the resized image
    bg_image = ImageTk.PhotoImage(resized_image)

    # Create a Label for the background image
    background_label = tk.Label(root, image=bg_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Create a Frame for the buttons
    button_frame = tk.Frame(root, bg='black')  # Set background color to black
    button_frame.place(x=630, y=620)

    # Create a button for selecting the Excel file
    select_file_button = tk.Button(button_frame, text="Select Excel File",
                                  command=select_file, bg='black', fg='black', highlightbackground='black', width=10)
    select_file_button.grid(row=0, column=0, padx=10)

    # Create a button for starting the extraction process
    start_button = tk.Button(button_frame, text="Start Process", command=start_process,
                             bg='black', fg='black', highlightbackground='black', width=10)
    start_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

    # Create a Frame for the log window
    log_frame = tk.Frame(root, bg='black')  # Set background color to black
    log_frame.place(x=240, y=620)

    # Create a scrolled text widget for the console log window
    log_window = scrolledtext.ScrolledText(log_frame, height=10, width=50,
                                           bg='black', fg='white')
    log_window.pack(side=tk.LEFT, padx=10)

    # Redirect the print statements to the console log window
    def redirect_print(output):
        log_window.insert(tk.END, output)
        log_window.see(tk.END)
    sys.stdout.write = redirect_print

    # Redirect the print statements to the console log window
    def redirect_print(output):
        log_window.insert(tk.END, output)
        log_window.see(tk.END)
    sys.stdout.write = redirect_print

    # Print the welcome message
    welcome_msg = "👾 URL_xTractor v0.0.1 👾\nSelect Excel file to begin ->"
    redirect_print(welcome_msg + '\n')  # \n is added to start logs from the next line

    # Start main event loop
    root.mainloop()

# Call main function only if script is executed directly
if __name__ == "__main__":
    main()