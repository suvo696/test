from flask import Flask,render_template
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

app=Flask(__name__)

@app.route("/")
def home():
    
    gChromeOptions = webdriver.ChromeOptions()
    gChromeOptions.add_argument("window-size=1920x1480")
    gChromeOptions.add_argument("disable-dev-shm-usage")
    gDriver = webdriver.Chrome(
        chrome_options=gChromeOptions, executable_path=ChromeDriverManager().install()
    )
    gDriver.get("https://www.python.org/")
    
    gDriver.save_screenshot("my_screenshot.png")
    gDriver.close()

    return render_template('index.html',l=l)


if __name__ == "__main__":
    app.run()#(debug=False,host='0.0.0.0')