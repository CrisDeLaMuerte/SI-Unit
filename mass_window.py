from customtkinter import CTkToplevel
from customtkinter import CTkOptionMenu, CTkEntry, CTkLabel,  CTkButton
from CTkMessagebox import CTkMessagebox

class MassWindow(CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Mass Unit Calculator")
        self.geometry("400x400")

        # conversion dict to calculate the values, base is kg, instead of if statements.
        self.conversion ={"kg": 1, "g": 1000, "mg": 1000000, "µg": 1000000000, "t": 0.001}


        # list of labels that are saved to show the values, like a container
        self.list_labels = []

        # label explanation option menu
        self.label_option_menu = CTkLabel(master=self, text="Choose a unit and convert it to other units")
        self.label_option_menu.grid(row=0, column=0, padx=90, pady=10)

        # option menu to select a "base" unit and then convert it to other
        self.unit_option_menu = CTkOptionMenu(master=self, values=["kg", "g", "mg", "t", "µg"])
        self.unit_option_menu.grid(row=1, column=0, padx=90, pady=10)

        # Input field for the user
        self.input_user = CTkEntry(master=self, placeholder_text="Enter your value here")
        self.input_user.grid(row=2, column=0, padx=90, pady=10)

        # button to calculate the values and create new labels to display the values
        self.button_calculate = CTkButton(master=self, text="Calculate", command=self.calculate)
        self.button_calculate.grid(row=3, column=0, padx=90, pady=10)



    def calculate(self):
        try:
            # get values to calculate into the units
            input_to_convert = float(self.input_user.get())
            get_option_value = self.unit_option_menu.get()

            # row variable to place the created labels
            row = 4
            # clear all the labels that are in list_labels before creating new ones ! Must be destroyed and cleared from the list !
            for labels in self.list_labels:
                labels.destroy()

            self.list_labels.clear()

            # calculate the given input into the base kg
            value_in_kg = input_to_convert / self.conversion[get_option_value]

            # calculate the values, create labels and display on the window
            for unit, factor in self.conversion.items():
                result = value_in_kg * factor
                label = CTkLabel(self, text=f"{unit}: {round(result, 4)}")
                label.grid(row=row, column=0, padx=90, pady=5)
                self.list_labels.append(label)
                row += 1

        except ValueError:
            CTkMessagebox(title="Warning", message="Invalid Input. Please be sure to enter a valid number. Avoid letters or symbols. E.g. 2.3, 123.46 , 333333.3333", icon="warning")
