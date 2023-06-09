//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;
// UNASSIGNED is used for empty cells in sudoku grid 
#define UNASSIGNED 0  

// N is used for the size of Sudoku grid.  
// Size will be NxN  
#define N 9  


// } Driver Code Ends

class Solution {
public:
    // Function to find a solved Sudoku.
    bool SolveSudoku(int grid[N][N]) {
        int row, col;
        
        if (!findEmptyCell(grid, row, col))
            return true;

        for (int num = 1; num <= 9; num++) {
            if (isValidMove(grid, row, col, num)) {
                grid[row][col] = num;

                if (SolveSudoku(grid))
                    return true;

                grid[row][col] = 0;
            }
        }

        return false;
    }

    // Function to print grids of the Sudoku.
    void printGrid(int grid[N][N]) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                cout << grid[i][j] << " ";
            }
        }
    }

private:
    // Function to find an empty cell in the Sudoku grid.
    bool findEmptyCell(int grid[N][N], int& row, int& col) {
        for (row = 0; row < N; row++) {
            for (col = 0; col < N; col++) {
                if (grid[row][col] == 0)
                    return true;
            }
        }
        return false;
    }

    // Function to check if a number can be placed in a specific cell.
    bool isValidMove(int grid[N][N], int row, int col, int num) {
        return !usedInRow(grid, row, num) &&
               !usedInColumn(grid, col, num) &&
               !usedInBox(grid, row - row % 3, col - col % 3, num);
    }

    // Function to check if a number is already used in a row.
    bool usedInRow(int grid[N][N], int row, int num) {
        for (int col = 0; col < N; col++) {
            if (grid[row][col] == num)
                return true;
        }
        return false;
    }

    // Function to check if a number is already used in a column.
    bool usedInColumn(int grid[N][N], int col, int num) {
        for (int row = 0; row < N; row++) {
            if (grid[row][col] == num)
                return true;
        }
        return false;
    }

    // Function to check if a number is already used in a 3x3 box.
    bool usedInBox(int grid[N][N], int startRow, int startCol, int num) {
        for (int row = 0; row < 3; row++) {
            for (int col = 0; col < 3; col++) {
                if (grid[row + startRow][col + startCol] == num)
                    return true;
            }
        }
        return false;
    }
};



//{ Driver Code Starts.

int main() {
	int t;
	cin>>t;
	while(t--)
	{
		int grid[N][N];
		
		for(int i=0;i<9;i++)
		    for(int j=0;j<9;j++)
		        cin>>grid[i][j];
		        
		Solution ob;
		
		if (ob.SolveSudoku(grid) == true)  
            ob.printGrid(grid);  
        else
            cout << "No solution exists";  
        
        cout<<endl;
	}
	
	return 0;
}
// } Driver Code Ends