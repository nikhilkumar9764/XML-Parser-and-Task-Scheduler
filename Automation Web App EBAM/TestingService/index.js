const express = require('express');
var app = express();
var testDashboard = require('./Dashboard.js').testDashboard;

app.use(express.urlencoded());
app.use(express.json());


function onServerListening() {
    console.log('Server Started ');
}

/*
    Requests
    {
        "DashboardId" : "",
        "Timeout" : "",
        "URL" : "",
        "ScreenShot" : "Path" 
    }

    Response
    { 
        Metrics/Error

    }
*/
app.post('/testDashboard', async function (req, res) {

   
    console.log(req.body);
    let dashboardId = req.body['dashboardId'];
    let TimeOut = req.body['TimeOut'];
    let URL = req.body['URL'];

    console.log(dashboardId, TimeOut, URL);
    let resp = await testDashboard(dashboardId, TimeOut , URL);
    res.send(resp);
});




var server = app.listen(3000, '127.0.0.1', onServerListening);