// ---------------------------------------------------------------------------
// Pull GitHub CSV
// ---------------------------------------------------------------------------

/**
 * Fetches a CSV from GitHub and replaces the target sheet entirely.
 *
 * @param {string} csvUrl    - Raw URL to the CSV (e.g. raw.githubusercontent.com/...)
 * @param {string} sheetName - Sheet tab to write into (created if missing).
 * @param {string} [token]   - GitHub personal access token (for private repos).
 */
function downloadReplace(csvUrl, sheetName, token) {
  const rows = fetchCsv_(csvUrl, token);
  const sheet = getOrCreateSheet_(sheetName);

  sheet.clearContents();
  sheet.getRange(1, 1, rows.length, rows[0].length).setValues(rows);

  Logger.log(`downloadReplace: wrote ${rows.length} rows to "${sheetName}".`);
}


// ---------------------------------------------------------------------------
// Push GitHub CSV
// ---------------------------------------------------------------------------

/**
 * Uploads a sheet's contents to GitHub as a CSV, creating or updating the file.
 *
 * @param {string} sheetName  - Sheet tab to read from.
 * @param {string} repoOwner  - GitHub username or org.
 * @param {string} repoName   - Repository name.
 * @param {string} filePath   - Path inside the repo (e.g. ".data/sidebar.csv").
 * @param {string} token      - GitHub personal access token (needs contents: write).
 * @param {string} [branch]   - Branch to commit to (default: "main").
 * @param {string} [message]  - Commit message (default: auto-generated).
 */
function uploadSheet(sheetName, repoOwner, repoName, filePath, token, branch, message) {
  branch  = branch  || "main";
  message = message || `Update ${filePath} from Google Sheets`;

  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(sheetName);
  if (!sheet) throw new Error(`Sheet not found: "${sheetName}"`);

  const csv    = sheetToCsv_(sheet);
  const base64 = Utilities.base64Encode(Utilities.newBlob(csv).getBytes());
  const apiUrl = `https://api.github.com/repos/${repoOwner}/${repoName}/contents/${filePath}`;
  const headers = { Authorization: `token ${token}`, Accept: "application/vnd.github+json" };

  // Get current file SHA (required by GitHub API to update an existing file)
  let sha;
  const getResp = UrlFetchApp.fetch(`${apiUrl}?ref=${branch}`, {
    headers,
    muteHttpExceptions: true,
  });
  if (getResp.getResponseCode() === 200) {
    sha = JSON.parse(getResp.getContentText()).sha;
  } else if (getResp.getResponseCode() !== 404) {
    throw new Error(`GitHub GET failed (${getResp.getResponseCode()}): ${getResp.getContentText()}`);
  }

  const body = { message, content: base64, branch };
  if (sha) body.sha = sha;

  const putResp = UrlFetchApp.fetch(apiUrl, {
    method: "put",
    headers,
    contentType: "application/json",
    payload: JSON.stringify(body),
    muteHttpExceptions: true,
  });

  const status = putResp.getResponseCode();
  if (status !== 200 && status !== 201) {
    throw new Error(`GitHub PUT failed (${status}): ${putResp.getContentText()}`);
  }

  Logger.log(`uploadSheet: "${sheetName}" → ${repoOwner}/${repoName}/${filePath} on ${branch}.`);
}

// ---------------------------------------------------------------------------
// Sync Spreadsheets
// ---------------------------------------------------------------------------

/**
 * Copies a sheet from the source spreadsheet to the target, replacing contents.
 *
 * @param {string} sourceId    - Spreadsheet ID to read from.
 * @param {string} sourceSheet - Sheet name in the source spreadsheet.
 * @param {string} targetId    - Spreadsheet ID to write to.
 * @param {string} targetSheet - Sheet name in the target spreadsheet (created if missing).
 */
function syncSheetReplace(sourceId, sourceSheet, targetId, targetSheet) {
  const source = SpreadsheetApp.openById(sourceId).getSheetByName(sourceSheet);
  if (!source) throw new Error(`Sheet "${sourceSheet}" not found in source (${sourceId}).`);
 
  const ss     = SpreadsheetApp.openById(targetId);
  const target = ss.getSheetByName(targetSheet) || ss.insertSheet(targetSheet);
 
  const data = source.getDataRange().getValues();
  target.clearContents();
  target.getRange(1, 1, data.length, data[0].length).setValues(data);
}
 
// ---------------------------------------------------------------------------
// Private
// ---------------------------------------------------------------------------

function fetchCsv_(csvUrl, token) {
  const options = { muteHttpExceptions: true };
  if (token) options.headers = { Authorization: `token ${token}` };

  const response = UrlFetchApp.fetch(csvUrl, options);
  if (response.getResponseCode() !== 200) {
    throw new Error(`Failed to fetch CSV (HTTP ${response.getResponseCode()}): ${csvUrl}`);
  }
  return parseCsv_(response.getContentText());
}

function getOrCreateSheet_(sheetName) {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  return ss.getSheetByName(sheetName) || ss.insertSheet(sheetName);
}

function getToken_() {
  return PropertiesService.getScriptProperties().getProperty("GITHUB_TOKEN") || "";
}

function sheetToCsv_(sheet) {
  return sheet.getDataRange().getValues()
    .map((row) => row.map(csvEscapeField_).join(","))
    .join("\r\n");
}

function csvEscapeField_(value) {
  const str = String(value);
  return /[",\r\n]/.test(str) ? `"${str.replace(/"/g, '""')}"` : str;
}

function parseCsv_(text) {
  text = text.replace(/\r\n/g, "\n").replace(/\r/g, "\n").trimEnd();

  const rows = [];
  let row = [], field = "", inQuotes = false;

  for (let i = 0; i < text.length; i++) {
    const ch = text[i], next = text[i + 1];
    if (inQuotes) {
      if (ch === '"' && next === '"') { field += '"'; i++; }
      else if (ch === '"')            { inQuotes = false; }
      else                            { field += ch; }
    } else {
      if      (ch === '"')  { inQuotes = true; }
      else if (ch === ",")  { row.push(field); field = ""; }
      else if (ch === "\n") { row.push(field); rows.push(row); row = []; field = ""; }
      else                  { field += ch; }
    }
  }
  row.push(field);
  if (row.some((f) => f !== "")) rows.push(row);
  return rows;
}
