$(document).ready(function() {
		$('textarea').overlay([
    	{
	        //match: /\B#\w+/g,
    		match : /(?:^|\s)\#(\w+)\b/g,
	        css: {
	            'background-color': '#d8dfea'
	        }
    	}
		]);
		$('#all_polls').on('click', '[class^="poll"]', (function(){
			option_id = $(this).attr('rel');
			poll_id = $(this).attr('id');
			overall = $(this).attr('class');
			$.ajax({
				type: "POST",
				url: "/sllod/option_vote/",
				data: {
					csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[1].value,
					poll: poll_id,
					option: option_id,
				},
				success: function(result){
					vote_id = ".vote" + option_id
					$(vote_id).html(result);
					$("." + overall).css("color","black")
				},
		});
		    
		})
		);
		$('#create_poll').click(function(){
			var dataString = $("#id_message").val();
			$.ajax({
				type: "POST",
				url: "/sllod/create_poll/",
				data: {
					csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
					message: dataString,
				},
				success: function(result){
					$("#id_message").val("");
					$(".textoverlay").find("span").remove();
					$("#all_polls").html(result);
					/*$.ajax({
						type: "GET",
						url: "/sllod/get_polls/",
						success: function(result){
							$("#all_polls").html(result);
						},
				});*/
				},
		});
       $("#poll_form").on('input',function() {
       		message = $("#id_message").val();
			index = message.lastIndexOf("#");
			
    	   $(".poll_message").val(message);
			if(index >= 0){
				globalIndex = index;
				highlightOptionText(message,globalIndex,message.length);
			}else{
				$("#highlight").empty();
			}
				
		});
		

		});
});


function highlightOptionText(message){
	options = message.split(" ");
	$("#highlight").empty();
	for(var i = 0; i < options.length; i++){
		if(options[i].indexOf("#") >= 0)
			$("#highlight").append("<div>" + options[i] + "</div>");
	}
		
}
function refreshPolls(){
	
}
