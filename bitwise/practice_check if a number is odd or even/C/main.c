#include <stdio.h>

int main(){

    int number;
    printf("Enter a number to check if it is even or odd: ");
    scanf("%d", &number);

    // Check if the number is even or odd
    // 1 -> 0001 2 -> 0010 

    // so if number & 1 is even number & 1 will retrun true
    // for example 2 & 1 = 0010 & 0001 = 0000 -> false
    // for example 3 & 1 = 0011 & 0001 = 0001 -> true

    if(number & 1){
        printf("%d is an odd number\n", number);
            
    }else{
        printf("%d is an even number\n", number);
    }

    return 0;
}
