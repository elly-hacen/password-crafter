from customtkinter import CTkCheckBox

class CheckBox:
    def __init__(self, **kwargs):
        self.checkbox = CTkCheckBox(
            master=kwargs.get('master'),
            text=kwargs.get('text', ''),
            width=kwargs.get('width', 10),
            height=kwargs.get('height', 10),
            variable=kwargs.get('variable'),
            command=kwargs.get('command')
        )

    def get_place(self, **kwargs):
        self.checkbox.place(relx=kwargs['relx'], rely=kwargs['rely'])
        return self.checkbox
