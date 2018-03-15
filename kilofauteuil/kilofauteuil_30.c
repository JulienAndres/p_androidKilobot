#include <kilolib.h>

#define STOP 0
#define FORWARD 1
#define LEFT 2
#define RIGHT 3

int val_g = 80;
int val_d = 80;
int down;
void setup() {
  down = 0;
}

void loop() {
    // OSCILLATION de 80 à 200 10 par 10 toutes les 2,5s
    // ---> periode d'1 minute, amplitude 120
    if(val_d >= 200){
      down = 1;
    }
    if(val_d <= 80){
      down = 0;
    }
    if(down){
      set_motors(val_g, val_d);
      val_d -= 10;
      val_g -= 10;
      set_color(RGB(1, 0, 0));

    } else {
      set_motors(val_g, val_d);
      val_d += 10;
      val_g += 10;
      set_color(RGB(0, 1, 0));
    }
    delay(2500);
}

int main() {

    kilo_init();
    kilo_start(setup, loop);

    return 0;
}
