//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// Back-end complete function Template for C++

class Solution{
public:
    char player = 'x', opponent = 'o';
 
    bool isMovesLeft(char board[3][3]){
        for (int i = 0; i<3; i++)
            for (int j = 0; j<3; j++)
                if (board[i][j]=='_')
                    return true;
        return false;
    }
    
    int evaluate(char b[3][3]){
        for (int row = 0; row < 3; row++){
            if (b[row][0] == b[row][1] && b[row][1] == b[row][2]){
                if (b[row][0]==player)
                    return +10;
                else if (b[row][0]==opponent)
                    return -10;
            }
        }
     
        for (int col = 0; col < 3; col++){
            if (b[0][col] == b[1][col] && b[1][col] == b[2][col]){
                if (b[0][col]==player)
                    return +10;
                else if (b[0][col]==opponent)
                    return -10;
            }
        }
        if (b[0][0] == b[1][1] && b[1][1] == b[2][2]){
            if (b[0][0]==player)
                return +10;
            else if (b[0][0]==opponent)
                return -10;
        }
     
        if (b[0][2] == b[1][1] && b[1][1] == b[2][0]){
            if (b[0][2] == player)
                return +10;
            else if (b[0][2] == opponent)
                return -10;
        }
        return 0;
    }
    
    int minimax(char board[3][3], int depth, bool isMax){
        int score = evaluate(board);
        if (score == 10)
            return score;
        if (score == -10)
            return score;
        if (isMovesLeft(board) == false)
            return 0;
        if (isMax){
            int best = -1000;
            for (int i = 0; i < 3; i++){
                for (int j = 0; j < 3; j++){
                    if (board[i][j] == '_'){
                        board[i][j] = player;
                        best = max( best, minimax(board, depth+1, !isMax) );
                        board[i][j] = '_';
                    }
                }
            }
            return best;
        }
        else{
            int best = 1000;
            for (int i = 0; i < 3; i++){
                for (int j = 0; j < 3; j++){
                    if (board[i][j] == '_'){
                        board[i][j] = opponent;
                        best = min(best, minimax(board, depth+1, !isMax));
                        board[i][j] = '_';
                    }
                }
            }
            return best;
        }
    }
    
    vector<int> findBestMove(char board[3][3]){
        int bestVal = -1000;
        int row = -1, col = -1;
        vector<int> res;
        for (int i = 0; i < 3; i++){
            for (int j = 0; j < 3; j++){
                if (board[i][j] == '_'){
                    // Make the move
                    board[i][j] = player;
                    int moveVal = minimax(board, 0, false);
                    // Undo the move
                    board[i][j] = '_';
                    if (moveVal > bestVal){
                        row = i;
                        col = j;
                        bestVal = moveVal;
                    }
                }
            }
        }
        res.push_back(row);
        res.push_back(col);
        return res;
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        char board[3][3];
        for(int i = 0;i < 3;i++)
            cin>>board[i][0]>>board[i][1]>>board[i][2];
        
        Solution ob;
        vector<int> ans = ob.findBestMove(board);
        cout<<ans[0]<<" "<<ans[1]<<"\n";
    }
    return 0;
}
// } Driver Code Ends