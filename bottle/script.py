import sqlite3
from bottle import route, run, template

@route('/script')
def show_script():
    db = sqlite3.connect('script.db')
    c = db.cursor()
    c.execute("SELECT item,quant FROM script")
    data = c.fetchall()
    c.close()
    output = template('bring_to_script', rows=data)
    return output

run(host='0.0.0.0', port=8080)
