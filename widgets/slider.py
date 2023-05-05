from customtkinter import CTkSlider


class Slider:
    def __init__(self, **kwargs):
        self.slider = CTkSlider(
            from_=0,
            to=40,
            master=kwargs['master'],
            width=kwargs.get('width', 200),
            height=kwargs.get('height', 10),
            command=kwargs.get('command', None)
        )

        self.slider.set(13)

    def get_place(self, **kwargs):
        self.slider.place(relx=kwargs['relx'], rely=kwargs['rely'])
        return self.slider
