var import_process_func = function() {
	var file_input = document.getElementById("upload_file_id");
	file_input.click();	
};

var  import_process_func_process = function() {
	var form = document.getElementById('process_import_form_id');
	var formdata = new FormData(form);
	var file_input = document.getElementById("upload_file_id");
	file_input.value = "";
	$.ajax({
	    url: '/process/import/',
	    data: formdata,
	    type: 'POST',
	    contentType: false, // NEEDED, DON'T OMIT THIS (requires jQuery 1.6+)
	    processData: false, // NEEDED, DON'T OMIT THIS
	    success: function(response, textStatus, jqXHR){
	    	div_content('main_content_div', '/process/list/', init_processes_table);
	    },
	    error: function(qXHR, textStatus, errorThrown){
	    	showErrorResponse("File upload failed", qXHR.responseText)
	    }
	});
};

