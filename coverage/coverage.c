#include <kilolib.h>

#define WAIT 0
#define MOVE 1




motion_dir previous_dir=STOP;
message_t message;
int new_message=0;

void message_rx(message_t *m, distance_measurement_t *d)
{
    new_message = 1;
    distance = estimate_distance(d);
}

void update_motors(motion_dir direction) {
    if (direction != previous_dir) {
        previous_dir = direction;
        switch(direction) {
            case STRAIGHT:
              previous_dir=STRAIGHT
                spinup_motors();
                set_motors(kilo_straight_left, kilo_straight_right);
                break;
            case LEFT:
            previous_dir=LEFT
                spinup_motors();
                set_motors(kilo_turn_left,0);
                break;
            case RIGHT:
            previous_dir=RIGHT
                spinup_motors();
                set_motors(0,kilo_turn_right);
                break;
            case STOP:
                previous_dir=STOP
                set_motors(0,0);
                break;
        }
      }
}
message_t *message_tx()
{
    return &message;
}

void message_rx(message_t *message, distance_measurement_t *distance)
{
    new_message = 1;
}
// void message_tx_success()
// {
//     // Set the flag on message transmission.
//     message_sent = 1;
// }

void update_msg(){
  message.data[0]=kilo_uid
}

void setup()
{
    // Initialize message:
    // The type is always NORMAL.
    message.type = NORMAL;
    message.data[0] = 0;
    message.crc = message_crc(&message);
}

void loop()
{
    // Blink the LED magenta whenever a message is sent.
    if (message_sent == 1)
    {
        // Reset the flag so the LED is only blinked once per message.
        message_sent = 0;

        set_color(RGB(1, 0, 1));
        delay(100);
        set_color(RGB(0, 0, 0));
    }
}


int main()
{
    kilo_init();
    // Register the message_rx & message_tx callback function.
    kilo_message_rx = message_rx;
    kilo_message_tx=message_tx;
    //start loop
    kilo_start(setup, loop);

    return 0;
}
