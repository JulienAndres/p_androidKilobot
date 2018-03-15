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
    //OSCILLATION PLUS LENTE de 80 à 150 3 par 3 toutes les 2 s
    //---> periode 46s*2, amplitude 70
    if(val_d >= 150){
      down = 1;
    }
    if(val_d <= 80){
      down = 0;
    }
    if(down){
      set_motors(val_g, val_d);
      val_d -= 3;
      val_g -= 3;
      set_color(RGB(1, 0, 0));
    } else {
      set_motors(val_g, val_d);
      val_d += 3;
      val_g += 3;
      set_color(RGB(0, 1, 0));
    }
    delay(2000);

}

int main() {
    kilo_init();
    kilo_start(setup, loop);

    return 0;
}
