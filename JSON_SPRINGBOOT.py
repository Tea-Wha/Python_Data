import requests # http 통신을 위한 모듈
import json 

member = {
    "userId": "anyj12345678",
    "email": "anyj123@gmail.com",
    "password": "test123456",
    "nickname": "안유진테스트3",
}

# 서버 URL 및 헤더 설정
url = "http://localhost:8111/auth/signup"
headers = {"Content-Type": "application/json"}

# POST 요청 보내기
response = requests.post(url, data=json.dumps(member), headers=headers)

# 응답 처리
if response.status_code == 200:
    # 서버에서 전달 받은 JSON을 객체로 변환하고 내용을 출력
    # dictionary 로 넘어옴
    data = response.json()
    print(f"ID: {data['id']}")
    print(f"userId: {data['userId']}")
    print(f"Email: {data['email']}")
    print(f"Nickname: {data['nickname']}")
    print(f"UserStatus: {data['userStatus']}")
    print("회원 가입에 성공했습니다.")
else:
    print("회원 가입에 실패했습니다.")