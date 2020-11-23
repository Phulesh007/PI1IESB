#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void mergesort(long int vet[],long int inicio,long int fim);
void ordena(long int vet[],long int inicio,long int meio, long int fim);
long int * aloca_vetor_randomico(long int qtd);

int main(){
    long int * vet;
    long int tam;
    clock_t t1,t2;
    printf("\n Digite o tamanho do vetor: ");
    scanf("%ld",&tam);

    t1 = clock();
    vet = aloca_vetor_randomico(tam);
    t1 = clock()-t1;

    printf("\n Tempo para criar vetor: %0.2lf ms",((double)t1)/((CLOCKS_PER_SEC/1000)));
    
    t2 = clock();
    mergesort(vet,0,tam-1);
    t2 = clock()-t2;
    
    printf("\n Tempo para ordenar o vetor: %0.2lf ms",((double)t2)/((CLOCKS_PER_SEC/1000)));
    return 0;
}


void mergesort(long int vet[],long int inicio,long int fim){
    long int meio;
    

    if(inicio<fim){
        meio = (inicio + fim) /2;
        mergesort(vet,inicio,meio);
        mergesort(vet,meio+1,fim);
        ordena(vet,inicio,meio,fim);
    }
    
    return ;
}

void ordena(long int vet[],long int inicio,long int meio, long int fim){
    long int i,j,k,*aux;

    aux=(long int*)calloc(sizeof(long int), fim - inicio + 1);
    i=inicio;
    j=meio+1;
    k=0;

    
    while(i <= meio && j <= fim){
        if(vet[i]<vet[j]){
            aux[k] = vet[i];
            i++;
        }else
        {
            aux[k] = vet[j];
            j++;
        }
        k++;
    }
    
    while(i<=meio){
        aux[k] = vet[i];
        i++;
        k++;
    }
    while(j<=meio){
        aux[k] = vet[j];
        j++;
        k++;
    }

    for(i=0;i<(fim-inicio)+1;i++){
        vet[inicio+1] = aux[i];
    }
    
    free(aux);
    return;
}
long int * aloca_vetor_randomico(long int qtd)
{
    long int * vetor;
    long int i;
    long int i_aux, aux;
    vetor = (long int*)malloc(sizeof(long int)*qtd);

    for(i=0;i<qtd;i++)
    {
        vetor[i] = i+1;
    }
    srand(time(NULL));

    for(i=0;i<qtd;i++)
    {
        i_aux = rand() % qtd;
        aux = vetor[i];
        vetor[i] = vetor[i_aux];
        vetor[i_aux] = aux;

    }

    return vetor;
}