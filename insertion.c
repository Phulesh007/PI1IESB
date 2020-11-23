#include <stdio.h>
#include <stdlib.h>

int main(){
    long int aux, i,j,qtd,k;
    long int *vetor;
    printf("digite a quantidade:");
    scanf("%ld",&qtd);

    vetor = (long int*)malloc(sizeof(long int) * qtd);

    srand(time(NULL));
    for(i=0;i<qtd;i++){
        do{
            vetor[i] = rand() % qtd;
            aux = 1;
            for(j=0;j<i;j++){
                if(vetor[j] == vetor[i]){
                    vetor[i] = rand()%qtd;
                    aux = 0;
                }
            }
        }while(aux!= 1);
        
        //printf("vetor na posicao %d: %d\n",i,vetA[i]);
    }
    for(i=0;i<qtd;i++){
        printf("%ld\t",vetor[i]);
    }
    for(i=1;i<=qtd-1;i++){
        aux = vetor[i];
        j=i-1;
        while(j>=0 && aux < vetor[j]){
            vetor[j+1] = vetor[j];
            j--;
        }
        vetor[j+1] = aux;
        
    }
    printf("\n **** \n");
   for(i=0;i<qtd;i++){
       printf("%ld \t",vetor[i]);
   }


    return 0;
}