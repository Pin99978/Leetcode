int maxProfit(int* prices, int pricesSize) {
    
    int min  = prices[0 ];
    int diff = 0 ;

    for (int i = 0 ; i < pricesSize ; i ++ ){

        if ( prices[i]< min) {
            min = prices[i];
        }
    
        if ( prices[i]- min > diff){
            diff = prices[i]- min;
        }

    }
    return diff;
}
