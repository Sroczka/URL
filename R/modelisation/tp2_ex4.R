#########CZESC 1##########
   ##################

simug <- function (alpha, t0, N){
  y = (runif(N))^(1/(alpha+1))*t0
  return(y)
}

#
alpha = 2
t0 = 1
N = 100
#

u <- simug(alpha,t0,N)
v <- sort(u)
w <- seq(1/N,1,by = 1/N)
plot(v,w, col = 'red', main = "porownanie proby i empirycznej")
curve((x/t0)^(alpha+1),add=T)
#####

hist(v,freq=F, col = 'lightblue',main = "porownanie gestosci generowanej i empirycznej")
lines(density(v), col = 'red',cex = 2)
curve((a+1)/t0^(a+1)*x^a,xlim = c(-1,1), cex = 2,add=T)



##############CZESC 2###################
         ##################

simuf <- function(alpha,N){
  v= rep(0,N)
  t0 = pi/2
  compt = 1
  for (i in 1:N){
    y <- simug(alpha, t0,1)
    u <- runif(1)
    while (u>cos(y)){
      y <- simug(alpha, t0,1)
      u <- runif(1)
      compt = compt+1
    }
    v[i] = y
  }
  return(list(v=v,compt=compt))
}

z = simuf(alpha,N)
hist(z$v, freq = F, col = "lightblue")
curve(x^alpha*cos(x)/(pi^2/4-2), col='red', cex = 2, add=T)
#dzielenie przez pi itd zeby znormalizowac! bo gestosc na calej prostej == 1