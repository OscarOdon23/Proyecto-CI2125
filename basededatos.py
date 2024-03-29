import sqlite3

conn = sqlite3.connect('parciales.db')
c = conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS parciales (
          Numero TEXT PRIMARY KEY ,
          PrimerParcial TEXT NOT NULL,
          SegundoParcial TEXT NOT NULL,
          TercerParcial TEXT NOT NULL)""")

c.execute("INSERT INTO parciales VALUES ('1', 'Tiene una esfera de masa M uniforme y radio R que puede rotar en torno a dos ejes, e1 o e2 (que pasa justo por su centro), con rapidez angular ω1 o ω2, respectivamente. Qué relación deben tener ω1 y ω2 para que las energías cinéticas sean iguales?','Considere 4 partículas de masa m dispuestas sobre un aro de masa m y radio R.. Las partículas equidistan una de otra. ¿Cuál es su inercia en los ejes X, Y, Z?','Como se define el calor?')")
conn.commit()

c.execute("SELECT * FROM parciales")
parciales = c.fetchone()
print(parciales)

conn.close()
