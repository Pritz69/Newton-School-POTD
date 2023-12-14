-->https://my.newtonschool.co/playground/code/byy0ku677u1s



import java.io.*; // for handling input/output
import java.util.*; // contains Collections framework

// don't change the name of this class
// you can add inner classes if needed
class Main {
    static final int MOD = 1000000007;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int t = scanner.nextInt();
        for (int testCase = 0; testCase < t; testCase++) {
            int x = scanner.nextInt();
            int k = scanner.nextInt();
            int result = countWaysToReachHome(x, k);
            System.out.println(result);
        }

        scanner.close();
    }

    static int countWaysToReachHome(int x, int k) {
        int[] dp = new int[x + 1];
        dp[0] = 1;

        for (int i = 1; i <= x; i++) {
            for (int j = 1; j <= k; j++) {
                if (i - j >= 0) {
                    dp[i] = (dp[i] + dp[i - j]) % MOD;
                }
            }
        }

        return dp[x];
    }
}


---> PYTHON --->
# Your code here
import sys
sys.setrecursionlimit(10**6)
mod=10**9 +7
for i in range(int(input())) :
    x,k=map(int,input().split())
    def rec(i) :
        if i==0 :
            return 1
        if i<0 :
            return 0
        if i in dp :
            return dp[i]
        c=0
        for j in range(1,k+1) :
            c = (c + rec(i-j))%mod
        dp[i]=c
        return c
    dp={}
    ans=rec(x)
    print(ans)
