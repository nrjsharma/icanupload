var get_token = {
    'X-CSRFToken': $.cookie("csrftoken")
}
function reset_variable() {
    $('#error-msg').html('');
    $('#error-msg').css("display", "none");
}

function compare_passwords(pass1, pass2) {
    if (pass1 == pass2) {
        return true
    }
    return false
}

function reset_border_color() {
    var input_field_list = ['firstname', 'lastname', 'username', 'email', 'password', 'confirm']
    for (var input_field_id of input_field_list) {
        document.getElementById(input_field_id).style.borderColor = "";
    }
}
$("#siginup-form").submit(function (event) {
    event.preventDefault();
    let empty_field_list = [];
    reset_variable()
    reset_border_color()
    let first_name = $('#firstname').val();
    let last_name = $('#lastname').val();
    let user_name = $('#username').val();
    let email = $('#email').val();
    let password = $('#password').val();
    let confirm_password = $('#confirm').val();
    if (!first_name) {
        empty_field_list.push('firstname')
    }
    if (!last_name) {
        empty_field_list.push('lastname')
    }
    if (!user_name) {
        empty_field_list.push('username')
    }
    if (!email) {
        empty_field_list.push('email')
    }
    if (!password) {
        empty_field_list.push('password')
    }
    if (!confirm_password) {
        empty_field_list.push('confirm')
    }
    if (empty_field_list.length > 0) {
        $('#error-msg').html('fill all required fields');
        $('#error-msg').css("display", "block");
        for (var empty_field_id of empty_field_list) {
            document.getElementById(empty_field_id).style.borderColor = "red";
        }
        console.info('fill all required fields')
    } else if (!compare_passwords(password, confirm_password)) {
        document.getElementById('password').style.borderColor = "red";
        document.getElementById('confirm').style.borderColor = "red";
        $('#error-msg').html('password did\'t match');
        $('#error-msg').css("display", "block");
        console.info('password did\'t match');
    } else if (password.length < 6) {
        document.getElementById('password').style.borderColor = "red";
        document.getElementById('confirm').style.borderColor = "red";
        $('#error-msg').html('password must be of minimum 6 characters length');
        $('#error-msg').css("display", "block");
    } else {
        // SIGNUP USER
        let form = $('#siginup-form');
        let form_data = form.serialize();
        let form_type = form.attr('method');
        $.ajax({
            url: SIGNUP_USER_URL,
            headers: get_token,
            type: form_type,
            data: form_data,
            success: function (data) {
                alert('user created')
            }, error: function (rs, e) {
                console.error(rs.responseText)
                $('#error-msg').css("display", "block");
                var errors = JSON.parse(rs.responseText)
                for (i in errors){
                    document.getElementById(i).style.borderColor = "red";
                    $('#error-msg').html($('#error-msg').html() + errors[i][0] + '<br />');
                }
            }, complete: function () {
                console.log('request completed')
            }

        }); // end ajax
    }

});
