import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import json
import os

def convert_excel_to_json():
    files = filedialog.askopenfilenames(filetypes=[("Excel files", "*.xlsx *.xls")])
    if not files:
        return

    output = {}

    for file in files:
        try:
            df = pd.read_excel(file)
            for _, row in df.iterrows():
                data = row.dropna().to_dict()
                client_name = data.get("Name") or f"Client_{len(output)+1}"
                output[client_name] = data

        except Exception as e:
            messagebox.showerror("Error", f"Failed to read {file}:\n{str(e)}")
            return

    output_path = filedialog.asksaveasfilename(
        defaultextension=".json", filetypes=[("JSON files", "*.json")], initialfile="clients.json"
    )
    if not output_path:
        return

    try:
        with open(output_path, "w") as f:
            json.dump(output, f, indent=2)
        messagebox.showinfo("Success", f"JSON file saved successfully at:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save JSON:\n{str(e)}")

# GUI Setup
root = tk.Tk()
root.title("Excel to JSON Converter for Chrome Extension")
root.geometry("440x200")

label = tk.Label(root, text="Convert Excel Files (Multiple Clients) to JSON", pady=10)
label.pack()

button = tk.Button(root, text="Select Excel Files and Convert", command=convert_excel_to_json, height=2, width=35)
button.pack(pady=20)

root.mainloop()
