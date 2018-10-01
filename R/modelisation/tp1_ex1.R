#ex 1.1
#jedna symulacja

x = 1
stock = x
while (x != 3){
  if(x == 1){
    x = sample(c(1,2,3),1)
  } else {x = sample(c(2,3),1)
  }
  stock = c(stock,x)
}
plot(1:length(stock), stock, 's', col = 'blue')

#ex 1.2
# N - symulacji + czas, srednia

N = 100
stock2 = rep(0,N)
for (i in 1:N){
  x = 2
  t = 0
  while (x != 3){
    t = t+1
    if(x == 1){
      x = sample(c(1,2,3),1)
    } else {x = sample(c(2,3),1)
    }
  }
  stock2[i] = t
}
tmoyen2 = sum(stock2)/N

#ex 1.3

stock1 = rep(0,N)
for (i in 1:N){
  x = 1
  t = 0
  while (x != 3){
    t = t+1
    if(x == 1){
      x = sample(c(1,2,3),1)
    } else {x = sample(c(2,3),1)
    }
  }
  stock1[i] = t
}
tmoyen1 = sum(stock1)/N

##############################################################
#ex.2.1

marche <- function(x,n,p){
  direc = sample(c(-1,1), n, prob = c(p,1-p))
  pos = cumsum(direc)
  pos = c(x,x+pos)
  return(pos)
}

#ex 2.2
a = c(0:n)
plot(a,pos)