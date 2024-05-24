import tkinter as tk
from tkinter import messagebox
import phonenumbers
from phonenumbers import geocoder, carrier

def get_phone_info():
    number = phone_number_entry.get()
    if not number:
        messagebox.showerror("Input Error", "Please enter a phone number")
        return

    try:
        # Parse the number for the country (CH - Switzerland)
        ch_number = phonenumbers.parse(number, "CH")
        location = geocoder.description_for_number(ch_number, "en")

        # Parse the number for the carrier info (RO - Romania)
        service_number = phonenumbers.parse(number, "RO")
        carrier_name = carrier.name_for_number(service_number, "en")

        result_text = f"Location: {location}\nCarrier: {carrier_name}"
        result_label.config(text=result_text)
    except phonenumbers.phonenumberutil.NumberParseException:
        messagebox.showerror("Input Error", "Invalid phone number")

# Create the main window
root = tk.Tk()
root.title("Phone Number Info")

# Create and place the widgets
frame = tk.Frame(root)
frame.pack(pady=20, padx=20)

phone_number_label = tk.Label(frame, text="Enter phone number:")
phone_number_label.grid(row=0, column=0, padx=10, pady=10)

phone_number_entry = tk.Entry(frame, width=20)
phone_number_entry.grid(row=0, column=1, padx=10, pady=10)

get_info_button = tk.Button(frame, text="Get Info", command=get_phone_info)
get_info_button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.pack(pady=20)

# Run the GUI event loop
root.mainloop()
