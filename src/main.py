import tkinter as tk
import json


class App:
    """
    A class representing the Photography Development Time Calculator application.

    Attributes:
    - window: The main window of the application.
    - temperature_label: A label for the temperature input.
    - temperature_entry: An entry field for the temperature input.
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

        self.control_temperature = 24

        self.window = tk.Tk()
        self.window.title("Photography Development Time Calculator")

        self.title_label = tk.Label(self.window, text="Photography Development Time Calculator", font=("Heather", 14))
        self.title_label.grid(row=0, column=0, columnspan=2)

        self.temperature_label = tk.Label(self.window, text="Temperature (°C):")
        self.temperature_label.grid(row=1, column=0)

        self.temperature_entry = tk.Entry(self.window)
        self.temperature_entry.grid(row=1, column=1)

        self.output_box = tk.Label(self.window, height=15, width=55, relief=tk.SUNKEN, anchor=tk.NW, justify=tk.LEFT, font=("Heather", 11))
        self.output_box.grid(row=2, column=0, columnspan=2)

        self.confirm_button = tk.Button(self.window, text="Calculate", command=self.calculate)
        self.confirm_button.grid(row=3, column=0, columnspan=2)

        self.selected_film_type = tk.StringVar()
        self.film_type_dropdown = tk.OptionMenu(self.window, self.selected_film_type, *self.json_data["film types"])
        self.film_type_dropdown.grid(row=3, column=0, columnspan=1)
    

    def get_json(self):
        """
        Reads the configuration file and returns its contents as a dictionary.
        """
        with open(self.config_file, "r") as file:
            return json.load(file)


    def calculate(self):
        """
        Placeholder method for performing the calculation based on the input temperature.
        """
        temperature = int(self.temperature_entry.get())
        temperature_difference = int(self.control_temperature - temperature)

        developer_time = int(self.json_data["formulas"]["development"]["control_time"])

        if temperature_difference > 0:
            developer_time = (6.5 * self.json_data["film types"][self.selected_film_type.get()] ** (24 - temperature)).__round__(2)

        output_text = f"Step 1: Combine {self.json_data["formulas"]["development"]["water"]}ml water and {self.json_data["formulas"]["development"]["solution"]}ml developer for {developer_time}\
                    \n\nStep 2: Combine {self.json_data["formulas"]["stopper"]["water"]}ml water and {self.json_data["formulas"]["stopper"]["solution"]}ml stopper for {self.json_data["formulas"]["stopper"]["time"]}\
                    \n\nStep 3: Remove the stopper and rinse for {self.json_data["formulas"]["rinse time"]} seconds\
                    \n\nStep 4: Combine {self.json_data["formulas"]["fixer"]["water"]}ml water and {self.json_data["formulas"]["fixer"]["solution"]}ml fixer for {self.json_data["formulas"]["stopper"]["time"]}\
                    \n\nStep 5: Remove the fixer and rinse for {self.json_data["formulas"]["rinse time"]} seconds\
                    \n\nStep 6: Combine Combine {self.json_data["formulas"]["wetting agent"]["water"]}ml water and {self.json_data["formulas"]["wetting agent"]["solution"]}ml wetting agent for {self.json_data["formulas"]["wetting agent"]["time"]}\
                    \n\nStep 7: Remove the wetting agent and rinse for {self.json_data["formulas"]["rinse time"]} seconds\
                    \n\nStep 8: Hang the film to dry"

        print(temperature_difference)
        self.output_box.config(text=output_text)


app = App()


if __name__ == "__main__":
    app.window.mainloop()
