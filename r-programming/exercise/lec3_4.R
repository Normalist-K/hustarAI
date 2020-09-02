# lec3_4.r
# Data handling
# Data analysis with autompg.csv

# data manipulation package
# select, filter, group by, summarise in dplyr package 
# install.packages("dplyr")
library(dplyr)

# set working directory
# change working directory 
setwd("C:/Users/uvent/source/repos/hustarAI/r-programming/exercise")

# Read txt file with variable name
# http://archive.ics.uci.edu/ml/datasets/Auto+MPG

# Data reading in R
car<-read.csv(file="autompg.csv")
attach(car)

# data checking
str(car)


# Data handling using "dplyr"

# 1 subset data : selecting a few variables
set1<-select(car, mpg, hp)

head(set1)

# 2 subset data : Drop variables with -
set2<-select(car, -starts_with("mpg"))
head(set2)

# 3. subset data : filter mpg>50
set3<-filter(car, mpg>30) 
head(set3)

# 4. create a derived variable w/ pipe operator(%>%)
set4<-car %>%
  filter(!is.na(mpg)) %>%
  mutate(mpg_km = mpg*1.609)

head(set4)

# mean and standard deviation
car %>%
  summarize(mean(mpg),mean(hp),mean(wt))

# mean of some variables
select(car, 1:6) %>%
  colMeans()

# table with descriptive statistics
a1 <- select(car, 1:6) %>% summarize_all(mean)
a2 <- select(car, 1:6) %>% summarize_all(sd)
a3 <- select(car, 1:6) %>% summarize_all(min)
a4 <- select(car, 1:6) %>% summarize_all(max)
table1 <- data.frame(rbind(a1,a2,a3,a4))
rownames(table1) <- c("mean","sd","min","max")
table1

# summary statistics by group variable
car %>%
  group_by(cyl) %>%
  summarize(mean_mpg = mean(mpg, na.rm = TRUE))


# -----------------------------------------

# 1. mpg, wt, accler 변수만 원래 table에서 추출하라. 그 뒤 기술통계치를 str, summary를 통해 관찰하라

table2 <- select(car, mpg, wt, accler)
str(table2)
summary(table2)

# 2. year가 72년도 이상인 변수들에 대해 cyl값 별로 disp, hp의 평균을 계산하라

set5 <- car %>%
  filter(year >= 72) %>%
  group_by(cyl) %>%
  select(disp, hp) %>%
  summarize_all(mean)

set5

# 3. Carname이 f 로 시작하고 mpg가 중앙값보다 높은 변수를 추출하라.

set6 <- car %>%
  filter(substr(carname, 1, 1) == 'f') %>%
  filter(mpg > median(mpg))


