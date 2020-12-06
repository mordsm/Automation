
var crumbs_data = {
		"Process Flows": build_crumb("Process Flows", function() {$("span:contains('Process Flows')").parent("a").click()}),
		"Accessibility": build_crumb("Accessibility", function() {$("span:contains('Accessibility')").parent("a").click()}),
		"Events": build_crumb("Events", function() {$("span:contains('Events')").parent("a").click()}),
		"Content": build_crumb("Content", function() {$("span:contains('Content')").parent("a").click()}),
		"My Process Flows": build_crumb("My Process Flows", function(){div_content("main_content_div", "/process/list/",init_processes_table);}),
		"Process Schedules": build_crumb("Process Schedules", function(){div_content("main_content_div", "/datatables/process_schedule_list/",init_process_schedules_table)}),
		"Schedules": build_crumb("Schedules", function(){$("#schedules").click()}),
		"Errors List": build_crumb("Errors List", function(){div_content("main_content_div", "/datatables/error_list/",init_errors_table);}),
		"Process Test": build_crumb_template("Process Test/%s", "#process-test-%s", "click"),
		"Process Report": build_crumb_template("Process Report/%s", "#process-report-%s", "click"),
		"Process Script": build_crumb_template("Process Report/%s", "#process-scriptt-%s", "click"),
		"Process Edit": build_crumb_template("Process Edit/%s", "#process-edit-%s", "click"),
		"Process Delete": build_crumb_template("Process Delete/%s", "#process-delete-%s", "click"),
		"Process Schedule Report": build_crumb_template("Process Schedule Report/%s", "#process-schedule-report-%s", "click"),
		"Process Schedule Test": build_crumb_template("Process Schedule Report/%s", "#process-schedule-test-%s", "click"),
		"Error List Details": build_crumb_template("Error List Details/%s", "#error-list-details-%s", "click"),
		"Error List Process Report": build_crumb_template("Error List Process Report/%s", "#error-list-process-report-%s", "click"),
};

var breadcrumb_stack = [];

function build_crumb_template(name, selector, function_name) {
	return {"name":name, "selector":selector, "function": function_name}
}

function build_crumb(name, action = null, id = null) {
	return {"name": name, "action": action, "id": id};
}

function crumb_from_template(template, id) {
	return {"name":format(template.name, id), "action": execute_function_by_name(template.function, $(format(template.selector, id))), "id": id}
}

function crumb_clicked(name) {
	pop_crumbs_to(name);
	if(breadcrumb_stack.length > 1) {
		crumbs_data[name].action();
	}
	if(breadcrumb_stack.length == 1) {
		clear_div_content();
	}
	set_breadcrumbs();
}

function is_root_collapsed(root_name) {
	var href = $("span:contains('" + root_name + "')").parent("a").attr('href');
	var div = $(href);
	return div.hasClass("show");
}

function branch(name, template=false, id=null, root=false) {
	return {"name": name, "template": template, "id": id, "root": root};
}

function push_branch(branch) {
	for(var i = 0; i < breadcrumb_stack.length; i++) {
		if(breadcrumb_stack[i].name == branch[i].name) {
			while(breadcrumb_stack.length > i) {
				breadcrumb_stack.pop();
			}
			for(var j = i; j < branch.length; j++) {
				c = branch[j];
				if(c.template) push_template(c.name, c.id, c.root)
				else push_crumb(c.name, c.root);
			}
		}
		return
	}
}

function push_template(name, id, root = false) {
	push(crumb_from_template(crumbs_data[name], id), root);
}

function push_crumb(name, root=false) {
	push(crumbs_data[name], root);
};

function push(crumb, root=false) {
	if(!root && breadcrumb_stack.length > 0 && last(breadcrumb_stack).name == crumb.name) return;
//	if(!root && breadcrumb_stack.length > 1) breadcrumb_stack.pop();
	if(root) {
		clear_crumbs();
		clear_div_content();
	}
	if(!root || (root && !is_root_collapsed(crumb.name))){
		breadcrumb_stack.push(crumb);
	}
	
	set_breadcrumbs();
};

function last(a) {
	return a.length > 0 ? a[a.length - 1] : null;
}

function pop_crumbs_to(name){
	while(breadcrumb_stack.length > 1 && last(breadcrumb_stack).name != name) {
		breadcrumb_stack.pop();
	}
}

function clear_crumbs() {
	while(breadcrumb_stack.length > 0) {
		breadcrumb_stack.pop();
	}
}

function crumb_to_string(crumb) {
	var name = crumb.id ? crumb.name + "/" + id : crumb.name;
	if(crumb.action) {
		var l = format('<li><a href="javascript: crumb_clicked(\'%s\');">%s</a></li>', name, name);
		return format(l, crumb.id);
	}
	return format("<li>%s</li>", name);
}

function set_breadcrumbs(breadcrumbs_id = "breadcrumbs") {
	var bc = $("#" + breadcrumbs_id);
	bc.empty();
	for (var i = 0; i < breadcrumb_stack.length -1; i++) {
		bc.append(crumb_to_string(breadcrumb_stack[i]));
	}
	if(breadcrumb_stack.length > i){
		bc.append(crumb_to_string({"name": breadcrumb_stack[i].name}));
	}
};
