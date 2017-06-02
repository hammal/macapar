var express = require('express');
var router = express.Router();
var exec = require('child_process').exec;


var scriptPath = '/scripts'

var snappsvisa = {
	name:"Snapsvisa",
  executionName:"Snapsa!",
	pythonScript : "abs.py",
	description : "Detta är snappsvisan.",
	api : 'snaps'
};

var checkStatus = {
	name:"Status Check",
  executionName:"check it out",
	pythonScript : "helloworld.py",
	description : "System status check.",
	api : 'status'
};

var toast = {
	name:"Toast",
  executionName:"fire in the hole",
	pythonScript : "helloworld.py",
	description : "Toasting what it is all about.",
	api : 'toast'
};

var intro = {
	name:"Intro",
  executionName:"Start",
	pythonScript : "helloworld.py",
	description : "This is the introduction script",
	api : 'intro'
};

var Leif = {
	name:"Leif",
  executionName:"Leffe",
	pythonScript : "helloworld.py",
	description : "Detta är leifs knapp.",
	api : 'leif'
};

var GunillaAnders = {
	name:"Gunilla och Anders",
  executionName:"Öppna Ridån",
	pythonScript : "helloworld.py",
	description : "Gunilla och Anders intro.",
	api : 'gunillaochanders'
};

var functions = [
	snappsvisa,
  checkStatus,
  toast,
  intro,
  Leif,
  GunillaAnders
];


/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'MacapÄär', functions: functions});
});

router.get('/scripts/:name', function(req, res) {
  for(index in functions) {
    if( functions[index].api == req.params.name){
      exec(`echo ${functions[index].pythonScript}`, function callback(error, stdout, stderr){
        if (error) {
            console.error(`exec error: ${error}`);
            return;
          }
          console.log(`stdout: ${stdout}`);
          // console.log(`stderr: ${stderr}`);
      });
      res.redirect('/')
    }
  }
});

module.exports = router;
