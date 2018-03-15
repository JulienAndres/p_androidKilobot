.PHONY: coverage clean
KILOLIB = /root/kilolib/build/kilolib.a
DIR_KILOLIB=/root/kilolib/

coverage: build/coverage.hex # build/coverage.lss build/coverage.elf

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
	rm build/coverage.elf

build:
	mkdir -p $@

build/coverage.elf: coverage.c $(KILOLIB) | build
	$(CC) $(CFLAGS) -o $@ $< $(KILOLIB) -I $(DIR_KILOLIB)

clean:
	rm -fR build
