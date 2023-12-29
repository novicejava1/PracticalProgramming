#include <stdio.h>

int main(void)
{
	int cookies = 5;
	int cookie_calories = 125;
	int totalEaten = 0;

	int eaten = 2;
	cookies = cookies - eaten;
	totalEaten = totalEaten + eaten;
	printf("\n I have eaten %d cookies. There are %d cookies left \n", eaten, cookies);

	eaten = 3;
	cookies = cookies - eaten;
	totalEaten = totalEaten + eaten;
	printf("\n I have eaten %d more cookies. There are %d cookies left \n", eaten, cookies);
	printf("\n Total energy consumed is %d calories \n", totalEaten * cookie_calories);
	return 0;

}
