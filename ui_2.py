from flet import Column, UserControl, IconButton, icons


class Page2():
    def __init__(self, page):
        self.page = page
        self.page.title = "EasyArch Uti"
        self.page.update()
    def build(self):

        return (
            IconButton(
                icon=icons.ARROW_RIGHT_ALT
            )
        )
