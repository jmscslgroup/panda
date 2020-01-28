#ifdef USE_TOYOTA_CAN_ID
#ifndef TOYOTA_CAN_ID
#define TOYOTA_CAN_ID


// 2018 Tacoma?
// 500kbs
#define TURN_SIGNALS_ID 0x614
#define LIGHTING_STATUS_ID 0x63F
#define PARKING_BRAKE_DOOR_ID 0x620
#define FOOT_BRAKE_ID 0x226
#define GEAR_INFORMATION_ID 0x3BC


#endif//TOYOTA_CAN_ID
#endif // USE_TOYOTA_CAN_ID


#ifndef TOYOTAVELLFIRE_COMMON_H
#define TOYOTAVELLFIRE_COMMON_H

namespace TOYOTA_VELLFIRE {
	//static const uint32_t TURN_INDICATOR_MSG_ID_TOYOTA_VELLFIRE = 0;
	static const uint32_t STEERING_WHEER_ANGLE_MSG_ID_TOYOTA_VELLFIRE = 0x025;
	static const uint32_t SHIFT_POS_MSG_ID_TOYOTA_VELLFIRE = 0x2d0;

	static const int32_t MAX_ABS_STEER_ANGLE		= 320;			// 转角绝对值最大值
	static const int32_t MAX_ABS_CAN_STEER_ANGLE	= 0x160;		// CAN帧中转角信息的最大绝对值
	static const int32_t CAN_STEER_LEFT_BEGIN_VAL	= 0x0000;		// 方向盘往左打时CAN帧中转角信息的起始值
	static const int32_t CAN_STEER_RIGHT_BEGIN_VAL	= 0x0fff;		// 方向盘往右打时CAN帧中转角信息的起始值

}

#endif
