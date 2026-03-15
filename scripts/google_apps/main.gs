function onOpen() {
  const ui = SpreadsheetApp.getUi();
  initGithubMenu_(ui);
  initSheetsMenu_(ui);
}
