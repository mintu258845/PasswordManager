
import random  # https://docs.python.org/3.6/library/random.html
import sqlite3  # https://docs.python.org/3.6/library/sqlite3.html
import string  # https://docs.python.org/3.6/library/string.html
import sqlite3 #https://docs.python.org/3.6/library/sqlite3.html
import json  # https://docs.python.org/3/library/json.html
import urllib.request   #https://docs.python.org/3/library/urllib.request.html


def generate_password(length: int, complexity: int) -> str:
    """Generates a random password with given length and complexity
    Complexity levels:
        Complexity == 1: return a password with only lowercase chars
        Complexity ==  2: Previous level plus at least 1 digit
        Complexity ==  3: Previous levels plus at least 1 uppercase char
        Complexity ==  4: Previous levels plus at least 1 punctuation char

    :param length: number of characters
    :param complexity: complexity level
    :returns: generated password
    """
    password = ''.join(random.choice(string.ascii_lowercase)
                        for _ in range(length-complexity+1))

    if complexity == 2:
        password += (random.choice(string.digits))

    elif complexity == 3:
        password += (random.choice(string.digits))
        password += (random.choice(string.ascii_uppercase))

    elif complexity == 4:
        password += (random.choice(string.digits))
        password += (random.choice(string.ascii_uppercase))
        password += (random.choice(string.punctuation))

    chars = list(password)
    random.shuffle(chars)
    password =''.join(chars)

    return password
    pass


def check_password_level(password: str) -> int:
    """Return the password complexity level for a given password

    Complexity levels:
        Return complexity 1: If password has only lowercase chars
        Return complexity 2: Previous level condition and at least 1 digit
        Return complexity 3: Previous levels condition and at least 1 uppercase char
        Return complexity 4: Previous levels condition and at least 1 punctuation

    Complexity level exceptions (override previous results):
        Return complexity 2: password has length >= 8 chars and only lowercase chars
        Return complexity 3: password has length >= 8 chars and only lowercase and digits

    :param password: password
    :returns: complexity level
    """
    complexity  = 0
    SpecialSym = string.punctuation

    if any(char.islower() for char in password):
        complexity = 2 if len(password) >=8 else 1

        if any(char.isdigit() for char in password):
            complexity = 3 if len(password) >=8 else 2

            if any(char.isupper() for char in password):
                complexity = 3

                if any(char in SpecialSym for char in password):
                    complexity = 4
    return complexity
    pass


def create_user(db_path: str) -> None:  # you may want to use: http://docs.python-requests.org/en/master/
    """Retrieve a random user from https://randomuser.me/api/
    and persist the user (full name and email) into the given SQLite db

    :param db_path: path of the SQLite db file (to do: sqlite3.connect(db_path))
    :return: None
    """
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS user
                        (fullname, email, password)''')

    with urllib.request.urlopen("https://randomuser.me/api/") as url:
        data = json.loads(url.read().decode())
        name = (data['results'][0]['name']['first']
                        + ' '
                        + data['results'][0]['name']['last'])
        email = data['results'][0]['email']
        cur.execute("INSERT INTO user VALUES(?,?,?)",(name, email, '') )
        conn.commit()
    pass


if __name__ == '__main__':
    for _ in range(10):
        """This is script to generate passwords with multiple scenarios
        and test them using assertion
        """
        complexity = random.randint(1,4)
        length = random.randint(6,12)
        pwd = generate_password(length, complexity )
        print("Success" if complexity == check_password_level(pwd) else "Fail")

    for _ in range (10):
        """This is script to generate 10 users and assign passwords
            in random complexity and length
        """
        conn = sqlite3.connect('userData11.db')
        create_user(conn)
        c = conn.cursor()
        complexity = random.randint(1,4)
        length = random.randint(6,12)
        pwd = generate_password(length, complexity )
        c.execute("UPDATE user SET password = ? WHERE password = ''", (pwd,) )
        conn.commit()

    conn.close()
