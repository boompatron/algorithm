#include <bits/stdc++.h>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL); cout.tie(NULL);
    priority_queue<int> pq;
    int n, x;
    cin >> n;
    while (n--){
        cin >> x;
        if(x == 0){
            if(!pq.empty()) {cout << -pq.top() << "\n"; pq.pop();}
            else            cout << "0\n";
        }
        else  pq.push(-x);
    }
    return 0;
}