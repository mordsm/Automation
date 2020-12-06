	//document.getElementById("timeDialog").style.visibility = "hidden";
	//document.getElementById("info").style.visibility = "hidden";

	$('#schedule-editor').on( "focusout",
		function(){ $('#schedule-editor').hide();});
	//minute.checked=true
	function show_dialog(){

		document.getElementById("timeDialog").style.display = "inline-block";
	    document.getElementById("choice").value = event.target.id

	}
    function get_schedule_processes_data(scheduele_id=null) {
 	   var processes = JSON.parse(document.getElementById("processes_data").value)
 	   var result = [];

 	   for (i = 0; i< processes.length; i++) {
 		   var p = processes[i];
 		   result.push({"value": p.id, "text": p.process_name + ' (' + p.url +')', "selected": (p.schedule__schedule_id == scheduele_id) && (scheduele_id!= null)})
 	   }
 	   return result;
    }
    function deleteSchedule(id) {

	var csrtoken = getCookie('csrftoken');

	$.ajax({
		url: "/schedule/delete/"+ id +"/",
		type: 'post',
		headers: {"X-CSRFToken": csrtoken},
		success: function(data) {
			$("#schedules-table").html(data);
			div_content('main_content_div', '/datatables/schedule_list/', init_schedules_table);
		},
		done: function(data) {
			$("#schedules-table").html(data);
			div_content('main_content_div', '/datatables/schedule_list/', init_schedules_table);
		}

	});
	//event.stopPropagation();
	};
    function submit_schedule_edit() {
    	event.stopPropagation();
		event.preventDefault();
        if ($("#submit-button").val() == "Save")
        	url = "/schedule/update/" + $("#id-input").val()
        else
        	url = "/schedule/add/"
        $.ajax({
            url: url,
            type: 'POST',
            data : $('#row-edit-form').serialize(),
            success: function(data){
				div_content('main_content_div', '/datatables/schedule_list/', init_schedules_table);
			  },
            fail: function(response) {
             alert("ERROR");	
            }
          });

    };

    function cnacelPeriod(event)
	{
		event.stopPropagation();
		event.preventDefault();
		document.getElementById("timeDialog").style.display = "none";
	}
	function show_editor(add=false) {
		editor= document.getElementById("schedule-editor")
		$("#period-input").attr('readonly', 'readonly');
		editor.style.display = "block";
		if (add)
			editor.querySelector("#submit-button").value="Add"
		data = get_schedule_processes_data()
		build_select("editor_select_container", data, "processes-select");
	}
	function setPeriod(event)
	{
		event.stopPropagation();
		event.preventDefault();
		if (period_num.value == ""){
			document.getElementById("info").style.display = "inline-block";
			return;}
		else
			var val = parseInt(period_num.value);
			document.getElementById("info").style.display = "none";

		var t_rep = document.querySelector('input[name="Time"]:checked').value;
		if (isNaN(val))
		    console.log("Not a Valid Value")
		else
		{
            var period = t_rep * val;
            t_rep_choice = document.getElementById("choice").value
            document.getElementById(t_rep_choice).value = period;
            document.getElementById("timeDialog").style.display = "none";
         }
	}
