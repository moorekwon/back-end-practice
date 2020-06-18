# urllib
# import urllib.request as req

# img_url = 'http://post.phinf.naver.net/20160621_169/1466482468068lmSHj_JPEG/If7GeIbOPZuYwI-GI3xU7ENRrlfI.jpg'
# html_url = 'http://google.com'

# save_path1 = '/home/hyojinkwon/Desktop/test1.jpg'
# save_path2 = '/home/hyojinkwon/Desktop/index.html'

# try:
#     file1, header1 = req.urlretrieve(img_url, save_path1)
#     file2, header2 = req.urlretrieve(html_url, save_path2)
# except Exception as e:
#     print('Download failed..')
#     print(e)
# else:
#     print('header1', header1)
#     print('header2', header2)
#     print()
    
#     print('file1', file1)
#     print('file2', file2)
#     print()
    
#     print('Download succeed!')


# urlopen
import urllib.request as req
from urllib.error import URLError, HTTPError

path_list = ['/home/hyojinkwon/Desktop/test1.jpg', '/home/hyojinkwon/Desktop/index.html']
url_list = ["http://post.phinf.naver.net/20160621_169/1466482468068lmSHj_JPEG/If7GeIbOPZuYwI-GI3xU7ENRrlfI.jpg", "http://google.com"]

for i, url in enumerate(url_list):
    try:
        response = req.urlopen(url)
        contents = response.read()
        print()
        
        print('header info - {}: {}'.format(i, response.info()))
        print('http status code: {}'.format(response.getcode()))
        print()
        
        with open(url_list[i], 'wb') as c:
            c.write(contents)
            
    except HTTPError as e:
        print('Download failed...')
        print('httperror code: ', e.code)
        print()
        
    except URLError as e:
        print('Download failed...')
        print('urlerror reason: ', e.reason)
        print()
        
    else:
        print('download succeed!')