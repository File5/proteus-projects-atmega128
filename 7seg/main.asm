;====================================================================
; Main.asm file generated by New Project wizard
;
; Created:   ?? ??? 24 2018
; Processor: ATmega128
; Compiler:  AVRASM (Proteus)
;====================================================================

;====================================================================
; DEFINITIONS
;====================================================================
.def temp = R16
.def temp2 = R17
.def temp3 = R18

.def buttons = R20
.def last_buttons = R21
.def number_byte = R22
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
      setup_ports:
	    in_ports:
		  ldi temp, 0x00
		  out DDRC, temp
		  ldi temp, 0xFF
		  out PORTC, temp
		  
	    out_ports:
		  ldi temp, 0xFF
		  out DDRD, temp
		  out DDRE, temp
		  
      ldi temp, 0xFF
      out PORTD, temp
      out PORTE, temp
      
      ldi last_buttons, 0xFF
      ldi number_byte, 0x0D
Loop:
      in buttons, PINC
      cpi buttons, 0xFF
      breq buttons_are_up
      buttons_are_down:
	    cp buttons, last_buttons
	    breq buttons_are_up
	    button_down_event:
		  mov temp, buttons
		  call ON_BUTTON_DOWN
      buttons_are_up:
      mov last_buttons, buttons
      
      out PORTE, number_byte
      mov temp, number_byte
      call CONVERT_temp_TO_SEG
      out PORTD, temp
      
      call SLEEP_FF
      
      jmp  Loop

;====================================================================
ON_BUTTON_DOWN:
      ldi temp2, 0x01
      sbrs temp, 0
      jmp button_1
      sbrs temp, 1
      jmp button_2
      sbrs temp, 2
      jmp button_3
      button_1:
      add number_byte, temp2
      jmp end_button
      button_2:
      ldi number_byte, 0x00
      jmp end_button
      button_3:
      sub number_byte, temp2
      jmp end_button
      end_button:
ret
CONVERT_temp_TO_SEG:
      ldi temp2, 0x00
      ldi ZH, high(seg_table * 2)
      ldi ZL, low(seg_table * 2)
      add ZL, temp
      adc ZH, temp2
      lpm temp, Z
ret
SLEEP_FF:
      ldi temp3, 0xFF
      sleep_loop:
	    cpi temp3, 0x00
	    breq end_sleep
	    dec temp3
	    jmp sleep_loop
      end_sleep:
ret
;====================================================================
; DATA
;====================================================================
seg_table: .db 0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x6F, 0x77,0x7C,0x39,0x5E,0x79,0x71
