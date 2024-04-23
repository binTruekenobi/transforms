# transforms
bunch of transforms

convolutions is the convolution of two functions

fourier_transform has a few different fourier transforms, currently only of 1d functions and images, the optimised fourier transform file just caches f(x) values so that on each integration, instead of re-calculating values it just does an array lookup - speeding things up a lot, but there's some fencepost errors on iterations that'll never get fixed so the values will be a tiny bit off

taylor_series finds the taylor series of a function and represents it using the polynomial_tools module, really bad as it uses a differencing method of differentiation so it can only be used to about 5 or 6 terms, but it's formatted so it can be copy pasted into geogebra or the likes without any issue.

laplace_transform does not find the laplace transform of a function directly, and instead it just finds a taylor series approximation and finds a transform of that instead as L(t^n) = n!/(s^(n-1)), a lot easier than a complex analytical integral (i don't know residue theorem)
