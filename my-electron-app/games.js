let games = []
const app = require('electron')
function Process(filename) {
const process = require('child_process');
var ls = process.spawn(`games\\${filename}`);
ls.stdout.on('data', function (data) {
  console.log(data);
});
ls.stderr.on('data', function (data) {
  console.log(data);
});
ls.on('close', function (code) {
    if (code == 0)
        console.log('Stop');
    else
        console.log('Start');
  });
};
let gamelist = document.getElementById('gamelist')
fs.readdirSync(__dirname + '\\games').forEach(file => {
    console.log(file);
    games.push(file);
    gamelist.innerHTML += `<li><button class="startbutton" type="button" id="${file}">${file}</button></li><br>`;
    
  });
games.forEach(game => {
    document.getElementById(game).addEventListener('click', (event) => {
    Process(game);
  })
})