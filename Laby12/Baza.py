import sqlite3



conn = sqlite3.connect('database.db')
print("BD otwarta")
conn.execute('DROP TABLE IF EXISTS pracownicy')
conn.execute('CREATE TABLE pracownicy (imie TEXT, nazwisko TEXT, nrpracownika TEXT, adres TEXT)')


print("Tabela utworzona")








cur = conn.cursor()

cur.execute("INSERT INTO pracownicy (imie, nazwisko, nrpracownika, adres) VALUES (?,?,?,?)",('Bogdan','Nejdrowicz','101','Wyczolkowskiego 9/11') )

cur.execute("INSERT INTO pracownicy (imie, nazwisko, nrpracownika, adres) VALUES (?,?,?,?)",('Tadeusz','Kowalewski','420','Grunwaldzka 14/10') )

cur.execute('SELECT * FROM pracownicy')
print(cur.fetchall())#drukowanie rezultatu

conn.close()