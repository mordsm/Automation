
function add_event_row_editor(event_id) {
    show_event_row_editor(event_id, add=true)

}

function get_event_data(event_id=null) {
 	   var events = JSON.parse(document.getElementById("events").innerText)
 	   var result = [];
 	   for (i = 0; i< events["events"].length; i++) {
 		   var e = events["events"][i];
 		   if (e.id == event_id)
 		   {
 		    var e_roles = e.roles.split()
 		    for (i = 0; i< events["roles"].length; i++) {
 		        result.push({"value":events["roles"][i],"text":events["roles"][i], "selected":e_roles.includes(events["roles"][i]) })

 		    }
 		   }
 	   }
 	   return {"name":e.name,"roles":result};
    }

function close_event_row_editor() {
	var editor = document.getElementById("event-editor");
	editor.style.display = "none";
}
function show_event_editor() {
	show_event_row_editor(event_id = null,  add = true);
}




function submit_event_edit() {
    	//event.stopPropagation();
		//event.preventDefault();
        if ($("#submit-button").text() == "Save")
        	url = "/event_type/edit/" + $("#id-input").val()
        else
        	url = "/event_type/create/"
        $.ajax({
            url: url,
            type: 'POST',
            data : $('#row-edit-form').serialize(),
            success: function(data){
				div_content('main_content_div',"/datatables/events_list/", init_event_table);
			  },
            fail: function(qXHR, textStatus, errorThrown){
                showErrorResponse("Save Event failed", qXHR.responseText)
              }
              ,
            error: function(qXHR, textStatus, errorThrown){
                showErrorResponse("Save Event failed", qXHR.responseText)
              }
          });

    };

function deleteEvent(event_id) {

	var csrtoken = getCookie('csrftoken');

	$.ajax({
		url: "/event_type/delete/"+event_id,
		type: 'post',
		headers: {"X-CSRFToken": csrtoken},
		success: function(data) {
			div_content('main_content_div',"/datatables/events_list/", init_event_table);
		},

        fail: function(qXHR, textStatus, errorThrown){
	    	showErrorResponse("Delete Event failed", qXHR.responseText)
	      }
	});

};

function init_event_table() {
   var row_editor_close = document.getElementById("event-editor-close");
	row_editor_close.onclick = close_event_row_editor;
	events_data=  JSON.parse(events.innerText);
   var table = $('#events_list_dt').DataTable({
    	"processing": true,
    	"serverSide": true,
    	"ajax": "/datatables/events_list_data/",
        "columns": [

            			{ "data": "id", "visible": false,},
                        { "data": "event_type_name", "className": "dt-body-left" },
                        { "data": "roles", "className": "dt-body-left" ,"render":function(roles,type,data){

                              for  (i=0;i<events_data["events"].length;i++) {
                                    if (events_data["events"][i].id == data["id"])
                                      return events_data["events"][i].roles
                                }
                             return events_data["roles"].join(",");}
                         },

                        { "data": "id", "orderable": false, "searchable": false, "width": "5%", "render": function (id, type, data) {
                        	var datastr = JSON.stringify(data);
                         	var editor_call = 'show_event_row_editor(' + id + ')';
                         	return '  <div class="dropdown">'
                            + '<button class="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown">Action<span class="caret"></span></button>'
                            + '<ul class="dropdown-menu">'
                            + '<li><a href="javascript:' + editor_call +';"  >Edit</a></li>'
                            + '<li><a href="javascript:deleteEvent('+id+');" >Delete</a></li>'
                            + '</ul>'
                          + '</div>'
                        	},
                        },
                        ],
    });
   



   



};

function show_event_row_editor(event_id = null,  add=false) {

    $("#id-input").val(""+event_id)
    results = []
    if (event_id)
    {
        results= get_event_data(event_id)
        document.getElementById("type").value = results["name"];
        document.getElementById("roles").innerHTML = '';
        build_select("editor_form_container", results["roles"], "roles");


    }
	var editor = document.getElementById("event-editor");
	if (add) {
	    document.getElementById("submit-button").innerText="Create";
	}
	else{
	    document.getElementById("submit-button").innerText="Save";
	}
	editor.style.display = "block";
}

