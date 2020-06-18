$(document).ready(function(){

    // hide login and logout button
    $(".login").hide();

    // require to store user session details
    sessionStorage.username = '';
    sessionStorage.userid = '';
    sessionStorage.loginid ='';

    // switch between login and logout
    $("#registeruser").click(function(e){
        $("#login_div").hide();
        $("#register_div").show();
    });
    $("#loginuser").click(function(e){
        $("#register_div").hide();
        $("#login_div").show();
    });

    // login button work
    $("#login").click(function(e){
        // validations 
        if($("#id").val()==''){
            $("#login-alert-name").show();
            $("#login-alert-name").fadeTo(2250, 500).slideUp(500, function(){
            $("#login-alert-name").hide();
            });
            return false;
        }
        if($("#pass").val()==''){
            $("#login-alert-pass").show();
            $("#login-alert-pass").fadeTo(2250, 500).slideUp(500, function(){
            $("#login-alert-pass").hide();
            });
            return false;
        }
        $.ajax(
          {
            type: "POST",
            url: "/user-login",
            global: false,
            async: false,
            datatype: "json",
            data: {"loginid":$("#id").val(), "userpassword":$("#pass").val()},
            success: function(resp){
                // status 0 : ok
                if(resp['status'] == 0){ 
                    // user data storing in session
                    sessionStorage.username = resp['firstname']+resp['lastname'];
                    sessionStorage.userid = resp['userid'];
                    sessionStorage.loginid = resp['loginid'];
                    $(".logo").click();
                }
                // status 1 : process failed
                else if (resp['status'] == 1){
                    $("#login-failed-alert").show();
                    $("#login-failed-alert").fadeTo(2250, 500).slideUp(500, function(){
                    $("#login-failed-alert").hide();
                    });
                    return false;
                }
                // status 2 : wrong password
                else if (resp['status'] == 2){
                    $("#login-alert").show();
                    $("#login-alert").fadeTo(2250, 500).slideUp(500, function(){
                    $("#login-alert").hide();
                    });
                    return false;
                }
                // status 3 : user not found
                else{
                    $("#login-alert-notexist").show();
                    $("#login-alert-notexist").fadeTo(2250, 500).slideUp(500, function(){
                    $("#login-alert-notexist").hide();
                    });
                    return false;
                }
            }
          });

    });

    // save new user
    $("#saveuser").click(function(e){
        // validations
        if($("#savefname").val()==''){
            $("#register-alert-fname").show();
            $("#register-alert-fname").fadeTo(2250, 500).slideUp(500, function(){
            $("#register-alert-fname").hide();
            });
            return false;
        }
        if($("#saveid").val()==''){
            $("#register-alert-name").show();
            $("#register-alert-name").fadeTo(2250, 500).slideUp(500, function(){
            $("#register-alert-name").hide();
            });
            return false;
        }
        if($("#savepass").val()==''){
            $("#register-alert-pass").show();
            $("#register-alert-pass").fadeTo(2250, 500).slideUp(500, function(){
            $("#register-alert-pass").hide();
            });
            return false;
        }

        // password validations
        var number = /([0-9])/;
        var alphabets = /([a-zA-Z])/;
        var special_characters = /([~,!,@,#,$,%,^,&,*,-,_,+,=,?,>,<])/;
        if($('#savepass').val().length<6) {
        $('#password-strength-status').html("Weak (should be atleast 6 characters.)");
        return false;
        } 
        else {  	
            if($('#savepass').val().match(number) && $('#savepass').val().match(alphabets) && $('#savepass').val().match(special_characters)) {            
            $('#password-strength-status').html("Strong");
            
            } 
            else {
            $('#password-strength-status').html("Medium (should include alphabets, numbers and special characters.)");
            return false;
            }
        }
        if($("#confpass").val()==''){
            $("#register-alert-confpass").show();
            $("#register-alert-confpass").fadeTo(2250, 500).slideUp(500, function(){
            $("#register-alert-confpass").hide();
            });
            return false;
        }
        if($("#savepass").val()!= $("#confpass").val() ){
            $("#register-alert-passnotmatch").show();
            $("#register-alert-passnotmatch").fadeTo(2250, 500).slideUp(500, function(){
            $("#register-alert-passnotmatch").hide();
            });
            return false;
        }
        $.ajax(
          {
            type: "POST",
            url: "/user-register",
            global: false,
            async: false,
            datatype: "json",
            data: {"firstname":$("#savefname").val(),"lastname":$("#savelname").val(),"loginid":$("#saveid").val(), "userpassword":$("#savepass").val()},
            success: function(resp){
                
                if(resp['status'] == 0){
                    $("#register-alert-success").show();
                    $("#register-alert-success").fadeTo(2250, 500).slideUp(500, function(){
                    $("#register-alert-success").hide();
                    $("#loginuser").click();
                    });
                    
                }
                else{
                    $("#register-alert-duplicate").show();
                    $("#register-alert-duplicate").fadeTo(2250, 500).slideUp(500, function(){
                    $("#register-alert-duplicate").hide();
                    });
                    return false;
                }
            }
          });

    });
})