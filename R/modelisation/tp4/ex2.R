r = 0.05;
t = 1
S0 = 100;
K = 95

sigma = 0.1

beta = (r-sigma^2 /2)*t
gama = sigma*sqrt(t)

N= 1000

Z <- rnorm(N)
(approx_naive = exp(-r*t)*mean(pmax(S0*exp(beta+gama*Z)-K,rep(0,N))))

#antithestique
V1 = exp(-r*t)*mean(pmax(S0*exp(beta+gama*Z)-K,rep(0,N)))
V2 = exp(-r*t)*mean(pmax(S0*exp(beta+gama*Z)-K,rep(0,N)))

(approxanti=(V1+V2)/2)

## Combinaison convexe


###########
MC_euro <- function(sigma,K,N){
  s = 0
  for(i in 1:N){
    Z <- rnorm(N)
    S=S0*exp(beta+gama*Z)
    s = s + max(S0*exp(beta+gama*Z)-K,0)
  }
  c_eur = exp(-r*t)*s/N
  return(c_eur)
}






