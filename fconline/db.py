# python database 연동 (SQLite)
# 테이블 생성 및 삽입

import datetime
import sqlite3

# 삽입 날짜 생성
now = datetime.datetime.now()
# print('now: ', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
# print('nowDatetime: ', nowDatetime)

# sqlite3 버전
# print('sqlite3.version: ', sqlite3.version)
# print('sqlite3.sqlite_version: ', sqlite3.sqlite_version)

# db 생성 & autocommit
# 본인 DB 파일 경로
conn = sqlite3.connect('/home/hyojinkwon/Desktop/database.db', isolation_level=None)

# cursor 연결
c = conn.cursor()
# print('cursor type: ', type(c))

# 테이블 생성 (datatype: TEXT NUMERIC INTEGER REAL BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)")

# 데이터 삽입
# c.execute("INSERT INTO users VALUES (1, 'Kwon', 'kwon@naver.com', '010-8276-0045', 'kwon.com', ?)", (nowDatetime))
c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)", (2, 'Park', 'Park@naver.com', '010-1111-1111', 'Park.com', nowDatetime))

# many 삽입(tuple, list)
