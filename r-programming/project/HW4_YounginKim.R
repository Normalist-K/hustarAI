# set working directory
setwd("C:/Users/uvent/source/repos/hustarAI/r-programming/project")

# heart data
heart<-read.csv("heart.csv")
attach(heart)
summary(heart)

# 1-1
val_h<-c("age","trestbps","chol","thalach","oldpeak")
pairs(heart[val_h], main ="heart",cex=1, col=as.factor(target))

# 1-2
cor(heart[val_h])

# 2-1
r1 <- lm(age~thalach, data=heart)

par(mfrow=c(1, 1))
plot(thalach, age, col=as.factor(target), pch=19, main="simple lm")
abline(r1, col="blue", lwd=2, lty=1)

# 2-2
summary(r1)

# 2-4
r2 <- lm(age ~ trestbps+chol+thalach+oldpeak, data=heart)
summary(r2)
r2 <- lm(age ~ trestbps+chol+thalach, data=heart)
summary(r2)

# 3-1
library(class)


library(gmodels)
library(scales)
heart_s <- cbind(as.data.frame(scale(heart[1:13])), heart[14])
summary(heart_s)

set.seed(1000)
N=nrow(heart_s)
tr.idx=sample(1:N, size=N*2/3, replace=FALSE)

heart.train<-heart_s[tr.idx,-14]
heart.test<-heart_s[-tr.idx,-14]
trainLabels<-heart_s[tr.idx,14]
testLabels<-heart_s[-tr.idx,14]

# 3-2
for (k in c(3, 5, 10)) {
  md = knn(train=heart.train, test=heart.test, cl=trainLabels, k=k)
  CrossTable(x=testLabels,y=md, prop.chisq=FALSE)
}

