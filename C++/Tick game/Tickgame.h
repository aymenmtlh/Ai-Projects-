//---------------------------------------------------------------------------

#ifndef TickgameH
#define TickgameH
//---------------------------------------------------------------------------
#include <System.Classes.hpp>
#include <Vcl.Controls.hpp>
#include <Vcl.StdCtrls.hpp>
#include <Vcl.Forms.hpp>
//---------------------------------------------------------------------------
class TForm2 : public TForm
{
__published:	// IDE-managed Components
	TButton *Button1;
	TButton *Button5;
	TButton *Button3;
	TButton *Button4;
	TButton *Button2;
	TButton *Button6;
	TButton *Button8;
	TButton *Button9;
	TButton *Button7;
	TLabel *Label1;
	TLabel *CurrentPlayerLabel;
	TLabel *WinnerLabel;
	void __fastcall ButtonClick(TObject *Sender);
private:
bool TForm2 ::  CheckIsWinner()   ;
	// User declarations
public:		// User declarations
	__fastcall TForm2(TComponent* Owner);
};
//---------------------------------------------------------------------------
extern PACKAGE TForm2 *Form2;
//---------------------------------------------------------------------------
#endif
