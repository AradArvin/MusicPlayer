$(function() {

    if (localStorage.chkbx && localStorage.chkbx === 'checked') {
        $('#rememberMe').attr('checked', 'checked');
        $('#id_username').val(localStorage.usrname);
        $('#id_password').val(localStorage.pass);
    } else {
        $('#rememberMe').removeAttr('checked');
        $('#id_username').val('');
        $('#id_password').val('');
    }

    $('#login_btn').click(function() {

        if ($('#rememberMe').is(':checked')) {
            // save username and password
            localStorage.usrname = $('#id_username').val();
            localStorage.pass = $('#id_password').val();
            localStorage.chkbx = $('#rememberMe').val();
        } else {
            localStorage.usrname = '';
            localStorage.pass = '';
            localStorage.chkbx = '';
        }
    });
});

