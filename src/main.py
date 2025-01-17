import tkinter as tk
import json
from tkinter import messagebox
import time
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Imports successful.")


class App:
    """
    A class representing the Photography Development Time Calculator application.

    Attributes:
    - config_file: The path to the configuration file.
    - title_label: A label for the title of the application.
    - window: The main window of the application.
    - temperature_label: A label for the temperature input.
    - temperature_spinbox: An entry field for the temperature input.
    - output_box: A text box for displaying the output.
    - confirm_button: A button for triggering the calculation.
    - output_text: The text to be displayed in the output box.
    """

    def __init__(self):
        """
        Initializes the App class by creating the main window and setting up the UI elements.
        """
        self.config_file = "src\\config.json"
        self.json_data = self.get_json()

        self.control_temperature = self.json_data['formulas']['control_temp']

        self.window = tk.Tk()
        self.window.title("Photography Development Time Calculator")
        self.window.configure(bg="#DBBD8F")

        self.title_label = tk.Label(self.window, text="Photography Development Time Calculator", font=("Heather", 20), bg="#DBBD8F")
        self.title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.temperature_label = tk.Label(self.window, text="Temperature (°C):", font=("Heather", 12), bg="#DBBD8F")
        self.temperature_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)

        self.temperature_spinbox = tk.Spinbox(self.window, bd=4, from_=0, to=50, width=10, font=("Heather", 12))
        self.temperature_spinbox.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        self.output_box = tk.Label(self.window, height=16, width=55, relief=tk.SUNKEN, anchor=tk.NW, justify=tk.LEFT, font=("Heather", 11), bd=10)
        self.output_box.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.confirm_button = tk.Button(self.window, text="Calculate", command=self.calculate, font=("Heather", 12), bd=5)
        self.confirm_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.selected_film_type = tk.StringVar()
        self.film_type_dropdown = tk.OptionMenu(self.window, self.selected_film_type, *self.json_data['film types'])
        self.film_type_dropdown.grid(row=3, column=0, columnspan=1, padx=10, pady=10)
        logging.info("UI elements set up.")
    

    def get_json(self):
        """
        Reads the configuration file and returns its contents as a dictionary.
        """
        with open(self.config_file, "r") as file:
            try:
                logging.info("Reading configuration file.")
                return json.load(file)
            except Exception as e:
                logging.error("Failed to read configuration file: " + str(e))
                return {}


    def calculate(self):
        """
        Calculates the film development time based on the temperature and selected film type.
        """
        logging.info("Calculating film development time.")
        
        if not self.selected_film_type.get():
            messagebox.showerror("Error", "Please select a film type.")
            logging.error("No film type selected.")
            return
        try:
            temperature = int(self.temperature_spinbox.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid temperature value. Please enter a valid integer.")
            logging.error("Invalid temperature value.")
            return
        temperature = int(self.temperature_spinbox.get())
        temperature_difference = int(self.control_temperature - temperature)

        developer_time = int(self.json_data['formulas']['development']['control_time'])

        if temperature_difference > 0:
            developer_time = (6.5 * self.json_data['film types'][self.selected_film_type.get()] ** (24 - temperature)).__round__(2)
            developer_time = time.strftime("%M:%S", time.gmtime(developer_time * 60))
        elif temperature_difference < 0:
            developer_time = (6.5 * self.json_data['film types'][self.selected_film_type.get()] ** (24 - temperature)).__round__(2)
            developer_time = time.strftime("%M:%S", time.gmtime(developer_time * 60))

        output_text = f"Step 1: Combine {self.json_data['formulas']['development']['water']}ml water and {self.json_data['formulas']['development']['solution']}ml developer for {developer_time}\
                    \n\nStep 2: Combine {self.json_data['formulas']['stopper']['water']}ml water and {self.json_data['formulas']['stopper']['solution']}ml stopper for {self.json_data['formulas']['stopper']['time']}\
                    \n\nStep 3: Remove the stopper and rinse for {self.json_data['formulas']['rinse time']} seconds\
                    \n\nStep 4: Combine {self.json_data['formulas']['fixer']['water']}ml water and {self.json_data['formulas']['fixer']['solution']}ml fixer for {self.json_data['formulas']['stopper']['time']} seconds\
                    \n\nStep 5: Remove the fixer and rinse for {self.json_data['formulas']['rinse time']} seconds\
                    \n\nStep 6: Combine Combine {self.json_data['formulas']['wetting agent']['water']}ml water and {self.json_data['formulas']['wetting agent']['solution']}ml wetting agent for {self.json_data['formulas']['wetting agent']['time']} seconds\
                    \n\nStep 7: Remove the wetting agent and rinse for {self.json_data['formulas']['rinse time']} seconds\
                    \n\nStep 8: Hang the film to dry"

        logging.info("Film development time calculated.")
        self.output_box.config(text=output_text)


app = App()
logging.info("Application declared.")


if __name__ == "__main__":
    logging.info("Application started.")
    app.window.mainloop()
