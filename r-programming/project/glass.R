library(class)
library(gmodels)
library(scales)
# set working directory
setwd("C:/Users/uvent/source/repos/hustarAI/r-programming/project")

glass <- read.csv("glass.csv")

summary(glass)

glass$Type <- as.factor(glass$Type)
summary(glass)
table(glass_n$Type)

normalize <- function(x) {
  return ((x - min(x)) / (max(x) - min(x)))
}
glass_n <- as.data.frame(lapply(glass[1:9], normalize))
glass_n['Type'] = glass[10]
summary(glass_n)
table(glass_n$Type)

set.seed(123)
N=nrow(glass)
tr.idx=sample(1:N, size=N*4/5, replace=FALSE)

glass.train <- glass_n[tr.idx, -10]
glass.test <- glass_n[-tr.idx, -10]
trainLabels <- glass_n[tr.idx, 10]
testLabels <- glass_n[-tr.idx, 10]

table(trainLabels)
table(testLabels)

knn_glass <- knn(train = glass.train, test = glass.test, cl=trainLabels, k=5)
knn_glass
CrossTable(x=testLabels,y=knn_glass, prop.chisq=FALSE)
