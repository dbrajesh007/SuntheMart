from flask import Flask

app = Flask(__name__)


@app.route('/price')
def HelloWorld():
    import pyodbc


    server = 'sunthedb.database.windows.net'
    database = 'sunthemart'
    username = 'suntheadmin'
    password = '$unthe123$'
    
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ',1433', user=username, password=password, database=database)
    cursor = conn.cursor()
                               

    cur = conn.cursor()

    cur.execute("select price from sm_Price where product_id = 1")
    
    for i in cur:
        
        return str(i)

if __name__ == '__main__':
    
    app.run()
