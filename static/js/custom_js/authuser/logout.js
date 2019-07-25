/**
 * Created by neeraj on 25/07/19.
 */
$("#logout_form").submit(function (event) {
    event.preventDefault();
    let form = $('#logout_form');
    $.ajax({
        url: LOGOUT_URL,
        type: "post",
        data: form.serialize(),
        success: function (data) {
            window.location = '/'
        }, error: function (rs, e) {
            console.error(rs.responseText)
            console.error(rs.status)
        }, complete: function () {
            console.log('request completed')
        }

    }); // end ajax
});