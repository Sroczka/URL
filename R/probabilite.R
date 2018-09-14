#######PROBABILITE#############
curve(dnorm(x,mean=2, sd=2), type ='l',xlim = c(-2,6))

######

a <- rnorm(50, mean = 2, sd = 2) 
hist(a, col = 'lightblue', freq=F, ylim = c(0,0.4),
     main = "Histogram rozkładu N(2,2)",prob= T)
curve(dnorm(x,mean = 2,sd = 2),col="red", add=T)

########

pexp(5, rate = 1, lower.tail = T)

####

X <- rbinom(1:20, prob = 0.2, size = 20)
barpl(table(X))

barplot(dbinom(1:20, prob = 0.2, size = 20))

#####

qnorm(mean = 0, sd = 1 ,p = 0.975)

qnorm(mean = 0, sd = 1 ,p = 0.95)


################################################################
#ex.2

sim_binom = function(N,n,p){
  X <- rbinom(N, size = n, prob = p)
  table <- prop.table(table(X))
  plot(0:20+0.1, dbinom(0:n,size = n, prob = p),
       xlim = c(0,20.5),type = 'h', xlab = 'x', ylab = 'probabilite')
  lines(as.integer(row.names(table)),table,type = 'h',col='red')
  title('Simulation')
}

############################################################
#ex.3

curve(dnorm(x,mean = 2, sd = 2), col = 'red', xlim = c(-2,6))

#F_d = function(N,t){
#  X <- rnorm(N, mean = 0, sd = 1)
#  a<-0
#  for (i in 1:N){
#    if(X[i]<=t) a = a+1
#  }
#  (a/N)
#}

N = 50
X <- rnorm(N, mean = 0, sd = 1)
X <- sort(X)
x=(1:N)/N
plot(X,x,type='s')
curve(pnorm(x),col='red',add=T)

plot(ecdf(X))


##################################################


