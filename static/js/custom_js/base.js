function openFileChooser() {
    $("#upload_btn").click(function () {
        $("#getFile").click();
    });
}

function SavePassword(event) {
    var token = $('#in_token').val()
    var password = $('#in_password').val()
    $.ajax({
        url: '/save-password/',
        type: 'POST',
        data: {'token':token, 'password':password, 'csrfmiddlewaretoken':$.cookie("csrftoken")},
        success: function (data) {
            alert('success')
            alert(data)
        }, error: function (rs, e) {
            alert('error')
            alert(rs.responseText);
        }

    });
}

function startUploading() {
    $("#getFile").change(function () {
        var progress_bar = new ldBar("#progressBar");
        var data = new FormData($('form')[1]);
        data.append('csrfmiddlewaretoken', $.cookie("csrftoken"));
        var form_url = $('#form_upload').attr('action');
        var form_type = $('#form_upload').attr('method');
        $('.ldBar-label').hide(); // hiding progress_bar percentage
        $('#form_upload').hide();
        $.ajax({
            // xhr method is for Progress bar
            xhr: function () {
                var xhr = new window.XMLHttpRequest();

                xhr.upload.addEventListener("progress", function (evt) {
                    var percent = Math.round(evt.loaded / evt.total * 100)
                    if (percent < 100) {
                        progress_bar.set(Math.round(percent));
                    }
                    else {
                        document.getElementById("progressBar").innerHTML = "<i>loading...</i>";
                    }
                });
                return xhr;
            },
            url: form_url,
            type: form_type,
            data: data,
            cache: false,
            processData: false,
            contentType: false,
            success: function (data) {
                $.dialog({
                    backgroundDismiss: false,
                    boxWidth: '300px',
                    icon: 'fas fa-file-upload',
                    useBootstrap: false,
                    animation: 'top',
                    title: 'Upload File',
                    content: '' +
                    '<form class="formName" id="main_form" method="post" onsubmit="SavePassword();return false;">' +
                    '<div class="form-group">' +
                    '<label>key</label>' +
                    '<input type="text" id="in_token" placeholder="Your name" name="token" class="name form-control" value=' + data + ' disabled="true"  required/>' +
                    '<label style="margin-top: 10px">password</label>' +
                    '<input type="password" id="in_password" placeholder="optional" name="password" class="name form-control" />' +
                    '<button class="btn btn-primary btn-lg" style="width: 100%;margin-top: 13px">Save</button>' +
                    '</div>' +
                    '<input type="hidden" name="hidden_token" value="' + data + '">' +
                    '</form>',
                });
            }, error: function (rs, e) {
                alert(rs.responseText);
            }
        });
    });
}


$(document).ready(function () {
    openFileChooser();
    startUploading();
});
