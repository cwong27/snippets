package algorithms.regex;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class IPFilter implements Filter {
    public IPFilter() {
        //10, 127, 192
    }

    @Override
    public boolean detect(String input) {
        Pattern ipPattern = Pattern.compile("(10|127|192)(.)\\d{1,}(.)\\d{1,}(.)\\d{1,}");
        Matcher ipMatcher = ipPattern.matcher(input);

        //System.out.println(input+" "+ ipMatcher.matches());

        return ipMatcher.matches();
    }
}
