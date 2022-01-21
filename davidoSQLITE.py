"""
@author: David Reyes
@date: 20/01/2022
"""
import sqlite3

class SQLITEpersonalizado:
    def __init__(self):pass
    def querySinRetornoDeDatos(self, nombreBD, querySQL, parametrosSQL):
        """[Funcion para ejecutar SQL sin retorno de datos]

        Args:
            nombreBD ([string]): [nombre de la Base de Datos]
            querySQL ([string]): [QUERY a ejecutar]
            parametrosSQL ([tuple]): [valores de interaccion]

        Returns:
            [string]: [mensaje de exito o error]
        """
        try:
            conexion = sqlite3.connect(nombreBD)
            cursor = conexion.cursor()
            cursor.execute(querySQL, parametrosSQL)
            conexion.commit()
            conexion.close()
            return "¡Script ejecutado con exito!"
        except Exception as e:return "¡ERROR!: {0}".format(e)
    def queryRetornoDeUnRegistro(self, nombreBD, querySQL, parametrosSQL):
        """[Funcion para ejecutar SQL con retorno de un registro]

        Args:
            nombreBD ([string]): [nombre de la Base de Datos]
            querySQL ([string]): [QUERY a ejecutar]
            parametrosSQL ([tuple]): [valores de interaccion]

        Returns:
            [tuple]: [contiene los datos del registro]
            [string]: [mensaje de error]
        """
        try:
            conexion = sqlite3.connect(nombreBD)
            cursor = conexion.cursor()
            ejecutar = cursor.execute(querySQL, parametrosSQL)
            conexion.commit()
            conexion.close()
            resultado = ejecutar.fetchone()
            return resultado
        except Exception as e:return "¡ERROR!: {0}".format(e)
    def queryRetornoDeMuchosRegistros(self, nombreBD, querySQL, parametrosSQL):
        """[Funcion para ejecutar SQL con retorno de varios registros]

        Args:
            nombreBD ([string]): [nombre de la Base de Datos]
            querySQL ([string]): [QUERY a ejecutar]
            parametrosSQL ([tuple]): [valores de interaccion]

        Returns:
            [tuple]: [contiene los datos de los registros]
            [string]: [mensaje de error]
        """
        try:
            conexion = sqlite3.connect(nombreBD)
            cursor = conexion.cursor()
            ejecutar = cursor.execute(querySQL, parametrosSQL)
            conexion.commit()
            conexion.close()
            resultados = ejecutar.fetchall()
            return resultados
        except Exception as e:return "¡ERROR!: {0}".format(e)