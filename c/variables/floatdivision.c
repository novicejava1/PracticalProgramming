#include <stdio.h>

int main(void)
{
	float plankLength = 10.0f;
	float pieceCount = 4.0f;
	float pieceLength = 0.0f;

	pieceLength = plankLength / pieceCount;
	printf("A plank %5.3f feet long can be cut into %5.3f pieces %5.3f feet long \n", plankLength, pieceCount, pieceLength);
	return 0;
}
