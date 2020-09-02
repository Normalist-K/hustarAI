setwd("C:/Users/Kim Jong Won/Desktop/1st_year/방학/데이터조교/HuStar혁신아카데미")


#1
help(rnorm)
#a
a = rnorm(10,mean = 10, sd = 10)
b = rnorm(2,mean = 4, sd = 3)
c=c()
for(i in c(1:5)){
  b = rnorm(2,mean = 4, sd = 3)
  c = c(c,b)
}
c
c = rep(b,5)
seq1 = a-c


#2
n = 100
d = c(a,b)
x = c()
for (i in 1:n){
  new_x = c(rep(0,n-i),rep(1,i))
  x = rbind(x,new_x)
}
x2 = c()
for (i in 1:n){
  new_x = c(1:i,rep(0,n-i))
  x2 = rbind(x2,new_x)
}
x3 = matrix(nrow=100,ncol=100)
for(i in 1:n){
  for(j in 1:n){
    x3[i,j] =i%%j+i%/%j
  }
}

x4 = x3%*%solve(t(x3)%*%x3)%*%t(x3)

x4[x4<0.1]=0

#3
hitter = read.csv("Hitters.csv")
write.csv(hitter, "Hitters2.csv")
hitter

#4
head(hitter)


Hits
attach(hitter)

hitter['타율']=hitter$Hits/hitter$AtBat

hitter['출루율']=(hitter$Hits+hitter$Walks)/(hitter$AtBat+hitter$Walks)

summary(hitter)
mean(hitter$타율)
# 출루율  Median :0.3302  Mean   :0.3273 
# 타율 Median :0.2591 Mean   :0.2599 

nrow(subset(hitter,(hitter$타율>0.2599)&(hitter$출루율>0.3273)))

new_hitter = hitter[c('CAtBat', 'CHits', 'CHmRun', 'CRuns', 'CRBI', 'CWalks')]
help(min)
a = function(x){
  return(  max(x)-min(x))
}

table=cbind(lapply(new_hitter,mean),
lapply(new_hitter,min),
lapply(new_hitter,max),
lapply(new_hitter,a))
colnames(table) = c("mean","min","max","max-min")
table

























hitter['타율']=hitter$Hits/hitter$AtBat







head(hitter)

hitter["newVar"] = hitter$NewLeague
hitte



m = array(0, dim=c(5,5))



m



