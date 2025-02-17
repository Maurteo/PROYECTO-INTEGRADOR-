import json
import csv
import sys
import requests
import pandas as pd  
from datetime import datetime 
import tkinter as tk
from tkinter import Label,Button,ttk,messagebox,Menu

import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

# Función para cargar y mostrar precios en una nueva ventana
def mostrar_precios():
    try:
        # Leer el archivo productos.csv
        productos = pd.read_csv('productos.csv', encoding='UTF-8')
        
        # Crear una nueva ventana para mostrar los precios
        ventana_precios = tk.Toplevel()
        ventana_precios.title("Lista de Precios")
        ventana_precios.geometry("600x400")

        # Crear el Treeview para mostrar los datos en tabla
        columnas = productos.columns.tolist()  # Obtener nombres de las columnas del CSV
        tree = ttk.Treeview(ventana_precios, columns=columnas, show="headings")

        # Configurar encabezados de la tabla
        for col in columnas:
            tree.heading(col, text=col)
            tree.column(col, width=150)

        # Insertar datos en la tabla
        for _, fila in productos.iterrows():
            tree.insert("", tk.END, values=fila.tolist())

        # Empaquetar el Treeview
        tree.pack(expand=True, fill=tk.BOTH)

    except FileNotFoundError:
        messagebox.showerror("Error", "El archivo productos.csv no se encontró.")
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un problema: {e}")



#LEER ARCHVOS
try:
    
    with open("C:/Users/Usuario/Desktop/PROYECTO INTEGRADOR/auth_usuarios.json","r") as archivo:
     datos_json = json.load(archivo)
except PermissionError: print("Error: hubo un problema con los permisos")
except FileNotFoundError: print("Error: el archivo de autentificación no fue encontrado")

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
        print(f"Error al obtener la cotización {e}")
        return None
      

#ACTUALIZAR PRECIOS
def actualizar_precios(productos, cotizacion):
    if cotizacion is None:
        print("Error: no se pudo obtener la cotización del dólar")
    return productos

#ITERAR PRODUCTOS 
def obtener_precio_dolar(productos, cotización):
 for productos in productos:
   productos = productos["precio"] * cotización
 return productos 

#LEER PRECIOS
def leer_precios():
    try:
        return pd.read_csv('productos.csv', encoding="UTF-8")
    except FileNotFoundError:
        print("Error: no se pudo encontrar el archivo")

    
#GUARDAR HISTORIAL
try:
    def guardar_historial(productos):
       if "precio actualizado" or "Precio Actualizado" in productos:
        with open('historial_precios', 'a', newline='') as file:
            writer = csv.writer(file)
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([fecha] + productos['precio actualizado'].round(2).tolist())
       else:
           print("Error: la clave precio actualizado no existe en PRODUCTOS")
        
finally: 

#ACTUALIZAR Y MOSTRAR PRECIOS
 def actualizar_y_mostrar():
     
    cotizacion = cotizacion_dolar()
    productos = leer_precios()
    if cotizacion and productos is not None:
        productos_actualizados = actualizar_precios(productos, cotizacion)
        guardar_historial(productos_actualizados)

#USAMOS TKINTER PARA HACER LA INTERFAZ GRÁFICA
def mensaje():
 print("mensaje del botón")

#VENTANA Y LABELS
ventana = tk.Tk()
ventana.geometry("2250x1000")
ventana.title("Por el momento es una ventana")
lbl = Label(ventana, text= "esta es una ventana")
lbl.pack()

def validar_credenciales(datos_json, usuario, contraseña):
    for registro in datos_json:
      if registro["usuario"] == usuario and registro["password"] == contraseña:
       print("credenciales correctas")
       return True 
      print("credenciales incorrectas dentro de la función")
    return False    
   
#ENTRADAS
entrada_var = tk.StringVar(value="INGRESAR USUARIO")
entrada_1 = ttk.Entry(ventana, width=30, textvariable=entrada_var)
entrada_1.pack(side=tk.TOP, pady=5, padx=5)

entrada_var_2 = tk.StringVar(value="INGRESAR CONTRASEÑA")
entrada_2=ttk.Entry(ventana,width=30,textvariable=entrada_var_2)
entrada_2.pack(pady=15,padx=15) 
    
def abrir_menu_principal():
    ventana.withdraw()
    Menu_Ventana = tk.Toplevel()
    Menu_Ventana.title("MENU PRINCIPAL")
    Label(Menu_Ventana, text="ELIJA UNA OPCIÓN", font=("Arial", 14)).pack(pady=10)
    Menu_Ventana.geometry("2250x1000")
    
    
# OPCIÓN HISTORIAL DE PRECIOS
    def historial_de_precios():
        
         try:
           columnas = ["fecha", "precio1", "precio2", "precio3", "precio4", "precio5", "precio6"]
           historial = pd.read_csv("C:/Users/Usuario/Desktop/PROYECTO INTEGRADOR/historial_precios.csv")
                  
           ventana_hdp = tk.Toplevel()
           ventana_hdp.title("HISTORIAL DE PRECIOS")
           ventana_hdp.geometry("500x300")
           
           
           tree = ttk.Treeview(ventana_hdp, columns=columnas, show="headings")
           for col in columnas:
                 tree.heading(col, text=col)
                 tree.column(col, width=100 )
           tree.pack(expand=True, fill=tk.BOTH)
                        
           for _, fila in historial.iterrows():
               tree.insert("",tk.END, values=fila.tolist())

         except FileNotFoundError: 
                 messagebox.showerror("ERROR","Error: no se encontró el archivo")
         except KeyError:
          messagebox.showerror("ERROR","Error: el archivo no contiene las columnas esperadas")    
            
            
    btn_2 = ttk.Button(Menu_Ventana, text="Precios", command=mostrar_precios)
    btn_2.pack(pady=5)
    btn_historial_de_precios = Button(Menu_Ventana, text="Historial de Precios", command=historial_de_precios, width=20).pack(pady=5)

    def obtener_precio_dólar():
     if cotización:
         messagebox.showinfo("OBTENER PRECIO DÓLAR", f"La cotización del dólar es {cotización}")
     else: messagebox.showerror("ERROR", "No se pudo obtener la cotización")    
    
    
    
    btn_cotización = ttk.Button(Menu_Ventana, text= "Cotización del Dólar", command=obtener_precio_dólar)
    btn_cotización.pack(pady=10)





    try: 
         with open("C:/Users/Usuario/Desktop/PROYECTO INTEGRADOR/productos.csv", mode="r") as productos:
          lector = csv.DictReader(productos)
          productos = leer_precios()
          cotización = cotizacion_dolar()          
          for fila in lector:
             print(fila)
             
          def actualizar_precios_en_pesos(productos, cotización):   
            if isinstance(productos, pd.DataFrame):
                 if "precio" in productos.columns:
                     productos["precio en pesos"] = productos["Precio"] * cotización
                     print("nueva columna PRECIOS EN PESOS creada exitosamente")
                 else:
                     print("Error: no se encontró la columna precios")
            else: print("Error: productos no es un dataframe")
                  

             
         productos_actualizados = actualizar_precios(productos, cotización) 
         print(f"la cotización del dolar es {cotización}")      
      
    except FileNotFoundError: print("Error: no se ha encontrado el archivo")
    except KeyError: print("Error: formato incorrecto de archivo de csv.")
    
    if productos is not None and cotización is not None:
             productos_actualizados = actualizar_y_mostrar()
             productos_actualizados = actualizar_precios_en_pesos(productos, cotización)
             guardar_historial(productos_actualizados)

             print(productos_actualizados)
    

    #VALIDAR Y LOGGEAR
def validar_y_loggear():
    usuario = entrada_1.get().strip()  # Obtener el valor del campo de usuario
    contraseña = entrada_2.get().strip()  # Obtener el valor del campo de contraseña

    if validar_credenciales(datos_json, usuario, contraseña):
        messagebox.showinfo("LOGIN", "CREDENCIALES CORRECTAS. BIENVENIDO!")
        abrir_menu_principal()
        return True    
    else:
        messagebox.showerror("LOGIN", "CREDENCIALES INCORRECTAS")
        
    
       
        return False
        
#BOTONES
btn_logging = Button(ventana, text="Logging", command= validar_y_loggear)
btn_logging.pack(padx=10, pady=50)




#ETIQUETAS
etiqueta_1 = tk.Label(ventana, text="AQUÍ SE MOSTRARÁ EL CONTENIDO")
etiqueta_1.pack()
def enviar_1():
   btn.config(text=entrada_var.get())
def enviar_2():
    etiqueta_1.config(text=entrada_1.get())
mensaje1= entrada_1.get()

#FUNCIONES
def evento_click():
    btn.config(text="botón presionado")
    print("ejecución del evento_click")
    


#FUNCION SALIR
def Salir():
    sys.exit()

btn = ttk.Button(ventana, text="Dar Click", command=evento_click)
btn_salir = ttk.Button(ventana, text="presionar Aquí Para Salir", command=Salir)
btn_salir.pack(side=tk.BOTTOM)

#MENU PRINCIPAL

menu_principal = Menu(ventana)
sub_menu = Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(menu=sub_menu)

#DAR LA BIENVENIDA  AL USUARIO
print("bienvenido usuario, ingrese sus credenciales")

#INGRESO DE CREDENCIALES
usuario = input("USUARIO: ")
contraseña = input("CONTRASEÑA: ")


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
    print("credenciales incorrectas dentro de la función")
    sys.exit()

print()

#SISTEMA DE OPCIONES 
while True:
 print()

 print("1. precios")
 print("2. historial de precios")
 print("3. salir")


#INPUTS PARA LAS OPCIONES 
 elegir = input("elija una opción: ")


#CONDICIONALES PARA LAS OPCIONES 
 if elegir == "1" or elegir.lower() == "precios": 
    print()
  
 
            
    print()
    print("salir")
        
#OPCIÓN SALIR
 elif elegir == "3" or elegir == "salir":
     print()
     print("saliendo del programa...")
     sys.exit()
 else: 
    print("opción no válida. intenta nuevamente.")
    

    
#LOOP FINAL
 ventana.mainloop()