var get_token = {
    'X-CSRFToken': $.cookie("csrftoken")
}
function reset_variable() {
    $('#error-msg').html('');
    $('#error-msg').css("display", "none");
}

function reset_border_color() {
    var input_field_list = ['username', 'password']
    for (var input_field_id of input_field_list) {
        document.getElementById(input_field_id).style.borderColor = "";
    }
}

$("#login-form").submit(function (event) {
    event.preventDefault();
    var empty_field_list = [];
    reset_variable();
    reset_border_color();
    var user_name = $('#username').val();
    var password = $('#password').val();
    if (!user_name) {
        empty_field_list.push('username')
    }
    if (!password) {
        empty_field_list.push('password')
    }

    if (empty_field_list.length > 0) {
        $('#error-msg').html('fill all required fields');
        $('#error-msg').css("display", "block");
        for (var empty_field_id of empty_field_list) {
            document.getElementById(empty_field_id).style.borderColor = "red";
        }
        console.info('fill all required fields')
    } else {
        let form = $('#login-form');
        let form_data = form.serialize();
        $.ajax({
            url: LOGIN_URL,
            headers: get_token,
            type: "post",
            data: form_data,
            success: function (data) {
                alert('user Login')
            }, error: function (rs, e) {
                console.error(rs.responseText)
                console.error(rs.status)
                if (rs.status == 404) {
                    $('#error-msg').html("user not found");
                } else {
                    var errors = JSON.parse(rs.responseText)
                    for (i in errors) {
                        $('#error-msg').html($('#error-msg').html() + errors[i] + '<br />');
                    }
                }
                 $('#error-msg').css("display", "block");
            }, complete: function () {
                console.log('request completed')
            }

        }); // end ajax
    }
});