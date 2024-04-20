import flet as ft
from datetime import datetime, timedelta


class StopWatch(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.start_time = None
        self.cnt = 0
        self.running = False

    def build(self):
        self.text = ft.Text(str(timedelta(seconds=self.cnt)))
        start_btn = ft.ElevatedButton("Start", on_click=self.start)
        stop_btn = ft.ElevatedButton("Stop", on_click=self.stop)
        reset_btn = ft.ElevatedButton("Reset", on_click=self.reset)
        return ft.Column([self.text, start_btn, stop_btn, reset_btn])

    def start(self, e):
        self.start_time = datetime.now()
        self.running = True
        while self.running:
            if datetime.now() - self.start_time > timedelta(seconds=1):
                self.start_time = datetime.now()
                self.cnt += 1
                self.text.value = str(timedelta(seconds=self.cnt))
                self.update()

    def stop(self, e):
        self.running = False
        self.update()

    def reset(self, e):
        self.cnt = 0
        self.text.value = str(timedelta(seconds=self.cnt))
        self.update()
