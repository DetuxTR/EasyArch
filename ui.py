import flet
import ui_2
from flet import Page, UserControl, Column, Container, colors, border_radius, padding, Text, Row, ElevatedButton, icons, \
    IconButton, Dropdown, dropdown, FontWeight, AlertDialog, Theme, OutlinedButton, ButtonStyle, RoundedRectangleBorder, BorderSide, Border


class App(UserControl):
    def __init__(self, style):
        super().__init__()
        self.style = style

    def ret_page1(self):
        return (
            Column(
                controls=[

                    Container(
                        # bgcolor=self.style["bg-color"],
                        width=450,
                        height=550,
                        border_radius=self.style["border-radius"],


                        content=(
                            Column(
                                alignment=flet.MainAxisAlignment.CENTER,
                                horizontal_alignment=flet.CrossAxisAlignment.CENTER,
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
                                                            Column(
                                                                expand=True,
                                                                alignment=flet.MainAxisAlignment.START,
                                                                horizontal_alignment=flet.CrossAxisAlignment.START,
                                                                controls=[
                                                                    # IconButton(
                                                                    #     icon=icons.INFO,
                                                                    #     scale=0.8,
                                                                    #     on_click=self.show_inf_dialog
                                                                    #
                                                                    # )
                                                                ]
                                                            ),
                                                            Column(
                                                                expand=True,
                                                                # width=175,
                                                                alignment=flet.MainAxisAlignment.START,
                                                                horizontal_alignment=flet.CrossAxisAlignment.CENTER,
                                                                controls=[
                                                                    Text("Hello!",
                                                                         size=35,

                                                                         )
                                                                ]

                                                            ),
                                                            Column(
                                                                expand=True
                                                            ),

                                                        ]
                                                    ),
                                                    Row(
                                                        # expand=True,
                                                        width=430,
                                                        height=250,

                                                        alignment=flet.MainAxisAlignment.CENTER,
                                                        controls=[
                                                            Container(
                                                                expand=True,
                                                                # bgcolor=self.style["secondary-bg-color"]
                                                                content=(
                                                                    Column(
                                                                        expand=True,
                                                                        controls=[
                                                                            Row(
                                                                                expand=True,
                                                                                controls=[
                                                                                    Row(
                                                                                        expand=True,
                                                                                        controls=[
                                                                                            Container(
                                                                                                expand=True,
                                                                                                # bgcolor=self.style[
                                                                                                #     "secondary-bg-color"]
                                                                                                content=(
                                                                                                    OutlinedButton(
                                                                                                        text="Start "
                                                                                                             "Custom "
                                                                                                             "Installation",
                                                                                                        width=50,
                                                                                                        height=200,
                                                                                                        style=self.ret_main_button_style()

                                                                                                    )
                                                                                                )
                                                                                            )
                                                                                        ]
                                                                                    ),
                                                                                    Row(
                                                                                        expand=True,
                                                                                        controls=[
                                                                                            Container(
                                                                                                expand=True,
                                                                                                # bgcolor=self.style[
                                                                                                #     "secondary-bg-color"]
                                                                                                content=(
                                                                                                    OutlinedButton(
                                                                                                        text="Use a preset",
                                                                                                        width=50,
                                                                                                        height=200,
                                                                                                        style=self.ret_main_button_style()

                                                                                                    )
                                                                                                )
                                                                                            )
                                                                                        ]
                                                                                    )
                                                                                ]
                                                                            ),
                                                                            Row(
                                                                                expand=True,
                                                                                controls=[
                                                                                    Row(
                                                                                        expand=True,
                                                                                        controls=[
                                                                                            Container(
                                                                                                expand=True,
                                                                                                # bgcolor=self.style[
                                                                                                #     "secondary-bg-color"]
                                                                                                content=(
                                                                                                    OutlinedButton(
                                                                                                        text="Search "
                                                                                                             "Presets "
                                                                                                             "From "
                                                                                                             "Github",
                                                                                                        width=50,
                                                                                                        height=200,
                                                                                                        style=self.ret_main_button_style()

                                                                                                    )

                                                                                                )
                                                                                            )
                                                                                        ]
                                                                                    ),
                                                                                    Row(
                                                                                        expand=True,
                                                                                        controls=[
                                                                                            Container(
                                                                                                expand=True,
                                                                                                # bgcolor=self.style[
                                                                                                #     "secondary-bg-color"]
                                                                                                content=(
                                                                                                    OutlinedButton(
                                                                                                        text="Installer Settings",
                                                                                                        width=50,
                                                                                                        height=200,
                                                                                                        style=self.ret_main_button_style()

                                                                                                    )
                                                                                                )

                                                                                            )
                                                                                        ]
                                                                                    )
                                                                                ]
                                                                            ),

                                                                        ]

                                                                    )
                                                                )

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
                                                                        scale=1.3,
                                                                        tooltip="Shutdown",
                                                                        style=self.ret_main_button_style()

                                                                    )
                                                                ]
                                                            ),
                                                            Column(
                                                                width=175,

                                                                alignment=flet.MainAxisAlignment.END,
                                                                horizontal_alignment=flet.CrossAxisAlignment.CENTER,
                                                                controls=[


                                                                ]
                                                            ),
                                                            Column(expand=True,
                                                                   alignment=flet.MainAxisAlignment.END,
                                                                   horizontal_alignment=flet.CrossAxisAlignment.END,
                                                                   controls=[
                                                                       IconButton(
                                                                           icon=icons.EXIT_TO_APP,
                                                                           tooltip="Use arch in archiso enviroment(Live CD)",
                                                                           scale=1.3,
                                                                           style=self.ret_main_button_style()
                                                                       )
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
        )

    def ret_page2(self):
        return (
            Column(
                controls=[

                    Container(
                        bgcolor=self.style["bg-color"],
                        width=1800,
                        height=875,
                        border_radius=self.style["border-radius"],

                        content=(
                            Column(
                                alignment=flet.MainAxisAlignment.CENTER,
                                horizontal_alignment=flet.CrossAxisAlignment.CENTER,
                                controls=[
                                    Container(
                                        width=1750,
                                        height=860,

                                        content=(
                                            Column(

                                                controls=[

                                                    Row(

                                                        expand=True,
                                                        alignment=flet.MainAxisAlignment.CENTER,
                                                        vertical_alignment=flet.CrossAxisAlignment.START,

                                                        controls=[
                                                            Column(
                                                                expand=True,
                                                                alignment=flet.MainAxisAlignment.START,
                                                                horizontal_alignment=flet.CrossAxisAlignment.START,
                                                                controls=[
                                                                    IconButton(
                                                                        icon=icons.ARROW_BACK,
                                                                        scale=0.8,
                                                                        on_click=self.to_page1,
                                                                        tooltip="Adjust Settings"

                                                                    )
                                                                ]
                                                            ),
                                                            Column(
                                                                expand=True,
                                                                width=175,
                                                                alignment=flet.MainAxisAlignment.START,
                                                                horizontal_alignment=flet.CrossAxisAlignment.CENTER,
                                                                controls=[
                                                                    Text("Select Region",
                                                                         size=25,

                                                                         )
                                                                ]

                                                            ),
                                                            Column(
                                                                expand=True,
                                                                alignment=flet.MainAxisAlignment.START,
                                                                horizontal_alignment=flet.CrossAxisAlignment.END,
                                                                controls=[
                                                                    IconButton(
                                                                        icon=icons.ARROW_FORWARD,
                                                                        tooltip="Next Page",
                                                                        scale=0.8
                                                                    )
                                                                ]
                                                            ),

                                                        ]
                                                    ),
                                                    Row(
                                                        expand=True,
                                                        alignment=flet.MainAxisAlignment.CENTER,
                                                        controls=[

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

                                                                ]
                                                            ),
                                                            Column(
                                                                width=175,

                                                                alignment=flet.MainAxisAlignment.END,
                                                                horizontal_alignment=flet.CrossAxisAlignment.CENTER,
                                                                controls=[

                                                                ]
                                                            ),
                                                            Column(expand=True,
                                                                   alignment=flet.MainAxisAlignment.END,
                                                                   horizontal_alignment=flet.CrossAxisAlignment.END,
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
        )

    def build(self):
        return self.ret_page1()

    def to_page1(self, e):
        self.page.clean()
        self.page.window_height = 600
        self.page.window_width = 500
        self.page.update()
        self.page.add(
            self.ret_page1()

        )

    def show_inf_dialog(self, event):
        dlg = flet.AlertDialog(
            title=flet.Text("Easy Arch Utily Beta \nwritten by Detux"), on_dismiss=lambda e: print("Dialog dismissed!")
        )
        self.page.dialog = dlg
        dlg.open = True
        self.page.update()

    def show_dialog(self, dialog, event):
        dlg = flet.AlertDialog(
            title=flet.Text("{}".format(dialog)), on_dismiss=lambda e: print("Dialog dismissed!")
        )
        self.page.dialog = dlg
        dlg.open = True
        self.page.update()

    def to_page2(self, e):
        self.page.clean()
        self.page.window_height = 900
        self.page.window_width = 1750
        self.page.update()
        self.page.add(
            self.ret_page2()

        )

    def ret_main_button_style(self):
        return ButtonStyle(
            color=
            self.style[
                "text-color"],
            shape={
                flet.MaterialState.DEFAULT: RoundedRectangleBorder(
                    radius=20)
            },
            bgcolor=self.style["secondary-bg-color"],
            side=BorderSide(color=self.style["border-color"],width=1.2)

        )


def main(page: Page):
    page.title = "EasyArch Utily"
    page.window_height = 600
    page.window_width = 500
    page.fonts = {
        "Open Sans": "/fonts/OpenSans-Regular.ttf",
        "Roboto": "/fonts/Roboto-Regular.ttf"
    }
    style = {
        "text-color": colors.WHITE,
        "secondary-bg-color": colors.BLACK12,
        "bg-color": colors.BLACK38,
        "border-radius": 12,
        "main-ui-font": "Roboto",
        "border-color": colors.BLUE_50
    }
    app = App(style)
    page.bgcolor=style["bg-color"]
    page.add(app)
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.theme = Theme(
        font_family="Roboto",

    )

    page.update()


flet.app(main)
