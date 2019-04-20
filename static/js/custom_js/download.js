/**
 * Created by neeraj on 31/03/19.
 */
function downloadModel(key, password=null) {
    if(key) {
        $.ajax({
            url: 'api/v1/show-download-list/?token=' + key + '&password=' + password,
            type: 'GET',
            success: function (data) {
                for(var value of data){
                    console.log(value)
                }
            }, error: function (responce) {
                alert(responce.responseText);
                alert(responce.status);
            }
        }); // ajax
    }else{
        alert('key is null')
    }
}