var express = require('express');
var router = express.Router();
var exec = require('child_process').exec;


var scriptPath = '/scripts'

var snappsvisa = {
	name:"Snapsvisa",
  executionName:"Snapsa!",
	executable : 'echo "snapsvisa"',
	description : "Detta är snappsvisan.",
	api : 'snaps'
};

var checkStatus = {
	name:"Status Check",
  executionName:"check it out",
	executable : 'echo "Status Check"',
	description : "System status check.",
	api : 'status'
};

var toast = {
	name:"Toast",
  executionName:"fire in the hole",
	executable : 'echo "Toast pa g"',
	description : "Toasting what it is all about.",
	api : 'toast'
};

var intro = {
	name:"Intro",
  executionName:"Start",
	executable : 'echo "Intro Intro Intro"',
	description : "This is the introduction script",
	api : 'intro'
};

var Leif = {
	name:"Leif",
  executionName:"Leffe",
	executable : "cd ../rpi-rgb-led-matrix-master; sudo python intro_Leif.py",
	description : "Detta är leifs knapp.",
	api : 'leif'
};

var GunillaAnders = {
	name:"Gunilla och Anders",
  executionName:"Öppna Ridån",
	executable : 'echo "Gunilla och Anders"',
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
			console.log(`Running ${functions[index].name} executable ${functions[index].executable}`)
      exec(`${functions[index].executable}`, function callback(error, stdout, stderr){
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
