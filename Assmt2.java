package com.company;

import java.util.Scanner;

public class Assmt2 {
    public static void calDigits(int n){
        int count=0;
        while(n!=0){
            n=n/10;
            count++;
        }
        switch(count){
            case 1,2:System.out.println("No. of digits are: "+ count);
                    break;
            case 3: System.out.println(count+" "+count*count*count); break;
            case 4: System.out.println(count+" "+count*count);break;
            case 5: System.out.println(count+" "+(count-1)*(count-1));break;
            case 6: System.out.println(count+" "+count*count);break;
            default:
                System.out.println("None");

        }

    }
    public static void takeNumber() {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter a number:");
        int num=sc.nextInt();
        calDigits(num);
    }
    public static void main(String[] args) {

        Assmt2 as1=new Assmt2();
        as1.takeNumber();

    }
}
