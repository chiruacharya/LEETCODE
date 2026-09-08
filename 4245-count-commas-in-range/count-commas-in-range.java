class Solution {
    public int countCommas(int n) {
        // COMPLETELY OWN SOLVED
        if(n<1000){
            return 0;
        }
        return n-999;
    }
}