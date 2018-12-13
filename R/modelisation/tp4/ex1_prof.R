## Ex 1 modifié
## Objectif : Calcul de pi=4\int_0^1\sqrt{1-x^2}dx
## Q1 : \int_0^1\sqrt{1-x^2}dx=E[h(U)]
## avec h(x)=\sqrt{1-x^2}.

## MMC naïve
MMC1<-function(n){
  s=0
  for (i in(1:n)){
    U=runif(1)
    s=s+sqrt(1-U^2); }
  return(s/n)
}
MMC1(1000)

## Tracé de l'évolution 
MMC2<-function(n){
  s=0;S=c()
  for (i in(1:n)){
    U=runif(1)
    s=s+sqrt(1-U^2);S=c(S,s) }
  return(S/1:length(S))
}

evol=MMC2(1000)
plot(1:length(evol),evol,'l',lwd='2')
curve(0*x+pi,lwd='2',col='2',add=TRUE)

### Avec estimation de la variance
MMC3<-function(n){
  s=0;S=c()
  scar=0;
  for (i in(1:n)){
    U=runif(1)
    s=s+sqrt(1-U^2);S=c(S,s);scar=scar+(1-U^2) }
  return(list(evol=S/1:length(S),varempir=scar/n-(s/n)^2))
}
evolvar=MMC3(1000)
evolvar$varempir

rho=0.01
VE=1 ## variance Empirique
s=0
scar=0;
c=(2*qnorm(0.975))^2
rhocar=rho^2
N=1;
while ((N<50)|(VE*c/N>rhocar)){
  U=runif(1)
  s=s+sqrt(1-U^2);scar=scar+1-U^2;
  VE=scar/N-(s/N)^2;N=N+1;
}
approx=s/N
approx
niter=N
niter

# Variable de contrôle

MMCVC<-function(n){
  s=0;sVC=0; S=c();SVC=c();
  scarVC=0;
  for (i in(1:n)){
    U=runif(1)
    s=s+sqrt(1-U^2)
    sVC=sVC+sqrt(1-U^2)-(1-U^2)
    S=c(S,s);
    SVC=c(SVC,sVC)
    scarVC=scarVC+(sqrt(1-U^2)-(1-U^2))^2
  }
  
  return(list(evol=S/1:length(S),
              evolVC=2/3+SVC/1:length(SVC),
              varempirVC=scarVC/n-(s/n)^2))
}


testVC=MMCVC(5000)
evol=testVC$evol
evolVC=testVC$evolVC
plot(1:length(evol),4*evol,'l',lwd='2',ylim=c(3.05,3.25),main="Evolution MMC/pi")
lines(1:length(evolVC),4*evolVC,'l',lwd='2',col='3')
curve(0*x+pi,lwd='2',col='2',add=TRUE)
## On rajoute l'antithétique dans le jeu
MMCanti<-function(n){
  s=0;sVC=0;santi= S=c();SVC=c();
  scarVC=0;
  for (i in(1:n)){
    U=runif(1)
    s=s+sqrt(1-U^2)
    sVC=sVC+sqrt(1-U^2)-(1-U^2)
    S=c(S,s);
    SVC=c(SVC,sVC)
    scarVC=scarVC+(sqrt(1-U^2)-(1-U^2))^2
  }
  
  return(list(evol=S/1:length(S),
              evolVC=2/3+SVC/1:length(SVC),
              varempirVC=scarVC/n-(s/n)^2))
}
testVC=MMCVC(5000)
evol=testVC$evol
evolVC=testVC$evolVC
plot(1:length(evol),4*evol,'l',lwd='2',ylim=c(3.05,3.25),main="Evolution MMC/pi")
lines(1:length(evolVC),4*evolVC,'l',lwd='2',col='3')
curve(0*x+pi,lwd='2',col='2',add=TRUE)

approche<-function(M,R){
  
  N=M*R;
  compt=M;
  U=runif(1)
  #S=U;
  S=0;
  Sbar=rep(1,R);
  Xbar=rep(1,R);
  for (i in 1:N){
    U=runif(1)
    # S=S+exp(U)
    if (i==compt){
      #Xbar[compt/M]=S/i
      #estimateur de la variance
      #construire les Xi
      S=c(S,exp(U))
      var=(sum((S-sum(S)/N))^2)
      Sbar[compt/M]=var/i
      compt=compt+M;
    }
  }
  return(Xbar)
  
}
#tracage de l'approximationcomment tester
#v=approche(100,50)
#length(v)
#plot(100*c(1:50),approche(100,50),"l")
#lines(100*c(1:51),rep(exp(1)-1,51),col="red")


approche1<-function(M,R){
  
  N=M*R;
  compt=M;
  U=runif(1)
  S=exp(U);
  Scar=S^2;
  Sbar=rep(1,R);
  Xbar=rep(1,R);
  for (i in 1:N){
    U=runif(1)
    Scar=Scar+exp(2*U)
    S=S+exp(U)
    if (i==compt){
      Esp=S/i
      Xbar[compt/M]=Esp
      v=Scar/i-Esp^2
      Sbar[compt/M]=V/i
      compt=compt+M;
    }
  }
  return(Sbar)
  
}
#estimation de la variance 
esti<-function(M,R){
  
  N=M*R;
  compt=M;
  U=runif(1)
  S=exp(1+U);
  Scar=S^2;
  Sbar=rep(1,R);
  Xbar=rep(1,R);
  
  for (i in 1:N){
    U=runif(1)
    Scar=Scar+exp(2*U)
    S=S+exp(U)
    if (i==compt){
      Esp=S/i
      Xbar[compt/M]=Esp
      v=Scar/i-Esp^2
      Sbar[compt/M]=V/i
      compt=compt+M;
    }
  }
  return(Sbar)
}
approchecontrole<-function(M,R){
  
  N=M*R;
  compt=M;
  U=runif(1)
  
  S=0;
  S=exp(U);
  Stilde=1+U;
  Xbar=rep(1,R);
  Xbarcontrole=rep(1,R)
  Xbaranti=rep(1,R)
  for (i in 1:N){
    U=runif(1)
    S=S+exp(U)
    Stilde=Stilde+1+U;
    S1=S1+exp(U)+exp(Stilde)
    if (i==compt){
      Xbar[compt/M]=S/i
      Xbarcontrole[compt/M]=(S-Stilde)/i
      Xbaranti[compt/M]=S1/(2*i)
      compt=compt+M;
    }
  }
  return(list(Xbar=Xbar,Xbarcont=Xbarcontrole+3/2))  
}
v=approchecontrole(100,100)
M=100
R=100
plot(M*c(1:R),v$Xbar,type="l")
lines(M*c(1:R),v$Xbarcont,col="red",type="l")
lines(M*c(1:R),(exp(1)-1)*rep(1,R),type="l",col="blue")
lines(M*c(1:R),v$Xbaranti,col="green",type="l")
