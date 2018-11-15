# ex3

###############################
#1

simulation = function(x,p,N){
  traj = x
  while(x * (N-x) != 0){
    x = x+2*(runif(1)<p) - 1
    traj = c(traj,x)
    return(traj)
  }
}

traje <- simulation(10,1/4,5)

##############################
#3

M = 1000
x0 = 5
N = 10
p = 1/2

stock = 0
for (i in (1:M)){
  x = x0
  while(x * (N-x) != 0){
    x = x+2*(runif(1)<p) - 1
  }
  stock = stock+(x == N)
}

approcher = stock/M

######################
#4

stock = 0
for (i in (1:M)){
  x = x0
  compt = 0
  while(x * (N-x) != 0){
    x = x+2*(runif(1)<p) - 1
    compt = compt + 1
  }
  stock = stock+compt
}

appro_temps = stock/M