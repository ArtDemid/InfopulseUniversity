import pymysql
import time

connection = pymysql.connect(host='localhost',
                            user='root',
                            password='mysql',
                            db='oxwa878',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

try:
    '''
    with connection.cursor() as cursor:
        sql = "INSERT INTO `ow_base_user` (`email`, `username`, `password`) VALUES (%s, %s, %s);"
        cursor.execute(sql, ('test2@test.org', 'test2', 'test2'))
    connection.commit()'''

    time.sleep(2)

    with connection.cursor() as cursor:
        sql = "SELECT `id`, `username`, `email` FROM `ow_base_user` WHERE `email`=%s;"
        #cursor.execute(sql, ('test@test.org',))
        #result = cursor.fetchone()
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()

