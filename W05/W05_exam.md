# Q3 projection and least squares

### a: relation between linear least squares and projections
00-projection, LLS section
Before, fit line with exact points needed. Perfect fit 
usually more points, best fitting line, some error (draw this)
design matrix not square. minimise sum of squared residuals 
orthogonal projection onto vector
3 points, fit affine line. design matrix, 2 columns. 3d col vectors span subspace 
vector b does not exist in subspace. Orthogonal projection to subspace of design matrix.
Projection is pseudo inverse
pseudo inverse does this projection for us. 

### b: linear least squares for model fitting
00-projection, LLS section
overdetermined system, more points than unknowns
least squares problem -> minimising SSR (draw this) (loss function)
solution -> pseudo inverse of design matrix, projection 
solve for w with pseudo inverse
look at MSE and RMSE for evaluation

### c: learning of affine functions and linear optimization
02-affine...
affine mapping between atrium image and map
multivariate function, design matrix (3 unknowns)
use matrix inverse to solve
optimize model with more training data points and use LLS, minimise loss