// =============================================================================
// GitHub sync scripts
//
// Script Properties:
//   GITHUB_TOKEN  - personal access token
//   GITHUB_OWNER  - GitHub username or org
//   GITHUB_REPO   - repository name
//   GITHUB_BRANCH - branch (default: "main")
//
// Config sheet: "config.github"
// Columns: Sheet | Path | Enabled | Last Download | Last Upload
// =============================================================================

const GITHUB_CONFIG_SHEET = "config.github";

// Fallback map used when no config sheet is present.
const SHEET_MAP = {
  "sidebar": "data/sidebar.csv"
};

let _sheetMap = null;

function getSheetMap_() {
  if (_sheetMap) return _sheetMap;

  const config = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(GITHUB_CONFIG_SHEET);
  if (config) {
    const map = {};
    const rows = config.getDataRange().getValues().slice(1);
    for (const [sheet, path, enabled] of rows) {
      if (sheet && path && String(enabled).trim().toUpperCase() === "TRUE") {
        map[String(sheet).trim()] = String(path).trim();
      }
    }
    _sheetMap = map;
  } else {
    _sheetMap = SHEET_MAP;
  }

  return _sheetMap;
}

// ---------------------------------------------------------------------------
// Buttons
// ---------------------------------------------------------------------------

function downloadAll() {
  const map = getSheetMap_();
  try {
    const token = getProp_("GITHUB_TOKEN");
    for (const [sheetName, filePath] of Object.entries(map)) {
      downloadReplace(rawUrl_(filePath), sheetName, token);
      setGithubStatus_(sheetName, "download");
    }
  } catch (e) {
    alert_(e.message);
  }
}

function uploadAll() {
  const map = getSheetMap_();
  try {
    const { token, owner, repo, branch } = getRepoProps_();
    for (const [sheetName, filePath] of Object.entries(map)) {
      uploadSheet(sheetName, owner, repo, filePath, token, branch);
      setGithubStatus_(sheetName, "upload");
    }
  } catch (e) {
    alert_(e.message);
  }
}

function downloadCurrent() {
  const sheetName = SpreadsheetApp.getActiveSheet().getName();
  const filePath  = getSheetMap_()[sheetName];

  if (!filePath) {
    alert_(`"${sheetName}" is not in the sheet map.`);
    return;
  }

  try {
    downloadReplace(rawUrl_(filePath), sheetName, getProp_("GITHUB_TOKEN"));
    setGithubStatus_(sheetName, "download");
  } catch (e) {
    alert_(e.message);
  }
}

function uploadCurrent() {
  const sheetName = SpreadsheetApp.getActiveSheet().getName();
  const filePath  = getSheetMap_()[sheetName];

  if (!filePath) {
    alert_(`"${sheetName}" is not in the sheet map.`);
    return;
  }

  try {
    const { token, owner, repo, branch } = getRepoProps_();
    uploadSheet(sheetName, owner, repo, filePath, token, branch);
    setGithubStatus_(sheetName, "upload");
  } catch (e) {
    alert_(e.message);
  }
}

function reloadConfig() {
  initGithubConfig_();
  _sheetMap = null;
  getSheetMap_();
}

function initGithubMenu_(ui) {
  ui.createMenu("GitHub")
    .addItem("Pull Sheet", "downloadCurrent")
    .addItem("Push Sheet",   "uploadCurrent")
    .addSeparator()
    .addItem("Pull All Sheets",     "downloadAll")
    .addItem("Push All Sheets",       "uploadAll")
    .addSeparator()
    .addItem("Reload Config",    "reloadConfig")
    .addToUi();
}

// ---------------------------------------------------------------------------
// Private
// ---------------------------------------------------------------------------

function getRepoProps_() {
  return {
    token:  getProp_("GITHUB_TOKEN"),
    owner:  getProp_("GITHUB_OWNER"),
    repo:   getProp_("GITHUB_REPO"),
    branch: getProp_("GITHUB_BRANCH") || "main",
  };
}

function getProp_(key) {
  const value = PropertiesService.getScriptProperties().getProperty(key);
  if (!value) throw new Error(`Missing script property: ${key}`);
  return value;
}

function rawUrl_(filePath) {
  const { owner, repo, branch } = getRepoProps_();
  return `https://raw.githubusercontent.com/${owner}/${repo}/${branch}/${filePath}`;
}

function alert_(message) {
  SpreadsheetApp.getUi().alert(`Error: ${message}`);
}

// Columns: Sheet(1) | Path(2) | Enabled(3) | Last Download(4) | Last Upload(5)
function setGithubStatus_(sheetName, direction) {
  const config = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(GITHUB_CONFIG_SHEET);
  if (!config) return;

  const data = config.getDataRange().getValues();
  for (let i = 1; i < data.length; i++) {
    if (String(data[i][0]).trim() === sheetName) {
      const col = direction === "download" ? 4 : 5;
      config.getRange(i + 1, col).setValue(new Date());
      return;
    }
  }
}

// Creates the config.github sheet with headers if it doesn't exist.
function initGithubConfig_() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  if (ss.getSheetByName(GITHUB_CONFIG_SHEET)) return;
  const sheet = ss.insertSheet(GITHUB_CONFIG_SHEET);
  sheet.appendRow(["Sheet", "Path", "Enabled", "Last Download", "Last Upload"]);
  sheet.setFrozenRows(1);
}
