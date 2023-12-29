#include <stdio.h>

int main(void)
{
	int totalPets;
	int cats;
	int dogs;
	int ponies;
	int others;

	cats = 2;
	dogs = 1;
	ponies = 1;
	others = 6;

	totalPets = cats + dogs + ponies + others;
	printf("We have %d pets in total \n", totalPets);
	return 0;
}
