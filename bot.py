import time

palabras_clave = ["donde vives", "te doy mi telefono", "ser tu amigo", "telefono", "celular", "pasame tu telefono", "en donde naciste", "conocerte", "te llamas", "tu nombre", "telefono", "direccion", "vives solo", "cuantos años tienes", "tu edad", "mandame fotos",  "foto", "videos", "video", "cual es tu casa", "donde estudias", "como se llaman tus papas"]

def detectar_palabras(texto):
    texto = texto.lower()
    palabras_encontradas = []
    for palabra in palabras_clave:
        if palabra in texto:
            palabras_encontradas.append(palabra)
    return palabras_encontradas



def monitorear_mensajes():

    while True:
        # Aquí simulas recibir un mensaje, por ejemplo desde un chat o consola
        mensaje = input(":")
        if mensaje.lower().strip() == "adios":
            print("Adios")
            break
        
        
            # Aquí puedes agregar lógica para notificar usuarios, registrar en archivo, etc.
        #else:
            #print("vere que pongo ")
        if mensaje.lower().strip() == "que vamos a jugar?":
            print("ya estoy dentro unete")  

        if mensaje.lower().strip() == "como se llaman tus papas":
            print("No te voy a decir")  

        if mensaje.lower().strip() == "no quiero jugar ahorita":
            print("entonces que quieres hacer?")  

        if mensaje.lower().strip() == "en donde vives":
            print("porque quieres saber") 
        
        if mensaje.lower().strip() == "te doy mi telefono":
            print("no me des tu telefono")

        if mensaje.lower().strip() == "tienes celular":
            print("no tengo celular")

        if mensaje.lower().strip() == "que te gusta hacer":
            print("jugar con mis amigos")

        if mensaje.lower().strip() == "y yo soy uno de tus amigos?":
            print("no te conozco")

        if mensaje.lower().strip() == "pero puedo ser tu amigo":
            print("no quiero que un desconocido sea mi amigo")
        
        if mensaje.lower().strip() == "como te dicen":
            print("por el nombre de mi usuario")

        resultado = detectar_palabras(mensaje)
        if resultado:
            print(f"Advertencia contenido sospechoso {resultado}")
        
        if mensaje.lower().strip() == "hola quieres jugar conmigo":
            print("claro que si")

        if mensaje.lower().strip() == "hola":
            print("hola")

        if mensaje.lower().strip() == "quieres jugar conmigo":
            print("claro que si")




if __name__ == "__main__":
    monitorear_mensajes()
