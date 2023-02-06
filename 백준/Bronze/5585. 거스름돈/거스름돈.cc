#include <iostream>
using namespace std;
int main(void)
{
    int money, change, tmp; change = 0;
    cin >> money;
    money = 1000 - money;
    tmp = money / 500;
    change += tmp; money -= tmp * 500;
    tmp = money / 100;
    change += tmp; money -= tmp * 100;
    tmp = money / 50;
    change += tmp; money -= tmp * 50;
    tmp = money / 10;
    change += tmp; money -= tmp * 10;;
    tmp = money / 5;
    change += tmp; money -= tmp * 5;
    change += money;
    cout << change;
    return 0;
}