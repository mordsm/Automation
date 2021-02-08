   function openContextMenu(element) {
      var contextMenu = document.createElement("div");
      contextMenu.addEventListener('mouseleave', e => {
        closeContextMenu(element.id);
      });
      contextMenu.classList.add('context-menu');
      contextMenu.classList.add('shadow-32');
      contextMenu.id = 'context-menu';
      contextMenu.style.top = element.offsetTop + "px";
      contextMenu.style.left = element.offsetLeft + "px";
      contextMenu.innerHTML = `
            <a href="">
            <div>
            Run now
        </div>
        </a>
            <a href="">
            <div>
            View schedule
        </div>
        </a>
            <a href="../processreport">
            <div>
            View report
        </div>
        </a>
            <a href="">
            <div>
            View script
        </div>
        </a>
        `;
      document.getElementById(element.id).parentElement.append(contextMenu);
    }

    function closeContextMenu(elementId) {
      if (document.getElementById('context-menu'))
        document.getElementById('context-menu').remove();
    }


    function toggleDialog() {
      document.getElementById('error_dialog_container_id').classList.toggle('open');
    }
function  startDictation(){

      if (window.hasOwnProperty('webkitSpeechRecognition')) {

        var recognition = new webkitSpeechRecognition();
        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.lang = "he-IL";
        recognition.start();
        recognition.onresult = function(e) {
          document.getElementById('transcript').value
                                   = e.results[0][0].transcript;
          recognition.stop();
          //document.getElementById(form_id).submit();
            $.ajax({ url: "tree_command",
                context: document.body,
                success: function(){
                   alert("done");
        }});

        };

        recognition.onerror = function(e) {
          recognition.stop();
        }

      }
    }
    function toast() {
      let toastElement = document.getElementById('toast_id');
      toastElement.classList.toggle('show');
      setTimeout(() => {
        toastElement.classList.toggle('show');
      }, 3000);
    }