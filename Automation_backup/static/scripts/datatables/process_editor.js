var init_process_editor = function() {

	 var startval = JSON.parse(document.getElementById("script-backup").innerHTML);
     var schema = JSON.parse(document.getElementById("schema-holder").innerHTML);
     var url = document.getElementById("url-holder").value;

     var change_count = 0;
     var editor = new JSONEditor(document.getElementById('editor_holder'),{
       display_required_only: true,
       show_opt_in: true,
       theme: 'spectre',
       schema: schema
     });     
     editor.setValue(startval);

	var csrftoken = getCookie('csrftoken'); 
	var responseel = document.getElementById('response');
 
      // Hook up the save button to log to the console
      document.getElementById('save').addEventListener('click',function() {
        // Get the value from the editor
         $.ajax({
			type: 'POST',
			headers: { 'X-CSRFToken': csrftoken, "Content-type": "application/json;charset=UTF-8"},
			url: url,
			data: JSON.stringify(editor.getValue()),
			success: function(response){
//				alert(response)
				editor.setValue(JSON.parse(response));
				document.getElementById('script-backup').innerHTML = response;
				change_count = 0;
				},
			error: function(response) {
				responseel.innerHTML = JSON.parse(response);
				responseel.style.display = "block";
				}
			})
      });
      // Hook up the clear button
      document.getElementById('clear').addEventListener('click',function() {
        // Clear the value from the editor
        editor.setValue({});
      });
	  if (startval != null) {
	      editor.setValue(startval);
	      // Hook up the restore button
	      document.getElementById('restore').addEventListener('click',function() {
	        var backup = document.getElementById('script-backup')
	        editor.setValue(startval);
	       });
      };
      
      editor.on('change',function() {
		  change_count++;
	  });
      
      window.onbeforeunload = function(){
          if(change_count > 1) {
		  	return 'Are you sure you want to leave?';
		  }
		};
};
