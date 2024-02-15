#include <iostream>
#include <string>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n, len;
    cin >> n;

    string str[51];

    for (int i = 0; i < n; i++) cin >> str[i];
    len = str[0].length();

    for(int i = 0; i< len; i++){
        char c = str[0][i];
        for(int j = 0; j < n; j++){
            if(c != str[j][i]){
                c = '?';
                break;
            }
        }
        cout << c;
    }

    return 0;
}
