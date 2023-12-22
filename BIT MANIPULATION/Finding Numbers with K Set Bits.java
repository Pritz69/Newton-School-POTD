-->https://my.newtonschool.co/playground/code/r3x8zgp2l7qa



import java.io.*;
import java.util.*; 

class Main {
     public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int k = scanner.nextInt();
        scanner.close();

        boolean found = false;

        for (int i = n; i >= 0; i--) {
            if (countSetBits(i) == k) {
                found = true;
                break;
            }
        }

        if (found) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }

    static int countSetBits(int x) 
    {
        /*int c=0;
        int v=1;
        while(x>0)
        {
            if ((x&v)==1)
            {
                c +=1;
            }
            x=x>>1;
        }
        return c;
        */
        return Integer.bitCount(x);
    }
}



--> PYTHON <--


TLE 

# Your code here
n,k=map(int,input().split())
def setbits(x) :
    c = 0
    while x > 0 :
        if x & 1 :
            c +=1
        x = x >> 1
    return c
#print(setbits(7),setbits(10))
f=0
for i in range(n,-1,-1) :
    if setbits(i)==k :
        f=1
        break
if f==0 :
    print("No")
else :
    print("Yes")
