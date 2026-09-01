class Solution {
    public double[] convertTemperature(double celsius) {
        // COMPLETELY OWN SOLVED
        double kelvin = celsius +273.15;
        double fahrenheit = (celsius *1.80) + 32.00;
        double[] nums = {Math.round(kelvin*100000.0)/100000.0,Math.round(fahrenheit*100000.0)/100000.0};
        return nums;
    }
}