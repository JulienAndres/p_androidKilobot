#ifndef MAIN__H
    #define MAIN__H


    void setup(void);
    void loop(void);

    typedef struct
    {
    	uint8_t curr_motion;
    	uint32_t last_motion_update;
    	uint8_t new_message;
      int distance_message;

    } data_t;

    enum motion {
      STOP,                /*!< The robot is stopped*/
      LEFT,                 /*!< The robot is moving to the left */
      RIGHT,               /*!< The robot is moving to the right */
      STRAIGHT         /*!< The robot is moving straight */
    };
#endif
