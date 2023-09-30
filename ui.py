import flet
from flet import Page, UserControl, Column, Container, colors, border_radius, padding, Text, Row, ElevatedButton, icons, IconButton,Dropdown, dropdown


class App(UserControl):
    def __init__(self, style):
        super().__init__()
        self.style = style

    def build(self):
        return Column(
            controls=[
                Container(
                    bgcolor=self.style["bg-color"],
                    width=450,
                    height=550,
                    border_radius=self.style["border-radius"],

                    content=(
                        Column(
                            alignment="center",
                            horizontal_alignment="center",
                            controls=[
                                Container(
                                    width=430,
                                    height=530,

                                    content=(
                                        Column(

                                            controls=[
                                                Row(
                                                    expand=True,
                                                    alignment=flet.MainAxisAlignment.CENTER,
                                                    vertical_alignment=flet.CrossAxisAlignment.START,

                                                    controls=[
                                                        Text("Hello!",
                                                             size=25,

                                                             )
                                                    ]
                                                ),
                                                Row(
                                                    expand=True,
                                                    alignment=flet.MainAxisAlignment.CENTER,
                                                    controls=[
                                                        ElevatedButton(
                                                            text="Start Installation",
                                                            icon=icons.ARROW_RIGHT,
                                                            color=self.style["text-color"],
                                                            scale=1.2
                                                        )
                                                    ]
                                                ),
                                                Row(
                                                    expand=True,
                                                    alignment=flet.MainAxisAlignment.CENTER,
                                                    vertical_alignment=flet.CrossAxisAlignment.START,
                                                    controls=[
                                                        Column(
                                                            expand=True,
                                                               alignment=flet.MainAxisAlignment.END,
                                                               horizontal_alignment=flet.CrossAxisAlignment.START,
                                                               controls=[
                                                                    IconButton(
                                                                        icon=icons.POWER_SETTINGS_NEW,
                                                                        scale=1.3

                                                                    )
                                                               ]
                                                               ),
                                                        Column(
                                                            width=175,

                                                            alignment=flet.MainAxisAlignment.END,
                                                            horizontal_alignment=flet.CrossAxisAlignment.CENTER,
                                                            controls=[
                                                                Dropdown(
                                                                    width=200,
                                                                    height=45,

                                                                    tooltip="Select Language",
                                                                    hint_text="Select Language",

                                                                    options=[
                                                                        dropdown.Option("English")
                                                                    ]
                                                                )

                                                            ]
                                                        ),
                                                        Column(expand=True,
                                                               alignment=flet.MainAxisAlignment.END,
                                                               horizontal_alignment=flet.CrossAxisAlignment.CENTER,
                                                               controls=[

                                                               ]
                                                               ),

                                                    ]
                                                )
                                            ]
                                        )
                                    )
                                )
                            ]
                        )

                    )

                )
            ]

        )


def main(page: Page):
    page.title = "EasyArch Utily"
    page.window_height = 600
    page.window_width = 500
    style = {
        "text-color": colors.WHITE,
        "secondary-bg-color": colors.WHITE60,
        "bg-color": colors.BLACK12,
        "border-radius": 8
    }
    app = App(style)
    page.add(app)
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    page.update()


flet.app(main)
