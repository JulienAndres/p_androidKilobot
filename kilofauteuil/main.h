#ifndef MAIN__H
    #define MAIN__H


    void setup(void);
    void loop(void);

    typedef struct
    {
    	uint8_t curr_motion;
    	uint32_t last_motion_update;
    	uint8_t new_message;

    } data_t;
#endif
