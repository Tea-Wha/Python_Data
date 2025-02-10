from bs4 import BeautifulSoup

html = '''
<html>
    <table border=1> 
        <tr>
            <td> 항목 </td> 
            <td> 2013 </td> 
            <td> 2014 </td> 
            <td> 2015 </td>
        </tr> 
        <tr>
            <td> 매출액 </td> 
            <td> 100 </td> 
            <td> 200 </td>
            <td> 300 </td>
        </tr> 
    </table>
</html> 
'''
soup = BeautifulSoup(html, 'html.parser')
result = soup.select('td') # td로 선택된 항목이 리스트 담김
print(result)

# 각 태그의 텍스트만 가져오기
for val in result :
    print(val.text)

html = '''
    <ul>
    <li> 100 </li>
    <li> 200 </li>
    </ul>
    <ol>
    <li> 300 </li>
    <li> 400 </li>
    </ol>
'''

soup = BeautifulSoup(html, 'html5lib')
result = soup.select('ul li')
print(result)

# 값만 출력
for r in result:
    print(r.text)
    
# 특정 요소 찾기 (find와 find.all)
# find : 조건에 맞는 첫 번째 요소 반환
# find_all : 조건에 맞는 모든 요소를 리스트로 반환
import requests
response = requests.get("https://naver.com")
soup = BeautifulSoup(response.text, 'lxml')
# print(soup)

print(soup.find(attrs={"class": "shopping_area"}))
