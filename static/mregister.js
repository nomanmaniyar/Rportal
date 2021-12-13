$(document).ready(function () {
    var chkError = false;

    var child = 1;
    var length = $("section").length - 1;
    console.log(length)
    $("#c2").hide();

    $("#prev").hide();
    $("#submit").hide();

    $(".button").click(function () {
        var id = $(this).attr("id");
        if (id == "next") {
            console.log("NEXT Section", child);
            if (child == 1) {
                //validate screen 1
                console.log("Validating screen 1 on next button");
                validateScreen1();
                console.log("V1 chkerror: ", chkError);
            } else if (child == 2) {
                //validate screen 2
                console.log("Validating screen 2 on next button");
                validateScreen2();
                console.log("V2 chkerror: ", chkError);
            }
            if (chkError == false) {
                console.log("$('#prev').removeClass('disabled');")
                $("#back").hide();
                $("#prev").show();
                if (child >= length) {
                    $(this).hide();
                    $('#submit').show();
                }
            }
            if (child <= length) {
                child++;
            }
            chkError = false
        } else if (id == "prev") {
            console.log("PREV Section", child);
            if (child == 2) {
                //validate screen 2
                console.log("Validating screen 2 on prev button");
                validateScreen2();
                console.log("V2 chkerror prev: ", chkError);
            }
            
            if (chkError == false) {
                $("#prev").hide();
                $("#next").show();
                $("#back").show();
                $('#submit').hide();
            }else{
                child++;
            }

            if (child <= 2) {
                $(this).hide;
            }
            if (child > 1) {
                child--;
            }
            chkError = false;
        }
        var currentSection = $("section:nth-of-type(" + child + ")");
        currentSection.fadeIn();
        currentSection.css('transform', 'translateX(0)');
        currentSection.prevAll('section').css('transform', 'translateX(-100px)');
        currentSection.nextAll('section').css('transform', 'translateX(100px)');
        $('section').not(currentSection).hide();
    });

    function validateScreen1() {
        console.log("HI---V1")
        // console.log("chkerror: ", chkError);
        var name = $("#Mname").val();
        var username = $("#Musername").val();
        var code = $("#Mcode").val();
        var flatno = $("#Mflatno").val();
        var swing = $("#Mwing").val();
        // var mobile = $("#Smobile").val();
        // var password = $("#Spassword").val();

        var nameError = '';
        var usernameEror = '';
        var codeEror = '';
        var flatnoEror = '';
        var swingEror = '';
        // var mobileEror = '';
        // var passwordEror = '';
        document.getElementById("Mpname").innerHTML = nameError;
        document.getElementById("Mpusername").innerHTML = usernameEror;
        document.getElementById("Mpcode").innerHTML = codeEror;
        document.getElementById("Mpflatno").innerHTML = flatnoEror;
        document.getElementById("Mpwing").innerHTML = swingEror;
        // document.getElementById("Spmobile").innerHTML = mobileEror;
        // document.getElementById("Sppassword").innerHTML = passwordEror

        if (name.length < 1) {

            child--;
            chkError = true;
            nameError = "Name is required"
            document.getElementById("Mpname").innerHTML = nameError;
            console.log(name, ' Length is: ', name.length);

        } if (username.length < 1) {

            if (child == 0) {
                chkError = true;
                usernameEror = "Username is required"
                document.getElementById("Mpusername").innerHTML = usernameEror;
                console.log(username, ' Length is: ', username.length);
            }
            else {
                child--;
                chkError = true;
                usernameEror = "Username is required"
                document.getElementById("Mpusername").innerHTML = usernameEror;
                console.log(username, ' Length is: ', username.length);
            }
        } if (code.length < 1) {

            if (child == 0) {
                chkError = true;
                codeEror = "R-Code is required"
                document.getElementById("Mpcode").innerHTML = codeEror;
                console.log(code, ' Length is: ', code.length);
            }
            else {

                child--;
                chkError = true;
                codeEror = "R-Code is required"
                document.getElementById("Mpcode").innerHTML = codeEror;
                console.log(code, ' Length is: ', code.length);
            }

        }
        if (flatno.length < 1) {

            if (child == 0) {
                chkError = true;
                flatnoEror = "Flat No is required"
                document.getElementById("Mpflatno").innerHTML = flatnoEror;
                console.log(flatno, ' Length is: ', flatno.length);
            }
            else {
                child--;
                chkError = true;
                flatnoEror = "Flat No is required"
                document.getElementById("Mpflatno").innerHTML = flatnoEror;
                console.log(flatno, ' Length is: ', flatno.length);
            }
        }

        if (swing.length < 1) {

            if (child == 0) {
                chkError = true;
                swingEror = "Wing Name/No is required"
                document.getElementById("Mpwing").innerHTML = swingEror;
                console.log(swing, ' Length is: ', swing.length);
            }
            else {
                child--;
                chkError = true;
                swingEror = "Wing Name/No is required"
                document.getElementById("Mpwing").innerHTML = swingEror;
                console.log(swing, ' Length is: ', swing.length);
            }
        }
    }
    function validateScreen2() {
        console.log("HI---V2")
        // console.log("chkerror: ", chkError);

        var email = $("#Memail").val();
        var mobile = $("#Mmobile").val();
        var password = $("#Mpassword").val();

        var emailEror = '';
        var mobileEror = '';
        var passwordEror = '';

        document.getElementById("Mpemail").innerHTML = emailEror;
        document.getElementById("Mpmobile").innerHTML = mobileEror;
        document.getElementById("Mppassword").innerHTML = passwordEror
        if (email.length < 1) {

            if (child == 0) {
                chkError = true;
                emailEror = "Email is required"
                document.getElementById("Mpemail").innerHTML = emailEror;
                console.log(email, ' Length is: ', email.length);
            }
            else {

                child--;
                chkError = true;
                emailEror = "Email is required"
                document.getElementById("Mpemail").innerHTML = emailEror;
                console.log(email, ' Length is: ', email.length);
            }

        } else {

            var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;

            if (email.match(validRegex)) {
                console.log(email, "true");
            } else {
                if (child == 0) {
                    chkError = true;
                    emailEror = "Invalid email address!";
                    document.getElementById("Mpemail").innerHTML = emailEror;
                    console.log(email, "false");

                    // document.form.Semail.focus();
                }
                else {
                    child--;
                    chkError = true;
                    emailEror = "Invalid email address!";
                    document.getElementById("Mpemail").innerHTML = emailEror;
                    console.log(email, "false");
                    // document.form.Semail.focus();
                }
            }
        }

        if (mobile.length < 1) {

            if (child == 0) {
                chkError = true;
                mobileEror = "Mobile No is required"
                document.getElementById("Mpmobile").innerHTML = mobileEror;
                console.log(mobile, ' Length is: ', mobile.length);
            }
            else {
                child--;
                chkError = true;
                mobileEror = "Mobile No is required"
                document.getElementById("Mpmobile").innerHTML = mobileEror;
                console.log(mobile, ' Length is: ', mobile.length);
            }
        } else {

            if (mobile.length >= 11) {
                if (child == 0) {
                    chkError = true;
                    mobileEror = "invalid Mobile No is "
                    document.getElementById("Mpmobile").innerHTML = mobileEror;
                    console.log(mobile, ' Length is: ', mobile.length);
                }
                else {
                    child--;
                    chkError = true;
                    mobileEror = "invalid Mobile No is "
                    document.getElementById("Mpmobile").innerHTML = mobileEror;
                    console.log(mobile, ' Length is: ', mobile.length);
                }
            }

        }
        if (password.length < 1) {
            if (child == 0) {
                chkError = true;
                passwordEror = "Password is required"
                document.getElementById("Mppassword").innerHTML = passwordEror
                console.log(password, ' Length is: ', password.length);
            }
            else {
                child--;
                chkError = true;
                passwordEror = "Password is required"
                document.getElementById("Mppassword").innerHTML = passwordEror
                console.log(password, ' Length is: ', password.length);
            }
        }
        else {
            var decimal = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,15}$/;
            if (password.match(decimal)) {
                console.log(password, "true");
            } else {
                if (child == 0) {
                    chkError = true;
                    passwordEror = "password must be between 8 to 15 characters which contain at least one lowercase letter, one uppercase letter, one numeric digit, and one special character";
                    document.getElementById("Mppassword").innerHTML = passwordEror;
                    console.log(password, "false");

                    // document.form.Semail.focus();
                }
                else {
                    child--;
                    chkError = true;
                    passwordEror = "password must be between 8 to 15 characters which contain at least one lowercase letter, one uppercase letter, one numeric digit, and one special character";
                    document.getElementById("Mppassword").innerHTML = passwordEror;
                    console.log(password, "false");

                    // document.form.Semail.focus();
                }
            }
        }
    }

});