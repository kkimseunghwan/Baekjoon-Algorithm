#include <stdio.h>

int main()
{
	int a,i,k,t;
	
	printf("¼ıÀÚ 1 : ");
	scanf(" %d",&a);
	
	for(i = 1 ; i <= a ; i++)
	{
		for(k = i ; k <= a ; k++)
		{
			printf(" ");
		}
		for(k = 1 ; k <= i ; k++)
		{
			printf("*");
		}
		printf("\n");		
	}
	
}
