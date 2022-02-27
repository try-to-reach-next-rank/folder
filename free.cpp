#include<bits/stdc++.h>
using namespace std;
#define forn(i,x,y,z) for(ll i=x;i<y;i+=z)
#define form(i,x,y,z) for(ll i=x;i>y;i+=z)
#define ll long long
#define gcd(a,b) (__gcd(a,b))
#define lcm(a,b) (a/gcd(a,b)*b)
#define len(x) (ll)(x.size())
#define fast_cin() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(0);
#define pb push_back
#define str string
#define n_solve() ll test_case;cin>>test_case;forn(i,0,test_case,1){solve();}

void solve(){
	int n,k; cin>>n>>k; str s,ans;cin>>s;
	form(i,n-1,-1,-1){
		ans+=s[i];
	}
	if(ans==s or k==0){
		cout<<"1\n";
	}
	else{
		cout<<"2\n";
	}

}
signed main(){
	//freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
    fast_cin();
	n_solve();
}



//function
int binarySearch(ll arr[], ll n, ll x){
	ll ans =0;
	ll end = n - 1;
	ll start = 0;
	while (end >= start) {
		ll mid = start + (end - start) / 2;
    	if(arr[mid] == x){
			end = mid-1;
			ans = mid;
		}
		else if(arr[mid]>x){
			end = mid-1;
			ans = mid;
		}
		else{
			start = mid+1;
		}
	}
	return ans;
}

str bin(int n){ 
    char buffer[33];
    return itoa(n,buffer,2);
}

int remove(int x){
	str s = to_string(x);
	forn(i,0,len(s),1){
		if(s[i] == '0'){
      		s.erase(s.begin() + i);
      		i--;
    	}
    }
	return stoi(s);
}
