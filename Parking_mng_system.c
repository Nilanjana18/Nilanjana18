//Simple parking management system in c


#include<stdio.h>
#include<conio.h>

int Menu();
void Car();
void Bus();
void MotorCycle();
void Bicycle();
void DeleteData();
void Show_Details();

int no_of_Buses=0,no_of_Cars=0,no_of_MotorCycles=0,no_of_BiCycles=0,count=0,amount=0;

int main()
{
    while(1){
    switch(Menu())
    {
        case 1:
        Car();
            break;
        case 2:
            Bus();
            break;
        case 3:
            MotorCycle();
            break;
        case 4:
            Bicycle();
            break;
        case 5:
            Show_Details();
        case 6:
            DeleteData();
            break;
		case 7:
			exit(0);
        default:
            printf("Invalid Choice please enter a valid choice and try again\n");
    }
    getch();
    }
}

int Menu()
{
    int ch;
    printf("\n---------Welcome to the Parking Management System---------\n");
    printf("1.Enter Cars:\n");
    printf("2.Enter Buses:\n");
    printf("3.Enter MotorCycles:\n");
    printf("4.Enter BiCycles:\n");
    printf("5.Show Details of the parking system:\n");
    printf("6.Delete Data of the day:\n");
	printf("7.Exit the system:\n");
    printf("Enter your Choice from 1 to 7:\n");
    scanf("%d",&ch);
	return(ch);
}

void DeleteData()
{
    no_of_Buses=0;
    no_of_Cars=0;
    no_of_MotorCycles=0;
    no_of_BiCycles=0;
    amount=0;
    count=0;
}
void Show_Details()
{
    printf("No of cars in the parking lot:%d\n",no_of_Cars);
    printf("No of buses in the parking lot:%d\n",no_of_Buses);
    printf("No of Bicycles in the parking lot:%d\n",no_of_BiCycles);
    printf("No of MotorCycles in the parking lot:%d\n",no_of_MotorCycles);
    printf("Total no of vehicles parked:%d\n",count);
    printf("Total Amount gained:%d\n",amount);
}
void Car()
{
    no_of_Cars++;
    amount=amount+100;
    count++;
}
void Bus()
{
    no_of_Buses++;
    amount=amount+70;
    count++;
}
void MotorCycle()
{
    no_of_MotorCycles++;
    amount=amount+50;
    count++;
}
void Bicycle()
{
    no_of_BiCycles++;
    amount=amount+40;
    count++;
}
