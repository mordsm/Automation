
function calculate_next_run(last_run, period, run_count, repeat) {
	if (last_run == null || last_run == "") {
		return last_run;
	}
	if (run_count >= repeat) {
		return null;
	}
	var new_date = new Date(last_run);
	new_date.setTime(new_date.getTime() + period * 1000);
	return new_date;
}

function init_process_schedules_table() { 
   $('#process_schedule_list_dt').DataTable({
    	"processing": true,
    	"serverSide": true,
    	"ajax": "/datatables/process_schedule_list_data/",
        "columns": [
                        { "data": "name", "className": "dt-body-left" },
                        { "data": "last_run_status", "className": "dt-body-left", "render": function(status, type, data){
                        	if (status == 1 || status == 'NotRun') { return "Not Executed";}
                        	if (status == 2 || status == 'OK') { return "OK";}
                        	if (status == 3 || status == 'Error') { return "Error";}
                        	return "Unknown";
                        } },
                        { "data": "accessibility_status", "className": "dt-body-left"  },
                        { "data": "last_time", "className": "dt-body-left", "render": format_date },
                        { "data": "last_time", "className": "dt-body-left", "render": function (last_time, type, data) {
                        	return format_date(calculate_next_run(last_time, data.schedule_period, data.run_count, data.schedule_repeat));
                        	}
                        },
                        { "data": "process_id", "orderable": false, "searchable": false, "width": "5%", "render": function (id, type, data) {
                        	return '  <div class="dropdown">'
                            + '<button class="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown">Action<span class="caret"></span></button>'
                            + '<ul class="dropdown-menu">'
                            + '<li><a id="process-schedule-test-' + id + '" href="javascript: div_content(\'main_content_div\', \'/process/check/' + id + '/\', init_process_schedules_table); push_template(\'Process Schedule Test\', id=\'' + id + '\');">Test</a></li>'
                            + '<li><a id="process-schedule-report-' + id + '" href="javascript: div_content(\'main_content_div\', \'/process/report/' + id + '/\', init_process_schedules_table); push_template(\'Process Schedule Report\', id=\'' + id + '\');">Report</a></li>'
                            + '</ul>'
                          + '</div>'
                        	},
                        },
                        ],
    });
   
};



