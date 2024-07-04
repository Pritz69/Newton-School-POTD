import java.io.*; // for handling input/output
import java.util.*; // contains Collections framework

// don't change the name of this class
// you can add inner classes if needed
class Main {
    public static void main (String[] args) {
        // Your code here
        Scanner sc=new Scanner(System.in);
        int a=sc.nextInt();
        int b=sc.nextInt();
        int r=1;
        int s=2;
        int ram=0;
        int shyam=0;
        while (ram <= a && shyam <=b)
        {
            ram += r;
            shyam += s;
            if (ram > a)
            {
                System.out.println("Shyam");
                break;
            }
            else if (shyam > b)
            {
                System.out.println("Ram");
                break;
            }
            r +=2;
            s +=2;
        } 
    }
}
