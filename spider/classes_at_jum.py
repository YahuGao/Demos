#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore")

url = 'https://catalog.jmu.edu/content.php?catoid=43&navoid=1740'

failed = []


def get_description(url):
    request_header = {
        'Host': 'catalog.jmu.edu',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0'
    }
    req = requests.get(url, headers=request_header, verify=False)
    req.encoding = 'utf-8'
    html = req.text

    bs = BeautifulSoup(html, 'lxml')
    description = bs.find('div', class_='').text.strip()
    return description


if False:
    debug_url = 'https://catalog.jmu.edu/ajax/preview_course.php?catoid=43&coid=158080&display_options=a:2:{s:8:~location~;s:8:~template~;s:28:~course_program_display_field~;N;}&show'
    description = get_description(debug_url)
    print(description)
    exit()


def get_classes(url):
    result = []
    req = requests.get(url=url, verify=False)  # headers=request_headers)
    req.encoding = 'utf-8'
    html = req.text
    bs = BeautifulSoup(html, 'lxml')
    table = bs.find('table', class_='table_default')

    classes_items = table.find_all('td', class_='width')
    try:
        with tqdm(classes_items) as classes:
            for class_item in classes:
                description_url_prev = 'https://catalog.jmu.edu/ajax/'
                description_url_class = class_item.a['href'] + \
                    '&display_options='
                description_url_class = description_url_class.replace(
                    '_nopop', '')
                description_url_suff = class_item.a['onclick'].split(
                    "'")[-2] + "&show"
                description_url = description_url_prev + \
                    description_url_class + description_url_suff
                # print(description_url)
                title = class_item.text.split('\t')[-1].strip()
                code = title.split('.')[0]
                name = title.split('.')[1]
                description = get_description(description_url)
                if description.startswith(title):
                    description = description[len(title):].strip()
                    unknown_number = re.search(            # e.g. 1.00 - 3.00
                        r'^\d+\.\d+(\ ?-\ ?\d+\.\d+)?', description)
                    if unknown_number:
                        description = description.replace(
                            unknown_number.group(0), unknown_number.group(0) + '\n')
                    cross_listed = re.search(
                        r'Crosslisted with: [A-Z]{3,}\ \d{3,}', description)
                    if cross_listed:
                        description = description.replace(
                            cross_listed.group(0), cross_listed.group(0) + '\n')
                    description = description.replace(
                        'Prerequisite', '\nPrerequisite')
                result.append(
                    [title, code, name, description])
    except KeyboardInterrupt:
        classes.close()
        raise

    return result


url_prev = 'https://catalog.jmu.edu/content.php?catoid=43&catoid=43&navoid=1740&filter[item_type]=3&filter[only_active]=1&filter[3]=1&filter[cpage]='
url_suff = '#acalog_template_course_filter'

results = []
for page in range(1, 14):
    page_url = url_prev + str(page) + url_suff
    page_result = get_classes(page_url)
    results.extend(page_result)

df = pd.DataFrame(results, columns=[
                  'title', 'code', 'name', 'description'])
df.to_excel('jmu.xls', index=False)
print('failed number:', len(failed))
