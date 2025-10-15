import sqlite3

def get_user(name):
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("CREATE TABLE users (name TEXT)")
    cur.execute("INSERT INTO users (name) VALUES ('alice')")
    # Vulnerable: direct string interpolation
    query = "SELECT * FROM users WHERE name = '%s'" % name
    cur.execute(query)  # 🚨 SQL injection
    return cur.fetchall()

if __name__ == "__main__":
    print(get_user(input("name> ")))
