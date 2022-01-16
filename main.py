from flask import Flask, render_template, redirect, url_for

from bs4 import BeautifulSoup
import requests

API_KEY = "563492ad6f91700001000001987f0f60638b4987965e636018e21c2c"
IM_URL1 = "https://www.google.com.br/search?q="
IM_URL2 = "&sxsrf=AOaemvI9VwAVK3gWxm81x-BDis2sW__Iqw:1642342095378&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi03saJubb1AhUCr5UCHTuOArkQ_AUoAXoECAEQAw&biw=1920&bih=969&dpr=1"

URL = "http://famous-quotes.uk/api.php?id="
app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get(f"{URL}random")
    body = response.json()[0]
    query = body[2].replace(" ","+").lower()
    response_photo = requests.get(f"{IM_URL1}{query}{IM_URL2}")
    soup = BeautifulSoup(response_photo.text, "html.parser")
    link = soup.find_all("img")[2]['src']
    return render_template("index.html", body=body, link= link)


if __name__ == "__main__":
    app.run(debug=True)
