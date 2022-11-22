package javas;

import java.util.Scanner;

public class CoolOutput {
    
    public static void main(String[] args) throws InterruptedException {//thank to wcq!
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter text: ");
        String temp = sc.next();
        String str = temp+(temp.substring(temp.length()-1,temp.length()));
        int what = str.length()-1;
        for (int i = 0; i < what;) {
            StringBuilder strBuilder = new StringBuilder(str);
            strBuilder.deleteCharAt(what - i);
           str = strBuilder.toString();
            System.out.println(strBuilder.toString());
           i++;
           Thread.sleep(25);
        }
        sc.close();
    }

}
