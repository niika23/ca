$( document ).ready(function() {

    $('#generate-btn').click(function(){
        generateGraph();
	});
})


function generateGraph()
{   
    // location.reload();
    var rule = $('#rule-input').val();
    var col = $('#col-input').val();

    req_url = "/generator/"+rule+"/"+col;
    console.log(req_url);

    $.ajax({
        url: req_url,
        data: {data: 1},
        type: 'POST',
        success: function(response){
            data = JSON.parse(response);
            $(".generated-graph-div").empty().append("<img id='generated-ca-img' src='' alt='Failed to load the image'>");
            $("#generated-ca-img").attr('src', data.url);
        },
        error: function(error){
            console.log("Something went wrong!");
        }
    });
}