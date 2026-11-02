class Solution {
    public int numIslands(char[][] grid) {
        int cnt = 0;
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                if(grid[i][j] == '1'){
                    fill(grid, i, j);
                    cnt++;
                }
            }
        }
        return cnt;
    }
    public boolean inbounds(int r, int c, char[][] grid){
        return r >= 0 && r < grid.length && c < grid[0].length && c >= 0;
    }
    public void fill(char[][] grid, int r, int c){
        if (inbounds(r, c, grid) && grid[r][c] == '1') {
            grid[r][c] = '2';
            fill(grid, r + 1, c);
            fill(grid, r - 1, c);
            fill(grid, r, c + 1);
            fill(grid, r, c - 1);
        }
    }
}
