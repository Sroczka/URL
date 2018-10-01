x = 1
stock = x
while (x != 3){
  if(x == 1){
    x = sample(c(1,2,3),1)
  } else {x = sample(c(2,3),1)
  }
  stock = c(stock,x)
}
plot(1:length(stock), stock, 's')