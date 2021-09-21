package com.company;

import java.util.Scanner;

public class Assmt1 {
    public static void fn1()
    {
        int a,b;
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter two numbers:");
        a=sc.nextInt();
        b=sc.nextInt();

        if(b%2!=0)
            System.out.println("b is odd");
        else{
            if(b==a*a)
                System.out.println("b is even and square of a");
            else if(b%a==0)
                System.out.println("b is even and multiple of a");
            else
                System.out.println("b is neither multiple nor square of a");
        }
    }
    public static void main(String[] args) {

            Assmt1 as=new Assmt1();
            as.fn1();


    }
}
