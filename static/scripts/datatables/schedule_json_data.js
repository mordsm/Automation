
function add_row_editor(schedule_id, name, repeat, period) {
    show_row_editor(schedule_id, name, repeat, period,add=true)
    data = get_schedule_processes_data(schedule_id)
	build_select("editor_select_container", data, "processes-select");

}
function show_row_editor(schedule_id = null, name = "", repeat = "", period, add=false) {	
	
	document.getElementById("id-input").value = schedule_id;
	document.getElementById("name-input").value = name;
	document.getElementById("repeat-input").value = repeat;
	document.getElementById("period-input").value = period;
	
	document.getElementById("period_num").value = period;
	document.getElementById("second").checked = true;
	
//	var form = document.getElementById('row-edit-form');
//	form.action = form.action + schedule_id;
	
	destroy_select("editor_select_container");
	data = get_schedule_processes_data(schedule_id)
	build_select("editor_select_container", data, "processes-select");

	var editor = document.getElementById("schedule-editor");
	if (add) {
	    editor.querySelector("#submit-button").value="Add";
	}

	editor.style.display = "block";
}

function show_editor() {
	show_row_editor(schedule_id = null, name = "", repeat = "", period = "", add = true);
}

function update_selected_processes() {
	select = document.getElementById("processes-select");
	var val = "";
	for(i = 0; i < select.options.length; i++) {
		var op = select.options[i];
		if(op.selected) {
			if(val != "") {
				val = val + ",";
			}
			val = val + op.value;
		}
	}
	document.getElementById("process-selected").value=val
}

function close_row_editor() {
	var editor = document.getElementById("schedule-editor");
	editor.style.display = "none";
}

function init_schedules_table() { 
	
	var row_editor_close = document.getElementById("schedule-editor-close");
	row_editor_close.onclick = close_row_editor;
	
	
   var table = $('#schedule_list_dt').DataTable({
    	"processing": true,
    	"serverSide": true,
    	"ajax": "/datatables/schedule_list_data/",
        "columns": [
			            {
			                "className":      'details-control',
			                "orderable":      false,
			                "data":           null,
			                "defaultContent": '',
			                "width": "5%"
			            },
            			{ "data": "id", "visible": false,},
                        { "data": "name", "className": "dt-body-left" },

                        { "data": "period", "className": "dt-body-left"  },
                         { "data": "repeat", "className": "dt-body-left" },
                        { "data": "id", "orderable": false, "searchable": false, "width": "5%", "render": function (id, type, data) {
                        	var datastr = JSON.stringify(data);
                        	var editor_call = 'show_row_editor(' + id + ',\''+ data.name + '\','+ data.repeat + ','+ data.period  + ')';
                        	var add_call = 'add_row_editor(' + id + ',\''+ data.name + '\','+ data.repeat + ','+ data.period  + ')';
                        	return '  <div class="dropdown">'
                            + '<button class="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown">Action<span class="caret"></span></button>'
                            + '<ul class="dropdown-menu">'
                            + '<li><a href="javascript: ' + editor_call +';">Edit</a></li>'
                            + '<li><a href="javascript: ' + add_call +';">Add</a></li>'

                            + '<li><a href="javascript:deleteSchedule('+id+')"   >Delete</a></li>'
                            + '</ul>'
                          + '</div>'
                        	},
                        },
                        ],
    });
   
   function format_processes( d ) {
		data = get_schedule_processes_data(d.id)
		return build_select_only(data, "select-expand", true, true)
	};
  
   function details_toggle() {
	    var tr = $(this).closest('tr');
	    var row = table.row( tr );

	    if ( row.child.isShown() ) {
	        // This row is already open - close it
	        row.child.hide();
	        tr.removeClass('shown');
	    }   
	    else {
	        // Open this row
	        row.child( format_processes(row.data()) ).show();
	        tr.addClass('shown');
	    }
	}
   
   $('#schedule_list_dt tbody').on('click', 'td.details-control', details_toggle);

   addEvent(document.getElementById("processes-select"), 'change', update_selected_processes);

};



