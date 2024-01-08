import yaml
import os
import subprocess
import random
from time import sleep

cache = yaml.safe_load(open('data.yaml', 'r'))

episodes = [
    episode for episode in cache
    if cache[episode]['year'] == 2022 #and cache[episode]['dow'] not in ('Friday', 'Wednesday')
]

for episode in episodes:
    print('-{}'.format(episode), end='')
    if os.path.exists('data/raw/{}.wav'.format(episode)):
        continue
    #
    for _ in range(13):
        try:
            output = subprocess.check_output(
                [
                    'youtube-dl',
                    '-x',
                    '--audio-format', 'wav',
                    '--audio-quality', '0',
                    '-o',
                    'data/raw/{}.%(ext)s'.format(episode),
                    '{}'.format(cache[episode]['link'])
                ]
            )
            break
        except Exception:
            sleep(random.randint(0, 300))
    #
    sleep(random.randint(0, 300))
