import json
import pymysql.cursors

from value_models.user_model import User

def _get_hash(item):
    hashed_items = {
        "pass": "bf6116af8e4b3e83a7646640590b9d5f5c95b06bf7eebf6c424487ff39293833",
        "test": "62fc22c0da68a727562013a405e45ad29fe67725db24870d8dff48a39b37f5ae",
        "secret": "94d1297b55907d7158b27cd91f0d0b0d212abc0ccd4a3e861b1f4e1f404c67e0"
    }
    return hashed_items[item]

class DbConnector:
    
    def __init__(self, *args, **kwargs):
        self.__connection = pymysql.connect(*args, **kwargs,
                        cursorclass=pymysql.cursors.DictCursor)
        self.__connection.autocommit(True)

    def close(self):
        self.__connection.close()

    def create_user(self, user):
        with self.__connection.cursor() as cursor:
            # Create a new record
            sql = """INSERT INTO `ow_base_user` (`username`, `email`, `password`, `joinIp`, `emailVerify`)
                     VALUES ("{}", "{}", "{}", "{}", "{}")"""
            cursor.execute(sql.format(user.username, user.email, _our_hash(user.password), "21423532", 0))
        # self.__connection.commit()
        with self.__connection.cursor() as cursor:
            sql1 = f"SELECT * FROM ow_base_user WHERE ow_base_user.username = '{user.username}'"
            cursor.execute(sql1)
            user_id = cursor.fetchone()['id']
            sql = f"""INSERT `ow_base_question_data` (`userId`, `textValue`, `questionName`)
                      VALUES ("{user_id}", "{user.full_name}", "realname")"""
            cursor.execute(sql)

    def get_users(self):
        with self.__connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id`,  `username`, `password`, `email` FROM `ow_base_user`"
            cursor.execute(sql)
            result = [User(**user_dict) for user_dict in cursor.fetchall()]
            return result

    def delete_user(self, user):
        with self.__connection.cursor() as cursor:
            sql = f'''DELETE FROM `ow_base_user`
                      WHERE `ow_base_user`.`username` = "{user.username}"'''
            cursor.execute(sql)
        # self.connection.commit()

    def get_last_text_status(self):
        """ Get status with maximum id that is last added """
        with self.__connection.cursor() as cursor:
            sql = """SELECT * FROM `ow_newsfeed_action`
                     WHERE `id`= (SELECT MAX(`id`) FROM `ow_newsfeed_action` WHERE `entityType`="user-status")
                     AND `entityType`="user-status"
                     """
            cursor.execute(sql)
            response = cursor.fetchone()
            data = json.loads(response["data"])["status"]
        return data        