import sqlite3
#Import "Almacen.db"
database = "Almacen.db"
class DB:
    def ejecutar_consulta(self,consulta,parametros =()):
        with sqlite3.connect(database)as conn:
            self.cursor = conn.cursor()
            result = self.cursor.execute(consulta, parametros)
            conn.commit()
            return result
    def consultar_por_id(self,consulta,parametros =()):
        with sqlite3.connect(database)as conn:
            self.cursor = conn.cursor()
            self.cursor.execute(consulta, parametros)
            result = self.cursor.fetchone()
            return result
