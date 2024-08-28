import java.io.*; // for handling input/output
import java.util.*; // contains Collections framework

// don't change the name of this class
// you can add inner classes if needed
class Main {
    public static void main (String[] args) {
        // Your code here
         Scanner scanner = new Scanner(System.in);
        
        // Read the number of test cases
        int t = scanner.nextInt();
        
        // To store results for all test cases
        StringBuilder results = new StringBuilder();
        
        // Process each test case
        for (int i = 0; i < t; i++) {
            int n = scanner.nextInt();
            int countOfTwos = 0;
            
            // Read the array and count the number of 2's
            for (int j = 0; j < n; j++) {
                int num = scanner.nextInt();
                if (num == 2) {
                    countOfTwos++;
                }
            }
            
            // Check if the count of 2's is a multiple of 8
            if (countOfTwos % 8 == 0) {
                results.append("Yes\n");
            } else {
                results.append("No\n");
            }
        }
        
        // Print all results at once
        System.out.print(results.toString());
        
        // Close the scanner
        scanner.close();
    }
}
