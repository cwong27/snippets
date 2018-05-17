package random;

import java.util.HashMap;
import java.util.Set;

public class MaxYear {
    private HashMap<Integer, Integer> yearCounts;
    private int result = 0;

    public MaxYear(int[] input) {
        yearCounts = new HashMap<>();

        if(input.length % 2 != 0) {
            result = -1;
        } else {
            parseInputs(input);
        }
    }

    public int getResult() {
        if(result == -1) {
            return -1;
        }

        Set<Integer> keys = yearCounts.keySet();
        int maxYear = 0;
        int maxPop = 0;

        for(int key : keys) {
            //System.out.println(key+" "+yearCounts.get(key));
            if(maxPop < yearCounts.get(key)) {
                maxYear = key;
                maxPop = yearCounts.get(key);
            }
        }

        return maxYear;
    }

    private void parseInputs(int[] input) {
        for(int i = 0; i < input.length; i+=2) {
            //System.out.println(input[i]+" "+input[i+1]);
            addYear(input[i], input[i+1]);
        }
    }

    private void addYear(int startYear, int endYear) {
        for(int i = startYear; i <= endYear; i++) {
            if(yearCounts.containsKey(i)) {
                int newCount = yearCounts.get(i) + 1;
                yearCounts.replace(i, newCount);
            } else {
                yearCounts.put(i, 1);
            }
        }
    }
}
