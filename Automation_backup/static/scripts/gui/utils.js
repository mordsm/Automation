
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
	}
    return cookieValue;
};

function toLocalTime(dateStr) {
	var tz = Intl.DateTimeFormat().resolvedOptions().timeZone;
	return new Date(dateStr).toLocaleString({timeZone: tz});
};


var error_response = function(data){
    $('.api-response').html("API Response: " + data.status + ' ' + data.statusText + '<br/>Content: ' + data.responseText);
};

var susccess_response = function(data){
    $('.api-response').html("API Response: OK<br/>Content: " + JSON.stringify(data));
};
  

var init_success_error_response = function(){
    $('form.ajax-post button[type=submit]').click(function(){
      var form = $('form.ajax-post');
      $.post(form.attr('action'), form.serialize())
      .fail(function(data){error_response(data);})
      .done(function(data){susccess_response(data);});
      return false;
    });
    $("#ContainsProcessesModal").modal('show');
     $(".local-time").each(function(i,v){$(v).html(toLocalTime($(v).text()));});
 };

 function addEvent(obj, evType, fn){ 
	 if (obj.addEventListener){ 
	   obj.addEventListener(evType, fn, false); 
	   return true; 
	 } else if (obj.attachEvent){ 
	   var r = obj.attachEvent("on"+evType, fn); 
	   return r; 
	 } else { 
	   return false; 
	 } 
	};
	
	addEvent(window, 'load', init_success_error_response);
	
  function div_content(div_id, url, call_back = null, type = 'GET') {
	  $.ajax({
		  beforeSend: function(xhr, settings){
			  xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
		  },
		  type: type,
		  url: url,
		  data: {},
		  success: function(response) {
			  document.getElementById(div_id).innerHTML = response;
			  if(call_back != null) {				  
				  call_back();
			  }
		  }
	  });
  }
  
  function clear_div_content(div_id = "main_content_div") {
	  $(document.getElementById(div_id)).empty();
	  set_breadcrumbs()
  }
	
  function toggle_handler(result_element_id, url) {
   	 var csrftoken = getCookie('csrftoken')
        $.ajax({
			type: 'POST',
			headers: { 'X-CSRFToken': csrftoken, "Content-type": "application/json;charset=UTF-8"},
			url: url,
			data: '{}',
			success: function(response){
				document.getElementById(result_element_id).innerHTML = response;
				},
			})
     };
	
	function format_date(data, type, full) {
		if (data == null || data == "") {
			return data;
		}
		return new Date(data).toLocaleString()
	};

	function toggle_details(el){
		if (el.parent('tr').hasClass('shown')) {
			el.parent('tr').removeClass('shown');
		} else {
			el.parent('tr').addClass('shown');
		}
	};
	
	function back_to(url) {
		  if (window.history && window.history.pushState) {
		    window.history.pushState('forward', null, null);
		    $(window).on('popstate', function () {
		      window.location.href = url;
		    });
		  }
		};
		
	function trigger_element_event(selector, event_name) {
		$(selector).trigger(event_name);
	}
	
	function format(str) {
	    var args = [].slice.call(arguments, 1),
	        i = 0;

	    return str.replace(/%s/g, () => args[i++]);
	};

	function execute_function_by_name(functionName, context /*, args */) {
		  var args = Array.prototype.slice.call(arguments, 2);
		  var namespaces = functionName.split(".");
		  var func = namespaces.pop();
		  for(var i = 0; i < namespaces.length; i++) {
		    context = context[namespaces[i]];
		  }
		  return context[func].apply(context, args);
		}
	