import MySQLdb


def get_db():
    return MySQLdb.connect(host="127.0.0.1", user="a",
                           passwd="a", db="tarea",
                           use_unicode=True, charset="utf8", client_flag=2)

def query(SQL):
    db = get_db()
    ds = db.cursor(MySQLdb.cursors.DictCursor)
    ds.execute(SQL, ())
    out = []
    for row in ds:
        out.append(row)
    return out

