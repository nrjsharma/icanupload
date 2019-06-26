var token;
var password;
var get_token = {
    'X-CSRFToken': $.cookie("csrftoken")
}


function openFileChooser() {
    $("#upload_btn").click(function () {
        $("#getFile").click();
    });
}

function search() {
    $("#search_form").submit(function (event) {
        var key = $("#search_key").val();
        event.preventDefault();
        if (key){
         window.location.href = '/?s='+key;
        }else{
            window.location.href = '/';
        }
    });
}


function ShowPassword() {
    $("#done_password").attr("type", "text");
}

function CopyLink() {

    var tempInput = document.createElement("input");
    tempInput.style = "position: absolute; left: -1000px; top: -1000px";
    tempInput.value = document.getElementById("done_link").value;
    document.body.appendChild(tempInput);
    tempInput.select();
    document.execCommand("copy");
    document.body.removeChild(tempInput);
    $.alert({
        icon: 'fas fa-thumbs-up',
        title: 'Done',
        content: 'Link Copy Successfully',
        type: 'green',
    });

}


function DoneModal() {
    var urls = "icanupload.com/?s=" + token
    if (password) {
        $.dialog({
            backgroundDismiss: false,
            boxWidth: '300px',
            icon: 'fas fa-check-circle',
            useBootstrap: false,
            animation: 'top',
            title: 'Done',
            content: '' +
            '<form class="formName" id="main_form" method="post">' +
            '<div class="form-group">' +
            '<label>key</label>' +
            '<input type="text" id="done_token" placeholder="Your name" name="token" class="name form-control" value=' + token + ' disabled="true"  required/>' +
            '<label style="margin-top: 10px">password</label><a href="javascript:ShowPassword()" style="padding-left: 10px">show</a>' +
            '<input type="password" id="done_password" placeholder="optional" name="password" class="name form-control"  disabled="true" value = ' + password + ' />' +
            '<label style="margin-top: 10px">link</label><a href="javascript:CopyLink()" style="padding-left: 10px">copy</a>' +
            '<input type="url" id="done_link" placeholder="optional" name="password" class="name form-control" value= ' + urls + ' disabled />' +
            '</form>',
            close: function (event, ui) {
                location.reload();
            }
        });
    } else {
        $.dialog({
            backgroundDismiss: false,
            boxWidth: '300px',
            icon: 'fas fa-check-circle',
            useBootstrap: false,
            animation: 'top',
            title: 'Done',
            content: '' +
            '<form class="formName" id="main_form" method="post">' +
            '<div class="form-group">' +
            '<label>key</label>' +
            '<input type="text" id="done_token" placeholder="Your name" name="token" class="name form-control" value=' + token + ' disabled="true"  required/>' +
            '<label style="margin-top: 10px">link</label><a href="#" onclick="CopyLink()" style="padding-left: 10px">copy</a>' +
            '<input type="url" id="done_link" placeholder="optional" name="password" class="name form-control" value= ' + urls + ' disabled />' +
            '</form>',
            close: function (event, ui) {
                location.reload();
            }
        });
    }
}

function SavePassword() {
    token = $('#in_token').val()
    password = $('#in_password').val()
    var delete_after = $('input[name=time]:checked').val();
    $.ajax({
        url: SAVE_PASSWORD_URL+ token + '/',
        headers: get_token,
        type: 'PATCH',
        data: {
            'password': password,
            'delete_after': delete_after,
            'csrfmiddlewaretoken': $.cookie("csrftoken")
        },
        success: function (data) {
            DoneModal()
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
                $.confirm({
                    backgroundDismiss: false,
                    boxWidth: '300px',
                    icon: 'fas fa-file-upload',
                    useBootstrap: false,
                    animation: 'top',
                    title: 'Upload File',
                    content: '' +
                    '<form class="formName" id="main_form" method="patch">' +
                    '<div class="form-group">' +
                    '<label>key</label>' +
                    '<input type="text" id="in_token" placeholder="Your name" name="token" class="name form-control" value=' + data + ' disabled="true"  required/>' +
                    '<label style="margin-top: 10px">password</label>' +
                    '<input type="password" id="in_password" placeholder="optional" name="password" class="name form-control" />' +
                    '<label style="margin-top: 10px;padding-bottom: 2px;">delete after</label>' +
                    '<div id="radiobtn" style="margin-top: -6px;">' +
                    '<div style="float: left;padding-left: 2px;">' +
                    '<span style="float: left;width: 16px;"><input type="radio" value="1" autocomplete="off" name="time" checked/></span> <span style="float: right">1 day</span>' +
                    '</div>' +
                    '<div style="float: left;padding-left: 10px;">' +
                    '<span style="float: left;width: 16px;"><input type="radio" value="3" autocomplete="off" name="time"/></span> <span style="float: right">3 day</span>' +
                    '</div>' +
                    '<div style="float: left;padding-left: 10px;">' +
                    '<span style="float: left;width: 16px;"><input type="radio" value="7" autocomplete="off" name="time" /></span> <span style="float: right">7 day</span>' +
                    '</div>' +
                    '<div style="float: left;padding-left: 10px;">' +
                    '<span style="float: left;width: 16px;"><input type="radio" value="30" autocomplete="off" name="time" /></span> <span style="float: right">30 day</span>' +
                    '</div>' +
                    '</div><!--radiobtn-->' +
                    '</div>' +
                    '<input type="hidden" name="hidden_token" value="' + data + '">' +
                    '</form>',
                    buttons: {
                        formSubmit: {
                            text: 'done',
                            btnClass: 'btn btn-primary btn-lg modal-button',
                            action: function () {
                                SavePassword()
                            }
                        },
                    }
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
    search();
});
