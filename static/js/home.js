$(document).ready(function(){
    
    // varifying logged In or Not
    // not logged in
    if (sessionStorage.username == ''){
        $("#loginbtn").show();
        $("#logoutbtn").hide();
    }
    // logged In
    else{
        $("#loginbtn").hide();
        $("#logoutbtn").show();
        // show edit button for that blog which having same loginid as in session
        $("."+(sessionStorage.loginid).toString()).show();
        // show profile details 
        $(".pro-details").show();
        $("#username").html(sessionStorage.username);
        $("#loginid").html(sessionStorage.loginid);
    }

    // empty session after logged out
    $("#logoutbtn").click(function(e){
        sessionStorage.username = '';
        sessionStorage.userid = '';
        sessionStorage.loginid ='';
    });
    
})