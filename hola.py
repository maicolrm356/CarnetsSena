from typing import Any, Sequence
import flet as ft

# python hola.py
# generar requirements.txt: pip freeze > requirements.txt


def main(page: ft.Page):
    page.title = 'Generar Carnets'
    page.bgcolor = "#23a80c"
    page.add(ft.Text("Hello Mundillo"))
    #page.update()

ft.app(main)