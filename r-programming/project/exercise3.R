# set working directory
setwd("C:/Users/uvent/source/repos/hustarAI/r-programming/exercise")

### student math grade data ####
stud<-read.csv("stud_math.csv")
summary(stud)

# 1.아버지의 직업(Fjob)이 G1에 끼치는 영향이 있는가? 
# 영향이 있다면 어떤 아버지의 직업을 가진 G1간 차이를 만드는지 확인해라.

table(stud$Fjob)
stud$Fjob <- as.factor(stud$Fjob)

attach(stud)
par(mfrow=c(1,1))
boxplot(G1~Fjob, boxwex=0.5, col=c(6, 2, 3, 4, 5))
a1 <- aov(G1~Fjob)
summary(a1)

# p-value = 0.00578로 0.05보다 작으므로, 유의미한 차이가 있다고 볼 수 있다.

TukeyHSD(a1, "Fjob")
plot(TukeyHSD(a1, "Fjob"))

# teacher-other, teacher-services 간의 차이가 영향이 크다.


# 2.G1과 G2는 같다고 할 수 있는가? 
# 이 경우 t-test paried를 사용할 수 있는가? 아니면 없는가?

library(ggplot2)
ggplot(stud, aes(x=G1, y=G2))+
  geom_point(size=2)

t.test(G1, G2, mu=0, paired=T)
t.test(G1, G2, mu=0)

# 둘 다 유의수준보다 p-value가 크므로, G1과 G2는 같다고 볼 수 있다.
# 또한 G1과 G2은 서로 짝지어져 있으므로, paired t-test를 사용해도 된다.

library(dplyr)
stud_0 <- stud %>%
  filter(G2!=0)

t.test(stud_0$G1, stud_0$G2, mu=0, paried=T)

# G2에는 중도에 학업을 포기한 학생들이 포함되어 있어, 
# stud 데이터가 학업중인 학생들의 모집단을 대표한다고 보기 힘들다.
# 그래서 G2 점수가 0점인 학생은 제외하고, 
# 다시 t-test한 결과 더 유의한 수준으로 두 성적 데이터가 같다고 볼 수 있다.