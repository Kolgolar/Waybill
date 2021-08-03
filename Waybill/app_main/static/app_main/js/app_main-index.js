let pastedForms = [];
let timeDiffs = {};
const MAX_RIDES = 4

$(document).ready(function () {
    $("#b_add").click(addForm);
    $("#b_remove").click(removeForm);

    $("#tr_id").on("change", function () {
        let tr_id = $("#tr_id").val();
        setTrId(tr_id);
    });

    $(document).on("change", ".time_in_class", function () {
        let num = getElementNum($(this).attr("id"));
        let timeInVal = $("#time_in" + num).val();


        let new_val = toMinutes(timeInVal) + timeDiffs[num];
        new_val = toTimeFormat(new_val);
        $("#time_out" + num).val(new_val);
    });

    $(document).on("change", ".time_out_class", function () {
        let timeOutVal = $("#time_out" + num).val();
    });

    $(document).on("input", ".route_id_class", function () {
        let route_id = $(this).val();
        let element_id = $(this).attr("id");
        setRouteDescAndTime(route_id, getElementNum(element_id));
    });

});


function addForm() {
    if (pastedForms.length + 1 < MAX_RIDES) {
        let formClone = $("#form_to_clone").clone();
        formClone.find("input[type=text], textarea").val(""); // Очищаем все поля скопированной формы
        let idsToRename = ['ride_head', 'route_id', 'route_desc', 'time_in', 'time_out'];

        // Добавляем к id выбранных элементов номер, чтобы избежать дубликатов и иметь возможность обращаться к ним в будущем
        let idAddition = parseInt(pastedForms.length + 1);
        idsToRename.forEach(function (item, i, idsToRename) {
            formClone.find('#' + item).prop('id', item + idAddition);
        });

        if (pastedForms.length > 0)
            formClone.insertAfter(pastedForms[0]);
        else
            formClone.insertAfter($("#paste_form_here"));

        //Меняем текст заголовка у каждой поездки:
        ride_head_text = document.getElementById('ride_head').textContent;
        document.getElementById('ride_head' + idAddition).textContent = ride_head_text.substring(0, ride_head_text.length - 2) + parseInt(idAddition + 1) + ':';

        
        pastedForms.unshift(formClone);
    }
    else
        alert(`В маршрутном листе не может быть больше ${MAX_RIDES} поездок`);
}

function removeForm() {
    if (pastedForms.length > 0) {
        let formToDelete = pastedForms[0];
        formToDelete.remove()
        delete timeDiffs[pastedForms.length + 1];
        pastedForms.splice(0, 1);
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

function getElementNum(el_id) {
    let num = el_id.slice(-1);
    if (!isNaN(num))
        return num;
    else
        return "";
}


function toTimeFormat(minutes) {
    if (minutes > 0) {
        let hoursPart = (minutes - minutes % 60) / 60;
        let minutesPart = minutes % 60;
        let zeroBeforeMinutes = '';
        if (minutesPart < 10)
            zeroBeforeMinutes = '0';
        return `${hoursPart}:${zeroBeforeMinutes}${minutesPart}`;
    }
    else
        return '';
}

function toMinutes(time) {
    let hoursInMins = time.split(':');
    let minutes = parseInt(hoursInMins[0]) * 60 + parseInt(hoursInMins[1]);
    return minutes;
}


function setRouteDescAndTime(route_id, el_num) {
    let rout_desc = $("#route_desc" + el_num);
    let time_in = $("#time_in" + el_num);
    let time_out = $("#time_out" + el_num);

    $.ajax({
        type: "GET",
        url: "get_route_info",
        data: { "arg": route_id },
        success: function (response) {
            let data = $.parseJSON(response);
            rout_desc.val(data.description);
            time_in.val(toTimeFormat(data.time_in));
            time_out.val(toTimeFormat(data.time_out));
            timeDiffs[el_num] = data.time_out - data.time_in;
        },
        error: function (response) {
            rout_desc.val("");
        }
    });
    return tr_name;
}