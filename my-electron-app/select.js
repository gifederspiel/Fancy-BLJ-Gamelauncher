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
  con.query("SELECT * FROM playerdata", function (err, result, fields) {
    if (err) throw err;
    console.log(result);
  });
});