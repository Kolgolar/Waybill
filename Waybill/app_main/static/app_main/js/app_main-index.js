let pasted_forms = [];

function addForm() {
    let formClone = $("#form_to_clone").clone();
    formClone.find("input[type=text], textarea").val("");

    if (pasted_forms.length > 0)
        formClone.insertAfter(pasted_forms[0]);
    else
        formClone.insertAfter($("#paste_form_here"));    

    pasted_forms.unshift(formClone);
}

function removeForm() {
    if (pasted_forms.length > 0) {
        let formToDelete = pasted_forms[0];
        formToDelete.remove()
        pasted_forms.splice(0, 1);
    }
}

function setTrId(tr_id) {    
    $.ajax({
        type: "GET",
        url: "get_transport_name",
        data: { "arg": tr_id },
        success: function (response) {
            $("#tr_name").val(response);
        },
        error: function (response) {
            $("#tr_name").val("");
        }
    });
    return tr_name;
}


$(document).ready(function () {
    $("#b_add").click(addForm);
    $("#b_remove").click(removeForm);

    $("#tr_id").on("change", function () {
        let tr_id = $("#tr_id").val();
        setTrId(tr_id);
    });
});
