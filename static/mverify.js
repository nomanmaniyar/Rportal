$(document).ready(function () {
    var base_color = "rgb(230,230,230)";
    var active_color = "rgb(237, 40, 70)";
    var chkError = false;

    var child = 1;
    var length = $("section").length - 1;
    $("#back").addClass("disabled");
    $("#submit").addClass("disabled");

    $("section").not("section:nth-of-type(1)").hide();
    $("section").not("section:nth-of-type(1)").css('transform', 'translateX(100px)');


});


