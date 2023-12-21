
function Userlogout() {
    $.ajax({
        type: "GET",
        url: "http://" + window.location.host + "/logout/",
        success: function (response) {
            if (response == "done") {
                window.location.href = "http://" + window.location.host;
            }
        }
    })
};

$('#logout').on('click', function () {
    Userlogout();
})