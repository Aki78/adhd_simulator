#include <stdio.h>

float *compute_mean(float* A, float* B, float* C, int n)
{
	int i;
	float sum = 0.0f;
	for(i=0; i<n; ++i)
  {
		C[i] = A[i] + B[i];
    printf("%f\n", C[i]);
  }
}
