const {app, BrowserWindow} = require('electron')

function createWindow () {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
    nodeIntegration: true,
    enableRemoteModule: true

    }
  })
  win.loadFile('index.html')
}

app.whenReady().then(createWindow)

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow()
  }
})

var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "12345Root",
  database: "playerdata1",
  port: "3307"
});

con.connect(function(err) {
  if (err) throw err;
  con.query("SELECT * FROM playerdata ORDER BY score DESC LIMIT 5", function (err, result, fields) {
    if (err) throw err;
    console.log(result);
  });
});
console.log(app.getAppPath())
