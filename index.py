from flask import Flask,render_template
from bs4 import BeautifulSoup
from selenium import webdriver
app=Flask(__name__)

@app.route("/")
def home():
    url = 'https://marketsmithindia.com/mstool/eval/RELIANCE/evaluation.jsp#/'
    driver = webdriver.Chrome(executable_path="chromedriver_win32/chromedriver.exe")
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