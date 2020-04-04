////////////////////////////////// Tirth Patel(18bce245) ///////////////////////////////////////

//I did this program in CPP because i was not getting interactive inputs in python , don't know why?


#include<bits/stdc++.h>
# define fast_io ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
#define all(a) begin(a),end(a)
typedef long long ll;
typedef unsigned long long ull;
using namespace std;
const int inf = 1e9 + 5, N = 2e5 + 5, d1[] = { 0,0,1,-1 }, d2[] = { 1,-1,0,0 };

int main()
{
    int test;
    int n;

    cin>>test>>n;

    while(test--)
    {
        int i,j;
          int d=-1,c=-1;

        string str(n,'?');

          char ls;
        char check;
  
        for(i=1,j=0;j<n/2;i+=2)
        {  
            if(i>10 && i%10==1)
            {
                if(c!=-1)
                {
                    cout << c+1 << endl;
                    cin >> ls;
                    if(str[c]!=ls)
                    {
                        for(char& x:str)
                        {
                          if(x=='1')
                          {
                            x='0';
                          }
                          else if(x=='0')
                          {
                            x='1';
                          }
                        }
                    }
                    
                }
                else 
                {
                  cout << "1\n";
                  cin>>ls;
                }
                if(d!=-1)
                {
                    cout << d+1 << endl;
                    cin >> ls;
                    if(str[d]!=ls)
                    {
                      reverse(all(str));
                    }
                }
                else
                {
                  cout << "1\n";
                  cin>>ls;
                }
            }
            else
            {
                cout << j+1 << endl;
                cin >> str[j];
                cout << n-j << endl;
                cin >> str[n-1-j];
                if(str[j]==str[n-1-j])
                {
                  c=j;
                }
                else if(str[j]!=str[n-1-j])
                {
                  d=j;
                }
                ++j;
            }
        }

          cout << str << endl;

          cin>>check;

        if(check=='N')
        {
            return 0;
        }
    }
}

////////////////////////////////// Tirth Patel(18bce245) ///////////////////////////////////////