#include <stdio.h>

int main(void)
{
	int cookies = 45;
	int children = 7;
	int cookiesPerChild = 0;
	int cookiesLeftOver = 0;

	cookiesPerChild = cookies / children;
	printf("There are %d cookies per child \n", cookiesPerChild);
	
	cookiesLeftOver = cookies % children;
	printf("There are %d cookies left over \n", cookiesLeftOver);

	return 0;
}
