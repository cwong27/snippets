package euler;

import java.util.HashMap;

public class Problem009 {

    public static void main(String[] args) {
        long res = 0;

        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

        for(int i=1; i < 999; i++) {
            int squareValue = ((Double)Math.pow(i, 2)).intValue();
            map.put((Integer)squareValue, i);
        }

        for(Integer value : map.keySet()) {
            for(Integer value2 : map.keySet()) {
                if(value == value2) continue;
                if(map.containsKey(value2 - value)) {
                    int i = map.get(value);
                    int j = map.get(value2);
                    int k = map.get(value2-value);
                    if(i+j+k==1000) {
                        res = i*j*k;
                    }
                }
            }
        }

//        for(int i=1; i < 999; i++) {
//            for(int j=1; j < 999; j++) {
//                for(int k=1; k< 999; k++) {
//                    if(i+j+k == 1000) {
//                        int i2 = (int) Math.pow(i, 2);
//                        int j2 = (int) Math.pow(j, 2);
//                        int k2 = (int) Math.pow(k, 2);
//                        if(i2+j2 == k2) {
//                            res = i*j*k;
//                        }
//                    }
//                }
//            }
//        }

        System.out.println("Ans: "+ res); //31875000
    }
}
