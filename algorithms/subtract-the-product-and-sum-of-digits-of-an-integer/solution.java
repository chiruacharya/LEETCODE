class Solution {
    public int subtractProductAndSum(int n) {
        // COMPLETELY OWN SOLVED
        int prd = 1;
        int sum = 0;
        int temp = n;
        while (temp>0){
            int a = temp%10;
            temp = temp/10;
            prd *=a;
            sum+=a;
        }
        return prd-sum;
        
    }
}