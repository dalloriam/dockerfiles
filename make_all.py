from argparse import ArgumentParser

from dalloriam.system.path import location

import os
import sh


def build_single(user: str, dir: str, push: bool) -> None:
    with location(dir):
        image = f'{user}/{dir}'
        print(f'Building {image}...')
        sh.docker.build('-t', image, '.')

        if push:
            print(f'Pushing {image}...')
            sh.docker.push(image)


def build_all(username: str, push: bool) -> None:
    for f in os.listdir('.'):
        if os.path.isdir(f) and not f.startswith('.'):
            build_single(username, f, push)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--uname', '-u')
    parser.add_argument('--push', '-p', action='store_true')

    args = parser.parse_args()
    build_all(args.uname, args.push)