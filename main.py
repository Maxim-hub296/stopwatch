import flet as ft
from App import StopWatch


def main(page: ft.Page):
    page.window_width = 250
    page.window_height = 200
    page.title = "Stopwatch"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.update()

    sw = StopWatch()
    page.add(sw)


if __name__ == '__main__':
    ft.app(target=main)
