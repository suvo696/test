from flask import Flask,render_template
from bs4 import BeautifulSoup
from selenium import webdriver
app=Flask(__name__)

@app.route("/")
def home():
    url = 'https://marketsmithindia.com/mstool/eval/RELIANCE/evaluation.jsp#/'

    GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
    CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.binary_location = GOOGLE_CHROME_PATH
    driver = webdriver.Chrome(execution_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    
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