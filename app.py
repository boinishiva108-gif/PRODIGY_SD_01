import tkinter as tk
from tkinter import ttk, messagebox

# ----------------- Conversion Functions -----------------
def to_celsius(value, unit):
    conversions = {
        "Celsius": lambda v: v,
        "Fahrenheit": lambda v: (v - 32) * 5 / 9,
        "Kelvin": lambda v: v - 273.15
    }
    return conversions[unit](value)

def from_celsius(c, target_unit):
    conversions = {
        "Celsius": lambda c: c,
        "Fahrenheit": lambda c: (c * 9 / 5) + 32,
        "Kelvin": lambda c: c + 273.15
    }
    return conversions[target_unit](c)

def convert_temperature(*args):
    try:
        value = float(temp_input.get())
        unit = selected_unit.get()

        celsius = to_celsius(value, unit)
        results = [(u, from_celsius(celsius, u)) for u in units if u != unit]

        for i, (u, val) in enumerate(results):
            result_labels[i].config(text=f"{u}:")
            result_vars[i].set(f"{val:.2f} {symbols[u]}")

    except ValueError:
        for i in range(2):
            result_labels[i].config(text="---")
            result_vars[i].set("")

# ----------------- Window Setup -----------------
app = tk.Tk()
app.title("Temperature Converter")
app.geometry("450x350")
app.resizable(True, True)

main_frame = ttk.Frame(app, padding=20)
main_frame.pack(expand=True, fill="both")

# --- Title ---
ttk.Label(main_frame, text="Temperature Converter", font=("Segoe UI", 20, "bold")).pack(pady=(0, 20))

# --- Input ---
input_frame = ttk.Frame(main_frame)
input_frame.pack(pady=10, fill='x')
input_frame.columnconfigure((0, 1), weight=1)

units = ["Celsius", "Fahrenheit", "Kelvin"]
symbols = {"Celsius": "°C", "Fahrenheit": "°F", "Kelvin": "K"}

ttk.Label(input_frame, text="Enter Temperature:", font=("Segoe UI", 12)).grid(row=0, column=0, sticky="e")
temp_input = ttk.Entry(input_frame, width=15, font=("Segoe UI", 12))
temp_input.grid(row=0, column=1, sticky="w")
temp_input.bind("<KeyRelease>", convert_temperature)

ttk.Label(input_frame, text="Select Unit:", font=("Segoe UI", 12)).grid(row=1, column=0, sticky="e")
selected_unit = tk.StringVar(value="Celsius")
unit_dropdown = ttk.Combobox(input_frame, textvariable=selected_unit, values=units, state="readonly", font=("Segoe UI", 12))
unit_dropdown.grid(row=1, column=1, sticky="w")
unit_dropdown.bind("<<ComboboxSelected>>", convert_temperature)

# --- Results ---
result_frame = ttk.LabelFrame(main_frame, text=" Results ", padding=20)
result_frame.pack(fill="x", expand=True)

result_labels, result_vars = [], []
for i in range(2):
    label = ttk.Label(result_frame, text="---", font=("Segoe UI", 14))
    label.grid(row=i, column=0, sticky="e", padx=10, pady=10)
    result_labels.append(label)

    var = tk.StringVar()
    entry = ttk.Entry(result_frame, textvariable=var, font=("Segoe UI", 14, "bold"), state="readonly", justify='center')
    entry.grid(row=i, column=1, sticky="w", padx=10, pady=10)
    result_vars.append(var)

temp_input.focus()
app.mainloop()
