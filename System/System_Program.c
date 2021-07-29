#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "../lib/STD_TYPES.h"

#include "System_Interface.h"
#include "System_Private.h"


void Add_patient(void)
{
	patient *current = NULL;
	u8 name[25];
	u32 age;
	u8 gender[10];
   // Allocate memory for new patient
    patient *link = (struct patient*) malloc(sizeof(struct patient));

	printf("enter the name: ");
	scanf("%s",name);
	printf("enter the age : ");
	scanf("%d",&age);
	printf("enter the gender : ");
	scanf("%s",gender);
   // insert the data to the new patient and make the next point to null
   link->ID =patient_Number+1;
   patient_Number++;
   strcpy(link->name,name);
   link->age = age;
   strcpy(link->gender,gender);
   link->next = NULL;

   // If head is empty, create new list
   if(head==NULL)
   {
      head = link;
      return;
   }

   current = head;

   // loop until reach the last patient in the old list
   while(current->next != NULL)
   {
	   current = current->next;
   }

   // Make the last patient in the old list point to new patient
   current->next = link;
}

void Edit_patient(void)
{
	patient* temp= head;        //pointer
	u32 Edit_ID;
	u32 InputUser;
	patient PatientInformation;
	patient* IdCheck= head;
	printf("\n***********************************\n*\n");
	printf("* please enter your ID : ");
	scanf("%d",&Edit_ID);
	printf("*\n***********************************\n\n");
	
	if(temp==NULL){ // empty
		printf("The list is Empty");
		return ;
	}
	
	while(temp!=NULL)
	{
		if(Edit_ID==temp->ID){
		  printf("\n	** Welcome %s \n",temp->name);
		  printf("	** Your Age is : %d \n	** Your Gender is : %s \n",temp -> age ,temp -> gender);
		  printf("\n***********************************\n*\n");
		  printf("*  To Edit Your name Press      1\n"
				 "*  To Edit Your Age  Press      2\n"
				 "*  To Edit Your Gender  Press   3\n"
				 "*  To Edit All Data Press       4\n");
		  printf("*\n***********************************\n\n");
		 scanf("%d",&InputUser);
			
	     switch(InputUser){
				case 1:
					printf("Enter Your New Name \n");
					scanf("%s",PatientInformation.name);
					strcpy(temp-> name, PatientInformation.name);
				    break;
				case 2:
					printf("Enter Your New Age \n");
					scanf("%d",&PatientInformation.age);
					(temp-> age) = (PatientInformation.age);
				    break;
				case 3:
					printf("Gender \n");
					scanf("%s",PatientInformation.gender);
					strcpy(temp-> gender,PatientInformation.gender);	
				   break;	
				case 4:
					printf("Enter Your New Name \n");
					scanf("%s",PatientInformation.name);
					strcpy(temp-> name, PatientInformation.name);
					
					printf("Enter Your New Age \n");
					scanf("%d",&PatientInformation.age);
					temp-> age = PatientInformation.age;
					
					printf("Gender \n");
					scanf("%s",PatientInformation.gender);
					strcpy(temp-> gender,PatientInformation.gender);
					
					break;
			}
		  
		  return;
		}
		else{
			temp=temp->next;
		}
	}
	printf("ID doesn't exist...\n");
}

void Patient_record(void)
{
	u32 ID=0;
	printf("enter the ID : ");
	scanf("%d",&ID);
   	struct patient *current = NULL;
   	u32 pos = 0;

   	if(head==NULL)
   	{
      	printf("does not exist in the System\n");
     	 return;
  	 }

   	// start checking from the first patient
   	current = head;
   	while(current != NULL)
   	{
      if(current->ID == ID)
      {
		printf("ID : %d\n",current->ID);
		printf("name : %s\n",current->name);
		printf("age : %d\n",current->age);
		printf("gender : %s\n",current->gender);
         return;
      }
      current = current->next;
      pos++;
   }
   // Patient's ID not found in the list
	printf("%d does not exist in the System\n", ID);
}

void Cancel_resrve(void)
{  
    u8 i=0;
    u32 reserved_user_ID=0; /* variable to store input id from user */
	patient* temp= head; /* pointer to struct ( initiate to point to head) */
	
	printf("please enter your ID :");
	scanf("%d",&reserved_user_ID);
	
	 /*looping on data base (list)  */
	while(temp!=NULL)
	{
		if( reserved_user_ID == temp->ID ){
			 for(i=0;i<5;i++){ /* looping on reserved... id*/
				 if(slot_arr[i].ID==reserved_user_ID){ 
					slot_arr[i].slot_status=0;/* statue 0 means not reserved */
					slot_arr[i].ID=0;
					printf("\n your slot at  %s was canceled \n",slot_arr[i].date);
					return;
				 }
				 
			 } 
			printf("you didn't reverse any slot...");/* if ID exist in Data Base but not reseve any slot */
			return;
		}
		else{
			temp=temp->next;
		}
		
	}
	printf("\n ID doesn't exist........\n"); /* if ID doesn't exist in Data Base */
}

void Print_patient_list(void)
{
	patient* node = head;
	
	if(NULL == node)
	{
		printf("*********************\n*                   *\n");
		printf("*   List is Empty   *\n*                   *\n");
		printf("*********************\n");
	}
	
	else
	{
		printf("****************************\n*\n");
		while(NULL != node)
		{
			printf("* Patient Name : %s\n",node->name);
			printf("* Age : %u\n",node->age);
			printf("* Gender : %s\n",node->gender);
			printf("* ID : %u\n*\n",node->ID);
			node = node->next;
		}
		printf("****************************\n");
	}
}

void Reserve_slot(void)
{
	u32 i=0 ,ID=0,avialable_slots=0, n=0;
	patient* temp = head;
	
	printf("\n\n----------------------------------------------------------------------");
	for(i=0 ; i<5 ; i++)
	{
		if (slot_arr[i].slot_status == 0)
	    {
			avialable_slots++;
			printf("\n%d - slot number %d from %s is avialabe press %d to reserve it \n  ",
					avialable_slots, avialable_slots, slot_arr[i].date, avialable_slots);
		    slot_arr[i].slot_number = avialable_slots;
	    }
    }
	if (avialable_slots == 0)
	{
		printf("\n\nAll Slots are reserved");
	}
	else
	{
		printf("\n\nPlease enter the patient ID : ");
		scanf("%d",&ID);
		while( (temp != NULL)&&(temp->ID != ID)  )
		{
			temp = temp->next;
		}
		if ((temp != NULL)&&(temp->ID == ID) )
		{
			printf("\nEnter Reserve slot number : ");
			scanf("%d", &n);
			if  ((n>0) && (n<=avialable_slots) )
			{	
				for(i=0 ; i<5 ; i++)
				{
					if ( (slot_arr[i].slot_status == 0) && (slot_arr[i].slot_number == n) )
					{
						slot_arr[i].slot_status = 1;
						slot_arr[i].ID = ID;
						printf("\n\nSlot is reserved successfully thank you");
						break;
					}
				}
			}
			else 
			{
				printf("\nInvalid Slot number");
			}	
		}
		else if (temp == NULL)
		{
			printf("\nIncorrect ID");
		}				
	}
	printf("\n----------------------------------------------------------------------");
}

void View_reserve(void)
{
	u32 i=0;
	for(i=0 ; i<5 ; i++)
    {
	    if ((slot_arr[i].slot_status == 1) && (slot_arr[i].ID != 0))
        {
	   	    printf("\n%d - Slot from %s is reserved by Patient whose ID is : %d\n  ",i,slot_arr[i].date,slot_arr[i].ID);
   	    }
		else if (slot_arr[i].slot_status == 1){
			printf("\n%d - Slot from %s is Avialable\n  ",i,slot_arr[i].date);
		}
    }
}
