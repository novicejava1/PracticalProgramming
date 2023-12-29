#include <stdio.h>

main()
{
	int fahr;
	int celsius;

	for (fahr = 0; fahr <= 300; fahr = fahr + 20) 
	{
		celsius = 5 * (fahr - 32) / 9;
		printf("%3d\t%6d\n", fahr, celsius);
	}
}
