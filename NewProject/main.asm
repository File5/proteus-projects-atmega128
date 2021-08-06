;====================================================================
; Main.asm file generated by New Project wizard
;
; Created:   �� ��� 16 2018
; Processor: ATmega128
; Compiler:  AVRASM (Proteus)
;====================================================================

;====================================================================
; DEFINITIONS
;====================================================================
.def temp = R16
.def led_switch = R17
.def last_state = R18
.def current_state = R19
;====================================================================
; VARIABLES
;====================================================================

;====================================================================
; RESET and INTERRUPT VECTORS
;====================================================================

      ; Reset Vector
      rjmp  Start

;====================================================================
; CODE SEGMENT
;====================================================================

Start:
      ; Write your code here
      SETUP_PORTS:
	 ; PORTA OUT
	 ldi temp, 0xFF
	 out DDRA, temp
	 
	 ; PORTB IN
	 ldi temp, 0x00
	 out DDRB, temp
	 ldi temp, 0xFF
	 out PORTB, temp
	
      SETUP_TIMER:
	 ldi temp, 0x00
	 out TCCR1B, temp
	 ldi temp, 0x80
	 out ACSR, temp
Loop:
      in current_state, PINB
      
      CPI current_state, 0xFE  
      brne button0_up
      button0_down:
	  cpi last_state, 0xFF
	  brne skip_button0
	       call ON_BUTTON0_DOWN
	  skip_button0:
      button0_up:
      
      ;in current_state, PINB
      CPI current_state, 0xFD  
      brne button1_up
      button1_down:
	  cpi last_state, 0xFF
	  brne skip_button1
	       call ON_BUTTON1_DOWN
	  skip_button1:
      button1_up:
      
      ;in current_state, PINB
      CPI current_state, 0xFB 
      brne button2_up
      button2_down:
	  cpi last_state, 0xFF
	  brne skip_button2
	       call ON_BUTTON2_DOWN
	  skip_button2:
      button2_up:
      
      mov last_state, current_state
      
      in temp, TCNT1L
      in temp, TCNT1H
      cpi temp, 0x04
      brlo skip_ontimer
      ontimer:
	 ldi temp, 0x02
	 eor led_switch, temp
      skip_ontimer:
      
      out PORTA, led_switch
      
      rjmp  Loop

;====================================================================
; PROCEDURES
;====================================================================
ON_BUTTON0_DOWN:
      ldi temp, 0x01
      eor led_switch, temp
      ret
ON_BUTTON1_DOWN:
      call TIMER_RESET
      call TIMER_START
      ret
ON_BUTTON2_DOWN:
      call TIMER_STOP
      call TIMER_RESET
      ret
LED_OUT:
      cpi led_switch, 0x00
      breq led_off
      led_on:
          ldi temp, 0xFF
          out PORTA, temp
      rjmp led_end
      led_off:
	  ldi temp, 0x00
	  out PORTA, temp
      led_end:
      ret
TIMER_RESET:
      ldi temp, 0x00
      out TCNT1H, temp
      out TCNT1L, temp
      ret
TIMER_START: 
      ldi temp, 0x01
      out TCCR1B, temp
      ret
TIMER_STOP:
      ldi temp, 0x00
      out TCCR1B, temp
      ret
;====================================================================
