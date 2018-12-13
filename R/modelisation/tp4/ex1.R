MMC1 <- function(n){
  s <- 0
  for(i in range(1:n)){
    U <- runif(1)
    #s = s + exp(U)
    s = s+ sqrt(1-U^2)
  }
  return(s/n)
}

###################################

MMC2 <- function(n){
  s <- 0;S = c()
  for(i in(1:n)){
    U <- runif(1)
    #s = s + exp(U)
    s = s+ sqrt(1-U^2);S = c(S,s)
  }
  return(S/1:length(S))
}

eval <- MMC2(1000)
plot(1:length(eval),eval, 'l')

#############

MMC_var <- function(n){
  srednia=0
  S=c()
  moment2=0
  for(i in (1:n)){
    U = runif(1)
    srednia = srednia + sqrt(1-U^2)
    S=c(S,srednia)
    moment2=moment2+(1-U^2)
  }
  return(list(evol=S/1:length(S),varempir= moment2/n-(srednia/n)^2))
}

evolVar = MMC_var(1000)

evolVar$varempir

##################

#4
rho = 0.05
VE = 1
s = 0
scar = 0
c = (2*qnorm(0.975))^2
rhocar = rho^2

##########
MCVC <- function(n){
  s = 0;VC = 0; S = c(); SCV = c()
  scarVC = 0
  for(i in 1:n){
    U = runif(1)
    s = s+sqrt(1-U^2) 
  }
}