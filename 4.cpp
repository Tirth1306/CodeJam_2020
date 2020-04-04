////////////////////////////////// Tirth Patel(18bce245) ///////////////////////////////////////

//I did this program in CPP because i was not getting interactive inputs in python , don't know why?
//I have done only 1st test case!

#include <bits/stdc++.h>
using namespace std;
int main()
{
  int t;
  int b;
 
  cin>>t>>b;
 
  for(int x=1;x<=t;x++)
  {
  	int ans[b+1];
   
  	for(int j=1;j<=b;j++)
  	{
  		cout<<j<<endl;
  		cin>>ans[j];
  	}
   
  	for(int i=1;i<=b;i++)
    {
        cout<<(char)(ans[i]+'0');
    }
  		
  	cout<<endl;
   
  	    char verd;
  	cin>>verd;
   
  	if(verd!='Y')
    {
        exit(0);
    }
  }
 
 	return 0;
}

////////////////////////////////// Tirth Patel(18bce245) ///////////////////////////////////////