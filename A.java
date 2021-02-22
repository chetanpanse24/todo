class A{
public static void m1(int a)
{
System.out.println("m1 class A");
} 
public static void m1(int a, int b)
{
System.out.println("m1 class A");
} 
public static void m1(int a,int b,int c)
{
System.out.println("m15 class A");
} 

public static void main(String args[])
{
m1(2);
m1(2,3);
m1(2,3,3);
}
}