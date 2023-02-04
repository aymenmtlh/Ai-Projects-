//---------------------------------------------------------------------------

#include <vcl.h>
#pragma hdrstop

#include "Tickgame.h"
char Symbole = 'X'  ;

//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.dfm"
TForm2 *Form2;


bool TForm2 ::  CheckIsWinner()
{
	if (! Button1->Caption.IsEmpty() &&   Button1->Caption==Button2->Caption &&  Button1->Caption==Button3->Caption ) {

	   return true ; }
	   if ( ! Button1->Caption.IsEmpty() && Button1->Caption==Button4->Caption &&  Button1->Caption==Button7->Caption ) {

	   return true ; }
	   if ( ! Button7->Caption.IsEmpty() &&   Button7->Caption==Button8->Caption &&  Button7->Caption==Button9->Caption ) {

	   return true ; }
	   if ( ! Button3->Caption.IsEmpty() &&    Button3->Caption==Button4->Caption &&  Button3->Caption==Button9->Caption ) {

	   return true ; }
	   if (  ! Button1->Caption.IsEmpty() &&   Button1->Caption==Button5->Caption &&  Button1->Caption==Button9->Caption ) {

	   return true ; }
	   if ( ! Button3->Caption.IsEmpty() &&  Button3->Caption==Button5->Caption &&  Button3->Caption==Button7->Caption ) {

	   return true ; }
	   if ( ! Button4->Caption.IsEmpty() &&  Button4->Caption==Button5->Caption &&  Button4->Caption==Button6->Caption ) {

	   return true ; }
	   else
	   return false  ;



}
//---------------------------------------------------------------------------
__fastcall TForm2::TForm2(TComponent* Owner)
	: TForm(Owner)
{
 CurrentPlayerLabel -> Caption =   Symbole  ;
}
//---------------------------------------------------------------------------
void __fastcall TForm2::ButtonClick(TObject *Sender)
{
	  TButton* ClickedButton = dynamic_cast<TButton*>(Sender) ;
	   ClickedButton->Caption=  Symbole  ;





			   if (Symbole == 'X' ) {

					Symbole =  ' O' ;

				  }
			 else
			  Symbole =  '  X' ;
			 CurrentPlayerLabel -> Caption =   Symbole  ;

				 if  ( CheckIsWinner() )
	 {
		  WinnerLabel -> Caption = " YOU WON ! " ;
		  return ;

	 }


}
//---------------------------------------------------------------------------
