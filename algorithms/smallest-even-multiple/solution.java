class Solution {
    public boolean checkDivisibility(int n) {
        // COMPLETELY OWN SOLVED
        int sum = 0;
        int product = 1;
        int temp = n;
        while(n>0){
            int digit = n%10;
            sum+=digit;
            product *= digit;
            n= n/10;
        }
        int total = sum + product;
        if (temp%total ==0){
            return true;
        }
        else{
            return false;
        }

    }
}