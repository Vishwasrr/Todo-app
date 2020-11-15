function pushdown(ckb) {
    const element = event.target;
    if (element.type === "checkbox") {
        if (element.checked) {
            element.parentNode.style.textDecoration = "line-through";
            element.parentNode.style.opacity = 0.5;

            const parent = element.parentElement.parentElement;
            parent.appendChild(element.parentElement);
        } else {
            element.parentNode.style.textDecoration = "none";
            element.parentNode.style.opacity = 1;

            const parent = element.parentElement.parentElement;
            parent.insertBefore(element.parentElement, parent.firstChild);
        }
    }
}

$("#btn").click(function () {
    var txt = $("#txt_item").val();
    // make sure the text is not empty
    if (txt.trim().length > 0) {
        //create li item
        var item = $("<li></li>")
            .append("<input type='checkbox'>")   // add checkbox
            .append(txt);                        // add text string

        $("#list").prepend(item);              // put the item at the top of the list
        $("#txt_item").val("");                // clear the textbox for next item 

    }

});



//since we will be adding elements dynamically, we can't use $().change()
// we have to use $(document).on() 

$(document).on('change', '#list input[type=checkbox]', function () {

    //do we have a checked box?
    if ($(this).is(":checked")) {  // if yes:

        var last = $("#list li").last();     // locate the last item
        $(this).parent().insertAfter(last);  // insert current one after it (at bottom)
    } else {
        // if not
        var first = $("#list li").first();   // locate the first item
        $(this).parent().insertBefore(first);// insert current one before it (on top)
    }
});