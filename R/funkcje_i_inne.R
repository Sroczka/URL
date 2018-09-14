A = data.frame(X=c(2,2,3),Y=c(1,2,3),F=c('a','b','c'))
save(A,file = "fichier.txt")

#####################################################
#ex.8
u <- c(1:5)
v <- c(rep(1:2, each =2),3)

u+v
u^2
sin(u)

cumsum(u)

##################################################
#ex.9

x<-c(1:6)

A<-matrix(x,ncol=2,byrow=T)
B<-matrix(x,ncol=3,byrow=T)
C<- rbind(c(1:4),c(1,3,2,4),c(rep(4,4)),c(1,2,2,1))
C<-as.matrix(C)

A%*%B #mnozenie macierzy

solve(C)
solve(C)%*%C # sprawdzenie macierzy odwrotnej

D<-C[-3,-4]
D2 <-C[c(1,2,4),1:3] # D2 == D

C
G<-cbind(C,C[,2])
H<-C[C[,1]==1]
as.matrix(H)

##############################################
#ex.10

A <- paste('A',1:4,sep='')
A
A2 <- factor(sample(A,1000,p=c(0.2,0.3,0.4,0.1),replace = T))
A2
table(A2)

B=paste('B',1:20,sep='')
B2 <- sample(B,1000,replace = T)
table(B2)/1000
table(A2,B2)

##########################################
###########GRAPHIQUES#####################

#ex.11

data(trees)
attach(trees)
#View(trees)
plot(Height,Girth,col="purple", main = "wykresik")

rug(Height,side=2)
rug(Girth)

abline(lm(Height~Girth))

#ex. 12

X=rnorm(500)
hist(X)
hist(X,breaks=50,xlim = c(-5,5))
hist(X,freq=FALSE,col="lightblue")
curve(dnorm(x),add=T,col="red")

hist(X,breaks=c(-5,-2,0,3,4)) #podzial jak chce

#ex.13

fac=sample(LETTERS[1:3],100,replace = T, p=c(0.2,0.3,0.5))
pie(table(fac))
barplot(table(fac))

#ex.14

data(iris)
attach(iris)
boxplot(Sepal.Length~Species)
stripchart(Sepal.Length~Species)

par(mfrow=c(3,1))


############################
#ex.19

funkcja1 = function(x){
  (x=x^5+log(x)+1)
}

funkcja2 = function(X){
  sd(X)/mean(X)
}

funkcja3 = function(n){
  a=1
  for (i in 1:n) a=a*i
  a
}

silnia = function(n){
  if (n==1 |n==0) n
    else silnia(n-1)*n
}


funkcja4 = function(x){
  if (x %% 2 == 0) (TRUE) else (FALSE)
} 

funkcja5 = function(n){
  A<-matrix(rep(0,n^2),nrow=n)
  for (i in 1:n) A[i,i]=1
  #diag(1,n) - macierz diagonalna
  A 
}

funkcja6 = function(n,lambda){
  y <- rpois(n,lambda)
  hist(y,freq=F)
  curve(dnorm(x, mean(y), sd(y)),add=T)
}