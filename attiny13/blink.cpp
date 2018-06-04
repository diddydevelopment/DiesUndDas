#include <avr/io.h>
#include <util/delay.h>


//void set_bit(bool b){
	
//}

int main(void)
{
  DDRB = (1 << PB3); //PB3 as output

  while (1) {
    PORTB |= (1 << PB3); //set bit PB3 of PORTB
    _delay_ms(500);
    PORTB &= ~(1 << PB3); //unset bit PB3 of PORTB
    _delay_ms(500);
  }
}
