from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL,MySQLdb #pip install flask-mysqldb https://github.com/alexferl/flask-mysqldb

  
app = Flask(__name__)
    
app.secret_key = "caircocoders-ednalan-2020"
    
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'drag_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
  
 
@app.route('/')
def main():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    result = cur.execute("SELECT * FROM gallery ORDER BY display_order")
    gallery = cur.fetchall()
    return render_template('drop_and_drop_reorder.html', gallery=gallery)
      
@app.route("/orderupdate",methods=["POST","GET"])
def orderupdate():
    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)   
    if request.method == 'POST':
        number_of_rows= cur.execute("SELECT * FROM gallery")    
        print(number_of_rows) #4        
        getorder = request.form['order']    
        order = getorder.split(",", number_of_rows)
        count=0    
        for value in order:
            count +=1
            #print(count)                       
            cur.execute("UPDATE gallery SET display_order = %s WHERE id = %s ", [count, value])
            mysql.connection.commit()       
        cur.close()
    return jsonify(order)
     
if __name__ == '__main__':
    app.run(debug=True)