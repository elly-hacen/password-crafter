from tkinter import StringVar
from customtkinter import CTkEntry


class EntryBox:
    def __init__(self, **kwargs):
        self.entry_box = CTkEntry(
            master=kwargs.get('master'),
            width=kwargs.get('width', 10),
            height=kwargs.get('height', 1),
            corner_radius=kwargs.get('corner_radius', 5),
            font=("Calibri", 17),
            placeholder_text=kwargs.get('placeholder_text', ''),
            textvariable=StringVar(value=kwargs.get('value', '13'))
        )

    def get_place(self, **kwargs):
        self.entry_box.place(relx=kwargs['relx'], rely=kwargs['rely'])
        return self.entry_box
    
