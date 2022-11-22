package javas;

public class Ghoul {
    
    public static void main(String[] args) throws InterruptedException {
        int ghoul = 1000;
        int minus = 7;

        while(ghoul>1){
            ghoul-=minus;
            if(ghoul-7==-1) {
                System.out.println("6 - 7 = 0\nI'm Ghoul");
                return;
            }
            System.out.println(Integer.toString(ghoul) + " - 7 = " + Integer.toString(ghoul-7));
            Thread.sleep(25);
        }


    }

}
