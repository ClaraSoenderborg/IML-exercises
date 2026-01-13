# Q4 - Manadatory 1

### a: preprocessing and feature extraction 
01-data
affine model, gaze estimation 
raw data as images, need pupil coordinates 
pupil detection, threshold and bounding box
some loss of data, noise in raw data (light, movement)
find mean pupil coordinate, map to screen coordinate
pitfalls -> data collection, feature extraction, bad training data

### b: model predictions and learning
02-gaze
data is preprocessed, extracted mean pupil coordinates 
multivariate affine model. 3 unknowns for each model x/y, 6 unknowns. 
build design matrices 
use LLS for learning model parameters. Minimise SSR
prediction = inner product of pupil coordinate and weights

### c: model evaluation
02-gaze, evaluating on own dataset
model is 2 multivariate affine models, for x and y. 
train/test split motivation
train on different patterns, test on last
evaluate errors 

### d: vector space, basis, independence
vector space = vectors from linear combination of basis vectors.
standard basis
linear independence, span a space 

question 2, solve with inverse, can only inverse for linearly independent columns

question 3, linearly independent vectors span a space. if vectors are dependent, exist in the same span

this theory is relevant for least squares and the projection. Also change of basis, making new basis vectors. 