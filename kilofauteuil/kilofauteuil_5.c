#include <kilolib.h>


#define STOP 0
#define FORWARD 1
#define LEFT 2
#define RIGHT 3

int val_g = 100;
int val_d = 100;
int down;
void setup() {
  down = 0;
}

void loop() {
    //OSCILLATION TRES RAPIDE de 100 à 110 1 par 1 toutes les 0,1 s
    if(val_d >= 110){
      down = 1;
    }
    if(val_d <= 100){
      down = 0;
    }
    if(down){
      set_motors(val_g, val_d);
      val_d -= 1;
      val_g -= 1;
      set_color(RGB(1, 0, 0));

    } else {
      set_motors(val_g, val_d);
      val_d += 1;
      val_g += 1;
      set_color(RGB(0, 1, 0));
    }
    delay(500);
}


int main() {
    kilo_init();
    kilo_start(setup, loop);
    return 0;
}
