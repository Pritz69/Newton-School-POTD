import java.io.*; // for handling input/output
import java.util.*; // contains Collections framework

// don't change the name of this class
// you can add inner classes if needed
class Main {
    private static Map<String, Long> memo = new HashMap<>();
    
    public static long countPaths(int i, int j, int n) {
        // Base case: If we reach the top-right corner
        if (i == 0 && j == n - 1) {
            return 1;
        }
        // Create a key for memoization
        String key = i + "," + j;
        // Check if the result is already computed
        if (memo.containsKey(key)) {
            return memo.get(key);
        }
        // Calculate the number of paths from (i, j)
        long paths = 0;
        // Move upwards if within bounds
        if (i > 0) {
            paths += countPaths(i - 1, j, n);
        }
        // Move rightwards if within bounds and above the diagonal
        if ((i + j) < n) {
            paths += countPaths(i, j + 1, n);
        }
        // Memoize the result
        memo.put(key, paths);
        return paths;
    }
    
    public static long countDiagTallyPaths(int n) {
        // Start from the bottom-left corner
        return countPaths(n - 1, 0, n);
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.close();
        long result = countDiagTallyPaths(n);
        System.out.println(result);
    }
}
