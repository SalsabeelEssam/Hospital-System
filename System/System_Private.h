#ifndef _SYSTEM_PRIVATE_H_
#define _SYSTEM_PRIVATE_H_
/*******************************Struct***********************************/
	typedef struct patient{
		u8 name[25];
		u32 age;
		u8 gender[10];
		u32 ID;
		struct patient* next;
	}patient;                   	 			  // patient structure stored as linked list

	typedef struct slot{
		u32 ID;    		  		/* some unique numbers */
		u32 slot_status; 		/* reserved 1  // notreserved 0 */
		u32 slot_number;
		s8 date[20];
	}slot;										  // slots structure
	
/*********************************Global Variables*****************************/
 
	patient* head= NULL;        //head pointer
	u16 patient_Number = 0;      //Number of Nodes

/*********************************Global Arrays********************************/
	slot slot_arr[5] = {{0,0,1,"2pm to 2:30pm"},
					   {0,0,2,"2:30pm to 3pm"},
					   {0,0,3,"3pm to 3:30pm"},
					   {0,0,4,"4pm to 4:30pm"},
					   {0,0,5,"4:30pm to 5pm"}};   // times of slots used to print it only
#endif