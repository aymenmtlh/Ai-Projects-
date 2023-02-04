//---------------------------------------------------------------------------

#include <vcl.h>
#pragma hdrstop

#include "Unit2.h"
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.dfm"
int client = 0 ;
int gclient = 1 ;
TForm2 *Form2;

//---------------------------------------------------------------------------
__fastcall TForm2::TForm2(TComponent* Owner)
	: TForm(Owner)
{
}
//---------------------------------------------------------------------------
void __fastcall TForm2::Button1Click(TObject *Sender)
{
	 client ++   ;
	Label2->Caption= client ;
}
//---------------------------------------------------------------------------
void __fastcall TForm2::Button2Click(TObject *Sender)
{
	   if(!Label2->Caption.IsEmpty() && Label2->Caption>Label4->Caption )

	   { gclient++ ;
		 client -- ;
	   }
	   Label4->Caption=gclient ;
	  Label6-> Caption = 1  ;

}
//---------------------------------------------------------------------------
void __fastcall TForm2::Button3Click(TObject *Sender)
{
        if(!Label2->Caption.IsEmpty() && Label2->Caption>Label4->Caption )

	   { gclient++ ;
		 client -- ;
	   }
	   Label4->Caption=gclient ;
	  Label6-> Caption = 2 ;

}
//---------------------------------------------------------------------------
void __fastcall TForm2::Button4Click(TObject *Sender)
{
 if(!Label2->Caption.IsEmpty() && Label2->Caption>Label4->Caption )

	   { gclient++ ;
		 client -- ;
	   }
	   Label4->Caption=gclient ;
	  Label6-> Caption = 3 ;

}
//---------------------------------------------------------------------------

