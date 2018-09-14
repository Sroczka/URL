(x<- c(0.27, 1.2, 3))
(y<-c(1:6))
z<-cumsum(y)
a<-seq(10,18,2)

u<-runif(5)
(sum(u))
(sort(u))
(cumsum(u))
(sin(u))

v<-1:2
rep(1:2,3)
c(rep(1,3),rep(2,3))

a<-c(1:4)
A<-matrix(c(5,2,a), ncol=2,byrow=T)
b<-c(5,1:3,2,4)
B<- matrix(b, nrow = 1)
C<- matrix(b,ncol=3,byrow = T)
C

rownames(A)<-c("jeden","dwa","trzy")
colnames(A) <- c("kolumna1","i druga")

d<-c(letters[1:6])
D<-matrix(d,byrow=T,ncol=2)
D