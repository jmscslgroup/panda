#ifdef USE_FORD_CAN_ID
#ifndef FORD_CAN_ID
#define FORD_CAN_ID

//125kbs?

#define	POWER_MODE_ID 0x3A0L
#define	VSS_ID 0x423L
#define	DIMMER_ID 0x3ABL
#define	DIMMER2_ID 0x10BL // 2005 Mustang
#define DIMMER4_ID 0x3B3L
#define PARKING_LIGHT_ID 0x3B8 // 2005 Mustang
#define GEAR_INFORMATION_ID 0x3B0L // 2005 Mustang
#define DOOR_STATUS_ID 0x3B1L
#define DOOR_STATUS2_ID 0x3C4L
#define	PARKING_BRAKE_ID 0x3C3L
#define	PARKING_BRAKE1_ID 0x3C2L
#define	PARKING_BRAKE2_ID 0x3C1L // 2005 Mustang
#define RAP_ID 0x3B6 // 2005 Mustang
#define RAP_ID 0x3C6 // 2010 Mustang
#define AUDIO_MASTER_REMOTE_RECEIVER_COMMAND_ID 0x2DB // 2005 Mustang
#define VIN_ID 0x22F
#define SATELLITE_RADIO_ID 0x3EA // 2005 Mustang
#define SATELLITE_RADIO2_ID 0x335 // 2005 Mustang

#define RSE_BUTTON_ID 0x2DEL
#define RSC_BUTTON_ID 0x2DFL
#define SYNC_PRESENT_ID 0x541L
#define SYNC_STATUS_ID 0x3EBL
#define SYNC_TEXT_ID 0x333L
#define SYNC_SEND_MODE_SWITCH_340_ID 0x340L
#define SYNC_SEND_CONF_MODE_SWITCH_350_ID 0x350L
#define SYNC_TEXT_MODE_ID 0x332L
#define SYNC_50B_STATUS_ID 0x50BL
#define SYNC_511_STATUS_ID 0x511L
#define SYNC_503_STATUS_ID 0x503L
#define OE_LCD_500_ID 0x55CL
#define OE_LCD_RESP_ID 0x324L
#define SAT_500_ID 0x542L
#define SAT_TEXT_ID 0x335L
#define SAT_TEXT_MODE_ID 0x334L
#define LCD_BUTTON_PRESS_ID 0x2E1L
#define DIGITAL_AMP_500_ID 0x546L
#define RSE_500_ID 0x512L
#define DIGITAL_AMP_SETTINGDS_ID 0x3EDL


#endif // FORD_CAN_ID
#endif // USE_FORD_CAN_ID
