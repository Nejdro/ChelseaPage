from flask import Flask, Response, redirect, url_for, request, session, abort, render_template
from flask_login import LoginManager, UserMixin,login_required, login_user, logout_user
import sqlite3 as sql

app = Flask(__name__)

app.config.update(
        DEBUG = False,
        SECRET_KEY = 'sekretny_klucz'
        )

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"



    

    

  



    
@login_manager.unauthorized_handler
def unauthorized():
    return render_template("blad2.html")





    
@app.route("/logout")
@login_required
def logout():
 logout_user() 
 return render_template('glowna.html')







            
    
    
    
        
@app.route("/rejes", methods=["GET", "POST"])
def rejes():
    
    
    if request.method == 'POST':        
        email = request.form.get('email')
        login = request.form.get('login')
        haslo = request.form.get('haslo')
        
        connection = sql.connect('database.db')
        connection.row_factory = sql.Row
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Users WHERE login = ?', (login,))
        user = cursor.fetchone()
        connection.close()
        
        if user == None:
            connection = sql.connect('database.db')
            connection.row_factory = sql.Row
            cursor = connection.cursor()
            cursor.execute('INSERT INTO Users VALUES(?, ?, ?)', (login, haslo, email))
            connection.commit()
            connection.close()
            
            return render_template('glowna.html')
        else:
            return render_template('blad2.html')
        
    else:
        return render_template('rejestracja.html')
    
    
    


    
@app.errorhandler(401)
def page_not_found(e): 
 return render_template('blad.html')

    


@app.route("/")
def main():
    return render_template ('glowna.html')

@app.route("/rejestracja")
def reje():
    return render_template("rejestracja.html")

@app.route("/dodaj")
@login_required
def dodaj():
    return render_template ('Dodaj.html')



@app.route("/log")
def logowanie():
    return render_template ('logowanie.html')

@app.route("/lista")
def lista():
    return render_template ('listapracownikow.html')
@app.route("/historia")
@login_required
def historia():
    return render_template('historia.html')

@app.route("/us", methods= ['POST','GET','DELETE'])
def us():
    return render_template ('rezultat.html')

@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")

@app.route("/addrec",methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            Nick = request.form['Nick']
            Temat_Posta = request.form['Temat_Posta']
            Tresc = request.form['Tresc']
            

            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO posty (Nick, Temat_Posta, Tresc) VALUES (?,?,?)",(Nick, Temat_Posta, Tresc) )


            con.commit()
            msg = "Post dodany"             
        except:
            con.rollback()
            msg = "Blad przy dodawaniu rekordu"

        finally:
            return render_template("rezultat.html",msg = msg)
            con.close()
            

 



@app.route("/for")

def forum2():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute('SELECT * FROM posty')
    rekordy = cur.fetchall()
    return render_template("forum.html",rekordy = rekordy)








class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.name = "mati"
        self.password = "haslo"

    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name,self.password)
users = [User(id) for id in range(1, 10)]

@app.route("/login", methods=["GET", "POST"])
def login():
 
 if request.method == 'POST':
    username = request.form['login']
    password = request.form['haslo']
 if password == "haslo":
    id = username
    user = User(id)
    login_user(user)
    return redirect(url_for("main"))
 else:
    return abort(401)


@login_manager.user_loader
def load_user(userid):
 return User(userid)




@app.route("/zmyka", methods=['POST', 'GET'])
def zmyka():
    
    nazwa = request.form['Temat_Posta']
    connection = sql.connect('database.db')
    connection.row_factory = sql.Row
    cursor = connection.cursor()
    cursor.execute('DELETE FROM Posty WHERE Temat_Posta = ?', (nazwa,))
    connection.commit()
    msg="Post usuniety"
    
    cursor.execute('SELECT * FROM Posty')
    
    
    connection.close()
    
    return render_template('rezultat.html', msg=msg)

@app.route("/kontakcik", methods=['POST', 'GET'])
def kontakcik():
    return render_template('wiadomosc.html')

if __name__== "__main__":
    app.run()


