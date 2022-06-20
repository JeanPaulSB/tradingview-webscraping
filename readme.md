# Web Scraping Project with Python using Selenium
# Libraries used
 -  Pandas
 -  Selenium
# Description
In this project, our main goal was extracting data about some Technical Indicators related to Nasdaq 100 in order to compute a sucess score in a speficic atcion (selling/buying) aiming to maximize profits.
# Key features of project
    - Performing calculations two times per minute
    - The webpage source of data was TradingView and in order to download it 
    we must have been logged in previously, so it was a key factor 
    because coding automatic login would cost us around 15s-20s per execution, 
    our solution was implemented by saving logged info in a local folder and after that our session will keep being signed in Chromium.

    - Using DOM Implicitly Wait implemented in Selenium, thanks to that our program will run as fast as it can acess to DOM elements to perform the desired operations .
    (This is way better than using time sleep because it means to wait a constant amount of time during every execution that could lead to overwating or underwaiting also leading the program to crash)
    * Implicitly wait fetches DOM every time until it found the required element *

