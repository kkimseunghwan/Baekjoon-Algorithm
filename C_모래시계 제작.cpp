#include <stdio.h>

int main()
{
	int a,i,k,t;
	
	printf("¼ıÀÚ : ");
	scanf(" %d",&a);
	t=1;
	for(i = 1 ; i <= a-1 ; i++)
	{
		for(k =1 ; k <= i ; k++)
		{
			printf(" ");
		}
		for(k = 1 ; k <= a*2-t ; k++)
		{
			printf("*");
		}		
		t+=2;	
		printf("\n");
	}
	
	for(i = 1 ; i <= a ; i++)
	{
		for(k = 0 ; k <= a-i ; k++)
		{
			printf(" ");
		}		
		for(k = 1 ; k <= i*2-1 ; k++)
		{
			printf("*");
		}
		printf("\n");
	}
	
}


