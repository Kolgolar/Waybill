function addForm() {
    alert("YES");
    let formClone = $("#form_to_clone").clone();
    formClone.appendTo($("#paste_form_here"));
}

function removeForm() {

}


$(document).ready(function () {
    $("#b_add").click(addForm());
    $("#b_remove").click(removeFrom());
})