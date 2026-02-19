import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Rangos de color en HSV
red_lower = np.array([0, 100, 100])
red_upper = np.array([10, 255, 255])
blue_lower = np.array([100, 100, 100])
blue_upper = np.array([130, 255, 255])

def detectar_formas(contorno):
    epsilon = 0.02 * cv2.arcLength(contorno, True)
    approx = cv2.approxPolyDP(contorno, epsilon, True)
    vertices = len(approx)
    
    if vertices == 3:
        return "triangulo"
    elif vertices == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspect = w / h
        return "cuadrado" if 0.9 < aspect < 1.1 else "rectangulo"
    elif vertices > 6:
        return "circulo"
    else:
        return "desconocido"

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Máscaras por color
    mask_red = cv2.inRange(hsv, red_lower, red_upper)
    mask_blue = cv2.inRange(hsv, blue_lower, blue_upper)
    
    # Encontrar contornos
    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    objetos_detectados = []
    
    for cnt in contours_red:
        area = cv2.contourArea(cnt)
        if area > 500:  # Filtrar ruido
            forma = detectar_formas(cnt)
            objetos_detectados.append({"color": "rojo", "forma": forma, "area": area})
            # Dibujar contorno
            cv2.drawContours(frame, [cnt], -1, (0, 0, 255), 2)
    
    # Similar para azul...
    
    cv2.imshow("Deteccion", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()