// =============================================================================
// Spreadsheet sync scripts
//
// Config sheet: "config.sheets"
// Columns: Sheet | Source Sheet | Public Sheet ID | Enabled | Last Download | Last Upload
// "Sheet" is the local sheet name.
// "Source Sheet" is the sheet name in the public spreadsheet.
// "Public Sheet ID" is the spreadsheet ID of the target public spreadsheet.
// =============================================================================

const SHEETS_CONFIG_SHEET = "config.sheets";

// Fallback map: local sheet name → { sourceSheet, publicId }
const SS_SHEET_MAP = {
  // "sidebar": { sourceSheet: "sidebar", publicId: "YOUR_PUBLIC_SHEET_ID" },
};

let _ssSheetMap = null;

function getSsSheetMap_() {
  if (_ssSheetMap) return _ssSheetMap;

  const config = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(SHEETS_CONFIG_SHEET);
  if (config) {
    const map = {};
    const rows = config.getDataRange().getValues().slice(1);
    for (const [sheet, sourceSheet, publicId, enabled] of rows) {
      if (sheet && sourceSheet && publicId && String(enabled).trim().toUpperCase() === "TRUE") {
        map[String(sheet).trim()] = {
          sourceSheet: String(sourceSheet).trim(),
          publicId:    String(publicId).trim(),
        };
      }
    }
    _ssSheetMap = map;
  } else {
    _ssSheetMap = SS_SHEET_MAP;
  }

  return _ssSheetMap;
}

// ---------------------------------------------------------------------------
// Buttons
// ---------------------------------------------------------------------------

function pushAll() {
  const map = getSsSheetMap_();
  const privateId = SpreadsheetApp.getActiveSpreadsheet().getId();
  try {
    for (const [localSheet, { sourceSheet, publicId }] of Object.entries(map)) {
      syncSheetReplace(privateId, localSheet, publicId, sourceSheet);
      setSsStatus_(localSheet, "upload");
    }
  } catch (e) {
    alert_(e.message);
  }
}

function pullAll() {
  const map = getSsSheetMap_();
  const privateId = SpreadsheetApp.getActiveSpreadsheet().getId();
  try {
    for (const [localSheet, { sourceSheet, publicId }] of Object.entries(map)) {
      syncSheetReplace(publicId, sourceSheet, privateId, localSheet);
      setSsStatus_(localSheet, "download");
    }
  } catch (e) {
    alert_(e.message);
  }
}

function pushCurrent() {
  const localSheet = SpreadsheetApp.getActiveSheet().getName();
  const entry      = getSsSheetMap_()[localSheet];

  if (!entry) {
    alert_(`"${localSheet}" is not in the sheet map.`);
    return;
  }

  try {
    const privateId = SpreadsheetApp.getActiveSpreadsheet().getId();
    syncSheetReplace(privateId, localSheet, entry.publicId, entry.sourceSheet);
    setSsStatus_(localSheet, "upload");
  } catch (e) {
    alert_(e.message);
  }
}

function pullCurrent() {
  const localSheet = SpreadsheetApp.getActiveSheet().getName();
  const entry      = getSsSheetMap_()[localSheet];

  if (!entry) {
    alert_(`"${localSheet}" is not in the sheet map.`);
    return;
  }

  try {
    const privateId = SpreadsheetApp.getActiveSpreadsheet().getId();
    syncSheetReplace(entry.publicId, entry.sourceSheet, privateId, localSheet);
    setSsStatus_(localSheet, "download");
  } catch (e) {
    alert_(e.message);
  }
}

function reloadSsConfig() {
  initSheetsConfig_();
  _ssSheetMap = null;
  getSsSheetMap_();
}

function initSheetsMenu_(ui) {
  ui.createMenu("Sheets Sync")
    .addItem("Pull Sheet",  "pullCurrent")
    .addItem("Push Sheet",  "pushCurrent")
    .addSeparator()
    .addItem("Pull All Sheets",      "pullAll")
    .addItem("Push All Sheets",      "pushAll")
    .addSeparator()
    .addItem("Reload Config", "reloadSsConfig")
    .addToUi();
}

// ---------------------------------------------------------------------------
// Private
// ---------------------------------------------------------------------------

function alert_(message) {
  SpreadsheetApp.getUi().alert(`Error: ${message}`);
}

// Columns: Sheet(1) | Source Sheet(2) | Public Sheet ID(3) | Enabled(4) | Last Download(5) | Last Upload(6)
function setSsStatus_(sheetName, direction) {
  const config = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(SHEETS_CONFIG_SHEET);
  if (!config) return;

  const data = config.getDataRange().getValues();
  for (let i = 1; i < data.length; i++) {
    if (String(data[i][0]).trim() === sheetName) {
      const col = direction === "download" ? 5 : 6;
      config.getRange(i + 1, col).setValue(new Date());
      return;
    }
  }
}

// Creates the config.sheets sheet with headers if it doesn't exist.
function initSheetsConfig_() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  if (ss.getSheetByName(SHEETS_CONFIG_SHEET)) return;
  const sheet = ss.insertSheet(SHEETS_CONFIG_SHEET);
  sheet.appendRow(["Sheet", "Source Sheet", "Public Sheet ID", "Enabled", "Last Download", "Last Upload"]);
  sheet.setFrozenRows(1);
}
