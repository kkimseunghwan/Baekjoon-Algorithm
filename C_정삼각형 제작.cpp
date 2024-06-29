#include <stdio.h>

int main()
{
	int a,i,k,t,y;
	
	printf("¼ıÀÚ 1 : ");
	scanf(" %d",&a);
	
	
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

