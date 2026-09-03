
class Solution {
    public boolean uniformArray(int[] nums1) {
        Arrays.sort(nums1);
        // System.out.println(Arrays.toString(nums1)[1]);
        if (nums1[0]%2 != 0 ){
            System.out.print("yes");
            return true;
        }
        
        else{
            int i = 0;
            int j = nums1.length -1;
            while (i<=j){
                if ((nums1[i]%2 != 0) || (nums1[j]%2 != 0)){
                    return false;
                }
                i++;
                j--;

            }
            
        }
        return true;
        
    }
}