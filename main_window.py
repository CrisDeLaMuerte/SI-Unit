from datetime import date
from customtkinter import CTk, CTkOptionMenu, CTkButton, CTkLabel
from mass_window import MassWindow
from length_window import LengthWindow

class MainWindow(CTk):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.geometry("700x700")
        self.title(f"SI Unit Calculator: {date.today()}")

        # window variables for checking if already exists, standard value is None
        self.mass_window = None
        self.length_window = None

        # label explanation
        self.label_appearance = CTkLabel(master=self, text="Change Appearance of this window", width=40, height=40,text_color="black")
        self.label_appearance.grid(row=1, column=0, padx=200, pady=10)


        # option menu to change the appearance
        self.change_appearance = CTkOptionMenu(master=self, values=["Light", "Dark"],command=self.callback_change_appearance)
        self.change_appearance.grid(row=2, column=0, padx=200, pady=10)


        # label explanation
        self.label_buttons = CTkLabel(master=self, text="Click the buttons to open a new window and start calculating")
        self.label_buttons.grid(row=3, column=0, padx=200, pady=10)

        # buttons to open a new window
        self.button_time = CTkButton(master=self, text="Mass Unit", command=self.callback_time_unit)
        self.button_time.grid(row=4, column=0, padx=200, pady=10)
        self.button_length = CTkButton(master=self, text="Length Unit", command=self.callback_length_unit)
        self.button_length.grid(row=5, column=0, padx=200, pady=10)
        self.button_mass = CTkButton(master=self, text="Time Unit")
        self.button_mass.grid(row=6, column=0, padx=200, pady=10)
        self.button_electric = CTkButton(master=self, text="Electric Unit")
        self.button_electric.grid(row=7, column=0, padx=200, pady=10)
        self.button_temperature = CTkButton(master=self, text="Temperature Unit")
        self.button_temperature.grid(row=8, column=0, padx=200, pady=10)
        self.button_substances = CTkButton(master=self, text="Substances Unit")
        self.button_substances.grid(row=9, column=0, padx=200, pady=10)




    # callback function for the option menu
    def callback_change_appearance(self, value):
        if value == "Dark":
            self._set_appearance_mode("dark")
            self.label_appearance.configure(text_color="white", bg_color="#242424")
            self.label_buttons.configure(text_color="white", bg_color="#242424")

        elif value == "Light":
            self._set_appearance_mode("light")
            self.label_appearance.configure(text_color="black", bg_color="transparent")
            self.label_buttons.configure(text_color="black", bg_color="transparent")



    # callback to open time window
    def callback_time_unit(self):
        if self.mass_window is None or not self.mass_window.winfo_exists(): # checks if the window is existing, if not create
            self.mass_window = MassWindow()


        else:
            self.mass_window.focus() # if already exists, then just focus on it



    # callback to open length  window
    def callback_length_unit(self):
        if self.length_window is None or not self.length_window.winfo_exists(): # checks if the window is existing, if not create
            self.length_window = LengthWindow()


        else:
            self.length_window.focus() # if already exists, then just focus on it








if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
