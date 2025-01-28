import json
import csv
import sys
import requests
import pandas as pd  
from datetime import datetime 

#COTIZAR DOLAR

def cotizacion_dolar():
    url = 'https://dolarapi.com/v1/dolares'
    try:
        response = requests.get(url,timeout=10)
        if response.status_code == 200:
         data = response.json()
        if isinstance(data, dict):   
         return data.get("compra")
        elif isinstance (data, list):
            return data[0].get("compra") 
        
    except Exception as e:
        print(f"error al obtener la cotización {e}")
        return None
      

#ACTUALIZAR PRECIOS
def actualizar_precios(productos, cotizacion):
    if cotizacion is None:
        print("error: no se pudo obtener la cotización del dólar")
    return productos


def obtener_precio_dolar():
 for productos in productos:
   productos["precio actualizado"] = productos["precio "] * cotización
 return productos 


def leer_precios():
    try:
        return pd.read_csv('productos.csv')
    except FileNotFoundError:
        return None

    
#GUARDAR HISTORIAL
def guardar_historial(productos):
    with open('historial_precios', 'a', newline='') as file:
        writer = csv.writer(file)
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([fecha] + productos['Precio Actualizado'].round(2).tolist())


#ACTUALIZAR Y MOSTRAR PRECIOS
def actualizar_y_mostrar():
    cotizacion = cotizacion_dolar()
    productos = leer_precios()
    if cotizacion and productos is not None:
        productos_actualizados = actualizar_precios(productos, cotizacion)
        guardar_historial(productos_actualizados)




#DAR LA BIENVENIDA  AL USUARIO


print("bienvenido usuario, ingrese sus credenciales")
#INGRESO DE CREDENCIALES


usuario = input("USUARIO: ")
contraseña = input("CONTRASEÑA: ")
#LEER ARCHVOS

try:
    
    with open("C:/Users/Usuario/Downloads/auth_usuarios.json","r") as archivo:
       datos_json = json.load(archivo)
except PermissionError: print("error: hubo un problema con los permisos")
except FileNotFoundError: print("el archivo de autentificación no fue encontrado")
print()
print()
print()
print()
print()
print()
print()

#FUNCIONES PARA VALIDAR CREDENCIALES
def validar_credenciales(datos_json, usuario, contraseña):
  
    for registro in datos_json:
      if registro["usuario"] == usuario and registro["password"] == contraseña:
       print("credenciales correctas")
       return True 
      print("credenciales incorrectas dentro de la función")
    return False
    
 
#VALIDAR USUARIO Y CONTRASEÑA PARA INGRESAR AL PROGRAMA
if validar_credenciales(datos_json, usuario, contraseña):
    print(f"bienvenido {usuario}")
else:
    print("credenciales incorrectas")
    sys.exit()

print()

#SISTEMA DE OPCIONES 

while True:
    
 print("1. precios")
 print("2. historial de precios")
 print("3. salir")


#INPUTS PARA LAS OPCIONES 
  
 elegir = input("elija una opción: ")


#CONDICIONALES PARA LAS OPCIONES 

 if elegir == "1" or elegir.lower() == "precios": 
    print()
    try: 
         with open("C:/Users/Usuario/Downloads/productos.csv", mode="r") as productos:
          lector = csv.DictReader(productos)
          productos = leer_precios()
          cotización = cotizacion_dolar()          
          for fila in lector:
             print(fila)
             
          def actualizar_precios_en_pesos():   
            if isinstance(productos, pd.DataFrame):
                 if "precio" in productos.columns:
                     productos["precio en pesos"] = productos["precio"] * cotización
                     print("nueva columna PRECIOS EN PESOS creada exitosamente")
                 else:
                     print("error: no se encontró la columna precios")
            else: print("productos no es un dataframe")
                  
             
             
             
             
             
             
         productos_actualizados = actualizar_precios(productos, cotización) 
         print()
         print(f"la cotización del dolar es {cotización}")      
         print()
         print(f"el precio es {productos_actualizados}")

         if productos is not None and cotización is not None:
              productos_actualizados = actualizar_precios_en_pesos(productos,cotización)
              guardar_historial(productos_actualizados)
              actualizar_y_mostrar() 
             
              productos_actualizados = actualizar_y_mostrar()
             
              print(productos_actualizados)
            
             
    except FileNotFoundError: print("no se ha encontrado el archivo")
    except KeyError: print("error: formato incorrecto de archivo de csv.")
    
   
    
    
    
    
 elif elegir == "2" or elegir.lower() == "historial de precios":
    with open("C:/Users/Usuario/Downloads/historial_precios.csv") as historial:
        historial_de_productos = csv.DictReader(historial)
        for historial_final in historial_de_productos:
            print(historial_final)
            
    print()
    print("salir")
        
    
 elif elegir == "3" or elegir == "salir":
     print()
     print("saliendo del programa...")
     sys.exit()
 else: 
    print("opción no válida. intenta nuevamente.")
    

    