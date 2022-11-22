package javas;

import java.util.Scanner;

public class Calculator {

    public static int calc(int num1, int num2, String operator) {
        int i = 0;
        switch (operator) {
            case "+":
                i = num1+num2;
            break;
            case "-":
                i = num1-num2;
            break;
            case "*":
                i = num1*num2;
            break;
            case "/":
                i = num1/num2;
            break;
            default:
                i = 0;
            break;
        }
        return i;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter first number: ");
        int num1 = sc.nextInt();
        
        System.out.println("Ok");

        System.out.print("Enter second number: ");
        int num2 = sc.nextInt();
    
        System.out.print("Enter operator (+,-,*,/): ");
        String operator = sc.next();

        System.out.println(calc(num1, num2, operator));
        sc.close();
    }
}