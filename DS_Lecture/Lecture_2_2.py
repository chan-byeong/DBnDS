from db_conn import *
import pandas as pd

conn, curs = open_db()

df = pd.read_csv('./DS_Lecture/top_movies.csv')

insert_sql = '''
  insert into top_movies (id,movie_name,release_year,watch_time,movie_rating,metascore,gross,votes,description)
    values (%s,%s,%s,%s,%s,%s,%s,%s,%s);
'''

df = df.fillna(0)
# N/a를 0으로 바꿔준다.

for idx , r in df.iterrows() :
  movie_name = r['Movie Name']
  release_year = r['Year of Release']
  watch_time = r['Watch Time']
  movie_rating = r['Movie Rating']
  metascore = r['Metascore of movie']
  gross = r['Gross']
  votes = r['Votes']
  description = r['Description']

  release_year = release_year[-4:]
  # II 2034 와 같은 문자열 예외처리. 끝 4자리만 받음

  votes = int(votes.replace(",",''))
  # 문자열로 처리되는 votes ','-> '' 지우고 Integer 형변환
  
  # print(movie_name,release_year,watch_time,movie_rating,metascore,gross,votes,description)

  gross = float(str(gross).replace("#",''))
  # #222 예외처리

  value = (idx,movie_name,release_year,watch_time,movie_rating,metascore,gross,votes,description)

  curs.execute(insert_sql , value)


close_db(conn, curs)