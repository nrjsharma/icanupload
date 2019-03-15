function openFileChooser() {
    $("#upload_btn").click(function () {
        $("#getFile").click();
    });
}

function startUploading() {
    $("#getFile").change(function () {
        var data = new FormData($('form')[1]);
        data.append('csrfmiddlewaretoken', $.cookie("csrftoken"));
        var form_url = $('#form_upload').attr('action');
        var form_type = $('#form_upload').attr('method');
        $.ajax({
            url: form_url,
            type: form_type,
            data: data,
            cache: false,
            processData: false,
            contentType: false,
            success: function (data) {
                alert(data);
            },error:function (rs,e) {
                alert(rs.responseText);
            }
        });
    });
}

$(document).ready(function () {
    openFileChooser();
    startUploading();
});


/*
 $.dialog({
 backgroundDismiss: true,
 animation: 'top',
 title: 'Alert!',
 content: 'Simple alert!',
 });*/
