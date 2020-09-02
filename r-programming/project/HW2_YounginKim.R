# HW2

library(ggplot2)
library(dplyr)

# set working directory
setwd("C:/Users/uvent/source/repos/hustarAI/r-programming/project")

# HW2-1 

# 1-A
search <- read.csv(file='search.csv')
gender <- read.csv(file='search_gender.csv')
age <- read.csv(file='search_age.csv')
local <- read.csv((file='search_local.csv'))

search$일 <- as.Date(search$일)

head(search)
dim(search)
str(search)
summary(search)

# 1-B
ggplot(search, aes(x=일)) +
  geom_line(aes(y=라면, colour="라면")) +
  geom_line(aes(y=zoom, colour="zoom")) +
  geom_line(aes(y=코로나, colour="코로나")) +
  geom_line(aes(y=BTS, colour="BTS"))

# 1-C
par(mfrow=c(1, 1))
pie(gender$라면, labels = paste(c('여성', '남성'), "\n", gender$라면, "%"), main='라면 검색량', clockwise=TRUE)

ggplot(gender, aes(x=2, y=라면, fill=성별)) +
  geom_bar(stat = "identity", color = "white") +
  geom_text(aes(y = 라면, label = 라면), color = "white")+
  coord_polar(theta = "y", start = 0)+
  theme_void()+
  xlim(0.5, 2.5)

# 1-D
summary(age)
age$연령 <- as.factor(age$연령)

ggplot(data=age, aes(연령))+
  geom_point(aes(y=라면, colour='라면')) +
  geom_point(aes(y=zoom, colour='zoom')) +
  geom_point(aes(y=코로나, colour='코로나')) +
  geom_point(aes(y=BTS, colour='BTS'))

# 1-E
summary(local)
local$지역 <- as.factor(local$지역)  
local$검색어 <- as.factor(local$검색어)

ggplot(data=local, aes(지역)) +
  geom_bar(aes(fill=검색어))

# 1-F

# BTS의 경우, 특정 시점에 검색량이 단발적으로 늘어나는 경향이 있으며, 
# 코로나의 경우 3월 급증했다가 이후 서서히 줄어드는 경향을 보인다.
# 라면과 zoom 검색량의 경우 코로나 검색량 증감에 뒤따라 가는 경향이 있으며,
# 이는 코로나 위기에 따라, 비상식량으로 인식되는 라면과
# 비대면 솔루션인 zoom의 검색량이 함께 움직이는 것이라고 생각된다.

# HW2-2 U.S SAT scores by state for 2010 
sat<-read.csv(file="SAT_2010.csv")

head(sat)
dim(sat)
str(sat)

attach(sat)

# HW2-2-A

par(mfrow=c(1, 2))
boxplot(math, col=c("green"), main='math', ylim=c(450, 620))
boxplot(write, col=c("orange"), main='write', ylim=c(450, 620))
