import sqlite3

# conn = sqlite3.connect("D:\database.db")
# curs = conn.cursor()
# conn.commit()
# conn.close()
def convert(value):
    if value.startswith('~'):
        return value.strip("~")
    if not value:
        value='0'
    return float(value)

conn=sqlite3.connect('food.db')
curs=conn.cursor()

curs.execute('''
CREATE TABLE food(
    id TEXT PRIMARY KEY,
    desc TEXT,
    water FLOAT,
    kcal FLOAT,
    protein FLOAT,
    fat FLOAT,
    ash FLOAT,
    carbs FLOAT,
    fiber FLOAT,
    sugar FLOAT
)
''')
query='INSERRT INTO food VALUES (?,?,?,?,?,?,?,?,?,?)'
for line in open('D:\SR-Leg_ASC\DATA_SRC.txt'):
    fields=line.split('^')
    vals=[convert(f) for f in fields[:field_count]]
    curs.execute(query.vals)

conn.commit()
conn.close()