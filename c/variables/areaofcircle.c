#include <stdio.h>
#define PI 3.1459265f


int main(void)
{
	float radius = 0.0f;
	float diameter = 0.0f;
	float circumference = 0.0f;
	float area = 0.0f;
	//float PI = 3.1459265f;

	printf("Input the diameter of the table : ");
	scanf("%f", &diameter);

	radius = diameter / 2.0f;
	circumference = 2.0f * PI * radius;
	area = PI * radius * radius;

	printf("Circumference of the circle is : %f \n", circumference);
	printf("Area of the circle is : %f \n", area);

	return 0;

}
