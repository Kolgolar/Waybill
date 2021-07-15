let pasted_forms = [];
const MAX_ROWS = 5

function addForm() {
    if (pasted_forms.length + 1 < MAX_ROWS) {
        let formClone = $("#form_to_clone").clone();
        formClone.find("input[type=text], textarea").val("");
        formClone.find('#route_id').prop('id', 'route_id' + parseInt(pasted_forms.length + 1));
        formClone.find('#route_desc').prop('id', 'route_desc' + parseInt(pasted_forms.length + 1));
        //TODO: Менять id у всех полей строки

        if (pasted_forms.length > 0)
            formClone.insertAfter(pasted_forms[0]);
        else
            formClone.insertAfter($("#paste_form_here"));
        pasted_forms.unshift(formClone);
    }
    else
        alert(`Вы таблице не может быть больше ${MAX_ROWS} строк`);
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
            $("#tr_name").val("ТС не найдено!");
        }
    });
    return tr_name;
}



function setRouteDesc(route_id, el_id) {
    let num;
    if (el_id == "route_id")
        num = "";
    else
        num = el_id.slice(-1);
        
    let rout_desc = $("#route_desc" + num);


    $.ajax({
        type: "GET",
        url: "get_route_desc",
        data: { "arg": route_id },
        success: function (response) {
            rout_desc.val(response);
        },
        error: function (response) {
            rout_desc.val("");
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

    $(document).on("input", ".route_id_class", function () {
        let route_id = $(this).val();
        let element_id = $(this).attr("id");
        setRouteDesc(route_id, element_id);
    });
    
});
