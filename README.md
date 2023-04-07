# undetectable-selenium-connection

How to start Undetectable profiles with API and connect them with Selenium using Python

With that code you can use Selenium with Undetectable browser profiles. 
You can download and try Undetectable browser for free from: https://undetectable.io 

We recommend to use our webdriver that you can download from link: 
https://undetectable.io/download/chromedriver.exe
You need to save this file in folder with script.py.

This script will start Undetectable profiles that stored in folder "test" one by one and open few sites in these profiles. 

How to use:
1. Install Python (you can download it from https://www.python.org/)
2. run in terminal with admin rules: 
  pip install selenium
  pip install requests
3. download chromedriver and put it to folder with script.py
4. open Undetectable browser, create few profiles and choose folder with name "test" for them.
5. run in terminal: python script.py
