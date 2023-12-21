var USING_MODE;
HideAllContent = () => {
    $("#Sys_info").addClass("disabledbutton");
    $("#Sys_info").find('input').each(function () {
        $(this).prop('disabled', true);
    });
}

UnhideContent = () => {
    $("#Sys_info").removeClass("disabledbutton");
    $("#Sys_info").find('input').each(function () {
        $(this).prop('disabled', false);
    });
}

function GetThongTin() {
    $.ajax({
        type: "GET",
        url: "http://" + window.location.host + "/request/datajson/general",
        // context: document.body,
        contentType: 'application/json',
        success: function (response) {
            console.log(response);
            response[0].sys_allow == 0 ? HideAllContent() : UnhideContent();
            //response[0]
            USING_MODE = response[0].sys_mode;
            console.log(USING_MODE);
            $("#pump").prop("checked", response[1].pump == 1 ? true : false);
            $("#van_3").prop("checked", response[1].phun_suong == 1 ? true : false);
            $("#van_1").prop("checked", response[2].nho_giot == 1 || response[3].nho_giot == 1 ? true : false);
            $("#van_2").prop("checked", response[4].nho_giot == 1 || response[5].nho_giot == 1 ? true : false);
            $("#van_4").prop("checked", response[1].fan == 1 ? true : false);
        }
    });
}
// SendButtonRequest = (buttonID, typeRequest) => {

// }
function CheckVanButton() {
    let van1State = $('#van_1').is(':checked');
    let van2State = $('#van_2').is(':checked');
    let van3State = $('#van_3').is(':checked');
    if (van1State == false && van2State == false && van3State == false) {
        return false;
    } else {
        return true;
    }
}
function CheckCheDo(using_mode, next_mode, SendData) {
    if (using_mode != next_mode) {
        $('#exampleModal').modal('show');
        let pre_mode, set_mode;
        let listCheDo = {
            0: 'Chưa thiết lập',
            1: "Tự động",
            2: "Hằng ngày",
            3: "Bằng tay"
        }
        for (let key in listCheDo) {
            if (using_mode == key) {
                pre_mode = listCheDo[key];
                break;
            }
            if (next_mode == key) {
                set_mode = listCheDo[key];
            }
        }
        if (pre_mode != 0) {
            document.getElementsByClassName('modal-body')[0].innerHTML = "Bạn đang dùng chế độ " + pre_mode + ". Xác nhận chuyển sang chế độ " + set_mode;
        } else {
            document.getElementsByClassName('modal-body')[0].innerHTML = "Bạn đang dùng chế độ " + pre_mode;
        }

        $('#confirm-mode').on('click', function () {
            $.ajax({
                type: "POST",
                url: "http://" + window.location.host + "/change_mode",
                data: {
                    csrfmiddlewaretoken: csrftoken,
                    'mode': next_mode,
                    'pre_mode': using_mode
                },
                success: function (response) {
                    $('#exampleModal').modal('hide');
                }
            })
        })
    }
}

function SendPumpRequestOFF() {
    let value;
    let state;
    state = false;
    value = 0;
    var csrftoken = $("input[name=csrfmiddlewaretoken]").val();
    $.ajax({
        type: "POST",
        url: "http://" + window.location.host + "/onhand/pump",
        data: {
            csrfmiddlewaretoken: csrftoken,
            'value': value,
            'type': 'pump'
        },
        success: function (response) {
            $("#pump").prop('checked', state);
            GetThongTin();
        }
    });
};

SendButtonRequest = (buttonID, typeRequest, url) => {
    vanState = CheckVanButton();
    if (vanState == false && buttonID == 'pump') {
        $("#" + buttonID).prop('checked', false);
        return;
    } else {
        $("#" + buttonID).prop('checked', !$("#" + buttonID).prop('checked'));
        SendRequest = () => {
            let value;
            let state;
            state = ($("#" + buttonID).prop("checked") == true) ? false : true;
            value = ($("#" + buttonID).prop("checked") == true) ? 0 : 1;
            var csrftoken = $("input[name=csrfmiddlewaretoken]").val();
            $.ajax({
                type: "POST",
                url: url,
                data: {
                    csrfmiddlewaretoken: csrftoken,
                    'value': value,
                    'type': typeRequest
                },
                success: function (response) {
                    $("#" + buttonID).prop('checked', state);
                    vanStateAfter = CheckVanButton();
                    if (vanStateAfter == false) {
                        SendPumpRequestOFF();
                    }
                    GetThongTin();
                }
            });
        }
        if (USING_MODE != 3) {
            CheckCheDo(USING_MODE, 3, SendRequest);

        } else {
            SendRequest();
        }
    }

}

$('#pump').on('click', function (e) {
    SendButtonRequest('pump', 'pump', "http://" + window.location.host + "/onhand/pump");
});

$('#van_1').on('click', function (e) {
    SendButtonRequest('van_1', 'van1', "http://" + window.location.host + "/onhand/van1");
});

$('#van_2').on('click', function (e) {
    SendButtonRequest('van_2', 'van2', "http://" + window.location.host + "/onhand/van2");
});

$('#van_3').on('click', function (e) {
    SendButtonRequest('van_3', 'van3', "http://" + window.location.host + "/onhand/van3");
});

$('#van_4').on('click', function (e) {
    SendButtonRequest('van_4', 'van4', "http://" + window.location.host + "/onhand/van4");
});
UpdateSystem = (message) => {
    let listCheDo = {
        1: "Tự động",
        2: "Hằng ngày",
        3: "Băng tay"
    }
    for (let key in listCheDo) {
        if (key == message.sys_mode) {
            USING_MODE = key;
        }
    }
    message.sys_allow == 0 ? HideAllContent() : UnhideContent();
}
UpdateSwitchInArea = (message, areaID) => {
    if (areaID < 3) {
        $("#van_1").prop("checked", message.nho_giot == 1 ? true : false);
    } else {
        $("#van_2").prop("checked", message.nho_giot == 1 ? true : false);
    }
}
UpdateSwitchInGeneral = (message) => {
    $("#van_4").prop("checked", message.fan == 1 ? true : false);
    $("#pump").prop("checked", message.pump == 1 ? true : false);
    $("#van_3").prop("checked", message.phun_suong == 1 ? true : false);
}

function ConnectWebSocket() {
    let socket = new WebSocket(
        'ws://' +
        window.location.host +
        '/ws/view/'
    );

    socket.onopen = (e) => {
        console.log("[open] Connection established");
        console.log("Sending to server");
    };

    socket.onmessage = (event) => {
        console.log(JSON.parse(event.data));
        messageData = JSON.parse(event.data);
        if (messageData.model == "General") {
            UpdateSwitchInGeneral(messageData);
        }
        if (messageData.model == "AreaInfo") {
            UpdateSwitchInArea(messageData, messageData.kv)
        }
        if (messageData.model == "System") {
            UpdateSystem(messageData);
        }
    }

    socket.onclose = (event) => {
        if (event.wasClean) {
            console.log(`[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
        } else {
            console.log('[close] Connection died');
        }
    };
    socket.onerror = (error) => {
        console.log(`[error] ${error.message}`);
    };
}

ConnectWebSocket();

$(document).ready(function () {
    GetThongTin();
})
