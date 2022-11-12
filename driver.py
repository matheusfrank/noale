from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

import time

driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))  # Optional argument, if not specified will search path.
path = '/home/matheus/prog/python/noale/data/'

with open(path+'data.txt', 'w') as data:
    data.write(f'Coordenadas Geográficas\tCidade, Estado, País\tSpecific photovoltaic power output\n')
    with open(path+'urls.txt') as urls:
        for line in urls:
            URL = line
            driver.get(URL)
            time.sleep(3)
            try:
                value = float(driver.find_element(By.XPATH, '/html/body/gsa-app/div/div/main/ng-component/section/gsa-map-sidebar/aside/div/gsa-map-sidebar-site/gsa-section[1]/section/div[3]/gsa-card/div/gsa-site-data/mat-list/mat-list-item[1]/div/gsa-site-data-item/div/div[4]/sg-unit-value/sg-unit-value-inner').text)
                coords = str(driver.find_element(By.XPATH, '/html/body/gsa-app/div/div/main/ng-component/section/gsa-map-sidebar/aside/div/gsa-map-sidebar-site/section[1]/gsa-selected-site/div/div[1]/sg-unit-toggle-value/span/span/sg-unit-value-inner').text)
                location = str(driver.find_element(By.XPATH, '/html/body/gsa-app/div/div/main/ng-component/section/gsa-map-sidebar/aside/div/gsa-map-sidebar-site/section[1]/gsa-selected-site/div/div[2]').text)
                data.write(f'{coords}\t{location}\t{value}\n')
            except NoSuchElementException:
                time.sleep(3)
                value = float(driver.find_element(By.XPATH, '/html/body/gsa-app/div/div/main/ng-component/section/gsa-map-sidebar/aside/div/gsa-map-sidebar-site/gsa-section[1]/section/div[3]/gsa-card/div/gsa-site-data/mat-list/mat-list-item[1]/div/gsa-site-data-item/div/div[4]/sg-unit-value/sg-unit-value-inner').text)
                coords = str(driver.find_element(By.XPATH, '/html/body/gsa-app/div/div/main/ng-component/section/gsa-map-sidebar/aside/div/gsa-map-sidebar-site/section[1]/gsa-selected-site/div/div[1]/sg-unit-toggle-value/span/span/sg-unit-value-inner').text)
                location = str(driver.find_element(By.XPATH, '/html/body/gsa-app/div/div/main/ng-component/section/gsa-map-sidebar/aside/div/gsa-map-sidebar-site/section[1]/gsa-selected-site/div/div[2]').text)
                data.write(f'{coords}\t{location}\t{value}\n')