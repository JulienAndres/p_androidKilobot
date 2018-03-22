
#define MAXVOISIN 5 //nombre de voisins dans la liste
#define SECONDE 32 //nombre de tick en 1 seconde
#define ASK 70  //mydata->distance minimale entre 2 kilobots

#define STOP 0
#define STRAIGHT 1
#define LEFT 2
#define RIGHT 3



// declare variables


typedef struct{   //Sert à garder les parametres de chacun des voisins
  uint32_t timestamp; //timestamp de la recetion du message de ce voisin
  uint8_t dist;  //mydata->distance estimé de ce voisin au dernier timestamp
  uint16_t id;  //id de ce voisin
}voisins;

typedef struct{
  uint8_t nb_voisins;  //nombre de voisins dans la liste
  voisins voisins_liste[MAXVOISIN]; //liste des voisins

  uint8_t next_direction;
  uint8_t previous_dir;
  int last_update; //derniere update de la direction


  message_t messagetx;    //message transmis
  message_t messagerx;    //message recu
  uint8_t new_message;   //est mis à 1 si un message arrive
  uint8_t distance;    //mydata->distance estimé du kilobot qui evoir le message

  uint8_t nb;
} USERDATA;
