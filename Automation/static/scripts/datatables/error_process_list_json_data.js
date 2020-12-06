function init_error_processes_table() {
	var error_id = $("#error_id").val()
    $('#error_process_list_dt').DataTable({
    	"processing": true,
    	"serverSide": true,
    	"ajax": "/datatables/error_process_list_data/" + error_id,
        "columns": [
            			{ "data": "id", "visible": false,},
                        { "data": "process_name", "className": "dt-body-left" },
                        { "data": "url", "className": "dt-body-left" },
                        { "data": "accessibility", "className": "dt-body-left"  },
                        { "data": "id", "orderable": false, "searchable": false, "render": function (id, type, data) {
                        	return '  <div class="dropdown">'
                            + '<button class="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown">Action<span class="caret"></span></button>'
                            + '<ul class="dropdown-menu">'
                            + '<li><a href="/error_process/graph/' + id + '">Graph</a></li>'
                            + '</ul>'
                          + '</div>'
                        	},
                        },
                        ],
    });
};
