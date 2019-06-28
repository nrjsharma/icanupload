/**
 * Created by neeraj on 31/03/19.
 */
function downloadModel(key, password="") {
    if(key) {
        $.ajax({
            url: SHOW_DOWNLOAD_LIST_URL + '/?token=' + key + '&password=' + password,
            type: 'GET',
            success: function (data) {
                var output = ""
                for(var value of data){
                    console.log(value)
                    output+='<p><a href='+value.document+' download>'+value.document_name+'</a></p>'
                }
                $.alert({
                    title: 'Download',
                    content: output,
                });
            }, error: function (response) {
                console.error(response.responseText);
                console.error(response.status);
                if(response.status == 404){
                    $.alert({
                        title: 'Password didn\'t match!',
                        content: 'entered password did\'t match',
                    });
                }else{
                    $.alert({
                        title: 'Error!',
                        content: response.status,
                    });
                }
            }
        }); // ajax
    }else{
        alert('key is null')
    }
}