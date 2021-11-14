$(document).ready(function () {
    var base_color = "rgb(230,230,230)";
    var active_color = "rgb(237, 40, 70)";
    var chkError = false;

    var child = 1;
    var length = $("section").length - 1;
    $("#prev").addClass("disabled");
    $("#submit").addClass("disabled");

    $("section").not("section:nth-of-type(1)").hide();
    $("section").not("section:nth-of-type(1)").css('transform', 'translateX(100px)');

    var svgWidth = length * 200 + 24;
    $("#svg_wrap").html(
        '<svg version="1.1" id="svg_form_time" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 ' +
        svgWidth +
        ' 24" xml:space="preserve"></svg>'
    );

    function makeSVG(tag, attrs) {
        var el = document.createElementNS("http://www.w3.org/2000/svg", tag);
        for (var k in attrs) el.setAttribute(k, attrs[k]);
        return el;
    }

    for (i = 0; i < length; i++) {
        var positionX = 12 + i * 200;
        var rect = makeSVG("rect", { x: positionX, y: 9, width: 200, height: 6 });
        document.getElementById("svg_form_time").appendChild(rect);
        // <g><rect x="12" y="9" width="200" height="6"></rect></g>'
        var circle = makeSVG("circle", {
            cx: positionX,
            cy: 12,
            r: 12,
            width: positionX,
            height: 6
        });
        document.getElementById("svg_form_time").appendChild(circle);
    }

    var circle = makeSVG("circle", {
        cx: positionX + 200,
        cy: 12,
        r: 12,
        width: positionX,
        height: 6
    });
    document.getElementById("svg_form_time").appendChild(circle);

    $('#svg_form_time rect').css('fill', base_color);
    $('#svg_form_time circle').css('fill', base_color);
    $("circle:nth-of-type(1)").css("fill", active_color);


    $(".button").click(function () {
        var form = $("#form");
        $("#svg_form_time rect").css("fill", active_color);
        $("#svg_form_time circle").css("fill", active_color);
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
            } else if (child == 3) {
                //validate screen 3
                console.log("Validating screen 3 on button");
                validateScreen3();
            }
            if (chkError == false) {
                console.log("$('#prev').removeClass('disabled');")
                $("#prev").removeClass("disabled");
                if (child >= length) {
                    $(this).addClass("disabled");
                    $('#submit').removeClass("disabled");
                }
            }
            if (child <= length) {
                child++;
            }
            chkError = false
        } else if (id == "prev") {
            console.log("PREV Section", child);
            if (child == 1) {
                //validate screen 1
                console.log("Validating screen 1 on prev button");
                validateScreen1();
                console.log("V1 chkerror prev: ", chkError);
            } else if (child == 2) {
                //validate screen 2
                console.log("Validating screen 2 on prev button");
                validateScreen2();
                console.log("V2 chkerror prev: ", chkError);
            } else if (child == 3) {
                //validate screen 3
                console.log("Validating screen 3 on button");
                validateScreen3();
                console.log("V3 chkerror prev: ", chkError);
            }
            if (chkError == false) {
                $("#next").removeClass("disabled");
                $('#submit').addClass("disabled");
            }
            if (child <= 2) {
                $(this).addClass("disabled");
            }
            if (child > 1) {
                child--;
            }
            chkError = false;
        } else {
            console.log("else")
            //validate screen 3
            validateScreen3();
            console.log("Submit Section", child);

            if (child < length) {
                child++
            }
            chkError = false
        }
        var circle_child = child + 1;
        $("#svg_form_time rect:nth-of-type(n + " + child + ")").css(
            "fill",
            base_color
        );
        $("#svg_form_time circle:nth-of-type(n + " + circle_child + ")").css(
            "fill",
            base_color
        );
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
        var name = $("#Sname").val();
        var username = $("#Susername").val();
        var email = $("#Semail").val();
        var flatno = $("#Sflatno").val();
        var swing = $("#Swing").val();
        var mobile = $("#Smobile").val();
        var password = $("#Spassword").val();

        var nameError = '';
        var usernameEror = '';
        var emailEror = '';
        var flatnoEror = '';
        var swingEror = '';
        var mobileEror = '';
        var passwordEror = '';
        document.getElementById("Spname").innerHTML = nameError;
        document.getElementById("Spusername").innerHTML = usernameEror;
        document.getElementById("Spemail").innerHTML = emailEror;
        document.getElementById("Spflatno").innerHTML = flatnoEror;
        document.getElementById("Spwing").innerHTML = swingEror;
        document.getElementById("Spmobile").innerHTML = mobileEror;
        document.getElementById("Sppassword").innerHTML = passwordEror

        if (name.length < 1) {

            child--;
            chkError = true;
            nameError = "Name is required"
            document.getElementById("Spname").innerHTML = nameError;
            console.log(name, ' Length is: ', name.length);

        } if (username.length < 1) {

            if (child == 0) {
                chkError = true;
                usernameEror = "Username is required"
                document.getElementById("Spusername").innerHTML = usernameEror;
                console.log(username, ' Length is: ', username.length);
            }
            else {
                child--;
                chkError = true;
                usernameEror = "Username is required"
                document.getElementById("Spusername").innerHTML = usernameEror;
                console.log(username, ' Length is: ', username.length);
            }
        } if (email.length < 1) {

            if (child == 0) {
                chkError = true;
                emailEror = "Email is required"
                document.getElementById("Spemail").innerHTML = emailEror;
                console.log(email, ' Length is: ', email.length);
            }
            else {

                child--;
                chkError = true;
                emailEror = "Email is required"
                document.getElementById("Spemail").innerHTML = emailEror;
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
                    document.getElementById("Spemail").innerHTML = emailEror;
                    console.log(email, "false");

                    // document.form.Semail.focus();
                }
                else {
                    child--;
                    chkError = true;
                    emailEror = "Invalid email address!";
                    document.getElementById("Spemail").innerHTML = emailEror;
                    console.log(email, "false");
                    // document.form.Semail.focus();
                }
            }
        }
        if (flatno.length < 1) {

            if (child == 0) {
                chkError = true;
                flatnoEror = "Flat No is required"
                document.getElementById("Spflatno").innerHTML = flatnoEror;
                console.log(flatno, ' Length is: ', flatno.length);
            }
            else {
                child--;
                chkError = true;
                flatnoEror = "Flat No is required"
                document.getElementById("Spslatno").innerHTML = flatnoEror;
                console.log(flatno, ' Length is: ', flatno.length);
            }
        }

        if (swing.length < 1) {

            if (child == 0) {
                chkError = true;
                swingEror = "Wing Name/No is required"
                document.getElementById("Spwing").innerHTML = swingEror;
                console.log(swing, ' Length is: ', swing.length);
            }
            else {
                child--;
                chkError = true;
                swingEror = "Wing Name/No is required"
                document.getElementById("Spwing").innerHTML = swingEror;
                console.log(swing, ' Length is: ', swing.length);
            }
        }
        if (mobile.length < 1) {

            if (child == 0) {
                chkError = true;
                mobileEror = "Mobile No is required"
                document.getElementById("Spmobile").innerHTML = mobileEror;
                console.log(mobile, ' Length is: ', mobile.length);
            }
            else {
                child--;
                chkError = true;
                mobileEror = "Mobile No is required"
                document.getElementById("Spmobile").innerHTML = mobileEror;
                console.log(mobile, ' Length is: ', mobile.length);
            }
        } else {

            if (mobile.length >= 11) {
                if (child == 0) {
                    chkError = true;
                    mobileEror = "invalid Mobile No is "
                    document.getElementById("Spmobile").innerHTML = mobileEror;
                    console.log(mobile, ' Length is: ', mobile.length);
                }
                else {
                    child--;
                    chkError = true;
                    mobileEror = "invalid Mobile No is "
                    document.getElementById("Spmobile").innerHTML = mobileEror;
                    console.log(mobile, ' Length is: ', mobile.length);
                }
            }

        }
        if (password.length < 1) {
            if (child == 0) {
                chkError = true;
                passwordEror = "Password is required"
                document.getElementById("Sppassword").innerHTML = passwordEror
                console.log(password, ' Length is: ', password.length);
            }
            else {
                child--;
                chkError = true;
                passwordEror = "Password is required"
                document.getElementById("Sppassword").innerHTML = passwordEror
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
                    document.getElementById("Sppassword").innerHTML = passwordEror;
                    console.log(password, "false");

                    // document.form.Semail.focus();
                }
                else {
                    child--;
                    chkError = true;
                    passwordEror = "password must be between 8 to 15 characters which contain at least one lowercase letter, one uppercase letter, one numeric digit, and one special character";
                    document.getElementById("Sppassword").innerHTML = passwordEror;
                    console.log(password, "false");

                    // document.form.Semail.focus();
                }
            }
        }
    }


    function validateScreen2() {


        console.log("HI---V2")
        // console.log("chkerror: ", chkError);
        // console.log("child:: ", child);

        var name = $("#name").val();
        var area = $("#area").val();
        var road = $("#road").val();
        var city = $("#city").val();
        var state = $("#state").val();
        var pin = $("#pin").val();


        var nameError = '';
        var areaEror = '';
        var roadEror = '';
        var cityEror = '';
        var stateEror = '';
        var pinEror = '';

        document.getElementById("Sspname").innerHTML = nameError;
        document.getElementById("Sparea").innerHTML = areaEror;
        document.getElementById("Sproad").innerHTML = roadEror;
        document.getElementById("Spcity").innerHTML = cityEror;
        document.getElementById("Spstate").innerHTML = stateEror;
        document.getElementById("Sppin").innerHTML = pinEror;


        if (name.length < 1) {
            child--;
            chkError = true;
            nameError = "Society Name is required"
            document.getElementById("Sspname").innerHTML = nameError;
            console.log(name, ' Length is: ', name.length);

        }
        if (area.length < 1) {
            if (child == 1) {
                chkError = true;
                areaEror = "Area is required"
                document.getElementById("Sparea").innerHTML = areaEror;
                console.log(area, ' Length is: ', area.length);
            }
            else if (child == 2) {
                child--;
                chkError = true;
                areaEror = "Area is required"
                document.getElementById("Sparea").innerHTML = areaEror;
                console.log(area, ' Length is: ', area.length);
            }
        }
        if (road.length < 1) {
            if (child == 1) {
                chkError = true;
                roadEror = "Landmark is required"
                document.getElementById("Sproad").innerHTML = roadEror;
                console.log(road, ' Length is: ', road.length);
            }
            else if (child == 2) {
                child--;
                chkError = true;
                roadEror = "Landmark is required"
                document.getElementById("Sproad").innerHTML = roadEror;
                console.log(road, ' Length is: ', road.length);
            }
        }
        if (city.length < 1) {
            if (child == 1) {
                chkError = true;
                cityEror = "City is required"
                document.getElementById("Spcity").innerHTML = cityEror;
                console.log(city, ' Length is: ', city.length);
            }
            else if (child == 2) {
                child--;
                chkError = true;
                cityEror = "City is required"
                document.getElementById("Spcity").innerHTML = cityEror;
                console.log(city, ' Length is: ', city.length);
            }
        }
        if (state.length < 1) {
            if (child == 1) {
                chkError = true;
                stateEror = "State is required"
                document.getElementById("Spstate").innerHTML = stateEror;
                console.log(state, ' Length is: ', state.length);
            }
            else if (child == 2) {
                child--;
                chkError = true;
                stateEror = "State is required"
                document.getElementById("Spstate").innerHTML = stateEror;
                console.log(state, ' Length is: ', state.length);
            }
        }

        if (pin.length < 1) {
            if (child == 1) {
                chkError = true;
                pinEror = "Pincode is required"
                document.getElementById("Sppin").innerHTML = pinEror;
                console.log(pin, ' Length is: ', pin.length);
            }
            else if (child == 2) {
                child--;
                chkError = true;
                pinEror = "Pincode is required"
                document.getElementById("Sppin").innerHTML = pinEror;
                console.log(pin, ' Length is: ', pin.length);
            }
        }
    }

    function validateScreen3() {
        console.log("HI---V3")
        // console.log("chkerror: ", chkError);
        var acname = $("#acname").val();
        var acno = $("#acno").val();
        var mmid = $("#mmid").val();
        var bankname = $("#bankname").val();
        var branch = $("#branch").val();
        var ifsc = $("#ifsc").val();
        var file = $("#file").val();

        var acnameError = '';
        var acnoEror = '';
        var mmidEror = '';
        var banknameEror = '';
        var branchEror = '';
        var ifscEror = '';
        var fileEror = '';

        document.getElementById("Spacname").innerHTML = acnameError;
        document.getElementById("Spacno").innerHTML = acnoEror;
        document.getElementById("Spmmid").innerHTML = mmidEror;
        document.getElementById("Spbankname").innerHTML = banknameEror;
        document.getElementById("Spbranch").innerHTML = branchEror;
        document.getElementById("Spifsc").innerHTML = ifscEror;
        document.getElementById("Spfile").innerHTML = fileEror;

        if (acname.length < 1) {
            child--;
            chkError = true;
            acnameError = "Account Holder Name is required";
            document.getElementById("Spacname").innerHTML = acnameError;
            console.log(acname, ' Length is: ', acname.length);
        }
        if (acno.length < 1) {
            if (child == 2) {
                chkError = true;
                acnameError = "Account No is required";
                document.getElementById("Spacno").innerHTML = acnoEror;
                console.log(acno, ' Length is: ', acno.length);
            }
            else {
                child--;
                chkError = true;
                acnameError = "Account No is required";
                document.getElementById("Spacno").innerHTML = acnoEror;
                console.log(acno, ' Length is: ', acno.length);
            }
        } else {
            if (acno.length < 8) {
                if (child == 2) {
                    chkError = true;
                    acnameError = "Account No is not Valid";
                    document.getElementById("Spacno").innerHTML = acnoEror;
                    console.log(acno, ' Length is: ', acno.length);
                }
                else {
                    child--;
                    chkError = true;
                    acnameError = "Account No is not Valid";
                    document.getElementById("Spacno").innerHTML = acnoEror;
                    console.log(acno, ' Length is: ', acno.length);
                }
            }


        }
        if (mmid.length < 1) {
            if (child == 2) {
                chkError = true;
                mmidEror = "MICR code is required"
                document.getElementById("Spmmid").innerHTML = mmidEror;
                console.log(mmid, ' Length is: ', mmid.length);
            }
            else {
                child--;
                chkError = true;
                mmidEror = "MICR code is required"
                document.getElementById("Spmmid").innerHTML = mmidEror;
                console.log(mmid, ' Length is: ', mmid.length);
            }
        }
        if (bankname.length < 1) {
            if (child == 2) {
                chkError = true;
                banknameEror = "Bank Name is required"
                document.getElementById("Spbankname").innerHTML = banknameEror;
                console.log(bankname, ' Length is: ', bankname.length);
            }
            else {
                child--;
                chkError = true;
                banknameEror = "Bank Name is required"
                document.getElementById("Spbankname").innerHTML = banknameEror;
                console.log(bankname, ' Length is: ', bankname.length);
            }
        }
        if (branch.length < 1) {
            if (child == 2) {
                chkError = true;
                branchEror = "Branch Name is required"
                document.getElementById("Spbranch").innerHTML = branchEror;
                console.log(branch, ' Length is: ', branch.length);
            }
            else {
                child--;
                chkError = true;
                branchEror = "Branch Name is required"
                document.getElementById("Spbranch").innerHTML = branchEror;
                console.log(branch, ' Length is: ', branch.length);
            }
        }
        if (ifsc.length < 1) {
            if (child == 0) {
                chkError = true;
                ifscEror = "IFCI Code is required"
                document.getElementById("Spifsc").innerHTML = ifscEror;
                console.log(ifsc, ' Length is: ', ifsc.length);
            }
            else {
                child--;
                chkError = true;
                ifscEror = "IFCI Code is required"
                document.getElementById("Spifsc").innerHTML = ifscEror;
                console.log(ifsc, ' Length is: ', ifsc.length);
            }
        }
        if (file.length < 1 || file != '') {
            var format =
                /(\.pdf|\.jpg|\.jpeg|\.png)$/i;
            if (child == 2) {
                chkError = true;
                if (!format.exec(file)) {
                    fileEror = "Invalid file type"
                    document.getElementById("Spfile").innerHTML = fileEror;
                    console.log(file, ' Length is: ', file.length);
                    file.value = '';
                }
            }
            else {
                child--;
                chkError = true;
                if (!format.exec(file)) {
                    fileEror = "Invalid file type"
                    document.getElementById("Spfile").innerHTML = fileEror;
                    console.log(file, ' Length is: ', file.length);
                    file.value = '';
                }
            }
        }
    }
});


