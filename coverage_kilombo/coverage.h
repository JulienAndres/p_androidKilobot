
#define MAXVOISIN 5 //nombre de voisins dans la liste
#define SECONDE 32 //nombre de tick en 1 seconde
#define ASK 50  //mydata->distance minimale entre 2 kilobots

#define STOP 0
#define STRAIGHT 1
#define LEFT 2
#define RIGHT 3

void set_random_direction();
void update_motors(uint8_t direction);
void loop();
uint8_t tooClose();
void setup();
void message_rx(message_t *message, distance_measurement_t *d);
message_t *message_tx();
void update_voisins();
void update_from_message();

// declare variables


typedef struct{   //Sert à garder les parametres de chacun des voisins
  uint32_t timestamp; //timestamp de la recetion du message de ce voisin
  uint8_t dist;  //mydata->distance estimé de ce voisin au dernier timestamp
  uint16_t id;  //id de ce voisin
}voisins;

typedef struct{
    uint32_t last_update; //derniere update de la direction
  uint8_t nb_voisins;  //nombre de voisins dans la liste
  voisins voisins_liste[MAXVOISIN]; //liste des voisins
  uint8_t next_direction;
  uint8_t previous_dir;



  message_t messagetx;    //message transmis
  message_t messagerx;    //message recu
  uint8_t new_message;   //est mis à 1 si un message arrive
  uint8_t distance;    //mydata->distance estimé du kilobot qui evoir le message

  uint8_t nb;
} USERDATA;
