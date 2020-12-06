
    function build_select_only(data, select_name, multi = true, disabled = false) {
       select = document.createElement("select");
       select.name = select_name;
	   select.name = select_name;
	   select.style = "height: 100%;";
	   if (multi) {
		   select.multiple = "multiple";		   
	   }
	   for (i = 0; i < data.length; i++) {
		   o = data[i];
		   var option = document.createElement("option");
		   option.value = o.value;
		   option.text = o.text;
		   option.disabled=disabled;
		   if (o.selected) {
			   option.selected = "selected";
		   }
		   select.appendChild(option);
	   }
	   return select;
    };

	function build_select(parent_id, data, select_name, multi = true, disabled=false) {
	   var parent = document.getElementById(parent_id);
	   var select = parent.querySelector("select");
	   if (select == null) {
		   select = document.createElement("select");
		   select.name = select_name;
		   select.name = select_name;
		   select.style = "height: 100%;";
		   if (multi) {
			   select.multiple = "multiple";		   
		   }
		   parent.appendChild(select)
	   }
	   for (i = 0; i < data.length; i++) {
		   o = data[i];
		   var option = document.createElement("option");
		   option.value = o.value;
		   option.text = o.text;
		   option.disabled=disabled;
		   if (o.selected) {
			   option.selected = "selected";
		   }
		   select.appendChild(option);
	   } 
   }
   
   function destroy_select(parent_id) {
	   var parent = document.getElementById(parent_id);
	   var select = parent.querySelector("select");
	   if (select != null) {
		   var i, L = select.options.length - 1;
		   for(i = L; i >= 0; i--) {
		      select.remove(i);
		   }
	   }
   }
   