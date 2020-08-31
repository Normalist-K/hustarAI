# lec1_4.r : Install package 

# install package 

install.packages("ggplot2")
library(ggplot2)
help(ggplot2)

# install scatterplot3d

install.packages("scatterplot3d")
library(scatterplot3d)
help(scatterplot3d)

# example program using scatterplot3d
z <- seq(-10, 10, 0.01)
x <- cos(z)
y <- sin(z)
scatterplot3d(x, y, z, highlight.3d=TRUE, col.axis="blue",
              col.grid="lightblue", main="scatterplot3d - 1", pch=20)

# to find out the package in google 
# example 1 : support vector machine

# step1 : install package
install.packages('e1071')
library(e1071)

# step2 
help("mean")

help("svm")

# update R verion
# update.packages(checkBuilt=TRUE, ask=FALSE) 
