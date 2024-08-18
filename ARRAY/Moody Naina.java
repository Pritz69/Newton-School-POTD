import java.io.*; // for handling input/output
import java.util.*; // contains Collections framework

// don't change the name of this class
// you can add inner classes if needed
class Main {
    public static void main (String[] args) {
        // Your code here
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();  // Number of test cases

        // Loop over each test case
        for (int t = 0; t < T; t++) {
            int N = sc.nextInt();  // Number of elements in the array
            int l = sc.nextInt();  // Lower bound of Naina's love range
            int r = sc.nextInt();  // Upper bound of Naina's love range

            int currentHappiness = 0;
            int maxHappiness = 0;
            int minHappiness = 0;

            // Reading the array
            for (int i = 0; i < N; i++) {
                int Ai = sc.nextInt();  // Current element in the array

                // Update happiness
                if (l <= Ai && Ai <= r) {
                    currentHappiness += 1;  // Naina loves this element
                } else {
                    currentHappiness -= 1;  // Naina doesn't love this element
                }

                // Track maximum and minimum happiness
                maxHappiness = Math.max(maxHappiness, currentHappiness);
                minHappiness = Math.min(minHappiness, currentHappiness);
            }

            // Output the result for this test case
            System.out.println(maxHappiness + " " + minHappiness);
        }

        sc.close();
    }
}
