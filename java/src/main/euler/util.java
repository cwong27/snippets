package euler;

import java.util.ArrayList;
import java.util.List;

public class util {

    public static boolean isPrime(long n) {
        boolean isPrime = true;
        if(n < 2) return false;
        for(long i = 2; i*i <= n; i++) {
            if(n%i == 0) {
                isPrime = false;
                break;
            }
        }
        return isPrime;
    }

    public static List<Long> primeFactors(long numbers) {
        long n = numbers;
        List<Long> factors = new ArrayList<Long>();
        for(long i = 2; i <= n / i; i++) {
            while(n % i == 0) {
                factors.add(i);
                n /= i;
            }
        }
        if(n > 1) {
            factors.add(n);
        }
        return factors;
    }

    public static List<Long> factors(long n) {
        List<Long> res = new ArrayList<Long>();
        long half = n/2;
        for(long i=2; i <= half; i++) {
            if(n%i == 0) res.add(i);
        }
        return res;
    }

    public static boolean isPalindrome(String s) {
        final String sReverse = new StringBuilder(s).reverse().toString();
        return s.equals(sReverse);
    }

    public static long gcd(long a, long b) {
        if(b==0) return a;
        return gcd(b, a%b);
    }

    public static long lcm(long a, long b) {
        long l;
        if(a < b) {
            l = (a*b)/gcd(b,a);
        } else {
            l = (a*b)/gcd(a,b);
        }
        return l;
    }

    public static long firstNSum(long n) {
        return n*(n+1)/2;
    }

    public static long fib(long n) {
        long prev1 = 0;
        long prev2 = 1;
        for(long i=0; i<n; i++) {
            long savePrev1 = prev1;
            prev1 = prev2;
            prev2 = savePrev1 + prev2;
        }
        return prev1;
    }

    public static String reverse(String s) {
        StringBuilder sb = new StringBuilder(s);
        return sb.reverse().toString();
    }
}
