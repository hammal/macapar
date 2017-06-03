var express = require('express');
var router = express.Router();
var exec = require('child_process').exec;
var locks = require('locks');

var mutex = locks.createMutex();

var scriptPath = '/scripts';
var preExecution = "cd ../rpi-rgb-led-matrix-master;";

var snappsvisa = {
	name:"Snapsvisa",
  executionName:"Snapsa!",
	executable : `${preExecution} sudo python snappsvisa1.py`,
	description : "Detta är snappsvisan.",
	api : 'snaps'
};

var checkStatus = {
	name:"Status Check",
  executionName:"check it out",
	executable : `${preExecution} sudo python checkstatus.py`,
	description : "System status check.",
	api : 'status'
};

var toast = {
	name:"Toast",
  executionName:"fire in the hole",
	executable : `${preExecution} sudo python toast.py`,
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
	executable : `${preExecution} sudo python intro_Leif.py`,
	description : "Detta är leifs knapp.",
	api : 'leif'
};

var GunillaAnders = {
	name:"Gunilla och Anders",
  executionName:"Öppna Ridån",
	executable : `${preExecution} sudo python intro_AoG2.py`,
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
			mutex.timedLock(30000, function (error) {
    		if (error) {
        	console.log('Could not get the lock within 5 seconds, so gave up');
    		} else {
    			console.log('We got the lock!');
    			// do stuff
					console.log(`Running ${functions[index].name} executable ${functions[index].executable}`)
      		exec(`${functions[index].executable}`, function callback(error, stdout, stderr){
        		if (error) {
            	console.error(`exec error: ${error}`);
            	return;
          	}
          	console.log(`stdout: ${stdout}`);
          	// console.log(`stderr: ${stderr}`);
						mutex.unlock();
      		});
				};
			});
      res.redirect('/')
    }
  }
});

module.exports = router;
