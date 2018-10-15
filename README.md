# automaton-v3
Automation framework (UI) - an example. Based on Python, Selenium, and Pytest

[![Build Status](https://travis-ci.org/BurhanH/automaton-v3.svg?branch=master)](https://travis-ci.org/BurhanH/automaton-v3)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/83a77e1b4a8242e6a4006e0f4ef0d928)](https://app.codacy.com/app/BurhanH/automaton-v3?utm_source=github.com&utm_medium=referral&utm_content=BurhanH/automaton-v3&utm_campaign=Badge_Grade_Dashboard)

## Requirements
Python 3.6.\*, Selenium 3.14.0, Pytest 3.8.1, <br> 
virtualenv (virtual environment manager), <br>
Firefox 62.\*, geckodriver 0.22, <br> 
Chrome 69.*, chromedriver 2.42 <br>

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
1) Go to any UI scenario and change the value of the `BROWSER` variable from `firefox` to `chrome`. Note! Before execution read steps 5-6 from [How to prepare environment](https://github.com/BurhanH/automaton-v3#how-to-prepare-environment) section

To be continue ...
