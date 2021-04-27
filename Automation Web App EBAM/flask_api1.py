from flask import Flask,json,render_template
from flask_restful import reqparse,Api,Resource
from test import Test
import pyodbc

app = Flask(__name__)
test = Test(app)
@app.route('/cockpit/Dashboard')
def getreq():
    return open('./UserInterface/dashboard_info.html').read()

@app.route('/cockpit/Home')
def t1():
    return open('./UserInterface/index.html').read()

@app.route('/cockpit/Styles/dashboard_info_style.css')
def xyz1():
    return open('./UserInterface/Styles/dashboard_info_style.css').read()

@app.route('/cockpit/UserInterface/Assets/image1.jpg')
def img1():
    return open('./UserInterface/Assets/image1.jpg').read()    

@app.route('/cockpit/Styles/index_style.css')
def xyz2():
    return open('./UserInterface/Styles/index_style.css').read()

@app.route('/cockpit/Scripts/dashboard_info.js')
def pqr():
    return open('./UserInterface/Scripts/dashboard_info.js').read()


@app.route('/cockpit/LastTenAccessed')
def get():
    pr = reqparse.RequestParser()
    pr.add_argument('did',required= True)
    args = pr.parse_args()
    my_dash_id = args['did']

    server = ''
    database = ''
    cnxn = pyodbc.connect(
        '')
    global cursor
    cursor = cnxn.cursor()
    query = ' Select  TOP 20 ca.UserId, ru.DisplayName from cockpit.Access ca INNER JOIN ref.[User] ru ON ca.UserId=ru.UserId WHERE ca.DashboardID = ?  GROUP BY ca.UserId,ru.DisplayName'
    cursor.execute(query,my_dash_id)
    resul = cursor.fetchall()
    lisa = []
    for row in resul:
        login = row[0]
        name = row[1]
        lisa.append((login,name))
    return json.dumps(lisa)

if __name__ == "__main__":
    app.run()
