runifdisque <- function(N){

  theta <- runif(N)*2*pi
  R <- sqrt(runif(N))
  return(cbind(R*cos(theta), r*sin(theta)))
}
