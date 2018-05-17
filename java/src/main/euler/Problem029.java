package euler;

import java.util.HashSet;

public class Problem029 {
    public static void main(String[] args) {
        long res = 0;
        HashSet<Long> set = new HashSet<>();

        for(int z=1; z<20; z++) {


            for (int i = 2; i <= z; i++) {
                for (int j = 2; j <= z; j++) {
                    long num = (long) Math.pow(i, j);
                    if (!set.contains(num)) {
                        set.add(num);
                    }
                }
            }
            System.out.println("z="+z+", size="+set.size());
        }

        System.out.println("Ans: "+ set.size());
    }
}
