.PHONY: kilofauteuil_46 clean
KILOLIB = /root/kilolib/build/kilolib.a
DIR_KILOLIB=/root/kilolib/

kilofauteuil_46: build/kilofauteuil_46.hex # build/kilofauteuil_46.lss build/kilofauteuil_46.elf

CC = avr-gcc
AVROC = avr-objcopy
AVROD = avr-objdump

CFLAGS = -mmcu=atmega328p -Wall -gdwarf-2 -O3 -funsigned-char -funsigned-bitfields -fpack-struct -fshort-enums -I .
CFLAGS += -DF_CPU=8000000

FLASH = -R .eeprom -R .fuse -R .lock -R .signature
EEPROM = -j .eeprom --set-section-flags=.eeprom="alloc,load" --change-section-lma .eeprom=0  

#%.lss: %.elf
#	$(AVROD) -d -S $< > $@

#%.eep: %.elf
#	$(AVROC) -O ihex $(EEPROM) $< $@

#%.bin: %.elf
#	$(AVROC) -O binary $(FLASH) $< $@ 


%.hex: %.elf
	$(AVROC) -O ihex $(FLASH) $< $@
	rm build/kilofauteuil_46.elf

build:
	mkdir -p $@

build/kilofauteuil_46.elf: kilofauteuil_46.c $(KILOLIB) | build
	$(CC) $(CFLAGS) -o $@ $< $(KILOLIB) -I $(DIR_KILOLIB)

clean:
	rm -fR build
