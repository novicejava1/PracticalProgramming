#include <stdio.h>

int main(void)
{
	const double unit_price = 3.50;
	int quantity = 0;
	printf("Enter the quantity to buy : ");
	scanf("%d", &quantity);

	double total = 0.0;
	if (quantity > 10)
		total = quantity*unit_price*.95;
	else
		total = quantity*unit_price;

	printf("The price for %d is %.2f \n", quantity, total);

	return 0;
}
