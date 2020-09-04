
# set working directory
setwd("C:/Users/uvent/source/repos/hustarAI/r-programming/project")

wine = read.csv("winequality-red.csv")
head(wine)
str(wine)
summary(wine)
attach(wine)

pairs(wine, main ="Wine",cex=1)

mlr<-lm(quality ~ ., data=wine)
summary(mlr)

mlr2<-lm(quality ~ volatile.acidity+chlorides+total.sulfur.dioxide+sulphates+alcohol, data=wine)
summary(mlr2)

val_wine=c("volatile.acidity", "chlorides","total.sulfur.dioxide","sulphates","alcohol", "quality")

pairs(wine[val_wine], main = "Wine", cex=1)
