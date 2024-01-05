--->https://my.newtonschool.co/playground/code/mphpbparlwog



import java.io.*; // for handling input/output
import java.util.*; // contains Collections framework

// don't change the name of this class
// you can add inner classes if needed
class Main {
    public static int minRepeats(String A, String B) {
        
        if(A.equals(B))
        return 1;
        String str=A;
        int count=1;
        while(str.length()<=B.length())
        {
            str=str+A;
            count++;
            if(str.contains(B))
            return count;
        }
        str=str+A;
        count++;
        if(str.contains(B))
        return count;
        return -1;
    }
    public static void main (String[] args) {
        // Your code here
        Scanner sc=new Scanner(System.in) ;
        String a=sc.next();
        String b=sc.next();
        System.out.println(minRepeats(a,b));
        }
}
