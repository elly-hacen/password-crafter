from customtkinter import CTkLabel


class Label:
    def __init__(self, **kwargs):
        self.master = kwargs.get('master', None)
        self.text = kwargs.get('text', '')
        self.fg_color = kwargs.get('fg_color', 'transparent')
        self.font = kwargs.get('font', ("DIN Condensed Web", 18))
        self.text_color = kwargs.get('text_color', 'white')
        self.justify=kwargs.get('justify', None)


        self.label = CTkLabel(
            text=self.text,
            font=self.font,
            master=self.master,
            fg_color=self.fg_color,
            text_color=self.text_color,
            justify=self.justify
            
        )

    def get_place(self, **kwargs):
        self.label.place(relx=kwargs.get('relx', 0.5), rely=kwargs.get('rely', 0.5))
        return self.label
