package javas;
import java.util.Scanner;
class MegaCoolProgram {

    private static char rndChar () {
        int rnd = (int) (Math.random() * 52);
        char base = (rnd < 26) ? 'A' : 'a';
        return (char) (base + rnd % 26);

    }


    public static void main(String[] args) throws InterruptedException {
        Scanner sc = new Scanner(System.in);

        int max = 500;
        int min = 1;
        int range = max - min + 1;

        System.out.print("Enter anything: ");
        String weifklwkgeweui = sc.next();
        
        for(int i = 0; i<200 ;i++){
            for(int x = 0; x<(int)(Math.random() * range) + min; x++){
                System.out.print(rndChar());
            }
            System.out.print("\n");
            Thread.sleep(5);
        }

        sc.close();

    }

}
