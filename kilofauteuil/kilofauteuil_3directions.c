#include <kilolib.h>
#include "main.h"
#include "movement.h"

#define STOP 0
#define FORWARD 1
#define LEFT 2
#define RIGHT 3

void setup() {
  //empty
}

void loop() {
// STRAIGHT 20s, LEFT 10s, RIGHT 10s
	set_motors(kilo_straight_left, kilo_straight_right);
	set_color(RGB(0, 1, 0));
	delay(20000);
	set_motors(kilo_turn_left,0);
	set_color(RGB(1, 0, 0));
	delay(10000);
	set_motors(0,kilo_turn_right);
	set_color(RGB(0, 0, 1));
	delay(10000);
}

int main() {

    kilo_init();
    kilo_start(setup, loop);

    return 0;
}
