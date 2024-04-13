import yaml
import os
import subprocess
import random
from time import sleep


def job(episode):
    """Download podcast episode as mp3 file using youtube-dl."""
    print('-{}'.format(episode), end='')
    if os.path.exists('data/raw/{}.mp3'.format(episode)):
        return
    #
    for _ in range(13):
        try:
            subprocess.call(
                [
                    'youtube-dl',
                    '-x',
                    '--audio-format', 'mp3',
                    '--audio-quality', '5',
                    '-o',
                    'data/raw/{}.%(ext)s'.format(episode),
                    cache[episode]['link']
                ]
            )
            return
        except Exception:
            sleep(random.randint(3, 300))
    #
    sleep(random.randint(3, 300))


if __name__ == '__main__':
    cache = yaml.safe_load(open('data.yaml', 'r'))
    for episode in cache:
        if cache[episode]['year'] in [2022, 2023]:
            job(episode)
