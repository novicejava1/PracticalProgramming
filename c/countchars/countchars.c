#include <stdio.h>

int main(void)
{
	long nc;
	nc = 0;

	while (getchar() != EOF)
		++nc;
	printf("%1d\n", nc);
}