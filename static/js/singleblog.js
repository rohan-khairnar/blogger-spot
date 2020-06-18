$(document).ready(function(){
    $("#userid").val(parseInt(sessionStorage.userid));
    if (sessionStorage.username == ''){
        $("#logoutbtn").hide();
        $("#loginbtn").show();
    }
    else{
        $("#loginbtn").hide();
        $("#logoutbtn").show();
    }

    $("#delete-btn").click(function(e){
        $.ajax({
            url: '/delete/'+$("#blogid").val(),
            type: 'DELETE',
            success: function(resp) {
                
                if(resp['status'] == 0){
                        $("#delete-success").show();
                        $("#delete-success").fadeTo(2250, 500).slideUp(500, function(){
                        $("#delete-success").hide();
                        $('.logo').click();
                        });
                    }
                else{
                    $("#delete-failed").show();
                    $("#delete-failed").fadeTo(2250, 500).slideUp(500, function(){
                    $("#delete-failed").hide();
                    });
                    return false;
                }
            }
        });
    });

    $("#update").click(function(e){
            $.ajax({
                url: '/update',
                type: 'PUT',
                data:{"blogid":$("#blogid").val(),"blogtitle":$("#title").val(),"blogdescription":$("#description").val(),"userid":parseInt(sessionStorage.userid)},
                success: function(resp) {
                    if(resp['status'] == 0){
                        $("#update-success").show();
                        $("#update-success").fadeTo(2250, 500).slideUp(500, function(){
                        $("#update-success").hide();
                        $('.logo').click();
                        });
                        }
                    else{
                        $("#update-failed").show();
                        $("#update-failed").fadeTo(2250, 500).slideUp(500, function(){
                        $("#update-failed").hide();
                        });
                        return false;
                        }
                    }
                    });
    });
})