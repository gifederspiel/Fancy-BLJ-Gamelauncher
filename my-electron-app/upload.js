const electron = require('electron'); 
const path = require('path');
const fs = require('fs'); 
const {basename} = require('path')


// Importing dialog module using remote 
const dialog = electron.remote.dialog; 
  
var uploadFile = document.getElementById('custom-button'); 
  
// Defining a Global file path Variable to store  
// user-selected file 
global.filepath = undefined; 
  
uploadFile.addEventListener('click', () => { 
// If the platform is 'win32' or 'Linux' 
    if (process.platform !== 'darwin') { 
        // Resolves to a Promise<Object> 
        dialog.showOpenDialog({ 
            title: 'Select the File to be uploaded', 
            defaultPath: __dirname,
            buttonLabel: 'Upload', 
            // Restricting the user to only Text Files. 
            filters: [ 
                { 
                    name: 'Text Files', 
                    extensions: ['exe'] 
                }, ], 
            // Specifying the File Selector Property 
            properties: ['openFile'] 
        }).then(file => { 
            console.log(file.name)
            fs.copyFile(file.filePaths[0], __dirname + '\\games\\' + basename(file.filePaths[0]), (err) => {
                if (err) throw err;
                console.log(`${ basename(file.filePaths[0])} was copied to destination.txt`);
              });
        }).catch(err => { 
            console.log(err) 
        }); 
    } 
}); 