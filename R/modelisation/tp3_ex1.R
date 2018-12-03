runifdisque <- function(N){

  theta <- runif(N)*2*pi
  R <- sqrt(runif(N))
  return(cbind(R*cos(theta), R*sin(theta)))
}

###
x = seq(-1,1,0.001)
plot(runifdisque(1000))
lines(x,sqrt(1-x^2), type = 'l', col='red')
lines(x,-sqrt(1-x^2), type = 'l', col='red')

#lub
w = seq(0,2*pi,0.01)
v = runifdisque(100)
plot(v[,1],v[,2],'p')
lines(cos(w),sin(w), col = "red")
###

simuelipse <- function(N){
  x1 = rep(0,N)
  x2 = rep(0,N)
  v = rep(0,N)
  compt = 1
  for(i in 1:N){
    y=runifdisque(1)
    u=runif(1)
    y1=y[1]
    y2=y[2]
    test = (y1^2+2*y2^2>1)*(2*y1^2+y2^2>1)
    while(test == 1){
      y=runifdisque(1)
      u=runif(1)
      y1=y[1]
      y2=y[2]
      test = (y1^2+2*y2^2-1)*(2*y1^2+y2^2-1)
      compt = compt+1
    }
    x1[i] = y1
    x2[i] = y2
    v = cbind(x1,x2)
  }
  return(list(v=v,compt=compt))
}

N = 1000

z=simuelipse(N)
lines(z$v[,1], z$v[,2],'p', col='3')
dim(v)

#Approximation aire Union-elipses podpunkt 2

aproxaire = pi/z$compt*N