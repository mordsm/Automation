    // Initialize the editor with a JSON schema
    var startval = JSON.parse(document.getElementById('script-backup').textContent);
    var the_schema = JSON.parse(document.getElementById('schema-data').textContent);
    var change_count = 0;
    var editor = new JSONEditor(document.getElementById('editor_holder'),{
      display_required_only: true,
      show_opt_in: true,
      theme: 'spectre',
      schema: the_schema
    });
    
    editor.setValue(startval);

	var csrftoken = getCookie('csrftoken'); 
	var responseel = document.getElementById('response');
	var ajax_url = document.getElementById('ajax_url_id').innerHTML;
     // Hook up the save button to log to the console
     document.getElementById('save').addEventListener('click',function() {
       // Get the value from the editor
        $.ajax({
			type: 'POST',
			headers: { 'X-CSRFToken': csrftoken, "Content-type": "application/json;charset=UTF-8"},
			url: ajax_url,
			data: JSON.stringify(editor.getValue()),
			success: function(response, textStatus, jqXHR){
//				alert(response)
				editor.setValue(JSON.parse(response));
				document.getElementById('script-backup').innerHTML = response;
				change_count = 0;
				showSuccessResponse("Script Updated " + response);
				},
			error: function(qXHR, textStatus, errorThrown) {
				showErrorResponse("Script Not Updated!", errorThrown);
				}
			})
     });
     // Hook up the clear button
     // Hook up the restore button
     document.getElementById('cancel').addEventListener('click',function() {
       var backup = document.getElementById('script-backup')
       editor.setValue(JSON.parse(backup.innerHTML));
      });
     
     editor.on('change',function() {
		  change_count++;
	  });
     
     window.onbeforeunload = function(){
         if(change_count > 1) {
		  	return 'Are you sure you want to leave?';
		  }
		};
