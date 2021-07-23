$(document).ready(function () {
    $("#b_print").click(function () { print(); });



    var doc = new jsPDF();
    var specialElementHandlers = {
        '#print_table': function (element, renderer) {
            return true;
        }
    };


    $('#b_pdf').click(function () {
        doc.fromHTML($('#content').html(), 15, 15, {
            'width': 170,
            'elementHandlers': specialElementHandlers
        });
        doc.save('sample-file.pdf');
    });
});
