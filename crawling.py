import os
import random
import yaml
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
launch_options = Options()
launch_options.add_argument('--headless')
launch_options.add_argument('--no-gpu')


def _get_data(episode):
    """
    Extract data from web page:
    - release date
    - title
    - duration
    - YouTube link for audio downloading
    - number of listenings at SoundCloud
    """
    driver = webdriver.Chrome(options=launch_options)
    driver.get('https://www.superdatascience.com/{}'.format(episode))
    driver.implicitly_wait(10)
    #
    data = {episode: {}}
    # release date
    date = driver.find_elements(
        webdriver.common.by.By.XPATH,
        "//div[@class='information']/p"
    )[1].text
    dow, month, day, year = date.split()
    #
    data[episode]['day'] = int(day.replace(',', ''))
    data[episode]['dow'] = dow  # day of week
    data[episode]['month'] = month
    data[episode]['year'] = int(year)
    # title
    data[episode]['title'] = driver.find_elements(
        webdriver.common.by.By.XPATH,
        "//div[@class='content-wrapper']/h2"
    )[0].text
    # duration in minutes
    duration = driver.find_elements(
        webdriver.common.by.By.XPATH,
        "//p[@class='read-time']"
    )[0].text
    data[episode]['duration'] = int(duration.split()[0])
    # YouTube link
    data[episode]['link'] = driver.find_elements(
        webdriver.common.by.By.TAG_NAME,
        'iframe'
    )[1].get_attribute('src')
    # number of listenings
    driver.switch_to.frame(0)
    stats = driver.find_element(
        webdriver.common.by.By.XPATH,
        "//span[@class='sc-ministats sc-font-tabular sc-ministats-small sc-ministats-plays']"
    ).get_attribute('title')
    data[episode]['stats'] = float(stats.split('K')[0])
    #
    driver.close()
    #
    return data


def get_data(episode):
    """
    Driver function for `_get_data`
    addressing possible exceptions and blockings.
    """
    for _ in range(13):
        try:
            return _get_data(episode)
        except Exception:
            print('!', end='')
            sleep(random.randint(0, 60))


def job(episodes, cache_file):
    """
    Get and save information about every podcast episode in the list.
    """
    cache = yaml.safe_load(open(cache_file)) if os.path.exists(cache_file) else {}
    #
    while episodes:
        print('.', end='')
        #
        episode = random.choice(episodes)
        episodes.remove(episode)
        #
        data = get_data(episode)
        if not data:
            continue
        cache.update(data)
        #
        sleep(random.randint(0, 60))

    yaml.safe_dump(
        cache,
        open(cache_file, 'w'),
        default_flow_style=False,
        sort_keys=False,
        allow_unicode=True
    )


if __name__ == '__main__':
    job(
        list(range(537, 745)),
        'data.yaml'
    )
