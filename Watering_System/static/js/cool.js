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

UpdateGauge = (gauge, outer, inner) => {
    gauge.style.setProperty('--outer-value', outer.value);
    gauge.style.setProperty('--inner-value', inner.value);
}

AddEventListenerGauge = (idGauge, idOuter, idInner) => {
        let gauge = document.getElementById(idGauge);
        let inner = document.getElementById(idOuter);
        let outer = document.getElementById(idInner);
        inner.addEventListener('keyup', function () {
            UpdateGauge(gauge, outer, inner);
        });
        outer.addEventListener('keyup', function () {
            UpdateGauge(gauge, outer, inner);
        });
    }
    (function () {
        let listID = {
            'temp': ['nhiet_do_min', 'nhiet_do_max'],
            'air-humid': ['khong_khi_min', 'khong_khi_max'],
        }
        for (elementID in listID) {
            gaugeID = elementID;
            outerID = listID[elementID][1];
            innerID = listID[elementID][0];
            AddEventListenerGauge(gaugeID, outerID, innerID);
        }
    })();

UpdateThongTinHeThong = () => {
    $.ajax({
        type: "GET",
        url: "http://" + window.location.host + "/request/datajson/general",
        // context: document.body,
        contentType: 'application/json',
        success: function (response) {
            response[0].sys_allow == 0 ? HideAllContent() : UnhideContent();
            // response[1]
            let listID = {
                'temp': ['nhiet_do_min', 'nhiet_do_max', 'temp_min', 'temp_max', 1],
                'air-humid': ['khong_khi_min', 'khong_khi_max', 'air_humid_min', 'air_humid_max', 1],
            }
            for (elementID in listID) {
                gaugeID = elementID;
                outerID = listID[elementID][1]; //max
                innerID = listID[elementID][0]; //min
                outerValue = listID[elementID][3]; //max value
                innerValue = listID[elementID][2]; //min value
                index = listID[elementID][4];
                let gauge = document.getElementById(gaugeID);
                let inner = document.getElementById(outerID);
                let outer = document.getElementById(innerID);
                $('#' + innerID).val(response[index][innerValue])
                $('#' + outerID).val(response[index][outerValue])
                UpdateGauge(gauge, outer, inner);
            }
            $("#cool").prop("checked", response[1].cool_sys == 1 ? true : false);
            $("#cool_ps").prop("checked", response[1].cool_ps == 1 ? true : false);
        }
    });
}
$(document).ready(function () {
    UpdateThongTinHeThong();
});

SendFormDataRequest = (alertID, minDataID, maxDataID, typeRequest) => {
    let dataMin = parseInt(document.getElementById(minDataID).value);
    let dataMax = parseInt(document.getElementById(maxDataID).value);
    let csrftoken = $("input[name=csrfmiddlewaretoken]").val();
    if (dataMin >= dataMax || dataMin >= 100 || dataMax >= 100 || dataMin < 0 || dataMax < 0) {
        $('#' + alertID).removeClass("alert-success").addClass("alert-danger");
        $('#' + alertID + '-text').text('Hãy thiết lập lại thông số');
        $('#' + alertID).show();
        window.setTimeout(() => {
            $('#' + alertID).hide();
        }, 2000);

    } else {
        $.ajax({
            type: "POST",
            url: "http://" + window.location.host + "/request/datajson/lam-mat",
            data: {
                csrfmiddlewaretoken: csrftoken,
                'dataMin': dataMin,
                'dataMax': dataMax,
                'type': typeRequest
            },
            success: function (response) {
                $('#' + alertID).removeClass("alert-danger").addClass("alert-success");
                $('#' + alertID + '-text').text('Lưu thông số thành công');
                $('#' + alertID).show();
                window.setTimeout(() => {
                    $('#' + alertID).hide();
                }, 3000);
            }
        });
    }
};

SendButtonRequest = (buttonID, typeRequest) => {
    $("#" + buttonID).prop('checked', !$("#" + buttonID).prop('checked'));
    let value;
    let state;
    state = ($("#" + buttonID).prop("checked") == true) ? false : true;
    value = ($("#" + buttonID).prop("checked") == true) ? 0 : 1;
    var csrftoken = $("input[name=csrfmiddlewaretoken]").val();
    $.ajax({
        type: "POST",
        url: "http://" + window.location.host + "/request/datajson/lam-mat",
        data: {
            csrfmiddlewaretoken: csrftoken,
            'value': value,
            'type': typeRequest
        },
        success: function (response) {
            $("#" + buttonID).prop('checked', state);
        }
    });
};
$("#submit-temp").on('click', function () {
    SendFormDataRequest('temp-alert', 'nhiet_do_min', 'nhiet_do_max', 'temp');
});

$("#air-humid-submit").on('click', function () {
    SendFormDataRequest('air-humid-alert', 'khong_khi_min', 'khong_khi_max', 'air_humid');
});

$("#cool").on('change', function (e) {
    SendButtonRequest('cool', 'cool_sys');
});

$("#cool_ps").on('change', function (e) {
    SendButtonRequest('cool_ps', 'cool_ps');
});

UpdateGeneralInfo = (message) => {
    $("#cool").prop("checked", message.cool_sys == 1 ? true : false);
    $("#cool_ps").prop("checked", message.cool_ps == 1 ? true : false);
}
UpdateSystem = (message) => {
    message.sys_allow == 0 ? HideAllContent() : UnhideContent();
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
        messageData = JSON.parse(event.data)
        if (messageData.model == "General") {
            UpdateGeneralInfo(messageData);
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