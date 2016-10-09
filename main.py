from test1 import get_site
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


mcheza_odds = {}
drivers = get_site("featured-matches")
for driver in drivers:
    sport_item = driver.find_elements_by_class_name('sport-item')
    for i in range(1):# len(sport_item)):
        mcheza_odds.setdefault(sport_item[i].text,{})
        while True:
            try:
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "matches-show-more")))
                for l in driver.find_elements_by_class_name("matches-show-more"):
                    l.click()
            except:
                break

        sport_item[i].click()
        matches_set = driver.find_element_by_class_name("match-section-sport-content")
        match_teams = driver.find_elements_by_class_name('match-teams')
        matches = driver.find_element_by_class_name('matches-set')
        match_cont = driver.find_elements_by_class_name('match')
        for team in range(len(match_teams)):
            try:
                mcheza_odds[sport_item[i].text].setdefault(match_teams[team].find_element_by_class_name('match-link').text, {
                'Time': match_cont[team].find_element_by_class_name("match-time").text,
                'Date': match_cont[team].find_element_by_class_name('match-date').text,
                'match-code': match_cont[team].find_element_by_class_name('match-code').text,
                'Match-category': match_cont[team].find_element_by_class_name('category-link').text,
                'League-division': match_cont[team].find_element_by_class_name('tournament-link').text,
                '1': match_cont[team].find_element_by_class_name('selection-button-1').find_element_by_class_name('sel-odds').text,
                'x': match_cont[team].find_element_by_class_name('selection-button-X').find_element_by_class_name('sel-odds').text,
                '2': match_cont[team].find_element_by_class_name('selection-button-2').find_element_by_class_name('sel-odds').text,
                'u': match_cont[team].find_element_by_class_name('selection-button-Under').find_element_by_class_name('sel-odds').text,
                'o': match_cont[team].find_element_by_class_name('selection-button-Over').find_element_by_class_name('sel-odds').text,
                })
            except:
                pass
with open('./mcheza.py', 'w') as fout:
    fout.write('all_date = ' + pprint.pformat(mcheza_odds)
keys = mcheza_odds.keys()
'''for i in keys:
    name = i + '.csv'
    ndict = mcheza_odds[i].keys()
    with open(name, 'w') as fout:
        try:
            dict_writer = csv.DictWriter(fout, ndict)
            dict_writer.writeheader()
            for val in mcheza_odds[i].values():
                dict_writer.writerow(val)
        except ValueError:
            continue''' # work on progress
