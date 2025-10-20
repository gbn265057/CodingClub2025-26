import tkinter as tk
import tkinter.ttk as ttk

from tkinter.messagebox import Message
from grades import calculate_final, write_message

def handle_calculations():
    try:
        score_needed = calculate_final(float(current.get()), float(desired.get()), float(share.get()))
        message = "You need a " + str(score_needed) + ". " + write_message(score_needed)
        Message(root, message=message, type="ok").show()

        if name.get():
            add_class_to_tree(name.get(), current.get(), desired.get(), share.get(), score_needed)
            sort_tree(class_list)
    except ValueError:
        pass

def add_class_to_tree(name, current, desired, share, needed):
    if class_list.exists(name):
        class_list.set(name, 'current', current)
        class_list.set(name, 'desired', desired)
        class_list.set(name, 'share', share)
        class_list.set(name, 'needed', needed)
    else:
        class_list.insert('', tk.END, name, text=name, values=(current, desired, share, needed))

def sort_tree(tree):
    sorted_classes = sorted(tree.get_children(''))
    for class_name in sorted_classes:
        tree.move(class_name, '', tk.END)

root = tk.Tk()
root.title("Final Grade Calculator")

inputs = ttk.Frame(root, padding=(5, 5, 5, 5))
classes = ttk.Frame(root, padding=(5, 5, 5, 5))

current_label = ttk.Label(inputs, text="What is your current grade?")
desired_label = ttk.Label(inputs, text="What grade are you hoping for?")
share_label = ttk.Label(inputs, text="What percent of your grade is your final?")
name_label = ttk.Label(inputs, text="What class is this? (optional)")

current = tk.StringVar()
current_field = ttk.Entry(inputs, textvariable=current)
desired = tk.StringVar()
desired_field = ttk.Entry(inputs, textvariable=desired)
share = tk.StringVar()
share_field = ttk.Entry(inputs, textvariable=share)
name = tk.StringVar()
name_field = ttk.Entry(inputs, textvariable=name)

calculate_button = ttk.Button(inputs, text="Calculate!", command=handle_calculations)
root.bind("<Return>", lambda _: calculate_button.invoke())

class_list = ttk.Treeview(classes, columns=('current', 'desired', 'share', 'needed'))
class_list.heading("#0", text="Class")
class_list.heading('current', text="Current Grade")
class_list.heading('desired', text="Grade Wanted")
class_list.heading('share', text="Final Share")
class_list.heading('needed', text="Final Needed")

inputs.grid(column=0, row=1, sticky='nesw')
current_label.grid(column=0, row=0, sticky='w', padx=1, pady=2)
current_field.grid(column=1, row=0, sticky='w', padx=1, pady=2)
desired_label.grid(column=0, row=1, sticky='w', padx=1, pady=2)
desired_field.grid(column=1, row=1, sticky='w', padx=1, pady=2)
share_label.grid(column=0, row=2, sticky='w', padx=1, pady=2)
share_field.grid(column=1, row=2, sticky='w', padx=1, pady=2)
name_label.grid(column=0, row=3, sticky='w', padx=1, pady=1)
name_field.grid(column=1, row=3, sticky='w', padx=1, pady=1)
calculate_button.grid(column=0, row=4, columnspan=2)

classes.grid(column=0, row=2, sticky="nesw")
class_list.grid(column=0, row=0, sticky="nesw")

root.mainloop()