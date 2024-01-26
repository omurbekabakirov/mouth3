CREATE_USER_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS telegram_users(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER ,
USERNAME CHAR(50),
FIRST_NAME CHAR(50),
LAST_NAME CHAR(50),
UNIQUE(TELEGRAM_ID))
"""
INSERT_USER_QUERY = """
INSERT OR IGNORE INTO telegram_users VALUES (?, ?, ?, ?,?,?,?)
"""
ALTER_USER_TABLE = """
ALTER TABLE telegram_users ADD COLUMN REFERENCE_LINK TEXT
"""

ALTER_USER_V2_TABLE = """
ALTER TABLE telegram_users ADD COLUMN BALANCE INTEGER
"""

CREATE_BAN_USER_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS ban_users(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER ,
BAN_COUNT INTEGER ,
UNIQUE(TELEGRAM_ID))
"""
CREATE_PROFILE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS profile(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER ,
NICKNAME CHAR(50) ,
BIO TEXT ,
AGE INTEGER,
ZODIAC_SIGN CHAR(50) ,
JOB CHAR(50) ,
GENDER CHAR(50) ,
PHOTO TEXT ,
UNIQUE(TELEGRAM_ID))
"""

INSERT_BAN_USER_QUERY = """
INSERT  INTO ban_users VALUES ( ?, ?,?)
"""

SELECT_BAN_USER_QUERY = """
SELECT * FROM  ban_users WHERE TELEGRAM_ID = ?
"""

UPDATE_BAN_USER_COUNT_QUERY = """
UPDATE ban_users SET BAN_COUNT = BAN_COUNT + 1 WHERE TELEGRAM_ID = ?
"""
INSERT_PROFILE_QUERY = """
INSERT  INTO profile VALUES (?,?,?,?,?,?,?,?,?)
"""
SELECT_PROFILE_QUERY = """
SELECT * FROM  profile WHERE TELEGRAM_ID = ?

"""
SELECT_ALL_PROFILES_QUERY = """
SELECT * FROM profile
"""

CREATE_LIKE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS like_system 
(
ID INTEGER PRIMARY KEY,
OWNER_TELEGRAM_ID INTEGER,
LIKER_TELEGRAM_ID INTEGER,
UNIQUE (OWNER_TELEGRAM_ID, LIKER_TELEGRAM_ID)
)
"""
CREATE_DISLIKE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS dislike_system 
(
ID INTEGER PRIMARY KEY,
OWNER_TELEGRAM_ID INTEGER,
DISLIKER_TELEGRAM_ID INTEGER,
UNIQUE (OWNER_TELEGRAM_ID, DISLIKER_TELEGRAM_ID)
)
 """
INSERT_LIKE_QUERY ="""
INSERT INTO like_system VALUES (?,?,?)"""
INSERT_DISLIKE_QUERY ="""
INSERT INTO dislike_system VALUES (?,?,?)"""


FILTER_LEFT_JOIN_PROFILE_QUERY = """
SELECT * FROM profile
LEFT JOIN like_system ON profile.TELEGRAM_ID = like_system.OWNER_TELEGRAM_ID
AND like_system.LIKER_TELEGRAM_ID = ?
WHERE like_system.ID IS NULL
AND profile.TELEGRAM_ID != ?
"""
FILTER_LEFT_JOIN_PROFILE_AND_DISLIKE_QUERY = """
SELECT * FROM profile
LEFT JOIN dislike_system ON profile.TELEGRAM_ID = dislike_system.OWNER_TELEGRAM_ID
AND dislike_system.DISLIKER_TELEGRAM_ID = ?
WHERE dislike_system.ID IS NULL
AND profile.TELEGRAM_ID != ?
"""
CREATE_REFERRAL_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS referral 
(
ID INTEGER PRIMARY KEY,
OWNER_TELEGRAM_ID INTEGER,
USERNAME TEXT,
REFERRAL_TELEGRAM_ID INTEGER,
UNIQUE (OWNER_TELEGRAM_ID, REFERRAL_TELEGRAM_ID)
)
"""
DOUBLE_SELECT_REFERRAL_USER_QUERY = """
SELECT
    COALESCE(telegram_users.BALANCE, 0) as BALANCE,
    COUNT(referral.ID) as total_referrals
FROM
    telegram_users
LEFT JOIN
    referral ON telegram_users.TELEGRAM_ID = referral.OWNER_TELEGRAM_ID
WHERE
    telegram_users.TELEGRAM_ID = ?
"""
SELECT_USER_QUERY = """
SELECT * FROM telegram_users WHERE TELEGRAM_ID = ?
"""
SELECT_MY_QUERY = """
SELECT * FROM referral WHERE OWNER_TELEGRAM_ID = ?
"""

SELECT_USER_BY_LINK_QUERY = """
SELECT * FROM telegram_users WHERE REFERENCE_LINK = ?
"""
UPDATE_USER_LINK_QUERY = """
UPDATE telegram_users SET REFERENCE_LINK = ? WHERE TELEGRAM_ID = ?
"""

INSERT_REFERRAL_QUERY = """
INSERT INTO referral VALUES (?,?,?,?)
"""

UPDATE_USER_BALANCE_QUERY = """
UPDATE telegram_users SET BALANCE = COALESCE(BALANCE, 0) + 100 WHERE TELEGRAM_ID = ?
"""
