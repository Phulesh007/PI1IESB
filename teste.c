#include <stdlib.h>
#include <stdio.h>

int main() {
    
    int result=0;
    int i,j;
    char vet[200];
    char vet2[200];
    char vet3[100];
    int cont=0,aux=0;
    FILE* arq;
    
    arq = fopen("casos_full2.txt", "r");



    if(arq==NULL){
        printf("Problemas na CRIACAO do arquivo\n");
        return 0;
    }
    
    /*for(i=0;i != EOF ;i++){
        vet[i] = getc(arq);

            printf("%c",vet[i]);

                  
    }*/
    
    while(fgets(vet,sizeof(vet),arq) != NULL){
        for(i=0;i != EOF ;i++){
            vet2[i] = vet[i];
            if(vet2[i] == ';'){
                cont++;
                if(cont >= 8){
                        for(j=i;j != ';';j++){
                            printf("%d",i);
                            printf("%d",j);
                            printf("%c",vet[j]);

                            printf("oi");                    
                            vet3[aux] = vet2[i];
                            aux++;
                            if(vet2[i] == ';'){
                                break;

                            }
                            //printf("%c",vet3[aux-1]);
                        }
                    
                }
                
            }

        }
            result++;
            //printf("\n");
        if(result == 10){
            break;

        }
    }

    fclose(arq);
    
    return 0;
}