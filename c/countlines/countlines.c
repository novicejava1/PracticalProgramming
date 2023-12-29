#include <stdio.h>

main()
{
	int c, line;
	line = 0;

	while ((c = getchar()) != EOF)
	{
		if (c == '\n')
			line = line + 1;
	}
	printf("The number of lines : %d", line);
}
