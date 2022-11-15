using System;

class DeadInside {  
    static void Main(string[] args)
    {
        for (int i = 1000; i > 2; i-=7)
        {
            if(i-7==-1) {
                Console.WriteLine("6 - 7 = 0");
                System.Threading.Thread.Sleep(1000);
                Console.WriteLine("I'm Ghoul");
                break;
            }    
            Console.WriteLine(i + " - 7 = " + (i - 7));
            System.Threading.Thread.Sleep(25);            
        }
    }       
}
    