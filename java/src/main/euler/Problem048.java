package euler;

public class Problem048 {
    public static void main(String[] args) {
        long res = 0;
        long mod = (long)Math.pow(10,10);

        for(int i=1; i <= 1000; i++) {
            long current = i;
            for(int j=2; j <= i; j++) {
                current = (current*i)%mod;
            }
            res += current%mod;
        }

        System.out.println("Ans: "+ res);
    }
}
