//gcc main.c ../System/System_Program.c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "../lib/STD_TYPES.h"

#include "../System/System_Interface.h"


int main(void)
{
	s16 choice = 0;
	system("cls");

	while(8 != choice)
	{
		printf(" ,__________Welcome__________,\n");
		printf(" |_LIST______________________|\n");
		printf(" |  1)Add Patient            |\n");
		printf(" |  2)Edit Patient           |\n");
		printf(" |  3)Print Patient List     |\n");
		printf(" |  4)Print Patient By ID    |\n");
		printf(" |  5)Show Reservation       |\n");
		printf(" |  6)Reserve                |\n");
		printf(" |  7)Cancel Reserve         |\n");
		printf(" |  8)Exit                   |\n");
		printf(" '~~~~~~~~~~~~~~~~~~~~~~~~~~~'\n\n\n\n");
		printf(" Want to do ");
		
		scanf("%d",&choice);
		
		switch(choice)
		{
			case 1:
				system("cls");
				Add_patient();
				system("cls");
				printf("\t    ,^^^^^,\n");
				printf("\t    |Added|\n");
				printf("\t    '~~~~~'\n");
				break;
			case 2:
				system("cls");
				Edit_patient();
				system("cls");
				printf(" \t,^^^^^^^^^^^,\n");
				printf(" \t|Modify Done|\n");
				printf(" \t'~~~~~~~~~~~'\n");
				break;
			case 3:
				system("cls");
				Print_patient_list();
				printf("\n <- Enter 1 to back ");
				while(1 != choice)
				{
					scanf("%d",&choice);
				}
				system("cls");
				break;
			case 4:
				system("cls");
				Patient_record();
				printf("\n <- Enter 1 to back ");
				while(1 != choice)
				{
					scanf("%d",&choice);
				}
				system("cls");
				break;
			case 5:
				system("cls");
				View_reserve();
				printf("\n <- Enter 1 to back ");
				while(1 != choice)
				{
					scanf("%d",&choice);
				}
				system("cls");
				break;
			case 6:
				system("cls");
				Reserve_slot();
				printf("\n <- Enter 1 to back ");
				while(1 != choice)
				{
					scanf("%d",&choice);
				}
				system("cls");
				printf(" \t,^^^^^^^^^^^^^^^^,\n");
				printf(" \t|Reservation Done|\n");
				printf(" \t'~~~~~~~~~~~~~~~~'\n");
				
				break;
			case 7:
				system("cls");
				Cancel_resrve();
				printf("\n <- Enter 1 to back ");
				while(1 != choice)
				{
					scanf("%d",&choice);
				}
				system("cls");
				printf(" \t,^^^^^^^^^^^^^^^^,\n");
				printf(" \t|Cancelation Done|\n");
				printf(" \t'~~~~~~~~~~~~~~~~'\n");
				break;
			case 8:
				system("cls");
				break;
			default:
				system("cls");
				printf("Invalid Number You can choose from 1 to 8 only\n");
		}
	}
	return 0;
}