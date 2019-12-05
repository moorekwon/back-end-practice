# Requests
# Requests 사용 스크랩핑 1

import requests

# session 활성화
# s = requests.Session()
# r = s.get('https://www.naver.com')

# 수신 데이터
# print(r.text)

# 수신 상태 모드
# print('Status Code: {}'.format(r.status_code))

# 확인
# print('ok?: {}'.format(r.ok))

# session 비활성화
# s = requests.Session()

# with 문 사용(권장)
with requests.Session() as s:
    r = s.get('https://www.naver.com')
    print(r.text)