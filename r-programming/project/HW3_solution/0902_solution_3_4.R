# 9/2 assignment - 3,4
# Graphical analysis 

# set working directory
setwd("C:/Users/user/Desktop/ASSIGNMENT/rcode_200902")

heart<-read.csv("heart.csv",fileEncoding="UTF-8-BOM")
dim(heart)
head(heart)
attach(heart)

sum(is.na(heart))

# 1. histogram with color and title, legend
hist(age, breaks = 10, col = "lightblue", main="Histogram of age" )
#hist(chol, breaks = 10, col = "green", main="Histogram of Grade trestbps" )
#heart_post<-subset(heart,heart$chol<500)
#head(heart_post)

hist(heart_post$chol, breaks = 10, col = "green", main="Histogram of Grade trestbps" )


# 2. boxplot
par(mfrow=c(1,2))
boxplot(age~target, boxwex = 0.5, col = c("yellow", "coral"), main="thalach by (no heart disease, heart disease)")
boxplot(chol~target, boxwex = 0.5, col = c("red","orange"), main="age by (no heart disease, heart disease)")


# 2. two sample t-test
## example 1 
# to test whether or not mean of G3 is same between Urban and Rural 
t.test(target~sex, data=heart)


library(ggplot2)
ggplot(data=heart, aes(factor(sex)))+geom_bar(aes(fill=factor(target)), width=.4, colour="black")+ ggtitle("Romantic by sex")
