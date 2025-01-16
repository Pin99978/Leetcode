#include <stdio.h>

void reverseString(char *s , int sSize ){

  // two pointer method
  int start = 0 , end = sSize - 1;
  while ( start < end ){
    char tmp = s[start];
    s[start ] = s[end];
    s[end] = tmp;
  }

  start ++ ;
  end -- ;
}
