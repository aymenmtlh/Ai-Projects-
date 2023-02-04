#include <iostream>
using namespace std ;

int main ()
{ 
    const int x = 5;
    int client , gclient = 1 ;
    int i ;
  
    
   while   (x>0)
   {     
   
      cout << " \t  welcome to  algerie telecome        " << endl ;
        cout << "   enter number 1 to take a  ticket    " << endl ;
        cout << "                                     \n" << endl ;
        cin >> i;
   if ( i==1)
   {   
       client ++ ;
       cout << " number of clients  " << client << endl;
       cout << "\n" << endl ;
       cout << "                                     \n" << endl ;
       cout << "                                     \n" << endl ;
   }

   
    else if ( i==5  )
      {     
         cout << " client number " <<  gclient++  << "   go to guchet n 1  " << endl ;
         cout << "                                     \n" << endl ;
         cout << " clients  number is " <<  client-- << endl ;
         cout << "                                     \n" << endl ;
         cout << "                                     \n" << endl ;
         
	  }
    else 
    {     cout << " wrong number try again" << endl ;
	}
		
        
   
}
return 0;

}
