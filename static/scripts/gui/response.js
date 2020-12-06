var toggleDialog = function() {
      document.getElementsByClassName('dialog-container')[0].classList.toggle('open');
};

var showTextResponse = function (the_text, element_id, callback) {
	var the_text_element = document.getElementById(element_id);
	the_text_element.innerHTML = the_text;
	callback();
};

var showErrorResponse = function (error_title, error_message) {
	var the_title = document.getElementById("error_title_id")
	the_title.innerHTML = error_title;
	error_message = error_message.replace(/^"(.*)"$/, '$1');
	showTextResponse(error_message, "error_text_id", toggleDialog);
};

var showSuccessResponse = function (success_message) {
	showTextResponse(success_message, "toast_text_id", toast);
};
