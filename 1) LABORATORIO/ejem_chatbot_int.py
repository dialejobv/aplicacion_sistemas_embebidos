import serial
import json
import re

arduino = serial.Serial('COM3', 9600, timeout=1)

# Estado simulado de objetos (en realidad vendría de OpenCV)
objetos_actuales = [
    {"color": "rojo", "forma": "circulo"},
    {"color": "azul", "forma": "cuadrado"},
    {"color": "verde", "forma": "triangulo"}
]

def interpretar_chat(entrada):
    entrada = entrada.lower()
    
    if re.search(r'cu[áa]ntos? (objetos?|cosas?)', entrada):
        return f"Veo {len(objetos_actuales)} objetos."
    
    if re.search(r'rojos?|azules?|verdes?', entrada):
        color = re.findall(r'rojos?|azules?|verdes?', entrada)[0][:3]  # simplificado
        count = sum(1 for o in objetos_actuales if o['color'] == color)
        return f"Hay {count} objetos de color {color}."
    
    if re.search(r'c[íi]rculos?|cuadrados?|tri[áa]ngulos?', entrada):
        forma = re.findall(r'c[íi]rculos?|cuadrados?|tri[áa]ngulos?', entrada)[0][:4]
        count = sum(1 for o in objetos_actuales if o['forma'] == forma)
        return f"Veo {count} {forma}s."
    
    if re.search(r'mueve|brazo|servo', entrada):
        # Comando para PIC: S=servo, 0/90/180 grados
        if '0' in entrada or 'cero' in entrada:
            arduino.write(b'S0\n')
        elif '90' in entrada:
            arduino.write(b'S90\n')
        elif '180' in entrada:
            arduino.write(b'S180\n')
        return "Moviendo brazo..."
    
    if re.search(r'alerta|buzzer|sonido', entrada):
        arduino.write(b'B\n')  # Buzzer
        return "Activando alerta sonora."
    
    return "No entendí. Pregunta por objetos, colores o formas."

print("Chatbot educativo iniciado. Pregunta algo...")
while True:
    texto = input("Tú: ")
    respuesta = interpretar_chat(texto)
    print("Bot:", respuesta)