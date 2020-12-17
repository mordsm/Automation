var recognition = new webkitSpeechRecognition();
var voices = null
var msg = new SpeechSynthesisUtterance();
msg.text = "good morning"
msg.rate = 0.8;
msg.pitch = 1;
msg.volume = 1;
msg.voiceURI = "native";
var first_time = true

window.onload = function() {

  console.log(location.href);
  //TODO consider return to voice activator
  var site_name = window.location.hostname.split(".")[1] // get site_name from url
  if (voices == null) {
    getVoices().then(function(val) {
      console.log(JSON.stringify(voices));
      voices = val;
      GM_setValue("voices", JSON.stringify(voices));
      console.log(GM_getValue("voices"));
    })
  }


  if (GM_getValue("request") &&
      GM_getValue("site_name") &&
      GM_getValue("site_name") == site_name
     ) {
    var script = JSON.parse(GM_getValue("actions"));
    var request = GM_getValue("request");
    var cmd_idx = parseInt(GM_getValue("index"));
    var i = findRequestIndex(script, request)
    if (cmd_idx == script[i].commands.length - 1) { //end of script
      return;
    }
    activateRequest(script[i], cmd_idx)
  } else {

    $.ajax({
      url: "http://127.0.0.1:8003/browser_request",
      method: "GET",
      data: {
        'action': site_name
      },
      dataType: 'json',
      context: site_name,
      success: function(data, textStatus) {

        GM_setValue("actions", JSON.stringify(Object.entries(data)[0][1]));
        var script = JSON.parse(GM_getValue("actions"));
        GM_setValue("request", "login");
        GM_setValue("index", 1);
        GM_setValue("site_name", site_name);
        //TODO when running straight from site openinig we start from second command
        //eval (script[0].commands[0]);
        activateRequest(script[0], 1)


      },
      fail: function(xhr, textStatus, errorThrown) {
        alert(errorThrown);
      }

    })

  }
};
var spacebar_pressed = false;



/*
document.onmusedown = function(event) {
    say ("document onmusedown");
    if (event.keyCode == 32) {
        spacebar_pressed = true;
        startDictation()

    };
};*/

document.onclick = function(event) {
  if (first_time && voices)
  {

    msg.voice = voices[2];
    say(msg.text);
    first_time = false;
  }

  if (event.keyCode == 32) {
    spacebar_pressed = true;
    startDictation()

  };
};

function debug(command) {
  console.log(document.url,document.title," - Current Command: ", command);
}

// activate all script commands from current position
function activateRequest(script, cmd_idx) {
  var pos = cmd_idx;
  for (var i = pos; i < script.commands.length; i++) {
    cmd_idx++;
    GM_setValue("index", cmd_idx);
    if (script.commands[i].includes("frame")) {
      i = script.commands.length;
    }
    debug(script.commands[i]);
    eval(script.commands[cmd_idx - 1]);
  }
}


function findRequestIndex(script, request) {
  for (var i = 0; i < script.length; i++) {
    if (script[i].name == request) {
      return i;
    }
  }
}


debug;
async function say(m) {
  //var msg = new SpeechSynthesisUtterance();
  msg.lang = "en-US";
  msg.text = m;
  try {
    /* msg.text = m
  //var voice = SpeechSynthesisVoice.class(voices[2])

  //voices = await getVoices();
  //var voice = GM_getValue("voices")[2];
  msg.rate = 0.8;
  msg.pitch = 1;
  msg.volume = 1;
  msg.lang = "en-US";
  //msg.voice = voices[2].__proto__;
  //msg.voice = (SpeechSynthesisVoice)(voices[2]);
  msg.voice = Object.assign(msg.voice, voices[2]);
  msg.voiceURI = "native";*/
    if (voices)
    {msg.voice = voices[2];}
    window.speechSynthesis.speak(msg);
    return true;
  } catch (err) {
    console.log(err)
    return false;
  }
  //var synth = window.speechSynthesis;
  //speechSynthesis.speak(msg);
}
async function get_user_answer(question) {
  try {
    msg.text = question;
    //window.jQuery("#userCode").click(say("testing"));
    //window.jQuery("#userCode").trigger("click" );
    //var elem = window.jQuery("#userCode")
    //elem.click();
    let said = await say(question);
    if (said)
    {
      while (true) {
        var transcript = await startDictation();
        if (transcript == "quit") {
          return null;
        }
        else
        { say("Did You  say : " + transcript + "? yes / no")
         var answer = await startDictation()
         if (answer == 'y' || answer == 'yes') {
           return transcript
         }
        }
      }
    }
    said = await say(question);
  } catch (err) {
    alert("get_user_answer : ", err);
    return null;
  }

}


const getVoices = () => {
  return new Promise((resolve) => {
    let voices = speechSynthesis.getVoices();
    if (voices.length) {
      resolve(voices);
      return;
    }
    speechSynthesis.onvoiceschanged = () => {
      console.log(JSON.stringify(voices));
      voices = speechSynthesis.getVoices();
      console.log(JSON.stringify(voices));
      resolve(voices);
    };
  });
};

function startDictation() {
  return new Promise(function(resolve, reject) {
    var $ = window.jQuery;
    //if (window.hasOwnProperty("webkitSpeechRecognition")) {
    var recognition = new webkitSpeechRecognition();
    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.lang = "he-IL";
    var d = recognition.stop();
    recognition.start();
    recognition.onresult = (event) => {
      const result = event.results[event.results.length - 1];
      if (result.isFinal) {
        $("#log").append("<br>" + result[0].transcript);
        resolve(result[0].transcript);
      }
    };
    setTimeout(() => {
      recognition.stop();
    }, 5000);

    recognition.onerror = function(e) {
      $("#log").append("<br/> error : " + e);
      recognition.stop();
    };
    //}

  });
}
recognition.continuous = true;

recognition.interimResults = true;

recognition.lang = 'en';

recognition.start();










