from Breezypythongui import EasyFrame

class LabelDemo(EasyFrame):
    '''
    Displays a greeting in a window.
    '''

    def __init__(self)_:
    """
    Set up the window and the label
    """
    EasyFrame.__init__(self):
    self.addLabel(text="Hello world!", row=0, column=0)


def main() -> None:
    """
    Instantiates and pops up the window.
    :return:
    """
    LabelDemo().mainloop()