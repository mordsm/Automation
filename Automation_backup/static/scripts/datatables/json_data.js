function local_set_action_breadcrumbs(action) {
	set_action_breadcrumbs(action, "My Process Flows");
};

function init_processes_table() {
	var parent = "My Process Flows";
    $('#process_list_dt').DataTable({
    	"processing": true,
    	"serverSide": true,
    	"ajax": "/datatables/process_list_data/",
        "columns": [
            			{ "data": "id", "visible": false,},
                        { "data": "process_name", "className": "dt-body-left" },
                        { "data": "url", "className": "dt-body-left" },
                        { "data": "accessibility", "className": "dt-body-left" ,
                        "render": function (val, type, data)
                            { if (val=="") return  '<span class="badge badge-secondary">UnKnown</span>'
                              else if (val=="0") return '<span class=" badge  progress-bar-danger">Inaccessible</span>'
                              else if (int(val) > 0 && int(val) < 100) return '<span class="badge label-table progress-badge-secondary">Partially accessible</span>';
                              else return '<span class="badge label-table progress-badge-success">Accessible</span>'

                            } },
                        { "data": "create_date", "className": "dt-body-left", "render": format_date },
                        { "data": "run_date", "className": "dt-body-left", "render": format_date },
                        { "data": "id", "orderable": false, "searchable": false, "render": function (id, type, data) {
                        	return '  <div class="dropdown">'
                            +   '<button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Action <i class="mdi mdi-chevron-down"></i></button>'

                            + '<ul class="dropdown-menu">'
                            + '<li><a id="process-test-' + id + '" href="javascript: div_content(\'main_content_div\', \'/process/check/' + id + '/\', init_processes_table); push_template(\'Process Test\', id=\'' + id + '\');">Test</a></li>'
                            + '<li><a id="process-report-' + id + '" href="javascript: div_content(\'main_content_div\', \'/process/report/' + id + '/\', init_processes_table); push_template(\'Process Report\', id=\'' + id + '\');">Report</a></li>'
                            + '<li><a id="process-script-' + id + '" href="javascript: div_content(\'main_content_div\', \'/process/script/' + id + '/\', init_processes_table); push_template(\'Process Script\', id=\'' + id + '\');">Script</a></li>'
                            + '<li><a id="process-edit-' + id + '" href="javascript: div_content(\'main_content_div\', \'/process/edit/' + id + '/\', init_process_editor); push_template(\'Process Edit\', id=\'' + id + '\');">Edit</a></li>'
                            + '<li><a id="process-delete-' + id + '" href="javascript: div_content(\'main_content_div\', \'/process/delete/' + id + '/\', init_processes_table); push_template(\'Process Delete\', id=\'' + id + '\');">Delete</a></li>'
                            + '</ul>'
                          + '</div>'
                        	},
                        },
                        ],
    
    });
};

addEvent(window, 'load', init_processes_table)
