from customtkinter import CTkButton


class Button:
    def __init__(self, **kwargs):
        self.button = CTkButton(
            image=kwargs.get('bg', None),
            master=kwargs.get('master', None),
            width=kwargs.get('width', 75),
            height=kwargs.get('height', 43),
            border_width=kwargs.get('border_width', 0),
            fg_color=kwargs.get('fg_color', '#654E92'),
            text_color=kwargs.get('text_color', 'white'),
            hover_color=kwargs.get('hover_color', '#6C9BCF'),
            text=kwargs.get('text', 'Hmm'),
            command=kwargs.get('command', None)
        )

    def get_place(self, **kwargs):
        self.button.place(relx=kwargs.get('relx', 0), rely=kwargs.get('rely', 0))
        return self.button

