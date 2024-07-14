import java.io.*; // for handling input/output
import java.util.*; // contains Collections framework

// don't change the name of this class
// you can add inner classes if needed
class Main {
    public static void main (String[] args) {
        // Your code here
        Scanner sc=new Scanner(System.in);
		    int n=sc.nextInt();
		    int a[]=new int[n];
		    for(int i=0;i<n;i++)
		    {
		        a[i]=sc.nextInt();
		    }
		    int mi=n;
		    int ma=1;
		    int c=1;
		    ArrayList<Integer>ans=new ArrayList<Integer>();
		    for(int i=1;i<n;i++)
		    {
		        if(a[i]-a[i-1]<=2)
		        {
		            c +=1;
		            ma=Math.max(ma,c);
		        }
		        else
		        {
		            ans.add(c);
		            c=1;
		        }
		    }
		    ma=Math.max(ma,c);
		    ans.add(c);
		    for(int i=0;i<ans.size();i++)
		    {
		        mi=Math.min(mi,ans.get(i));
		    }
		    System.out.println(mi+" "+ma);
    }
}
