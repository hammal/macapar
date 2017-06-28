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
	executable : `sudo python snappsvisa1.py`,
	description : "Detta är snappsvisan.",
	api : 'snaps'
};

var checkStatus = {
	name:"Status Check",
  executionName:"check it out",
	executable : `sudo python checkstatus.py`,
	description : "System status check.",
	api : 'status'
};

var toast = {
	name:"Toast",
  executionName:"fire in the hole",
	executable : `sudo python toast.py`,
	description : "Toasting what it is all about.",
	api : 'toast'
};

var intro = {
	name:"Intro",
  executionName:"Start",
	executable : 'sudo python run_emojis.py',
	description : "This is the introduction script",
	api : 'intro'
};

var antikrundan = {
	name:"Antikrundan",
	executionName: "Kör",
	executable: "sudo python intro_sas.py",
	description: "Antikrundan scriptet.",
	api: "antikrundan"
}

var Leif = {
	name:"Leif",
  executionName:"Leffe",
	executable : `sudo python intro_Leif.py`,
	description : "Detta är leifs knapp.",
	api : 'leif'
};

var GunillaAnders = {
	name:"Gunilla och Anders",
  executionName:"Öppna Ridån",
	executable : `sudo python intro_AoG2.py`,
	description : "Gunilla och Anders intro.",
	api : 'gunillaochanders'
};

var TextArgument = {
	name: "Display Text",
	executionName: "Submit",
	executable: "sudo python textFranHTML.py",
	description: "Submit text to display.",
	api: "textArgument",
	argument: "Put text here"
};

var Slumpen = {
	name: "Slumpgenerator",
	executionName: "Slumpa",
	executable: "sudo python intro_slump.py",
	description: "Slumpgenerera följande namn.",
	api: "slumpGenerator",
	argument: "Namn"
}

var restart = {
	name:"Restart",
	executionName:"Now",
	executable: "sudo reboot now",
	description: "This button restarts the RPi for the display",
	api: "restart"
};

var shutdown = {
	name:"Shutdown",
	executionName:"Now",
	executable: "sudo shutdown -h now",
	description: "This button turns the RPi off safely",
	api: "shutdown"
};

var functions = [
	snappsvisa,
  checkStatus,
  toast,
  intro,
  Leif,
	antikrundan,
  GunillaAnders,
	TextArgument,
	Slumpen
	// restart
	// shutdown
];


/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'MacapÄär', functions: functions});
});

router.get('/scripts/:name', function(req, res) {
  for(index in functions) {
    if( functions[index].api == req.params.name){
			mutex.timedLock(5000, function (error) {
    		if (error) {
        	console.log('Could not get the lock within 5 seconds, so gave up');
    		} else {
    			console.log('We got the lock!');
    			// do stuff
					console.log(`Running ${functions[index].name} executable ${functions[index].executable}`)
      		exec(`${preExecution} ${functions[index].executable} `, function callback(error, stdout, stderr){
        		if (error) {
            	console.error(`exec error: ${error}`);
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


router.post('/scripts/:name', function(req, res) {
	for(index in functions) {
		if( functions[index].api == req.params.name){
			mutex.timedLock(5000, function (error) {
				if (error) {
					console.log('Could not get the lock within 5 seconds, so gave up');
				} else {
					console.log('We got the lock!');
					console.log('At time')
					// do stuff
					console.log(`Running ${functions[index].name} executable ${functions[index].executable} "${req.body.argument}"`)
					exec(`${preExecution} ${functions[index].executable} "${req.body.argument}"`, function callback(error, stdout, stderr){
						if (error) {
							console.error(`exec error: ${error}`);
						}
						console.log(`stdout: ${stdout}`);
						// console.log(`stderr: ${stderr}`);
						mutex.unlock();
					});
				};
			});
		res.redirect('/')
		};
	}
});

module.exports = router;
