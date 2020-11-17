function favPost(url) {
    console.log('Requesting JSON');
    $.post(url, {}, function (rowz) {
       console.log(url, 'finished');   
    }).fail(function (xhr) {
        alert('Url failed with ' + xhr.status + ' ' + url);
    });
}