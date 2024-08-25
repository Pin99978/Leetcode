#include <stdio.h>

void swapNumber(int *a , int *b){
    *a = *a ^ *b; 
    *b = *a ^ *b;  
    *a = *a ^ *b;
}



int main(){
    int x, y ;
    printf("Enter two numbers: ");
    scanf("%d %d", &x, &y);
    printf("Before swapping: x = %d, y = %d\n", x, y);
    swapNumber(&x, &y);
    printf("\n");
    printf("After swapping:  x = %d, y = %d\n", x, y);

    return 0;
}
