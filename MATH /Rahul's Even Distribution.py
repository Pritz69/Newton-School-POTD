import java.io.*; // for handling input/output
import java.util.*; // contains Collections framework

// don't change the name of this class
// you can add inner classes if needed
class Main {
    public static int gcd(int n,int m)
    {
        if(m==0)
        {
            return n;
        }
        return gcd(m,n%m);
    }
    public static void main (String[] args) {
        // Your code here
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while (t-- >0 )
        {
            int n=sc.nextInt();
            int m=sc.nextInt();
            int ans=gcd(n,m);
            System.out.println(ans);
        }
        sc.close();
    }
}
