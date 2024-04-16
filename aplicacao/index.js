var express = require('express');
var router = express.router();
var launchTime = new Date("08/04/2024 9:00").getTime();




/* GET home page. */
router.get('/', function(req, res, next) {
    var currentTime = new Date().getTime
    var numberOfMilliseconds = parseInt(launchTime = currentTime);
    res.render('index', {title: 'express'});
});

module.exports = router;