# /bin/R

library(reticulate)
os <- import("os")
os$chdir("Documents")
os$getcwd()

np <- import("numpy", convert = FALSE)
# do some array manipulations with NumPy
a <- np$array(c(1:4))
sum <- a$cumsum()
print(a)
# convert to R explicitly at the end
py_to_r(sum)