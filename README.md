## 1. Give a point (𝑥,𝑦), let 𝑧=𝑥+𝑖𝑦

and create a function that computes

𝑓1(𝑧)=𝑧2+𝑐

for some 𝑐=𝑐1+𝑖𝑐2
.

## 2. Given a starting point (𝑥,𝑦), create a function escape_time that recursivly computes

z_i = f(f(f(...f(z)...)

stopping when |𝑧𝑖|>2
. The function should return the number 𝑖 of times the function has to be applied before |𝑧𝑖|>2

.

## 3. Compute escape_time for every number on a grid for x in [-2,2] and y in [-2,2] with a step of .01. Construct an array with the results, and plot the array using plt.imshow. Run this for

𝑐=1

𝑐=1+𝑖
𝑐=.7885

Extra

## 1. Instead of 𝑓2(𝑧)=𝑧2+𝑐, use a different function line 𝑥3+𝑐. What do you get?

## 2. Rewrite escape_time so that it switches between 𝑓1 and 𝑓2 randomly at each step.
