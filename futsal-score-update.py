#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests


def get_data():
    ranking = 'rangschikking'
    results = 'wedstrijden'
    region = 'namur'
    division = '4ième Provinciale B'

    url = 'http://www.automaticresults.be/' + region + '.aspx'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html5lib')

    data_ranking = soup.find(id=ranking).find('th', text=division).parent.parent
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
    soup.find(id='classement').tbody.replaceWith(soup_data[0])

    # Maj scores
    html_matches = soup.find(id='matches')
    # Pour chaque resultat
    for result in soup_data[1]:
        # Déterminer si la ligne existe déjà sur base du numéro du match
        existing_element = soup.find('td', text=result.find('td').text).parent
        if existing_element is not None:
            # Si oui, on l'écrase
            existing_element.replaceWith(result)
        else:
            # Si non, on l'ajoute
            html_matches.append(existing_element)

    file_handle.seek(0)
    file_handle.truncate()
    file_handle.write(str(soup))
    file_handle.close()

update_data('index.html', get_data())
print 'DONE'
