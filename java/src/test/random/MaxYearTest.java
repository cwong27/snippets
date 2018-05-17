package random;

import org.junit.Assert;
import org.junit.Test;

public class MaxYearTest {
    @Test
    public void test1() {
        int[] input = {1};
        MaxYear test = new MaxYear(input);
        Assert.assertEquals(-1, test.getResult());
    }

    @Test
    public void test2() {
        int[] input = {1900, 1903, 1901, 1903, 1902, 1903};
        MaxYear test = new MaxYear(input);
        Assert.assertEquals(1902, test.getResult());
    }

    @Test
    public void test3() {
        int[] input = {1900, 1910, 1900, 1901, 1900, 1902};
        MaxYear test = new MaxYear(input);
        Assert.assertEquals(1900, test.getResult());
    }

    @Test
    public void test4() {
        int[] input = {1900, 1910, 1900, 1908, 1906, 1907, 1907, 1920};
        MaxYear test = new MaxYear(input);
        Assert.assertEquals(1907, test.getResult());
    }
}
