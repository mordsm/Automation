
function add_role_row_editor(role_id) {
    show_role_row_editor(role_id, add=true)

}

function get_role_data(role_id=null) {
 	   var roles = JSON.parse(document.getElementById("roles").innerText)
 	   var result = [];
 	   for (i = 0; i< roles["roles"].length; i++) {
 		   var e = roles["roles"][i];
 		   if (e.id == role_id)
 		   {
 		    var e_users = e.users.split()
 		    for (i = 0; i< roles["users"].length; i++) {
 		        result.push({"value":roles["users"][i],"text":roles["users"][i], "selected":e_users.includes(roles["users"][i]) })

 		    }
 		    return {"name":e.name,"users":result};
 		   }
 	   }
 	   return {"name":e.name,"users":result};
    }

function close_role_row_editor() {
	var editor = document.getElementById("role-editor");
	editor.style.display = "none";
}
function show_role_editor() {
	show_role_row_editor(role_id = null,  add = true);
}




function submit_role_edit() {

        if ($("#submit-button").text() == "Save")
        	url = "/role/edit/" + $("#id-input").val()
        else
        	url = "/role/create/"
        $.ajax({
            url: url,
            type: 'POST',
            data : $('#row-edit-form').serialize(),
            success: function(data){
				div_content('main_content_div',"/datatables/role_list/", init_role_table);
			  },
            fail: function(qXHR, textStatus, errorThrown){
                showErrorResponse("Save role failed", qXHR.responseText)
              }
              ,
            error: function(qXHR, textStatus, errorThrown){
                showErrorResponse("Save role failed", qXHR.responseText)
              }
          });

    };

function deleteRole(role_id) {

	var csrtoken = getCookie('csrftoken');

	$.ajax({
		url: "/role/delete/"+role_id,
		type: 'post',
		headers: {"X-CSRFToken": csrtoken},
		success: function(data) {
			div_content('main_content_div',"/datatables/role_list/", init_role_table);
		},

        fail: function(qXHR, textStatus, errorThrown){
	    	showErrorResponse("Delete role failed", qXHR.responseText)
	      }
	});

};

function init_role_table() {
   var row_editor_close = document.getElementById("role-editor-close");
	row_editor_close.onclick = close_role_row_editor;
	roles_data=  JSON.parse(roles.innerText);
   var table = $('#roles_list_dt').DataTable({
    	"processing": true,
    	"serverSide": true,
    	"ajax": "/datatables/role_list_data/",
        "columns": [

            			{ "data": "id", "visible": false,},
                        { "data": "name", "className": "dt-body-left" },
                        { "data": "users", "className": "dt-body-left" ,"render":function(roles,type,data){

                              for  (i=0;i<roles_data["users"].length;i++) {
                                    if (roles_data["users"][i].id == data["id"])
                                      return roles_data["users"][i].roles
                                }
                             return roles_data["users"].join(",");}
                         },

                        { "data": "id", "orderable": false, "searchable": false, "width": "5%", "render": function (id, type, data) {
                        	var datastr = JSON.stringify(data);
                         	var editor_call = 'show_role_row_editor(' + id + ')';
                         	return '  <div class="dropdown">'
                            + '<button class="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown">Action<span class="caret"></span></button>'
                            + '<ul class="dropdown-menu">'
                            + '<li><a href="javascript:' + editor_call +';"  >Edit</a></li>'
                            + '<li><a href="javascript:deleteRole('+id+');" >Delete</a></li>'
                            + '</ul>'
                          + '</div>'
                        	},
                        },
                        ],
    });
   



   



};

function show_role_row_editor(role_id = null,  add=false) {

    $("#id-input").val(""+role_id)
    results = []
    if (role_id)
    {
        results= get_role_data(role_id)
        document.getElementById("name").value = results["name"];
        document.getElementById("users").innerHTML = '';
        build_select("editor_form_container", results["users"], "users");


    }
	var editor = document.getElementById("role-editor");
	if (add) {
	    document.getElementById("submit-button").innerText="Create";
	}
	else{
	    document.getElementById("submit-button").innerText="Save";
	}
	editor.style.display = "block";
}

