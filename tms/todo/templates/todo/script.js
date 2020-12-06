function favPost(url) {
    console.log('Requesting JSON');
    $.post(url, {}, function (rowz) {
        console.log(url, 'finished');
        location.reload(true);
    }).fail(function (xhr) {
        alert('Url failed with ' + xhr.status + ' ' + url);
    });


}

function myFunction() {
    var x = document.getElementById("myDIV");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

function Submitform() {
    var x = document.getElementById("myForm").elements[0].value;
    var y = document.getElementById("myForm").elements[1].value;
    console.log(x)
    $.post("/create/", {
        task: x,
        desc: y,
        csrfmiddlewaretoken: '{{csrf_token}}'
    }, function (rowz) {
        console.log('finished');
        location.reload(true);
    }).fail(function (xhr) {
        alert('Url failed with ' + xhr.status + ' ' + url);
    });


}
