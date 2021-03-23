'use strict';

const express = require('express');

// Constants
const PORT = 9000;
const HOST = '0.0.0.0';

const app = express();

app.post('/initialize', (req, res) => {
  // console.log(JSON.stringify(req.headers));
  var rid = req.headers['x-fc-request-id']
  console.log(`FC Initialize Start RequestId: ${rid}`)
  // do your things
  res.send('Hello FunctionCompute, initialize \n');
  console.log(`FC Initialize End RequestId: ${rid}`)
});

// invocation
app.post('/invoke', (req, res) => {
  // console.log(JSON.stringify(req.headers));
  var rid = req.headers['x-fc-request-id']
  console.log(`FC Invoke Start RequestId: ${rid}`)
  // get body to do your things
  res.send('Hello World');
  console.log(`FC Invoke End RequestId: ${rid}`)
});

var server = app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);

server.timeout = 0; // never timeout
server.keepAliveTimeout = 0; // keepalive, never timeout
