#include <stdio.h>

int main()
{
	int a,i,k;
	
	printf("¼ıÀÚ 1 : ");
	scanf(" %d",&a);
	
	for(i = 1 ; i <= a ; i++)
	{
		for(k = 1 ; k <= i ; k++)
		{
			printf("* ");
		}
		printf("\n");		
	}
	
	
	
	
	
}
