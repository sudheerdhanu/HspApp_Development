//Flsh message agter form submit

$(document).ready(function () {

        $('form').submit(function () {
            $('#myAlert').show('fade');

            setTimeout(function () {
                $('#myAlert').hide('fade');
            }, 2000);

        });

        $('#linkClose').submit(function () {
            $('#myAlert').hide('fade');
        });

    });


// signup form validating

$(function() {

        $("#first_error_message").hide();
            var errot_first_name=false;

         $("#last_error_message").hide();
            errot_last_name=false;

        $("#password_error_message").hide();
            error_password=false;

        $("#conform_password_error_message").hide();
            error_conform_password=false;

        $("#email_error_message").hide();
            error_email=false;

        $("#mobile_error_message").hide();
            error_mobile=false;




         $("#first_name").focusout(function() {
            check_first_name();

        })

        $("#last_name").focusout(function() {
            check_last_name();

        })



        $("#password").focusout(function() {
            check_password();

        })

        $("#conform_password").focusout(function() {
            check_conform_password();

        })

        $("#email").focusout(function() {
            check_email();

        })


        $("#mobile").focusout(function() {
            check_mobile();

        })


});

function  check_first_name(){
        var firstname=$("#first_name").val().length;


        if (firstname <5 || firstname>20){
                $("#first_error_message").html("should be between 5 to 20 chars");
                $("#first_error_message").show();
                errot_first_name=true;
        }

        else{
        $("#first_error_message").hide();

        }




}
function  check_last_name(){
        var lastname=$("#last_name").val().length;


        if (lastname <0 || lastname>20){
                $("#last_error_message").html("should be between 5 to 20 chars");
                $("#last_error_message").show();
                errot_last_name=true;
        }

        else{
        $("#first_error_message").hide();

        }

}
//




function  check_password(){
        var password=$("#password").val().length;

        if (password < 8){
                $("#password_error_message").html("should be between 8 letters");
                $("#password_error_message").show();
                error_password=true;
        }

        else{
        $("#password_error_message").hide();

        }

}

function  check_conform_password(){
        var password=$("#password").val();
        var conform_password=$("#conform_password").val();

        if (password != conform_password){
                $("#conform_password_error_message").html("Password should be match");
                $("#conform_password_error_message").show();
                error_conform_password=true;
        }

        else{
        $("#conform_password_error_message").hide();

        }

}

function check_email(){

        var email=$("#email").val();
        var pattern = /^\b[A-Z0-9._%-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b$/i

        if(pattern.test(email)){
            $("#email_error_message").hide();

        }
        else
        {
        $("#email_error_message").html("Enter valid email address");
        $("#email_error_message").show();

        error_email=true;

        }
}

function check_mobile(){

        var mobile_number=$("#mobile").val();
        var pattern = /\(?([0-9]{3})\)?([ .-]?)([0-9]{3})\2([0-9]{4})/

        if(pattern.test(mobile_number)){
            if(mobile_number.length==10){
                   $("#mobile_error_message").hide();
              }
            else {
                  $("#mobile_error_message").html("mobile number should me 10 digits");
                  $("#email_error_message").show();
              }

        }
        else
        {
        $("#mobile_error_message").html("Enter valid mobile number");
        $("#mobile_error_message").show();

        error_mobile=true;

        }
}