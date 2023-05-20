import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def calculate_wage():
    hourly = float(hourly_entry.get())
    work_hours = float(work_hours_entry.get())

    result = hourly * work_hours * 13 // 3
    messagebox.showinfo("Result", f"You get {result}€ monthly wage before taxes (brutto)")

def calculate_again():
    hourly_entry.delete(0, tk.END)
    work_hours_entry.delete(0, tk.END)

window = tk.Tk()
window.title("Wage Calculator")
window.geometry("400x300")  # Set the initial size of the window (width x height)

# Load and display the background image
background_image = Image.open("cat-974.gif")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

hourly_label = tk.Label(window, text="Hourly Pay:", bg='white')
hourly_label.pack()
hourly_entry = tk.Entry(window)
hourly_entry.pack()

work_hours_label = tk.Label(window, text="Weekly Work Hours:", bg='white')
work_hours_label.pack()
work_hours_entry = tk.Entry(window)
work_hours_entry.pack()

calculate_button = tk.Button(window, text="Calculate", command=calculate_wage)
calculate_button.pack()

calculate_again_button = tk.Button(window, text="Calculate Again", command=calculate_again)
calculate_again_button.pack()

window.mainloop()
