#include <stdio.h>
 

int main(){

int mulheres;
int quantas;
int porcentagem;
int resultado;

printf("Qual a porcentagem do Matheus de ser viado?:\n  ");

printf("Quantas mulheres Matheus teve contato?:\n ");
scanf("%d", &mulheres);

printf("Quantas ele realmente teve relação:\n ");
scanf("%d", &quantas);

porcentagem = mulheres * quantas;

if (porcentagem >= 50){
    printf("mais que baitola maior bicha de todas");
}
else if (porcentagem >= 30 && porcentagem < 50){
    printf("Ta chegando a virar bicha, mas ainda gosta de muie");
}

printf("%d", porcentagem);

return 0;

}
