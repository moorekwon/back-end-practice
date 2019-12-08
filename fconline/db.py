# # # python database 연동 (SQLite)
# # # 테이블 생성 및 삽입

# import datetime
# import sqlite3

# # # 삽입 날짜 생성
# now = datetime.datetime.now()
# # # print('now: ', now)

# nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
# # # print('nowDatetime: ', nowDatetime)

# # # sqlite3 버전
# # # print('sqlite3.version: ', sqlite3.version)
# # # print('sqlite3.sqlite_version: ', sqlite3.sqlite_version)

# # # db 생성 & autocommit
# # # 본인 DB 파일 경로
# conn = sqlite3.connect('/home/hyojinkwon/Desktop/database.db', isolation_level=None)

# # # cursor 연결
# c = conn.cursor()
# # # print('cursor type: ', type(c))

# # # 테이블 생성 (datatype: TEXT NUMERIC INTEGER REAL BLOB)
# c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)")

# # # 데이터 삽입
# # c.execute("INSERT INTO users VALUES (1, 'Shin', 'shin@naver.com', '010-6666-6666', 'shin@com', ?)", nowDatetime)
# c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)", (1, 'Shin', 'Shin@naver.com', '010-6666-6666', 'Shin.com', nowDatetime))

# # many 삽입(tuple, list)
# userList = {
#     (3, 'Kwon', 'kwon@naver.com', '010-2222-2222', 'kwon.com', nowDatetime),
#     (4, 'Kim', 'kim@naver.com', '010-3333-3333', 'kim.com', nowDatetime),
#     (5, 'Lee', 'lee@naver.com', '010-4444-4444', 'lee.com', nowDatetime),
# }

# c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)", userList)

# # 테이블 데이터 삭제
# print('users db deleted: ', conn.execute("delete from users").rowcount, "rows")

# # commit: isolation_level=None 경우, 자동 반영 (auto commit)
# # conn.commit()

# # 롤백
# # conn.rollback()

# # 접속 해제
# # conn.close()


# # # 테이블 조회
# import sqlite3

# # # db 파일 조회 (없으면 새로 생성)
# conn = sqlite3.connect('/home/hyojinkwon/Desktop/database.db')

# # # 커서 바인딩
# c = conn.cursor()

# # # 데이터 조회(전체)
# c. execute("SELECT * FROM users")

# # 커서 위치가 변경됨
# # 1개 로우 선택
# # print('One -> ', c.fetchone())

# # 지정 로우 선택
# # print('three -> ', c.fetchmany(size=3))

# # 전체 로우 선택
# # print('all -> ', c.fetchall())

# # 순회 1
# # rows = c.fetchall()
# # for row in rows:
# #     print('retrieve 1 > ', row)
    
# # 순회 2
# # for row in c.fetchall():
# #     print('retrieve 2 > ', row)
    
# # 순회 3
# # for row in c.execute("SELECT * FROM users ORDER BY id desc"):
# #     print('retrieve 3 > ',row)

# # WHERE Retrieve 1
# param1 = (1, )
# c.execute('SELECT * FROM users WHERE id=?', param1)
# # print('param1: ', c.fetchone())
# print('param1: ', c.fetchall())

# # WHERE Retrieve 2
# param2 = 2
# c.execute("SELECT * FROM users WHERE id='%s'" % param2)
# # print('param2: ', c.fetchone())
# print('param2: ', c.fetchall())

# # WHERE Retrieve 3
# c.execute("SELECT * FROM users WHERE id=:Id", {"Id": 3})
# # print('param3: ', c.fetchone())
# print('param3: ', c.fetchall())

# # WHERE Retrieve 4
# param4 = (3, 4)
# c.execute('SELECT * FROM users WHERE id IN(?, ?)', param4)
# print('param3, param4: ', c.fetchall())

# # WHERE Retreive 5
# c.execute("SELECT * FROM users WHERE id In('%d', '%d')" % (4, 5))
# print('param4, param5: ', c.fetchall())

# # WHERE Retreive 6
# c.execute("SELECT * FROM users WHERE id=:id1 OR id=:id5", {"id1": 1, "id5": 5})
# print('param1, param5: ', c.fetchall())

# with conn:
#     # dump 출력 (db 백업 시 중요!)
#     with open('/home/hyojinkwon/Desktop/dump.sql', 'w') as f:
#         for line in conn.iterdump():
#             f.write('%s\n' % line)
#         print('dump print completed.')
        
        
# 테이블 수정 및 삭제
import sqlite3

# db 생성(파일)
conn = sqlite3.connect('/home/hyojinkwon/Desktop/database.db')

# cursor 연결
c = conn.cursor()

# 데이터 수정 1
# c.execute("UPDATE users SET website=? WHERE id=?", ('Kwon.com', 3))

# 데이터 수정 2
# c.execute("UPDATE users SET username=:name WHERE id=:id", {"name": 'niceman', "id": 4})

# 데이터 수정 3
# c.execute("UPDATE users SET website='%s' WHERE id='%s'" % ('Kim.com', 4))

# 중간 데이터 확인 1
# for user in c.execute('SELECT * FROM users'):
#     print(user)
    
# raw delete 1
# c.execute("DELETE FROM users WHERE id=?", (5, ))

# raw delte 2
# c.execute("DELETE FROM users WHERE id=:id", {'id': 8})

# raw delete 3
# c.execute("DELETE FROM users WHERE id='%s'" % 4)

# 중간 데이터 확인 2
# for user in c.execute('SELECT * FROM users'):
#     print(user)

# 테이블 전체 데이터 삭제
print("users db deleted: ", conn.execute("delete from users").rowcount, "rows")

# 관계형 데이터베이스

# 커밋
conn.commit()

# 접속 해제
conn.close()