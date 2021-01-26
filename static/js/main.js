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
            console.log(data.url);
            $("#generated-ca-img").attr('src', data.url);
        },
        error: function(error){
            console.log("Something went ");
        }
    });
}