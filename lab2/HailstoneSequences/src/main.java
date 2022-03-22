import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        // Read in a long from the user
        Scanner scanner = new Scanner(System.in);
        long n = scanner.nextLong();
        int counter = 1;

        // Base case is when n = 1;
        while (n!=1){
            counter++;
            // if the number is even, perform this calculation
            if (n % 2 == 0){
                n = n/2;
            } else {
                n = (3 * n) + 1;
            }
        }
        // return how many times to took to reach n = 1
        System.out.println(counter);
    }
}
