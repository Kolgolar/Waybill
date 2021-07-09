function addForm() {
    let formClone = $("#form_to_clone").clone();
    formClone.appendTo($("#paste_form_here"));
}

function removeForm() {
    let formToDelete = $("#paste_form_here").children(':first');
    formToDelete.remove();
}


$(document).ready(function () {
    $("#b_add").click(addForm);
    $("#b_remove").click(removeForm);
})