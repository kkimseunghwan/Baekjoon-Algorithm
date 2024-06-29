#include <stdio.h>

int main()
{
	int a,b,i,k;
	
	printf("숫자 1 : ");
	scanf(" %d",&a);
	printf("숫자 2 : ");
	scanf(" %d",&b);
		
	for(i = 1 ; i <= a ; i++)
	{
		for(k = 1 ; k <= b ; k++)
		{
			printf("* ");
		}
		printf("\n");		
	}
	
	
	
	
	
}
