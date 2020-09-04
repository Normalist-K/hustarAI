library(e1071)
library(caret)
library(tree)


setwd("C:/Users/uvent/source/repos/hustarAI/r-programming/project")

heart <- read.csv("heart.csv")

heart$target <- as.factor(heart$target)
attach(heart)

# 1.1
set.seed(1000)
N<-nrow(heart)
tr.idx<-sample(1:N, size=N*2/3, replace=FALSE)
train<-heart[tr.idx,]
test<-heart[-tr.idx,]

# 1.2
m1<-svm(target~., data=train, kernel='radial')
m2<-svm(target~., data=train, kernel='polynomial')
m3<-svm(target~., data=train, kernel='sigmoid')
m4<-svm(target~., data=train, kernel='linear')
summary(m1)
summary(m2)
summary(m3)
summary(m4)

pred1<-predict(m1, test)
pred2<-predict(m2, test)
pred3<-predict(m3, test)
pred4<-predict(m4, test)
confusionMatrix(pred1, test$target)
confusionMatrix(pred2, test$target)
confusionMatrix(pred3, test$target)
confusionMatrix(pred4, test$target)

# 1.3

model1<-tree(target~., data=train)
summary(model1)
model1
plot(model1)
text(model1, cex=0.5)

treepred1<-predict(model1, test, type='class')
confusionMatrix(treepred1,test$target)

# 1.4
cv.tr<-cv.tree(model1, FUN=prune.misclass)
cv.tr
plot(cv.tr)

model2<-prune.misclass(model1, best=6)
plot(model2)
text(model2)

treepred2<-predict(model2, test, type='class')
confusionMatrix(treepred2,test$target)

