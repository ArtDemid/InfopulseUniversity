import pymysql.cursors
import pytest
import pytest_selenium

@pytest.fixture()
def db(config):
    #db = DBConnector(host = 'localhost', user = 'root', password = 'mysql', db = 'oxwa878', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    db = DBConnector(**config["db"])
    yield
    db.close()

@pytest.fixture(scope="session")
def config():
    with open(os.path.join(PROJECT_DIR, "config.json")) as f:
        config = json.load(f)
        return config

def pytest_addoption(parser):
    parser.addoption("--config", action="store", default="config.json", help="config file")

@pytest.fixture()
def driver(selenium):
    driver = selenium
    driver.get("http://127.0.0.1/oxwall/")
    yield driver
    driver.quit()

    #for run from cmd type follow: pytest --driver Chrome or pytest --driver Firefox



class DBConnector:
    def __init__(self, *args, **kwargs):
        self.__connection = pymysql.connect(*args, **kwargs)
        #self.__connection.autocommit_mode = True
        self.__connection.autocommit(True)

    def close(self):
        self.__connection.close()

    def create_user(self, user):
        with self.__connection.cursor() as cursor:
            sql = "INSERT INTO `ow_base_user` (`email`, `username`, `password`) VALUES (%s, %s, %s);"
            cursor.execute(sql, (user.username, user.email, user.password))

    def get_users(self, user):
        with self.__connection.cursor() as cursor:
            sql = "SELECT `id`, `username`, `email` FROM `ow_base_user` WHERE `email`=%s;"
            result = [User(**user_dict) for user_dict in cursor.fetchall()]

    