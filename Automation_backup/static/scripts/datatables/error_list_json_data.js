function init_error_element_table() {
	var error_id = $("#error_id").val();
    $('#error_element_dt').DataTable({
        "paging":   false,
        "ordering": false,
        "info":     false,
        "searching": false,
    	"processing": true,
    	"serverSide": true,
    	"ajax": "/datatables/error_details/element/" +  error_id + "/",
        "columns": [
                        { "data": "target", "className": "dt-body-left" },
                        { "data": "local_url", "className": "dt-body-left" },
			            { "data": "impact", "className": "dt-body-left" },
                        ],
    });
    
    div_content('page_source', '/page_source/' + error_id +'/');
    $("body").on('DOMNodeInserted', "#page_source", function() {
    	$("#tag-wrapper")[0].scrollIntoView();
    	$("html, body").animate({
            scrollTop: 0
        }, 0); 
    });
    
}


function init_errors_table() {
    var table = $('#error_list_dt').DataTable({
    	"processing": true,
    	"serverSide": true,
    	
    	"ajax": "/datatables/error_list_data/",
        "columns": [
            {
                "className":      'details-control',
                "orderable":      false,
                "data":           null,
                "defaultContent": '',
                "width": "5%"
            },
			            { "data": "id", "visible": false,},
			            { "data": "impact", "className": "dt-body-left" },
                        { "data": "target", "className": "dt-body-left" },
                        { "data": "local_url", "className": "dt-body-left" },
                        { "data": "error_name", "searchable": true, "visible": false},
                        { "data": "discovered", "visible": false},
                        { "data": "id", "orderable": false, "searchable": false, "render": function (id, type, data) {
                        	return '  <div class="dropdown">'
                            + '<button id="error-list-details-' + id + '" class="btn btn-primary" type="button" onclick="javascript: div_content(\'main_content_div\', \'/datatables/error_details/' + id + '/\', init_error_element_table); push_template(\'Error List Details\', id=\'' + id + '\');">Details</span></button>'
                          + '</div>'
                        	},
                        },
                        ],
    });

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
		    	row.child( row.data().errors ).show();
		        tr.addClass('shown');
		    }
		};
			
	$('#error_list_dt tbody').on('click', 'td.details-control', details_toggle);


};
