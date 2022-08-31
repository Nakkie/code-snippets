function onOpen(e) {

// update script menu with options
  var ui = SpreadsheetApp.getUi()
  ui.createMenu('Scripts')
    .addItem('Multi-select for this cell...', 'showDialog')
    .addItem('Replace value with link', 'swapValueForFormula')
    .addItem('Update DB...', 'updateDB')
    .addSubMenu(
      ui.createMenu('Developer Tools')
      .addItem('SOSN LU Update','combinedSOSN')
      .addItem('INDI LU Update','combinedINDI')
      .addItem('PSSN LU Update','combinedPSSN')
      .addItem('Programme LU Update','combinedProgram')
      .addItem('Policy LU Update','combinedPol')
      )
    .addToUi();

// run lookup scripts on open
  combinedSOSN();
  combinedINDI();
  combinedProgram();
  combinedPol();
  combinedPSSN();
}
