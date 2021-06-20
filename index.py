from flask import Flask,render_template
from bs4 import BeautifulSoup
from selenium import webdriver
import os
app=Flask(__name__)

@app.route("/")
def home():
    url = 'https://marketsmithindia.com/mstool/eval/RELIANCE/evaluation.jsp#/'
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

    # Now you can start using Selenium
    driver.get(url) 


    content = driver.page_source
    soup = BeautifulSoup(content, features = "lxml")
    v=(soup.findAll('td',class_='surveillancetext'))
    l=[]
    for i in v:
        try:
            l.append(i.text)
        except:
            l.append(i.findAll('a').text)
    driver.close()

    return render_template('index.html',l=l)


if __name__ == "__main__":
    app.run()#(debug=False,host='0.0.0.0')