using System;

namespace CsAlgorithm
{
    class Program1000
    {
        static void Main(string[] args)
        {
            int answer = 0;
            //케이스의 개수
            int num = Convert.ToInt32(Console.ReadLine());

            //케이스의 개수 만큼 반복
            for (int i = 0; i < num; i++)
            {
                string[] a = Console.ReadLine().Split();

                for (int j = 0; j < 360; j++)
                {

                    double[] zo = { Convert.ToInt32(a[0]) + (Convert.ToInt32(a[2]) * Math.Cos(j * (Math.PI / 180))), 
                        Convert.ToInt32(a[1]) + (Convert.ToInt32(a[2]) * Math.Sin(j* (Math.PI/180))) };
                    double[] ba = { Convert.ToInt32(a[3]) + (Convert.ToInt32(a[5]) * Math.Cos(j* (Math.PI/180))), 
                        Convert.ToInt32(a[4]) + (Convert.ToInt32(a[5]) * Math.Sin(j* (Math.PI/180))) };                    

                    if (zo[0] == ba[0] && zo[1] == ba[1])
                    {
                        answer += 1;
                    }
                    //Console.WriteLine(zo[0] + " " + zo[1] + "] [ " + ba[0] + " " + ba[1]);
                    Console.WriteLine(Math.Cos(j * (Math.PI/180) ) + ", " + Math.Sin(j * (Math.PI / 180)));

                }

            }
            
            Console.WriteLine(answer);
        }

        //문제 1000
        void Problem1000()
        {
            string[] a = Console.ReadLine().Split();
            Console.WriteLine(int.Parse(a[0]) + int.Parse(a[1]));
        }

        //문제 1001
        void Problem1001()
        {
            string[] a = Console.ReadLine().Split();
            Console.WriteLine(int.Parse(a[0]) - int.Parse(a[1]));
        }

        //문제 1002
        void Problem1002()
        {
            int answer = 0;
            //케이스의 개수
            int num = Convert.ToInt32(Console.ReadLine());

            //케이스의 개수 만큼 반복
            for (int i = 0; i < num; i++)
            {
                string[] a = Console.ReadLine().Split();

                for(int j = 0; j < 360; j++)
                {
                    double[] zo = { (Convert.ToInt32(a[2]) * Math.Sin(j)), (Convert.ToInt32(a[2]) * Math.Sin(j)) };
                    zo[0] = zo[0] + Convert.ToInt32(a[0]);
                    zo[1] = zo[1] + Convert.ToInt32(a[1]);

                    double[] ba = { (Convert.ToInt32(a[5]) * Math.Sin(j)), (Convert.ToInt32(a[5]) * Math.Sin(j)) };
                    ba[0] = ba[0] + Convert.ToInt32(a[3]);
                    ba[1] = ba[1] + Convert.ToInt32(a[4]);

                    if(zo == ba)
                    {
                        answer += 1;
                    }

                }
                
            }
                                    
            Console.WriteLine(answer);
        }
    }
}