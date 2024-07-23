#include<stdio.h>
int main(){
    int num1, num2, product;

    printf("Enter the two numbers \n");
    scanf("%d ,  %d " ,&num1, &num2 );

    product = num1*num2;
    printf("PRoduct of %d and %d is %d " , num1, num2, product);
}