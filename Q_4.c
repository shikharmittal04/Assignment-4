//Question 4: Transformation method
#include <stdio.h>    
#include <stdlib.h>
#include <math.h>
int main() //Main function.
{
	int N=10000;
	double x[N];
	double y[N];
	for(int i=0;i<N;i++)
	{
		x[i]=rand()/(double)RAND_MAX;
		y[i]=-0.5*log(1-x[i]);
	}
	
	FILE *data;
	data = fopen("Q_4.txt","w");
	for(int j=0;j<N;j++)
	{
		fprintf(data,"%lf\t%lf\n",x[j],y[j]); /*Send data to a file to be
		used later in python code.*/
	}
	fclose(data);	
}
//To compile: gcc -Wall Q_4.c -lm -lgsl -lgslcblas -o Q_4
//To run	: ./Q_4
