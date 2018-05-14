package algorithms.regex;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class URLFilter implements Filter {
    public URLFilter() {

    }

    @Override
    public boolean detect(String input) {
        Pattern httpsPattern = Pattern.compile("http://.*+");
        Matcher httpsMatcher = httpsPattern.matcher(input);

        Pattern wwwPattern = Pattern.compile(".*(bad|evil)(.com)?");
        Matcher wwwMatcher = wwwPattern.matcher(input);

        //System.out.println(input+" "+httpsMatcher.matches() + " " + wwwMatcher.matches() );

        return httpsMatcher.matches() || wwwMatcher.matches();
    }
}
