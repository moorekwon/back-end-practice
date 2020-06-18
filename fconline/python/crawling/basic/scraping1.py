# python crawling basic
# # urllib 사용법 및 기본 스크랩핑
# import urllib.request as req

# # 파일 URL
# img_url = "http://post.phinf.naver.net/20160621_169/1466482468068lmSHj_JPEG/If7GeIbOPZuYwI-GI3xU7ENRrlfI.jpg"
# html_url = "http://google.com"

# # 다운받을 경로
# save_path1 = "/home/hyojinkwon/Desktop/test1.jpg"
# save_path2 = "/home/hyojinkwon/Desktop/index.html"

# # 예외 처리
# try:
#     file1, header1 = req.urlretrieve(img_url, save_path1)
#     file2, header2 = req.urlretrieve(html_url, save_path2)
# except Exception as e:
#     print('Download failed.')
#     print(e)
# else:
#     # header 정보 출력
#     # print(header1)
#     # print(header2)
    
#     # download 파일 정보
#     print('filename1 {}'.format(file1))
#     print('filename2 {}'.format(file2))
#     print()
    
#     # 성공
#     print('Download succeed.')


# urlopen 함수 기초 사용법
import urllib.request as req
from urllib.error import URLError, HTTPError

# download 경로 및 파일명
path_list = ["/home/hyojinkwon/Desktop/test1.jpg", "/home/hyojinkwon/Desktop/index.html"]

# download resource URL
target_url = ["http://post.phinf.naver.net/20160621_169/1466482468068lmSHj_JPEG/If7GeIbOPZuYwI-GI3xU7ENRrlfI.jpg", "http://google.com"]

for i, url in enumerate(target_url):
    # 예외 처리
    try:
        # 웹 수신정보 읽기
        response = req.urlopen(url)
        
        # 수신내용
        contents = response.read()
        print('-------------------------------------')
        
        # 상태정보 중간 출력
        print('header info - {}: {}'.format(i, response.info()))
        print()
        print('HTTP status code: {}'.format(response.getcode()))
        print('---------------------------------------')
        
        # 파일 쓰기
        with open(path_list[i], 'wb') as c:
            c.write(contents)
            
        # HTTP 에러 발생 시
    except HTTPError as e:
        print('Download failed.')
        print('HTTPError code: ', e.code)
        
        # URL 에러 발생 시
    except URLError as e:
        print('Download failed.')
        print('URL error reason: ', e.reason)
        print()
        
        # 성공
    else:
        print('Download succeed.')