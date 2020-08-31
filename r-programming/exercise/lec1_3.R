# lec1_3.r 
# description

  x1<-c(1,3,5,7,9)

  # x is numeric or character?
  class(x1)
  is.numeric(x1)
  
  # integer is numeric 
  is.integer(x1)
  # need to define as.integer as.numeric as.character
  x2<-as.integer(x1)

  
  # length of x
  length(x1)
  
  # x is a vector?
  is.vector(x1)
  
  # class - character
  "I like apple"
  class("I like apple")

  ## lec1_3 ####
  
  # Basic operations
  
  x2<-c(1,4,9)
  sqrt(x2)
  min(x2)
  max(x2)
  mean(x2)
  
  y2=2+x2
  
  plot(x2, y2)
  
  # functions
  
  log10(10)
  log(10)
  exp(10)
  
  sin(pi/2)
  
  # list 
  ls()
  
  # remove object
  rm(x1)
  
  # change to lower or upper case for variable (name)
  
  c1 <- "MiXeD cAsE 123"
  tolower(c1)
  toupper(c1)
  
  # generating data from distributions
  # 100 values from normal distribution with mean=0, sd=1
  x3<-rnorm(100)
  # head(x3)
  mean(x3)
  sd(x3)
  min(x3)
  max(x3)
  
  hist(x3)
  
  # 10000 values from normal distribution with mean=0, sd=1
  x4<-rnorm(10000)
  mean(x4)
  sd(x4)
  
  hist(x4)
  


  