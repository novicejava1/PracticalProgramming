#include <stdio.h>

#define LOWER 0
#define UPPER 300
#define STEP 20

main()
{
	int fahr;
	int celsius;
	for (fahr = LOWER; fahr <= UPPER; fahr = fahr + STEP)
	{
		celsius = 5 * (fahr - 32) / 9;
		printf("%3d\t%6d\n", fahr, celsius);
	}

}
