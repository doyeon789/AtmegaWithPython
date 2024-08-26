/* C언어 코드 */
/*
 * pyton_test.c
 *
 * Created: 2024-08-26 / 11:44:58
 * Author : doyeon
 */ 

#define F_CPU 16000000UL
#include <avr/io.h>
#include <util/delay.h>
#include <stdio.h>

// USART0 초기화 함수
void usart0_init(unsigned int UBRR0) {
	UBRR0L = (unsigned char)UBRR0;
	UCSR0B = (1 << RXEN0) | (1 << TXEN0);
}

// USART0로 단일 문자 송신 함수
void tx0_ch(unsigned char data) {
	while (!(UCSR0A & (1 << UDRE0)));
	UDR0 = data;
}

// USART0로 문자열 송신 함수
void tx0_str(unsigned char *str) {
	while (*str){tx0_ch(*str++);}
}

int main(void){
    
	char buffer[10];
	unsigned int value = 0;

  	// USART0 초기화, 9600bps 보율 설정 (UBRR0 = 103)
	usart0_init(103);
	
	while (1) {
		//파이썬으로 전송할 문자열 설정
		sprintf(buffer, sizeof(buffer), "%d\n", value);
   		 //전송
		tx0_str(buffer);
		value++;
		_delay_ms(1000);
	}
}
