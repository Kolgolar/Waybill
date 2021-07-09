function addForm() {
    let formClone = $("#form_to_clone").clone();
    formClone.appendTo($("#paste_form_here"));
}

function removeForm() {
    $("#paste_form_here").last().remove();
}


$(document).ready(function () {
    $("#b_add").click(addForm);
    $("#b_remove").click(removeForm);
})