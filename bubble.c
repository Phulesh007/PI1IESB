#include <stdio.h>
#include <stdlib.h>

int main(){
    long int aux,pass,i,qtd,j;
    int flag = 1;
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
    
    for(pass = 0;pass <qtd-1 && flag == 1;pass++){
        flag = 0;
        for(i=0;i<qtd-1-pass;i++){  
            if(vetor[i] > vetor[i+1]){
                aux =  vetor[i+1];
                vetor[i+1] = vetor[i];
                vetor[i] = aux;
                flag = 1;
            }
        }
    }
    printf("\n **** \n");
    for(i=0;i<qtd;i++){
        printf("%ld\t",vetor[i]);
    }
    


    return 0;
}