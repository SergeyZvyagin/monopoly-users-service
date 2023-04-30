import psycopg2

class DatabaseManager:
    def __init__(self, logger, **kwargs):
        self.logger = logger

        self.conn = psycopg2.connect(
                dbname=kwargs['db_name'],
                user=kwargs['db_user'],
                password=kwargs['db_pass'], 
                host=kwargs['db_host'],
                port=kwargs['db_port']
        )
        
        self.cursor = self.conn.cursor()

    def getUserInfoByID(self, id: int) -> tuple:
        self.cursor.execute('SELECT nickname, is_guest, rating FROM users WHERE id=%d' % int(id))
        return self.cursor.fetchone()


    def getUserIDByVKID(self, vk_id:int) -> int:
        self.cursor.execute('SELECT id FROM users WHERE vk_id=%d;' % int(vk_id))
        row = self.cursor.fetchone()
        return None if not row else row[0]


    def createUserAndReturnID(self, nickname: str, vk_id:int=None) -> int:
        variables = 'nickname' + (', vk_id, is_guest' if vk_id else '')
        values = f"'{nickname}'" + ('' if not vk_id else f', {vk_id}, false')

        self.cursor.execute(f'INSERT INTO users ({variables}) VALUES ({values}) RETURNING id;')
        user_id = self.cursor.fetchone()[0]
        self.conn.commit()
        
        return user_id


    
