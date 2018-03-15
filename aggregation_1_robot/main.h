#ifndef MAIN__H
    #define MAIN__H


    void setup(void);
    //void loop(void);
    void aggregation(void);
    void searching(void);
    uint8_t found_to_aggregate(void);
    void converging(void);
    void sleeping(void);
    void set_motion(uint8_t);
    void set_random_direction(void);
    uint8_t is_too_close(void);
    void set_random_turning_direction(void);

    typedef struct {
      uint8_t dist;                    /*!< the last known dist of the neighbor */
      uint32_t timestamp;     /*!<the tick where the last information was received from this neighbor ) */
    } Neighbor_t;

    typedef struct
    {
      uint8_t state;
    	uint8_t curr_motion;
    	uint32_t last_motion_update;
    	uint8_t new_message;

      uint8_t dist;
      uint8_t last_dist_update;

      Neighbor_t toAggregate;

    } data_t;

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
