package algorithms.regex;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class WhiteListFilter implements Filter {
    public WhiteListFilter() {
        //ok, corp, good
    }

    @Override
    public boolean detect(String input) {
        Pattern httpsPattern = Pattern.compile("https://\\w*(.)?(ok|good|corp)(.com)?");
        Matcher httpsMatcher = httpsPattern.matcher(input);

        Pattern wwwPattern = Pattern.compile("\\w*(.)?(ok|good|corp)(.com)?");
        Matcher wwwMatcher = wwwPattern.matcher(input);

        //System.out.println(input+" "+httpsMatcher.matches() + " " + wwwMatcher.matches() );

        return httpsMatcher.matches() || wwwMatcher.matches();
    }
}
