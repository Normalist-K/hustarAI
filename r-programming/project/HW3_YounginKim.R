# 1. 데이터 다루기

setwd("C:/Users/uvent/source/repos/hustarAI/r-programming/project")

dat1<-read.csv("data1_2019.csv")
dat2<-read.csv("data2_2019.csv")
dat3<-read.csv("data3_2019.csv")

summary(dat1)

# 1-1

whr<-merge(dat1, dat2, by="Country.or.region")
whr<-rbind(whr, dat3)

summary(whr)

# 1-2 
# ① 1.Finland 2.Denmark 3.Norway 4.Iceland 5. Netherlands
whr<-whr[order(whr$Overall.rank),]
head(whr)

# ② 1.Somalia 2.Central African Republic 3.Burundi 4.Liberia 5.Congo(Kinshasa)
head(whr[order(whr$GDP.per.capita, whr$Generosity),])

# 1-3
whr100 <- subset(whr, whr$Overall.rank<=100)

# 1-4 
df_whr <- whr100[1:8]
str(df_whr)

# 2. 데이터의 기술 통계치 요약

attach(df_whr)

# 2-1 mean: 6.07, sd: 0.74, median: 6.02
library(psych)
describe(df_whr[c("Score")])

# 2-2 59개
m_score<-mean(Score)
sd_score<-sd(Score)
df_whr2 <- subset(df_whr, Score >= (m_score - sd_score) & Score <= (m_score + sd_score))
summary(df_whr2)

# 2-3 Finland
max(df_whr[c("Score")])
min(df_whr[c("Score")])
subset(df_whr, Score==7.769)

# 모범답
df_whr[1,which.max(abs(Score - 6.07))]

# 3. 그래프를 이용한 데이터의 탐색

heart <- read.csv("heart.csv")
attach(heart)

summary(heart)

# 3-1 50대
hist(age, breaks = 10, col = 'lightblue')

# 3-2 
boxplot(thalach~target, boxwex=0.5, col=c("lightblue", "coral"))
# 질병이 있는 사람의 최대심박수 평균이 질병이 없는 사람보다 약 20정도 더 높고,
# 질병이 있는 사람의 분포가 평균에 더 모여있다. (분산이 작다)

# 4. t-test
# 4-1
library(ggplot2)
summary(heart)

ggplot(data=heart, aes(factor(sex)))+
  geom_bar(aes(fill=factor(target)))

t.test(target~sex, data=heart)
# p-value < 유의수준 이므로, 성별에 따라 heart disease의 발병 여부에 차이가 있다고 볼 수 있다.
# 또한 막대 그래프를 살펴보면, 남성은 발병 비율이 약 50% 수준인 것에 반해
# 여성의 경우 발병 비율이 현저하게 높은 것을 알 수 있다.