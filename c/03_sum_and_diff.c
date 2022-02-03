#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
	int n, m;
    float fn, fm;
    
    scanf("%d %d", &n, &m);
    scanf("%f %f", &fn, &fm);

    printf("%d %d\n", n+m, n-m);
    printf("%.1f %.1f\n", fn+fm, fn-fm);             
    
    return 0;
}
