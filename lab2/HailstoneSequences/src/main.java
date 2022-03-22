import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long n = scanner.nextLong();
        int counter = 1;
        while (n!=1){
            counter++;
            if (n % 2 == 0){
                n = n/2;
            } else {
                n = (3 * n) + 1;
            }
        }
        System.out.println(counter);
    }
}
