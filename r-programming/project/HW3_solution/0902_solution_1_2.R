# 9/2 assignment - 1,2
## Data management : merge, sorting, subset 

# set working directory
setwd("C:/Users/user/Desktop/ASSIGNMENT/HW3_solution/HW3_solution")

# 1.1 solution

dat1<-read.csv(file="data1_2019.csv")
head(dat1)
dat2<-read.csv(file="data2_2019.csv")
head(dat2)

# data merging
dat12<-merge(dat1, dat2, by="Country.or.region")
head(dat12)

# add more data (combine in a row)
dat3<-read.csv(file="data3_2019.csv")
dat123<-rbind(dat12, dat3)
head(dat123)

dim(dat123)

#1.2 solution

# data sorting
#method 1
dats<-dat123[order(dat123$Overall.rank), ]

#method 2
dats<-dat123[order(dat123$Score, decreasing=T), ]
head(dats)

dats<-dat123[order(dat123$GDP.per.capita, dat123$Generosity), ]
head(dats)

#1.3 solution
newdat<-subset(dat123, dat123$Overall.rank<=100)
head(newdat)
dim(newdat)


# 1.4 solution (excluding variables)
df_whr<-newdat[!names(dat123) %in% c("Overall.rank")]
df_whr


##Numerical analysis

head(df_whr)
dim(df_whr)
str(df_whr)

attach(df_whr)

# 2.1 solution

#method 1
summary(df_whr)
mean(Score)
var(Score)
median(Score)

#method 2(creating interested variable list)
vars<-c("Score","Generosity")
head(df_whr[vars])
summary(df_whr[vars])
# sapply function
sapply(df_whr[vars], mean)
sapply(df_whr[vars], var)
sapply(df_whr[vars], median)


#method 3(descriptive statistics using "psych" package)
install.packages("psych")
library(psych)
# require "psych" for "describe" function
describe(df_whr[vars])

#2.2 solution
newdat<-subset(df_whr, df_whr$Score>=(6.07-0.74) & df_whr$Score<= (6.07+0.74))
dim(newdat)

newdat<-subset(df_whr, df_whr$Score>=(mean(Score)-sd(Score)) & df_whr$Score<= (mean(Score)+sd(Score)))
dim(newdat)

#2.3 solution
which.max(abs(Score - 6.07) )
df_whr[18,]

