import sqlite3

connect = sqlite3.connect('db.sqlite')
cursor = connect.cursor()


def add_user(user_id, username):
    try:
        cursor.execute('INSERT INTO USERS VALUES(?, ?, ?)', (user_id, username, None))
        connect.commit()
    except sqlite3.IntegrityError:
        pass


def add_reg_user(site_id):
    cursor.execute('INSERT INTO POSTBACK VALUES(?, ?)', (site_id, 0))
    connect.commit()


def update_user_site_id(user_id, site_id):
    cursor.execute('UPDATE USERS SET site_id = ? where user_id = ?', (site_id, user_id))
    connect.commit()


def get_user_by_site_id(site_id):
    return cursor.execute('SELECT * FROM USERS WHERE SITE_ID = ?', (site_id,)).fetchone()


def update_deposit(site_id, amount):
    cursor.execute('UPDATE POSTBACK SET amount = ? where site_id = ?', (amount, site_id))
    connect.commit()


def get_user(user_id):
    return cursor.execute('SELECT * FROM USERS WHERE user_id = ?', (user_id, )).fetchone()


def get_postback_by_site_id(site_id):
    return cursor.execute('SELECT * FROM POSTBACK where site_id = ?', (site_id, )).fetchone()
