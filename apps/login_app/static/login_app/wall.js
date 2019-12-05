$(document).ready(function(){
    $('#email').change(function(){
        console.log( "a change has been made")
    })})


        var username = $(this).val();

        $.ajax({
            url: '/ajax/validate_email/',
            data: {
                'email': email
            },
            dataType: 'json',
            success: function (data) {
                if (data.is_taken) {
                    alert("A user with this email address already exists.");
                }
            }
        });

