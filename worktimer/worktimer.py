""" Analytics-enabled work timing script. """
from dalloriam.datahose.client import DatahoseClient

from http import HTTPStatus

from time import sleep

import os
import requests
import subprocess
import tqdm

ORC_PORT = os.getenv('ORC_PORT', '8080')
OS_TYPE = os.getenv('HOST_OS', 'linux-gnu')

# Workaround since --net=host is not supported on mac
ORC_HOST = 'docker.for.mac.host.internal' if OS_TYPE.startswith('darwin') else 'localhost'


def send_message(title: str, message: str) -> None:
    # TODO: Enable only if ORC supports notifications on this machine.
    resp = requests.post(f'http://{ORC_HOST}:{ORC_PORT}/local/notify', json={'title': title, 'message': message})

    if resp.status_code != HTTPStatus.OK:
        raise ValueError(resp.text)


class WorkTimer:

    def __init__(self):
        # self._client = DatahoseClient()
        pass

    def run(self, title: str, minutes: int) -> None:
        send_message("Work Timer", title)
        seconds = minutes * 60
        for _ in tqdm.tqdm(range(seconds), desc=title, total=seconds):
            sleep(1)

    def log_task(self):
        send_message("Work Timer", "Time to start task!")
        task_goal = input('Enter next task goal: ').strip()
        self.run('Task Start', minutes=25)
        return
        # TODO: Fix datahose push
        try:
            self._client.push(
                key='work.pomodoro.task',
                data={
                    'description': task_goal
                }
            )
        except Exception as e:
            print(f'Error pushing task to datahose: {e}.')

    def start(self):
        while True:
            for i in range(4):
                self.log_task()
                if i != 3:
                    self.run("Short Break!", minutes=5)

            self.run("Long Break!", minutes=15)


def main():
    w = WorkTimer()
    w.start()


if __name__ == '__main__':

    main()
