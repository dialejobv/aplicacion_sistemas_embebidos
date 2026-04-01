# Instalación y uso del Pickit 3
Para utilizar el pickit 3, lo primero que se debe desarrollar son los siguientes pasos:
1. Ir a la página oficial de Microchip y descargar la última versión de MPLAB X IDE, el enlace oficial es: [Enlace Oficial](https://www.microchip.com/en-us/tools-resources/develop/mplab-x-ide)
<img width="2762" height="1692" alt="image" src="https://github.com/user-attachments/assets/433bbdb7-ed7c-4c3d-b965-160601946d32" />

2. Posteriormente descargar el programador del pickit 3, el enlace oficial es: [Enlace Oficial]()
<img width="2660" height="529" alt="image" src="https://github.com/user-attachments/assets/ceece726-c840-4e57-a2d9-38c364a09fe6" />

3. Luego buscar el instalador de pic c compiler y descargarlo (este se descarga por facilidad de programación para los estudiantes), también pueden usar el XC8 Compiler de Microchip.
<img width="2390" height="1636" alt="image" src="https://github.com/user-attachments/assets/1b1f2960-2be9-4248-ba71-cc9ecafce30e" />

4. Posteriormente deben conectar el pickit 3 que es  una herramienta de desarrollo de hardware y software diseñada por Microchip Technology para programar, depurar (debug) y emular una amplia gama de microcontroladores PIC y dsPIC, así como memorias EEPROM. Permite cargar código, realizar pruebas en tiempo real e implementar la programación en circuito (ICSP) mediante conexión USB, siendo un dispositivo fundamental en electrónica. A continuación se comparte una foto de los pines que se deben tener presentes en la conexión del pickit 3 y una foto de conexión al pc:
<img width="1982" height="1100" alt="image" src="https://github.com/user-attachments/assets/e83b4dff-9c2c-429c-bcee-b24549729606" />

5. Posteriormente se debe abrir el pickit 3, con pic C, generar el respectivo archivo .hex, verificar que se detecte el pic, importar el archivo .hex en el software **pickit 3 programmer** luego de desarrollar la lectura, escritura y posteriormente la verificación de cada uno de los pasos, como se expone a continuación:
<img width="2374" height="1142" alt="image" src="https://github.com/user-attachments/assets/cd4789d8-ac04-46f0-b6d3-977ac0cc6563" />

6. Si se tienen más dudas sobre el uso del pickit 3 y la forma en como cargar al pic se invita a los estudiantes a revisar los siguientes enlaces:
   * [Enlace 1](https://www.youtube.com/watch?v=OPN4hIGuZnY)
   * [Enlace 2](https://www.youtube.com/watch?v=1AJ-c8pVNak)
   * [Enlace 3](https://www.youtube.com/watch?v=AO_Eief349E)
     
# ¿Qué es Microchip?
Microchip Technology o Microchip, es una empresa estadounidense líder mundial en el suministro de microcontroladores (MCU), semiconductores analógicos y soluciones de control integrado. Sus productos son esenciales en una amplia gama de dispositivos electrónicos, desde electrodomésticos y automóviles hasta sistemas aeroespaciales y equipos industriales

## ¿Qué productos genera?
Los productos que genera son:

| Categoría de Producto | Descripción / Series Destacadas | Aplicaciones Clave |
| :--- | :---: | ---: |
|   Microcontroladores (MCUs)  |    El núcleo de su negocio. Familias PIC (8, 16 y 32 bits), AVR, y SAM (32-bit ARM Cortex).   |   Control industrial, automotriz, consumo, IoT.   |
|   Microprocesadores (MPUs)   |    Unidades de procesamiento más potentes, como la familia SAMA7, para aplicaciones que requieren sistemas operativos como Linux.   |   Interfaces humano-máquina (HMI), conectividad, control de maquinaria.   |
|   FPGAs   |    Adquiridos a Microsemi, como las familias PolarFire e IGLOO. Son conocidos por su bajo consumo y alta fiabilidad.   |   Aeroespacial, defensa, comunicaciones, procesamiento de video.   |
|   Analogía e Interface   |    Amplia gama de productos, desde reguladores de potencia y controladores de iluminación hasta interfaces USB, Ethernet y CAN.   |   Gestión de energía, conectividad en automóviles y datacenters.   |
|   Seguridad   |    Soluciones de hardware y software, como las familias CryptoAuthentication™ y TrustFLEX.   |   Autenticación de dispositivos, pago seguro en terminales.   |
|   Conectividad Inalámbrica   |    Soluciones Wi-Fi, Bluetooth, LoRa, y tecnología KeeLoq para acceso remoto seguro.   |   IoT, ciudades inteligentes, sistemas de alarma.   |
|   Temporización (Timing)   |    Dispositivos de sincronización de alta precisión, como el TimeProvider 4500, esenciales para redes 5G y centros de datos.   |   Infraestructura de telecomunicaciones.   |

## ¿Cuál es la arquitectura del PIC16F887?
 La aqruitectura es la siguiente:
 <img width="1682" height="1654" alt="image" src="https://github.com/user-attachments/assets/66cc0649-abc1-48a0-9144-a5eb3b5bc5cc" />
 Para más información revisar la [ficha técnica](https://www.alldatasheet.com/html-pdf/197543/MICROCHIP/PIC16F887/488/1/PIC16F887.html)



