
// using Brian Kernighan's Algorithm

int countSetBits(int n){

    int counts = 0;

    while(n){
        n = n & (n-1);
        counts ++ ;
    }

    return counts;
}


int hammingWeight(int n) {
    
    int result;
    result = countSetBits(n);

    return result;
}
