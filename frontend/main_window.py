import tkinter as tk

# retrieve info from app.py and display
def show_open(libraries):
    # hide the button
    button.pack_forget()

    


root = tk.Tk()
root.title("UC Library Hours Checker")

# label styling
font_title = ("Arial", 14)
anchor_title = "center"

title = tk.Text(root)
label = tk.Label(root, text="UC Library Hours Checker", font=font_title, anchor=anchor_title)

label.pack(padx=20,pady=10)

# go button
button = tk.Button(root, text="What's Open?", command=show_open)

root.mainloop()

