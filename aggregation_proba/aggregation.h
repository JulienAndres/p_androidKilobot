#ifndef AGGREGATION__H
    #define AGGREGATION__H

    #define MAXVOISIN 10

    void setup(void);
    void emission(void);
    //void loop(void);
    void update_voisins();
    void update_from_message();
    void aggregation(void);
    void searching(void);
    uint8_t found_to_aggregate(void);
    void converging(void);
    void sleeping(void);
    void set_motion(uint8_t);
    void set_random_direction(void);
    uint8_t is_too_close(void);
    void set_random_turning_direction(void);
    int lost_aggregate(void);

    typedef struct {
      uint8_t dist;
      uint16_t id;                /*!< the last known dist of the neighbor */
      uint32_t timestamp;     /*!<the tick where the last information was received from this neighbor ) */
    } Neighbor_t;

    typedef struct
    {
      uint8_t state;
      uint32_t nb_voisins;
      Neighbor_t voisins_liste[MAXVOISIN];

    	uint8_t curr_motion;
    	uint32_t last_motion_update;
      uint32_t start_repelling;
    	uint8_t new_message;

      uint8_t dist;
      uint8_t last_dist_update;

      Neighbor_t toAggregate;

      message_t message;
      uint8_t broadcast;
      uint8_t message_sent;

    } USERDATA;

    enum motion {
      STOP,                /*!< The robot is stopped*/
      LEFT,                 /*!< The robot is moving to the left */
      RIGHT,               /*!< The robot is moving to the right */
      STRAIGHT         /*!< The robot is moving straight */
    };

    enum state {
    SEARCHING,             /*!< The robot is searching for an other robot */
    CONVERGING,          /*!< The robot is moving to a neighbor */
    SLEEPING                /*!< The robot is sleeping */
    };

#endif
