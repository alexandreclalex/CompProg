#include <cstdio>
using namespace std;

int main(){
    int n, m;
    int a[10];
    bool arr[1000001];

    while(scanf("%d %d", &n, &m) == 2){
        for(int i=0; i<m; i++){
            scanf("%d", &a[i]);
        }

        arr[0] = false;
        for(int i=1; i <= n; i++){
            arr[i] = false;
            for(int j=0; j<m; j++){
                if(i>=a[j] && !arr[i-a[j]]){
                    arr[i] = true;
                    break;
                }
            }
        }
        if(arr[n]){
            printf("Stan wins\n");
        } else{
            printf("Ollie wins\n");
        }
    }
}
