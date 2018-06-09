#####################################################################
#                                                                   #
#   Database operation of creating and inserting into table         #
#                                                                   #
#####################################################################


import sqlite3

conn = sqlite3.connect('faq.db')

c = conn.cursor()


def create_answer_table():
    try:
        c.execute("""CREATE TABLE IF NOT EXISTS answer(
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        question TEXT NOT NULL,
                                        answer TEXT NOT NULL
                                        )""")

    except sqlite3.OperationalError:
        print('Answer table could not be created.')


def create_subject_table():
    try:
        c.execute("""CREATE TABLE IF NOT EXISTS subject(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    subject TEXT NOT NULL,
                                    answer_id integer NOT NULL,
                                    FOREIGN KEY(answer_id) REFERENCES answer(id)
                                    )""")

    except sqlite3.OperationalError:
        print('Subject table could not be created.')


def create_root_table():
    try:
        c.execute("""CREATE TABLE IF NOT EXISTS root(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    root TEXT NOT NULL,
                                    answer_id integer NOT NULL,
                                    FOREIGN KEY(answer_id) REFERENCES answer(id)
                                    )""")

    except sqlite3.OperationalError:
        print('Root table could not be created.')


def create_object_table():
    try:
        c.execute("""CREATE TABLE IF NOT EXISTS object(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    object TEXT NOT NULL,
                                    answer_id integer NOT NULL,
                                    FOREIGN KEY(answer_id) REFERENCES answer(id)
                                    )""")

    except sqlite3.OperationalError:
        print('Object table could not be created.')


# Insert question along with their answer
def insert_answer(question, answer):

    conn = sqlite3.connect('faq.db')

    c = conn.cursor()
    try:
        c.execute("INSERT INTO answer VALUES (NULL, ?,?);", (question, answer))
        conn.commit()

    except sqlite3.OperationalError:
        print('Error while inserting into answer table.')

    c.close()
    conn.close()


# Subject of the parsed question and its answer id
def insert_subject(subject, answer_id):
    conn = sqlite3.connect('faq.db')

    c = conn.cursor()
    try:
        c.execute("INSERT INTO subject VALUES (NULL, ?,?)", (subject, answer_id))
        conn.commit()

    except sqlite3.OperationalError:
        print('Error while inserting into subject table.')

    c.close()
    conn.close()


# Root of the parsed question and its answer id
def insert_root(root, answer_id):
    conn = sqlite3.connect('faq.db')

    c = conn.cursor()
    try:
        c.execute("INSERT INTO root VALUES (NULL, ?,?)", (root, answer_id))
        conn.commit()

    except sqlite3.OperationalError:
        print('Error while inserting into subject table.')

    c.close()
    conn.close()


# Object of the parsed question and its answer id
def insert_object(object, answer_id):
    conn = sqlite3.connect('faq.db')

    c = conn.cursor()
    try:
        c.execute("INSERT INTO object VALUES (NULL, ?,?)", (object, answer_id))
        conn.commit()

    except sqlite3.OperationalError:
        print('Error while inserting into subject table.')

    c.close()
    conn.close()


# gives max id from answer table
def no_of_rows():
    conn = sqlite3.connect('faq.db')
    c = conn.cursor()
    # n = c.execute("SELECT last_insert_rowid() FROM answer")
    # n = c.execute("select seq from sqlite_sequence where name='answer'")
    n = c.execute("SELECT MAX(id) FROM answer")
    print(n)
    c.close()
    conn.close()
    return n



create_answer_table()
create_object_table()
create_subject_table()
create_object_table()

no_of_rows()

c.close()
conn.close()
