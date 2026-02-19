#include <xc.h>
#define _XTAL_FREQ 20000000

// Configuración básica
#pragma config FOSC = HS  // Cristal HS
#pragma config WDTE = OFF  // Watchdog off
#pragma config PWRTE = ON  // Power-up timer
#pragma config MCLRE = ON  // MCLR habilitado
#pragma config CP = OFF     // Protección código off
#pragma config BOREN = ON   // Brown-out reset
#pragma config LVP = OFF    // Low voltage programming off

void UART_Init() {
    TRISC6 = 0; // TX salida
    TRISC7 = 1; // RX entrada
    SPBRG = 129; // 9600 baud con Fosc=20MHz
    TXSTA = 0x24;
    RCSTA = 0x90;
}

void UART_Write(char data) {
    while(!TXIF);
    TXREG = data;
}

char UART_Read() {
    while(!RCIF);
    return RCREG;
}

void servo_move(int grados) {
    // PWM por software simple
    int pulso = 500 + (grados * 1000 / 180); // 500-2500us
    for(int i=0; i<20; i++) {  // 20 ciclos para estabilidad
        RD2 = 1;
        __delay_us(pulso);
        RD2 = 0;
        __delay_us(20000 - pulso); // Periodo ~20ms
    }
}

void buzzer_beep(int frecuencia, int duracion) {
    int periodo = 1000000 / frecuencia; // en microsegundos
    long ciclos = (duracion * 1000) / periodo;
    for(long i=0; i<ciclos; i++) {
        RD3 = 1;
        __delay_us(periodo/2);
        RD3 = 0;
        __delay_us(periodo/2);
    }
}

void main() {
    // Inicializar puertos
    TRISD = 0x00;  // RD como salidas
    PORTD = 0x00;
    
    UART_Init();
    
    char buffer[20];
    int idx = 0;
    
    while(1) {
        if(RCIF) {
            char c = UART_Read();
            if(c == '\n') {
                buffer[idx] = '\0';
                
                // Procesar comando
                if(buffer[0] == 'S') {  // Servo
                    int grados = atoi(buffer+1);
                    servo_move(grados);
                    UART_Write('O'); UART_Write('K'); UART_Write('\n');
                }
                else if(buffer[0] == 'B') {  // Buzzer
                    buzzer_beep(1000, 500); // 1kHz por 500ms
                    UART_Write('O'); UART_Write('K'); UART_Write('\n');
                }
                else if(buffer[0] == 'L') {  // LEDs
                    if(buffer[1] == '1') RD0 = 1;
                    if(buffer[1] == '2') RD1 = 1;
                    if(buffer[1] == '0') { RD0 = 0; RD1 = 0; }
                    UART_Write('O'); UART_Write('K'); UART_Write('\n');
                }
                else {
                    UART_Write('?'); UART_Write('\n');
                }
                
                idx = 0;
            }
            else {
                buffer[idx++] = c;
            }
        }
    }
}