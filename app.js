// we use express and multer libraries to send images
const express = require('express');
const multer = require('multer');
const server = express();
const PORT = 3000;
const {spawn} = require('child_process');

// uploaded images are saved in the folder "/upload_images"
const upload = multer({dest: __dirname + '/upload_images'});

server.use(express.static('public'));

// "myfile" is the key of the http payload
server.post('/', upload.single('myfile'), function(request, respond) {
  if(request.file) console.log(request.file);
  console.log("Uploading " + request.file.originalname + " to S3")
  const python = spawn('python', ['/home/ubuntu/s3_uploader/s3_data_mover.py', request.file.originalname]);
  //spawn('python', ['/home/ubuntu/s3_uploader/s3_data_mover.py']);
  
  // save the image
  var fs = require('fs');
  fs.rename(__dirname + '/upload_images/' + request.file.filename, __dirname + '/upload_images/' + request.file.originalname, function(err) {
    if ( err ) console.log('ERROR: ' + err);
  });

  respond.end(request.file.originalname + ' uploaded!');
});

// You need to configure node.js to listen on 0.0.0.0 so it will be able to accept connections on all the IPs of your machine
const hostname = '0.0.0.0';
server.listen(PORT, hostname, () => {
    console.log(`Server running at http://${hostname}:${PORT}/`);
  });