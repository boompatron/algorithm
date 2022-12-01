#include <iostream>
using namespace std;
int main(void)
{
    int n, k; //동전개수 n, 거스름돈 k
    int price[11];//동전 가격을 저장하는 배열
    cin >> n;
    cin >> k;
    for (int i = 0; i < n; i++)
        cin >> price[i];        //값을 받고
    int count = 0;              //답
    int check = n - 1;          //큰 값부터 비교해야 하므로 역순으로
    for (int i = 0; i < n; i++) {       //나누는 중
        if (k / price[check] > 0) {
            int a = k / price[check];
            //cout << price[check] << " : price[check]," << a << " : a" << endl;
            count += a;
            k -= a * price[check];
        }
        check--;
    }
    cout << count;
    return 0;
}