#include <stdio.h>
void compute_kernel(double* kernel, int * inputImage, int* outputImage, int x, int y, int radius, int kernelW, int w, int h)
{
   double redValue = 0.0;
   double greenValue = 0.0;
   double blueValue = 0.0;
  
  for (int kernelX = -radius; kernelX < radius; kernelX++){
       for (int kernelY = -radius; kernelY < radius; kernelY++)
       {
            /*kernelValue = kernel[kernelX + radius,kernelY + radius]*/
            double kernelValue = kernel[kernelW*(kernelX + radius) + kernelY + radius];
            /*printf("%d %d \n", kernelX, kernelY);*/

            /*redValue += inputImage[x - kernelX, y - kernelY, 0] * kernelValue*/
            /*greenValue += inputImage[x - kernelX, y - kernelY, 1] * kernelValue*/
            /*blueValue += inputImage[x - kernelX, y - kernelY, 2] * kernelValue*/
            /*printf("RED %d\n",inputImage[3*w*(x - kernelX)   +   3*(y - kernelY) + 0] );*/
            redValue += (double) inputImage[6*h*(x - kernelX)   +   6*(y - kernelY) + 0] * kernelValue;
            greenValue += (double) inputImage[6*h*(x - kernelX) + 6*(y - kernelY) + 2] * kernelValue;
            blueValue += (double) inputImage[6*h*(x - kernelX) + 6*(y - kernelY) + 4] * kernelValue;
       }
  }

            /*printf("%d %d %f\n", x, y,  redValue);*/
    outputImage[6*h*x+6*y+0] = (int) redValue;
    outputImage[6*h*x+6*y+2] = (int) greenValue;
    outputImage[6*h*x+6*y+4] = (int) blueValue;
}
