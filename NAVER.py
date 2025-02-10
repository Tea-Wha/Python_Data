import requests # http protocol 웹페이지 문서 불러오기
from bs4 import BeautifulSoup # 파싱
import pandas as pd # 2차원의 데이터를 가공하기 위해 사용
import openpyxl # 엑셀 문서를 만들거나 불러오기 위해 사용
from flask import Flask

app = Flask(__name__)

@app.route("/stock/<code>")
def crawl(code):
    url = f"https://finance.naver.com/item/main.naver?code={code}"
    res = requests.get(url)
    bs_obj = BeautifulSoup(res.text, "html.parser")
    div_today = bs_obj.find("div", {"class" : "today"})
    em = div_today.find("em")
    price = em.find("span", {"class" : "blind"}).text
    h_company = bs_obj.find("div", {"class" : "h_company"})
    name = h_company.a.text
    div_description = h_company.find("div", {"class" : "description"})
    code = div_description.span.text
    print(code)

    table_no_info = bs_obj.find("table", {"class" : "no_info"})
    tds = table_no_info.tr.find_all("td")
    volume = tds[2].find("span", {"class" : "blind"}).text

    html = ""
    html += f"<h1>이름 : {name} </h1>"
    html += f"<h3>가격 : {price} </h3>"
    html += f"<h3>코드 : {code} </h3>"
    html += f"<h3>거래량 : {volume} </h3>"
    return html


if __name__ == "__main__":
    app.run()