#1

#a
a <- rnorm(10, mean = 10, sd = 10)
a

#b
b <- rnorm(2, mean=3, sd=4)
b

#c
c <- rep(b, 5)
c

#d
d <- a-c
d


#2
setwd("C:/Users/uvent/source/repos/r-programming/project")
hitters <- read.csv(file="Hitters.csv")

str(hitters)

attach(hitters)

#a
BatAve <- Hits/AtBat 
hitters["BatAve"] = BatAve

#b
hitters["OnBase"] = (Hits + Walks) / (AtBat + Walks)

#c
summary(hitters)

mean_BatAve = mean(BatAve)
mean_BatAve
class(mean_BatAve)

mean_OnBase = mean(OnBase)
mean_OnBase

#d
higher_c <- length(which(BatAve >= mean_BatAve & OnBase >= mean_OnBase))
higher_c

p <- higher_c / length(BatAve) * 100
p

#e
hitters_sub <- subset(hitters, select=c(CAtBat, CHits, CHmRun, CRuns, CRBI, CWalks))
hitters[c("CAtBat", "CHits", "CHmRun", "CRuns", "CRBI", "CWalks")]

#f
a1 <- lapply(hitters_sub, mean)
class(a1)
a2 <- lapply(hitters_sub, min)
a3 <- lapply(hitters_sub, max)
a4 <- lapply(hitters_sub, function(x){max(x) - min(x)})

table1 <- cbind(a1, a2, a3, a4)
table1
colnames(table1) <- c("mean", "min", "max", "max-min")
table1

#3

#a
ones <- matrix(1, nrow=100, ncol=100)


for (i in 1:100) {
  j <- 100 - i
  if (i == 100) {
    break
  }
  ones[i,][1:j] <- 0
}

ones

#b

zeros <- matrix(0, nrow=100, ncol=100)

for (i in 1:100) {
  for (j in 1:i) {
    zeros[i,j] = j
  }
}

zeros



