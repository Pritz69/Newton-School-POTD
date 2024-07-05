import java.io.*; // for handling input/output
import java.util.*; // contains Collections framework

// don't change the name of this class
// you can add inner classes if needed
class Main {
    public static void main (String[] args) {
        // Your code here
        Scanner sc=new Scanner(System.in);
        int x=sc.nextInt();
        int y=sc.nextInt();
        int z=sc.nextInt();
        int t=x*y;
        double p=z/(t*1.0);
        if (p > 0.5)
        {
            System.out.println("Yes");
        }
        else
        {
            System.out.println("No");
        }
    }
}
