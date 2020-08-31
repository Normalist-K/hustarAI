# lec8_3_reg.r : Linear model 
# Regression

library(dplyr)

# set working directory
setwd("D:/tempstore/moocr/wk8")

# autompg data
car<-read.csv("autompg.csv")
  head(car)
  str(car)

# subset with cyl=4,6,8
# car1<-subset(car, cyl==4 | cyl==6 | cyl==8)
car1<-filter(car, cyl==4 | cyl==6 | cyl==8 )
  attach(car1)
  table(cyl)

# 1. simple Regression(independent variable : wt)
r1<-lm(mpg~wt, data=car1)
  summary(r1)
  anova(r1)

# (lec4_3.R) scatterplot with best fit lines
par(mfrow=c(1,1))
plot(car1$wt, car1$mpg, col=as.factor(car1$cyl), pch=19)
# best fit linear line
abline(lm(mpg~wt), col="red", lwd=2, lty=1)

# 2. simple Regression(independent variable : disp)
r2<-lm(mpg~disp, data=car1)
summary(r2)
anova(r2)

# pariwise plot
pairs(car1[,1:6], main ="Autompg",cex=1, col=as.integer(car1$cyl),pch =substring((car1$cyl),1,1))

# 3. multiple Regression
r3<-lm(mpg~wt+accler, data=car1)
summary(r3)
anova(r3)

# SSE Calculation
#sse = sum((mpg-fitted(r3))^2)
#sse

# filtered data
car2<-filter(car, cyl==4 | cyl==6 )
car3<-filter(car, cyl==8)

# car cyl =4,6  vs cyl=8
par(mfrow=c(1,2))
plot(car2$wt, car2$mpg, col=as.integer(car2$cyl), pch=19, xlim=c(1500,5000),ylim=c(5,50), main="cyl=4 or 6")
abline(lm(car2$mpg~car2$wt), col="red", lwd=2, lty=1)
plot(car3$wt, car3$mpg, col="green", pch=19, xlim=c(1500,5000),ylim=c(5,50), main="cyl=8")
abline(lm(car1$mpg~car1$wt), col="red", lwd=2, lty=1)

m2<-lm(mpg~wt, data=car2)
summary(m2)

m3<-lm(mpg~wt, data=car3)
summary(m3)

# SSE depending on cyl
#car4 <- cbind(car3,fitted(r3))
#names(car4)[5] <-"fitted_value"
#head(car4)
#cyl_sse<-car4 %>% 
#  group_by(cyl)%>%
#  summarise(sse =sum((fitted_value - mpg)^2))
#cyl_sse
#sse-sum(cyl_sse$sse)

# par(mar=c(4,4,4,4))
# par(mfrow=c(1,1))
# plot(disp, mpg,  col=as.integer(car1$cyl), pch=19)
# best fit linear line
# abline(lm(mpg~disp), col="red", lwd=2, lty=1)






