#include<stdio.h>
#include<math.h>
#include<stdlib.h>

#include<iostream>
using namespace std;

long gcd(long a, long b) {
    long x = max(a,b);
    long y = min(a,b);
    int remainder = x % y;

    if (remainder == 0) {
        return y;
    }

    return gcd(y, remainder);
}

int main()
{
	long total = 0;
	long reflections = 12017639147;
	long m; 
	float progress;
	m = (reflections + 3) / 2;

	for(long i = 0; i <= m / 2; i = i + 1){
		long x = i;
		long y = m - i;
	
		if( (x - y) % 3 == 0 && gcd(x, y) == 1 ){
			total = total + 1;
		}
		
		if(i % 10000000 == 0){
			progress = (float)i / (m / 2);
			printf("%.7f \t %ld \n",progress , 2*total);
		}
	}

	printf("%ld \n",2 * total);
	return 0;
}
