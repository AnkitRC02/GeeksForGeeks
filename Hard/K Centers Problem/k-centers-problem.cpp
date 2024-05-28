//{ Driver Code Starts
//Initial Template for C++

#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++

class Solution{
    public: 
    int f(int* dis,int x){
        int val =INT_MIN;
        int l;
        for(int i=0;i<x;i++){
            if(dis[i]>val){
                val = dis[i];
                l=i;
            }
        }
        return l;
        
    }
    int selectKcities(int n, int k, vector<vector<int>>& mat){
        int ans = INT_MAX;
        for(int i=0;i<n;i++){
           int distance[n+1];
           int dummy=i;
           for(int r=0;r<n;r++){
               distance[r] = INT_MAX;
           }
           for(int j=0;j<k;j++){
               for(int p=0;p<n;p++){
                   distance[p] = min(distance[p],mat[dummy][p]);
               }
               dummy = f(distance,n);
           }
           ans = min(ans,distance[dummy]);
        }
        return ans;
    }
    
   
};



//{ Driver Code Starts.


int main(){
    int t;
    cin>>t;
    while(t--){
        int n,k;
        cin>>n>>k;
        vector<vector<int>> mat(n, vector<int>(n));
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                cin>>mat[i][j];
            }
        }
        
        Solution obj;
        int ans = obj.selectKcities(n, k, mat);
        
        cout<<ans<<endl;
    }
}
// } Driver Code Ends