import sqlite3
from database import sql_queries

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('db.sqlite3')
        self.cursor = self.connection.cursor()
    def sql_create_table(self):
        if self.connection:
            print("database connected successfully")
        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_BAN_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_PROFILE_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_LIKE_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_DISLIKE_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_REFERRAL_TABLE_QUERY)
        try:
            self.connection.execute(sql_queries.ALTER_USER_TABLE)
            self.connection.execute(sql_queries.ALTER_USER_V2_TABLE)
        except sqlite3.OperationalError:
            pass
        self.connection.commit()



    def sql_insert_user(self, tg_id, username, first_name, last_name):
        self.cursor.execute(
            sql_queries.INSERT_USER_QUERY,
            (None, tg_id, username, first_name, last_name, None, 0)
        )
        self.connection.commit()


    def sql_insert_ban_user(self,tg_id):
        self.cursor.execute(sql_queries.INSERT_BAN_USER_QUERY,
                            (None,tg_id,1)
                            )
        self.connection.commit()


    def sql_select_ban_users(self,tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            'telegram_id': row[1],
            'count': row[2]
        }
        return self.cursor.execute(
            sql_queries.SELECT_BAN_USER_QUERY,
            (tg_id,)
        ).fetchone()

    def sql_update_ban_count(self,tg_id):
        self.cursor.execute(sql_queries.UPDATE_BAN_USER_COUNT_QUERY,
                            (tg_id,)
                            )
        self.connection.commit()

    def sql_insert_profile(self,tg_id,nickname,bio,age,zodiac_sign,job,gender,photo):
        self.cursor.execute(sql_queries.INSERT_PROFILE_QUERY,
                            (None,tg_id,nickname,bio,age,zodiac_sign,job,gender,photo)
                            )
        self.connection.commit()

    def sql_select_profile(self,tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            'telegram_id': row[1],
            'name': row[2],
            'bio': row[3],
            'age': row[4],
            'zodiac sign': row[5],
            'job': row[6],
            'gender': row[7],
            'photo': row[8]
        }
        return self.cursor.execute(
            sql_queries.SELECT_PROFILE_QUERY,
            (tg_id,)
        ).fetchone()


    def sql_insert_like(self,owner,liker):
        self.cursor.execute(sql_queries.INSERT_LIKE_QUERY,
                            (None,owner,liker)
                            )
        self.connection.commit()
    def sql_insert_dislike(self,owner,disliker):
        self.cursor.execute(sql_queries.INSERT_DISLIKE_QUERY,
                            (None,owner,disliker)
                            )
        self.connection.commit()

    def sql_select_all_profiles(self,owner):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            'telegram_id': row[1],
            'name': row[2],
            'bio': row[3],
            'age': row[4],
            'zodiac sign': row[5],
            'job': row[6],
            'gender': row[7],
            'photo': row[8]
        }
        return self.cursor.execute(
            sql_queries.FILTER_LEFT_JOIN_PROFILE_QUERY,(owner,owner)).fetchall()

    def sql_select_user(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            'telegram_id': row[1],
            'username': row[2],
            'first_name': row[3],
            'last_name': row[4],
            'link': row[5],
            'balance': row[6],
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_QUERY,
            (tg_id,)
        ).fetchone()

    def sql_update_link(self, link, tg_id):
        self.cursor.execute(
            sql_queries.UPDATE_USER_LINK_QUERY,
            (link, tg_id,)
        )
        self.connection.commit()

    def sql_select_referral_menu_info(self, owner):
        self.cursor.row_factory = lambda cursor, row: {
            'balance': row[0],
            'total_referrals': row[1],
        }
        return self.cursor.execute(
            sql_queries.DOUBLE_SELECT_REFERRAL_USER_QUERY,
            (owner,)
        ).fetchone()

    def sql_select_user_by_link(self, link):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            'telegram_id': row[1],
            'username': row[2],
            'first_name': row[3],
            'last_name': row[4],
            'link': row[5],
            'balance': row[6],
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_BY_LINK_QUERY,
            (link,)
        ).fetchone()
    def sql_select_my_refs(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            'owner': row[1],
            'username': row[2],
            'ref': row[3]
        }
        return self.cursor.execute(
            sql_queries.SELECT_MY_QUERY,
            (tg_id,)
        ).fetchall()

    def sql_insert_referral(self, owner,username, referral):
        self.cursor.execute(
            sql_queries.INSERT_REFERRAL_QUERY,
            (None, owner,username, referral)
        )
        self.connection.commit()

    def sql_update_balance(self, owner):
        self.cursor.execute(
            sql_queries.UPDATE_USER_BALANCE_QUERY,
            (owner,)
        )
        self.connection.commit()