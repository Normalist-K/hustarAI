library(class)
library(gmodels)
library(scales)

# set working directory
setwd("C:/Users/uvent/source/repos/hustarAI/r-programming/exercise")

# read csv file
iris<-read.csv("iris.csv")
# head(iris)
# str(iris)
attach(iris)

# training/ test data : n=150
set.seed(123)
N=nrow(iris)
tr.idx=sample(1:N, size=N*4/5, replace=FALSE)

# attributes in training and test
iris.train<-iris[tr.idx,-5]
iris.test<-iris[-tr.idx,-5]
# target value in training and test
trainLabels<-iris[tr.idx,5]
testLabels<-iris[-tr.idx,5]

train<-iris[tr.idx,]
test<-iris[-tr.idx,]

# knn (3-nearest neighbor)
md1<-knn(train=iris.train,test=iris.test,cl=trainLabels,k=3)
md1

# accuracy of 5-nearest neighbor classification
CrossTable(x=testLabels,y=md1, prop.chisq=FALSE)

# knn (5-nearest neighbor)
md2<-knn(train=iris.train,test=iris.test,cl=trainLabels,k=5)
md2

# accuracy of 5-nearest neighbor classification
CrossTable(x=testLabels,y=md2, prop.chisq=FALSE)

# knn (10-nearest neighbor)
md3<-knn(train=iris.train,test=iris.test,cl=trainLabels,k=10)
md3

# accuracy of 5-nearest neighbor classification
CrossTable(x=testLabels,y=md3, prop.chisq=FALSE)
