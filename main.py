from random import choice
from tkinter import StringVar, END, IntVar
from customtkinter import CTk, set_appearance_mode
from widgets import Button, EntryBox, Label, Slider, CheckBox
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


class App(CTk):
    def __init__(self):
        super().__init__()
        self.length = 13 # Sets the initial length of the generated password to 13, which is a recommended password length
        self.title("Password Crafter")
        self.geometry("505x585")
        set_appearance_mode("Dark")
        self.resizable(False, False)
        self.ui_elements()

    def ui_elements(self):
        self.top_label()
        self.check_boxes()
        self.generate_button()
        self.password_count()
        self.password_display()
        self.check_boxes_label()
        self.password_count_label()
        self.password_length_slider()
        self.password_generating_logic()

    def top_label(self):
        label_texts = [
            'PASSWORD GENERATOR',
            'CREATE STRONG AND SECURE PASSWORD TO KEEP', 
            'YOUR ACCOUNTS SAFE ONLINE'
        ]
        label_sizes = [25, 18, 18]
        label_relx_values = [0.28, 0.18, 0.28]
        label_rely_values = [0.08, 0.15, 0.21]

        for i in range(len(label_texts)):
            label = Label(master=self, text=label_texts[i], font=('DIN Condensed Web', label_sizes[i]), text_color="#f2e7fe")
            label.get_place(relx=label_relx_values[i], rely=label_rely_values[i])


    def generate_button(self):
        Button(master=self, text="Generate",
               command=self.password_generating_logic).get_place(relx=0.73,
                                                                 rely=0.30)

    def password_count(self):
        self.integer_count = EntryBox(master=self,
                                      width=67, height=40,
                                      corner_radius=8,
                                      ).get_place(relx=0.40, rely=0.47)

    def password_display(self):
        self.password_displayed = EntryBox(master=self,
                                           width=300, height=43,
                                           corner_radius=0,
                                           ).get_place(relx=0.10, rely=0.3)

    def password_count_label(self):
        Label(master=self,
              text='PASSWORD COUNT: ').get_place(relx=0.11, rely=0.48)

    def password_length_slider(self):
        self.slider = Slider(
            master=self,
            width=395, height=18,
            command=self.change_password_length).get_place(
            relx=0.10,
            rely=0.6)

    def change_password_length(self, value):
        self.length = int(value)
        self.integer_count.configure(textvariable=StringVar(value=f"{self.length}"))
        self.password_generating_logic()

    def check_boxes(self):
         # Define labels for each checkbox
        self.checkbox_labels = ['Uppercase', 'Lowercase', 'Special Character', 'Numbers']
        # Create a list to hold the checkboxes and a list of IntVars to store their values
        self.checkboxes = []
        self.checkbox_vars = [IntVar() for _ in range(len(self.checkbox_labels))]
        # Loop through the checkbox labels and create a checkbox for each one
        for i, label in enumerate(self.checkbox_labels):
            # Create a checkbox with an IntVar to store its value and assign it to a variable
            self.checkbox = CheckBox(master=self,
                                     variable=self.checkbox_vars[i],
                                     command=self.password_generating_logic) \
                .get_place(relx=0.83, rely=0.70 + i * 0.07)

            self.checkboxes.append(self.checkbox)

    def check_boxes_label(self):
        """
           Creates labels for each checkbox option and places them on the GUI.
           Returns: None
        """
        text = self.checkbox_labels
        for i in range(len(text)):
            Label(master=self, text=text[i]).get_place(relx=0.11, rely=0.70 + i * 0.07)

    def password_generating_logic(self):

        """
        Password_generating_logic(self) -> None
        Generates a password based on user input and updates the password display.
        """

        def generate_password(uppercase, lowercase, numbers, special_chars, length):

            """
            This function first gets the user's selected options for uppercase letters,
            lowercase letters, numbers, and special characters. It then calls the `generate_password`
            function to generate a random password based on these options and the length
            chosen by the user using the slider.

            Finally, it updates the password display with the newly generated password.
            If the slider is not moved, the length of the password is set to a default value of 13.

            If there is an `IndexError` during password generation, the function does nothing.

            :param uppercase:
            :param lowercase:
            :param numbers:
            :param special_chars:
            :param length:
            :return:
            """
            try:
                chars = ''
                # If the checkbox for uppercase letters is checked, add uppercase letters to chars
                if uppercase:
                    chars += ascii_uppercase
                # If the checkbox for lowercase letters is checked, add lowercase letters to chars
                if lowercase:
                    chars += ascii_lowercase
                # If checkbox for numbers is checked, add numbers to chars
                if numbers:
                    chars += digits
                #  If the checkbox for special characters is checked, add special characters to chars
                if special_chars:
                    chars += punctuation
                # Use random.choice() to generate a random password with the specified length
                password_string = ''.join(choice(chars) for _ in range(length))
                return password_string
            # Catch an IndexError exception that may occur if length is less than or equal to 0
            except IndexError:
                pass

        # Clear the password displayed in the GUI for displaying the next iteration
        self.password_displayed.delete(0, END)
        # Set the maximum password length to 40
        length = min(self.length, 40)

        # Get the current value of each checkbox
        uppercase_letters = self.checkbox_vars[0].get()
        lowercase_letters = self.checkbox_vars[1].get()
        special_characters = self.checkbox_vars[2].get()
        integer_numbers = self.checkbox_vars[3].get()

        if self.slider.get():
            password = generate_password(uppercase_letters, lowercase_letters,
                                         integer_numbers, special_characters, length)
            self.password_displayed.configure(textvariable=StringVar(value=password))


if __name__ == '__main__':
    app = App()
    app.mainloop()
