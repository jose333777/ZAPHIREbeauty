#include<iostream>
using namespace std;

int main(){
''09float N1,N2,N3,N4,N5,N6,elect1,elect2,elect3,ETo,Prom;
cout<<"Potencia del primer elctrodomestico";
cin>>N1;
cout<<"Tiempo del primer elctrodomestico";
cin>>N2;
cout<<"Potencia del segundo elctrodomestico";
cin>>N3;
cout<<"Tiempo del segundo elctrodomestico";
cin>>N4;
cout<<"Potencia del tercer elctrodomestico";
cin>>N5;
cout<<"Tiempo del tercer elctrodomestico";
cin>>N6;
elect1= N1+N2;
elect2= N3+N4;
elect3= N5+N6;
cout<<"el consumo total del primero es de: "<< elect1<<"del segundo es de: "<< elect2<<"del tercero es de: "<<elect3;
ETo= elect1+elect2+elect3;
cout<<"el total consumido es de: "<<ETo;
prom= ETo/3;
cout<<"el promedio es: "<<prom;
}