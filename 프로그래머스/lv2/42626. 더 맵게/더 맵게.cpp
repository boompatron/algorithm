#include <bits/stdc++.h>
using namespace std;
int solution(vector<int> scoville, int k) {
    priority_queue<int, vector<int>, greater<int
    > > pq;
    for (int s: scoville){
        pq.push(s);
    }
    int cnt = 0;
    while (pq.size() >= 2 && pq.top() < k){
        int a = pq.top();
        pq.pop();
        int b = pq.top();
        pq.pop();
        pq.push(a + b * 2);
        cnt++;        
    }
    if (pq.top() < k)
        return -1;
    return cnt;
}