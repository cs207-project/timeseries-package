/************************************************
* FFT code from the book Numerical Recipes in C *
* Yuhan Tang 
* Havard University
************************************************/

// The following line must be defined before including math.h to correctly define M_PI
#define _USE_MATH_DEFINES
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#define PI	M_PI	/* pi to machine precision, defined in math.h */
#define TWOPI	(2.0*PI)

/*
 FFT/IFFT routine. (see pages 507-508 of Numerical Recipes in C)

 Inputs:
	data[] : array of complex* data points of size 2*NFFT+1.
		data[0] is unused,
		* the n'th complex number x(n), for 0 <= n <= length(x)-1, is stored as:
			data[2*n+1] = real(x(n))
			data[2*n+2] = imag(x(n))
		if length(Nx) < NFFT, the remainder of the array must be padded with zeros

	nn : FFT order NFFT. This MUST be a power of 2 and >= length(x).
	isign:  if set to 1, 
				computes the forward FFT
			if set to -1, 
				computes Inverse FFT - in this case the output values have
				to be manually normalized by multiplying with 1/NFFT.
 Outputs:
	data[] : The FFT or IFFT results are stored in data, overwriting the input.
*/

void four1(double data[], int nn, int isign)
{
    int n, mmax, m, j, istep, i;
    double wtemp, wr, wpr, wpi, wi, theta;
    double tempr, tempi;
    
    n = nn << 1;
    j = 1;
    for (i = 1; i < n; i += 2) {
	if (j > i) {
	    tempr = data[j];     data[j] = data[i];     data[i] = tempr;
	    tempr = data[j+1]; data[j+1] = data[i+1]; data[i+1] = tempr;
	}
	m = n >> 1;
	while (m >= 2 && j > m) {
	    j -= m;
	    m >>= 1;
	}
	j += m;
    }
    mmax = 2;
    while (n > mmax) {
	istep = 2*mmax;
	theta = TWOPI/(isign*mmax);
	wtemp = sin(0.5*theta);
	wpr = -2.0*wtemp*wtemp;
	wpi = sin(theta);
	wr = 1.0;
	wi = 0.0;
	for (m = 1; m < mmax; m += 2) {
	    for (i = m; i <= n; i += istep) {
		j =i + mmax;
		tempr = wr*data[j]   - wi*data[j+1];
		tempi = wr*data[j+1] + wi*data[j];
		data[j]   = data[i]   - tempr;
		data[j+1] = data[i+1] - tempi;
		data[i] += tempr;
		data[i+1] += tempi;
	    }
	    wr = (wtemp = wr)*wpr - wi*wpi + wr;
	    wi = wi*wpr + wtemp*wpi + wi;
	}
	mmax = istep;
    }
}

/********************************************************
* The following is a test routine that generates a ramp *
* with 10 elements, finds their FFT, and then finds the *
* original sequence using inverse FFT                   *
********************************************************/



/*

Nx = 10
NFFT = 16

Input complex sequence (padded to next highest power of 2):
x[0] = (0.00 + j 0.00)
x[1] = (1.00 + j 0.00)
x[2] = (2.00 + j 0.00)
x[3] = (3.00 + j 0.00)
x[4] = (4.00 + j 0.00)
x[5] = (5.00 + j 0.00)
x[6] = (6.00 + j 0.00)
x[7] = (7.00 + j 0.00)
x[8] = (8.00 + j 0.00)
x[9] = (9.00 + j 0.00)
x[10] = (0.00 + j 0.00)
x[11] = (0.00 + j 0.00)
x[12] = (0.00 + j 0.00)
x[13] = (0.00 + j 0.00)
x[14] = (0.00 + j 0.00)
x[15] = (0.00 + j 0.00)

FFT:
X[0] = (45.00 + j 0.00)
X[1] = (-25.45 + j 16.67)
X[2] = (10.36 + j -3.29)
X[3] = (-9.06 + j -2.33)
X[4] = (4.00 + j 5.00)
X[5] = (-1.28 + j -5.64)
X[6] = (-2.36 + j 4.71)
X[7] = (3.80 + j -2.65)
X[8] = (-5.00 + j 0.00)
X[9] = (3.80 + j 2.65)
X[10] = (-2.36 + j -4.71)
X[11] = (-1.28 + j 5.64)
X[12] = (4.00 + j -5.00)
X[13] = (-9.06 + j 2.33)
X[14] = (10.36 + j 3.29)
X[15] = (-25.45 + j -16.67)

Complex sequence reconstructed by IFFT:
x[0] = (0.00 + j -0.00)
x[1] = (1.00 + j -0.00)
x[2] = (2.00 + j 0.00)
x[3] = (3.00 + j -0.00)
x[4] = (4.00 + j -0.00)
x[5] = (5.00 + j 0.00)
x[6] = (6.00 + j -0.00)
x[7] = (7.00 + j -0.00)
x[8] = (8.00 + j 0.00)
x[9] = (9.00 + j 0.00)
x[10] = (0.00 + j -0.00)
x[11] = (0.00 + j -0.00)
x[12] = (0.00 + j 0.00)
x[13] = (-0.00 + j -0.00)
x[14] = (0.00 + j 0.00)
x[15] = (0.00 + j 0.00)

*/