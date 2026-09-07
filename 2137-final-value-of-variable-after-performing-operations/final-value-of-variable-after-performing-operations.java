class Solution {
    public int finalValueAfterOperations(String[] operations) {
        // COMPLETELY OWN SOLVED THE LOGIC BUT CONFUSED IN == AND .equals IN JAVA SO I CHECKED AI FOR THAT == FOR CHECKING OBJECTS ARE SAME ARE NOT .equals FOR ACTUAL VALUE COMPARATION.
        int x = 0;
        for (String i:operations){
            String s = i;
            if ((s.equals("++X")) ||( s.equals("X++")) ){
                x++;
            }
            else{
                x--;
            }
        
        }
        return x;
    }
}