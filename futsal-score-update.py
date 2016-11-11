#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re


def get_data():
    ranking = 'rangschikking'
    results = 'wedstrijden'
    region = 'namur'
    division = '4ième Provinciale B'

    url = 'http://www.automaticresults.be/' + region + '.aspx'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html5lib')

    data_ranking = soup.find(id=ranking).find('th', text=division).parent.parent if len(soup.find(id=ranking).findChildren()) > 1 is not None else None
    element_results = soup.find(id=results).find('th', text=division).parent

    data_results = []
    next_element = element_results.findNext('tr')
    while True:
        if len(next_element.find_all('td')) > 1:
            data_results.append(next_element)
            next_element = next_element.findNext('tr')
        else:
            break

    return data_ranking, data_results


def update_data(file_path, soup_data):
    file_handle = open(file_path, 'r+')
    html = file_handle.read()
    soup = BeautifulSoup(html, 'html5lib')

    # Maj classement
    if soup_data[0] is not None:
        soup.find(id='classement').tbody.replaceWith(soup_data[0])

    # Maj scores
    if soup_data[1] is not None:
        # Pour chaque resultat
        for result in soup_data[1]:
            # Déterminer si la ligne existe déjà sur base du numéro du match
            tmp = soup.find('td', text=result.find('td').text)
            existing_element = tmp.parent if tmp is not None else None
            # Mise en forme CSS selon le résultat du match
            update_winlose(result)
            if existing_element is not None:
                # Si oui, on l'écrase
                existing_element.replaceWith(result)
            else:
                # Si non, on l'ajoute
                tbody = soup.find(id='matches').tbody
                tbody.append('\t')
                tbody.append(result)
                tbody.append('\n\t\t\t\t')

    file_handle.seek(0)
    file_handle.truncate()
    file_handle.write(str(soup))
    file_handle.close()


def update_winlose(result):
    search = result.find('td', text=re.compile('NAMUR CITY.*'))
    if search is not None:
        tds = result.findAll('td')
        index = tds.index(search)
        score = tds[7].text.split()
        if len(score) == 3:
            if (index == 6 and int(score[0]) < int(score[2])) or (index == 5 and int(score[0]) > int(score[2])):
                result['class'] = result.get('class', []) + ['success']
            elif int(score[0]) == int(score[2]):
                pass
            else:
                result['class'] = result.get('class', []) + ['danger']
    return

print 'Retrieving results from web...'
update_data('index.html', get_data())
print 'Done.'
