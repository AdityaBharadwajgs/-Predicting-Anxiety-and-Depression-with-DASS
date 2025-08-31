import tkinter as tk
from tkinter import ttk
import numpy as np
import skfuzzy as fuzz  # For fuzzy calculations (if needed later)
from ttkbootstrap import Style
from ttkbootstrap.widgets import Meter
# Initialize main window
root = tk.Tk()
root.title("🌍 Air Quality Monitoring System")
root.geometry("550x720")
root.resizable(False, False)

# Apply modern theme
style = Style("solar")  
root.configure(bg="#2C2F33")  

# Fixed AQI Mapping Based on Given Table
def get_base_aqi(co, no2):
    """Returns the base AQI value based on CO and NO2 levels."""
    mapping = {
        (1, 100): 45,  # Good
        (3, 400): 80,  # Moderate
        (7, 700): 150, # Unhealthy
        (12, 1000): 250, # Very Unhealthy
        (18, 1400): 400 # Hazardous
    }
    return mapping.get((co, no2), -1)  # Return -1 for out-of-range values

#fuzzy logic

def calculate_aqi():
    try:
        
        temp = float(temp_var.get())
        humidity = float(humidity_var.get())
        co = float(co_var.get())
        no2 = float(no2_var.get())

        # Get base AQI from CO and NO2 levels
        base_aqi = get_base_aqi(co, no2)

        if base_aqi == -1:
            status = "Unknown ❓"
            color = "gray"
        else:
            # Temperature Effect: Higher temperature worsens AQI
            temp_adjust = (temp - 22) * 1.5  # Small increase per °C above 22
            # Humidity Effect: Higher humidity traps pollution, increasing AQI
            humidity_adjust = (humidity - 55) * 0.5  # Small increase per % above 55

            # Final AQI Calculation
            aqi_value = round(base_aqi + temp_adjust + humidity_adjust)

            # Determine AQI category and color
            if aqi_value <= 50:
                status = "Good 😊"
                color = "green"
            elif aqi_value <= 100:
                status = "Moderate 😐"
                color = "blue"
            elif aqi_value <= 199:
                status = "Unhealthy 😷"
                color = "orange"
            elif aqi_value <= 299:
                status = "Very Unhealthy 🤒"
                color = "red"
            else:
                status = "Hazardous ☠"
                color = "purple"

        # Update UI
        meter.configure(amountused=aqi_value, subtext=status, bootstyle=color)
        aqi_label.config(text=f"Air Quality Index: {aqi_value}", foreground=color)
        status_label.config(text=f"Status: {status}", foreground=color)

    except ValueError:
        aqi_label.config(text="Air Quality Index: --", foreground="white")
        status_label.config(text="Status: --", foreground="white")

# UI Design
ttk.Label(
    root, text="🌍 Air Quality Monitoring System", font=("Arial", 20, "bold"),
    background="#2C2F33", foreground="white"
).pack(pady=15)

# AQI Meter
meter_frame = ttk.Frame(root, padding=10, style="dark")
meter_frame.pack(pady=10)

meter = Meter(
    meter_frame,
    bootstyle="primary",
    metertype="full",
    amountused=0,
    amounttotal=500,  
    subtext="AQI",
    interactive=False,
    metersize=220,  
    meterthickness=18,  
    stripethickness=9,
    textfont=("Arial", 16, "bold"),  
    subtextfont=("Arial", 13),
    subtextstyle="info",
)
meter.pack()

# User Input Fields
frame = ttk.Frame(root, style="dark")
frame.pack(pady=10, padx=10, fill="both")

# Variables for user input
temp_var = tk.StringVar(value="22")
humidity_var = tk.StringVar(value="55")
co_var = tk.StringVar(value="1")
no2_var = tk.StringVar(value="100")

fields = [
    ("🌡 Temperature (°C)", temp_var),
    ("💧 Humidity (%)", humidity_var),
    ("🛑 CO Level (ppm)", co_var),
    ("🚗 NO₂ Level (ppb)", no2_var),
]

entries = []
for label_text, var in fields:
    row = ttk.Frame(frame)
    row.pack(fill="x", pady=5)
    
    label = ttk.Label(
        row, text=label_text, font=("Arial", 12, "bold"),
        background="#2C2F33", foreground="white", width=18, anchor="w"
    )
    label.pack(side="left", padx=(10, 5))

    entry = ttk.Entry(row, textvariable=var, width=10, font=("Arial", 12))
    entry.pack(side="right", padx=(5, 10))
    entries.append(entry)

temp_entry, humidity_entry, co_entry, no2_entry = entries

# Calculate Button
calc_button = ttk.Button(root, text="🔍 Calculate AQI", command=calculate_aqi, bootstyle="primary")
calc_button.pack(pady=20)

# AQI Output Labels
aqi_label = ttk.Label(root, text="Air Quality Index: --", font=("Arial", 16, "bold"), background="#2C2F33", foreground="white")
aqi_label.pack()
status_label = ttk.Label(root, text="Status: --", font=("Arial", 14, "bold"), background="#2C2F33", foreground="white")
status_label.pack()

# Run App
root.mainloop()