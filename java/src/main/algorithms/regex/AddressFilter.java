package algorithms.regex;

public class AddressFilter {
    private static WhiteListFilter whiteListFilter;
    private static IPFilter IPFilter;
    private static URLFilter URLFilter;

    public AddressFilter() {
        whiteListFilter = new WhiteListFilter();
        IPFilter = new IPFilter();
        URLFilter = new URLFilter();
    }

    public boolean filter(String input) {
        if(whiteListFilter.detect(input)) {
            return true;
        } else if(IPFilter.detect(input)) {
            return false;
        } else if(URLFilter.detect(input)) {
            return false;
        }

        return false;
    }
}
