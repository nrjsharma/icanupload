function openFileChooser() {
    $("#upload_btn").click(function () {
        $("#getFile").click();
    });
}

function startUploading() {
    $("#getFile").change(function () {
        $.dialog({
            backgroundDismiss: true,
            animation: 'top',
            title: 'Alert!',
            content: 'Simple alert!',
        });
    });
}

$(document).ready(function () {
    openFileChooser();
    startUploading();
});