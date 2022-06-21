#include<iostream>
#include<algorithm>
using namespace std;
int n, dp[50001];
int main(){
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);

	cin >> n;

	dp[1] = 1;

	for (int i = 1; i <= n; i++){
		dp[i] = dp[1] + dp[i - 1];
		for (int j = 2; j * j <= i; j++){
			dp[i] = min(dp[i], 1 + dp[i - j * j]);
		}
	}
	cout << dp[n];
    return 0;
}
// 어떻게 했는지 이해하는중
// 작성자가 써 놓은 로직은 
// ex) 101이 들어왔다면, dp[1] + dp[100], dp[4] + dp[97].... 이런식으로 찾는 방법
// 저 중에서 가장 작은 값을 찾는 방법
// 여기는 이해가 되는데 그렇다면 dp배열 초기화는?
// dp[1], dp[4] 등 제곱수는 dp[n**2] = 1 로 초기화한다
// 