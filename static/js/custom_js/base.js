function openFileChooser() {
    $("#upload_btn").click(function () {
        $("#getFile").click();
    });
}

function startUploading() {
    $("#getFile").change(function () {
        var progress_bar = new ldBar("#progressBar") ;
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
                    if(percent<100){
                        progress_bar.set( Math.round(percent));
                    }
                    else {
                        document.getElementById("progressBar").innerHTML="<i>loading...</i>";
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
                    backgroundDismiss: true,
                    animation: 'top',
                    title: 'Done!',
                    content: data,
                });
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
