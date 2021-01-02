# Automaton-v3
Automation testing framework (UI) - an example. Based on Python, Selenium, and Pytest

[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/BurhanH/automaton-v3/blob/master/LICENSE)
[![Build Status](https://travis-ci.org/BurhanH/automaton-v3.svg?branch=master)](https://travis-ci.org/BurhanH/automaton-v3)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/83a77e1b4a8242e6a4006e0f4ef0d928)](https://app.codacy.com/app/BurhanH/automaton-v3?utm_source=github.com&utm_medium=referral&utm_content=BurhanH/automaton-v3&utm_campaign=Badge_Grade_Dashboard)
[![HitCount](http://hits.dwyl.com/BurhanH/automaton-v3.svg)](http://hits.dwyl.com/BurhanH/automaton-v3)

## Requirements
Python 3.6.\*/3.7.\*, Selenium 3.141.0, Pytest 4.4.1, <br> 
virtualenv (virtual environment manager), <br>
Firefox 75.0, geckodriver 0.26.0, </br>
Chrome 81.0.4044.122, chromedriver 81.0.4044.69

## Project structure
```text
-- automaton-v3
   |-- .gitattributes
   |-- .gitignore
   |-- .travis.yml
   |-- LICENSE
   |-- README.md
   |-- requirements.txt
   `-- tests
       |-- __init__.py
       |-- test_browser.py
       |-- test_initial.py
```

## How to prepare environment
1) Install [Python](https://www.python.org/downloads/)
2) Install and configure [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
3) Clone or copy (download) the repository into your virtual environment
4) Activate virtual environment, move to `automaton-v3` folder, and execute command `pip install -r requirements.txt`
5) Install Firefox / Chrome web browser
6) Download, extract and move geckodriver / chromedriver into `bin` folder for Mac/Linux, `Scripts` folder for Windows on virtual environment

## How to run tests
1) Open terminal window
2) Move to virtual environment folder
3) Activate virtual environment 
4) Move to `automaton-v3` folder
5) Execute `pytest`

## How to run test/s in Chrome browser
Go to any UI scenario and change the value of the `BROWSER` variable from `firefox` to `chrome`. <br> Note! Before execution read steps 5-6 from [How to prepare environment](https://github.com/BurhanH/automaton-v3#how-to-prepare-environment) section

## Technology stack and helpful info
[Python 3.6](https://docs.python.org/3.6/) / [Python 3.7](https://docs.python.org/3.7/) <br>
[virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/) <br>
[GitHub, cloning repository](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) <br>
[Pytest](https://docs.pytest.org/en/latest/contents.html#toc) <br>
[Selenium](https://www.selenium.dev/documentation/en/) <br>
[Firefox](https://www.mozilla.org/en-US/firefox/) <br>
[geckodriver](https://github.com/mozilla/geckodriver/releases) <br>
[Chrome](https://www.google.com/chrome/) <br>
[ChromeDriver](https://chromedriver.chromium.org/downloads) <br>
