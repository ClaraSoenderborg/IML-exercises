# Q2 - linear transformations

### focus a: linear transformations in 2d and 3d space
04-transformations
transform data with linear transformations
changing space that data exists in
transformation matrix T, multiplied with data, linear combination 
scaling, shearing, rotation
linear = origin stays. Translation shifts (affine)
use homogeneous coordinates to add bias

### b: learning model parameters
01-linear-algebra, task 5
system of linear equations, set up as inner products Ax = b.
isolate unknowns with matrix inverse (square, det != 0)
learn model parameters with data points 

01-polynomials
similar, linearity in weights, write as inner product 
write 2nd degree polynomial 
design matrix, 2 weights and a bias 
solve with inverse 

as many points as unknowns (degree + 1)

### c: affine transformation
04-transformations, bottom
affine transformation = linear + translation
Tx + b 
homogeneous coordinates, add 1 as extra dimension
add column to T, with bias terms for input as homogeneous coord
design matrix for affine model, affine transformation matrix

