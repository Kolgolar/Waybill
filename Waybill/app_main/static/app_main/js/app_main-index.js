function addForm() {
    let formClone = $("#form_to_clone").clone();
    formClone.find("input[type=text], textarea").val("");
    formClone.appendTo($("#paste_form_here"));
}

function removeForm() {
    let formToDelete = $("#paste_form_here").children(':first');
    formToDelete.remove();
}

function sendForm(e) {
    var info = $("#wbform").serialize();
    e.preventDefault();
    $.ajax({
        url: '',
        type: 'post',
        dataType: 'json',
        data: $("#wbform").serialize(),
        success: function (data) {
            alert("fock");
        }

    })
    alert('fuck you')
}


$(document).ready(function () {
    $("#b_add").click(addForm);
    $("#b_remove").click(removeForm);

    $("#b_submit").click(function (e) {
        sendForm(e);
    });
})