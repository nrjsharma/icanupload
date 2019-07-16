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
    var input_field_list = ['firstname', 'lastname', 'username', 'email', 'password', 'conform']
    for (var input_field_id of input_field_list) {
        document.getElementById(input_field_id).style.borderColor = "";
    }
}
$("#siginup-form").submit(function (event) {
    event.preventDefault();
    var empty_field_list = [];
    reset_variable()
    reset_border_color()
    var first_name = $('#firstname').val();
    var last_name = $('#lastname').val();
    var user_name = $('#username').val();
    var email = $('#email').val();
    var password = $('#password').val();
    var conform_password = $('#conform').val();
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
    if (!conform_password) {
        empty_field_list.push('conform')
    }
    if (empty_field_list.length > 0) {
        $('#error-msg').html('fill all required fields');
        $('#error-msg').css("display", "block");
        for (var empty_field_id of empty_field_list) {
            document.getElementById(empty_field_id).style.borderColor = "red";
        }
        console.info('fill all required fields')
    } else if (!compare_passwords(password, conform_password)) {
        document.getElementById('password').style.borderColor = "red";
        document.getElementById('conform').style.borderColor = "red";
        $('#error-msg').html('password did\'t match');
        $('#error-msg').css("display", "block");
        console.info('password did\'t match');
    } else if (password.length < 6) {
        document.getElementById('password').style.borderColor = "red";
        document.getElementById('conform').style.borderColor = "red";
        $('#error-msg').html('password must be of minimum 6 characters length');
        $('#error-msg').css("display", "block");
    }else{
        // submit form
    }

});
