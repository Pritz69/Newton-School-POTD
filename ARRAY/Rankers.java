import java.io.*; // for handling input/output
import java.util.*; // contains Collections framework

// don't change the name of this class
// you can add inner classes if needed
class Main {
    public static void main (String[] args) {
        // Your code here
        Scanner sc=new Scanner(System.in);
        int a[]=new int[3];
        int sa=0;
        int sb=0;
        for(int i=0;i<3;i++)
        {
            a[i]=sc.nextInt();
            sa += a[i];
        }
        int b[]=new int[3];
        for(int i=0;i<3;i++)
        {
            b[i]=sc.nextInt();
            sb +=b[i];
        }
        if(sa > sb)
        {
            System.out.println("Ram");
        }
        else if(sb>sa)
        {
            System.out.println("Shyam");
        }
        else
        {
            if(a[0]>b[0])
            {
                System.out.println("Ram");
            }
            else if(b[0]>a[0])
            {
                System.out.println("Shyam");
            }
            else
            {
                if(a[1]>b[1])
                {
                    System.out.println("Ram");
                }
                else if(b[1]>a[1])
                {
                    System.out.println("Shyam");
                }
                else
                {
                    System.out.println("Tie");
                }
            }
        }
    }
}
