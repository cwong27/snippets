package algorithms.regex;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class AddressFilterTest {

    private static AddressFilter filter;
    private static String[] goodAddress = {"www.good.com", "www.corp.com", "https://ok.com", "https://www.ok.com", "sub.corp.com", "https://ok.good.com"};
    private static String[] badIP = {"127.0.0.1", "10.0.0.1", "192.0.0.1", "10.0.10.127"};
    private static String[] badURL = {"http://hello.com", "bad.com", "evil.com", "https://www.evil.com"};

    @Before
    public void setUp() {
        filter = new AddressFilter();
    }

    @Test
    public void testWhiteList() {
        Assert.assertEquals(true, filter.filter(goodAddress[0]));
        Assert.assertEquals(true, filter.filter(goodAddress[1]));
        Assert.assertEquals(true, filter.filter(goodAddress[2]));
        Assert.assertEquals(true, filter.filter(goodAddress[3]));
        Assert.assertEquals(true, filter.filter(goodAddress[4]));
        Assert.assertEquals(true, filter.filter(goodAddress[5]));

    }

    @Test
    public void testIPFilter() {
        Assert.assertEquals(false, filter.filter(badIP[0]));
        Assert.assertEquals(false, filter.filter(badIP[1]));
        Assert.assertEquals(false, filter.filter(badIP[2]));
        Assert.assertEquals(false, filter.filter(badIP[3]));


    }

    @Test
    public void testURLFilter() {
        Assert.assertEquals(false, filter.filter(badURL[0]));
        Assert.assertEquals(false, filter.filter(badURL[1]));
        Assert.assertEquals(false, filter.filter(badURL[2]));
        Assert.assertEquals(false, filter.filter(badURL[3]));

    }
}
