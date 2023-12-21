var USING_MODE;
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
ToggleRow = (index) => {
    rowID = 'day-' + index;
    numOfRowID = 'l' + index + '-row';
    kvOfRow = 'khuvuc_l' + index;
    modeOfRow = 'mode_l' + index;
    timeOfRowID = 'start_time' + index;
    lengthOfRowID = 'length' + index;
    $("#" + numOfRowID).toggleClass("disable");
    $("#" + kvOfRow).prop('disabled', $("#" + numOfRowID).hasClass("disable"));
    $("#" + modeOfRow).prop('disabled', $("#" + numOfRowID).hasClass("disable"));
    $("#" + timeOfRowID).prop('disabled', $("#" + numOfRowID).hasClass("disable"));
    $("#" + lengthOfRowID).prop('disabled', $("#" + numOfRowID).hasClass("disable"));
}
UpdateRowTable = (message, rowID) => {
    try {
        let rowElementInTable;
        $('#start_time' + rowID).val(message.time_start);
        $('#length' + rowID).val(message.time_length);
        $('#mode_l' + rowID + ' option[value=' + message.chedo + ']').prop('selected', true);
        $('#khuvuc_l' + rowID + ' option[value=' + message.khuvuc + ']').prop('selected', true);
        if (message.trangthai == 0) {
            $('#l' + rowID + '-row').addClass("disable");
            $('#day-' + rowID).prop('checked', false);
            rowElementInTable = `<tr>
                <td>${rowID}</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>`;
        } else {
            let cheDoHienThi, khuVucHienThi;
            console.log('#mode_l' + rowID + 'option[value=' + message.chedo + ']');
            $('#l' + rowID + '-row').removeClass("disable");
            $('#day-' + rowID).prop('checked', true);
            listChedo = {
                1: 'Phun sương',
                2: 'Nhỏ giọt',
                3: 'Tất cả'
            }
            listKhuvuc = {
                1: 'Khu vực 1,2',
                2: 'Khu vực 3,4',
                3: 'Tất cả'
            }
            cheDoHienThi = listChedo[parseInt(message.chedo)];
            khuVucHienThi = listKhuvuc[parseInt(message.khuvuc)];
            rowElementInTable = `<tr>
                <td>${rowID}</td>
                <td>${khuVucHienThi}</td>
                <td>${cheDoHienThi}</td>
                <td>${message.time_start.slice(0,5)}</td>
                <td>${message.time_length + " phút"}</td>
                </tr>`;
        }
        return rowElementInTable;
    } catch (err) {
        emptyRow = `<tr><td>${rowID}</td><td></td><td></td><td></td><td></td></tr>`;
        return emptyRow;
    }
}
UpdateTable = (response) => {
    $('#schedule').html('');
    let rowTable1 = UpdateRowTable(response[0], 1);
    let rowTable2 = UpdateRowTable(response[1], 2);
    let rowTable3 = UpdateRowTable(response[2], 3);
    let rowTable4 = UpdateRowTable(response[3], 4);
    let rowTable5 = UpdateRowTable(response[4], 5);
    let rowTable6 = UpdateRowTable(response[5], 6);
    $('#schedule').append(
        `<thead>
            <tr>
                <th class="text-center">Lần tưới</th>
                <th class="text-center">Khu vực</th>
                <th class="text-center">Chế độ</th>
                <th class="text-center">Bắt đầu</th>
                <th class="text-center">Thời lượng</th>
            </tr>
        </thead>
        <tbody> ` + rowTable1 + rowTable2 + rowTable3 + rowTable4 + rowTable5 + rowTable6 + ' </tbody>'
    );
}
$('#day-1').on('change', function () {
    ToggleRow(1);
});

$('#day-2').on('change', function () {
    ToggleRow(2);
});

$('#day-3').on('change', function () {
    ToggleRow(3);
});

$('#day-4').on('change', function () {
    ToggleRow(4);
});

$('#day-5').on('change', function () {
    ToggleRow(5);
});
$('#day-6').on('change', function () {
    ToggleRow(6);
});


$('#submit').on('click', function () {
    let stateRow1, khuvuc1, mode1, startTime1, length1;
    let stateRow2, khuvuc2, mode2, startTime2, length2;
    let stateRow3, khuvuc3, mode3, startTime3, length3;
    let stateRow4, khuvuc4, mode4, startTime4, length4;
    let stateRow5, khuvuc5, mode5, startTime5, length5;
    let stateRow6, khuvuc6, mode6, startTime6, length6;
    let allowedSend;
    let khuvucArray = [];
    let modeArray = [];
    let startTimeArray = [];
    let lengthArray = [];
    let stateArray = [];
    checkData = () => {
        for (let i = 0; i < 6; i++) {
            if (document.getElementById('start_time' + (i + 1)).value.length == 0 ||
                document.getElementById('length' + (i + 1)).value.length == 0) {
                return 0;
            }
        }
        return 1;
    }
    getRowData = () => {
        let rowDataJson = [];
        for (let i = 0; i < 6; i++) {
            if ($("#l" + (i + 1) + "-row").hasClass('disable') == false) {
                let start_time = (document.getElementById('start_time' + (i + 1)).value);
                let timeLength = parseInt(document.getElementById('length' + (i + 1)).value);
                let khuvuc = parseInt(document.getElementById('khuvuc_l' + (i + 1)).value);
                let mode = parseInt(document.getElementById('mode_l' + (i + 1)).value);
                rowDataJson.push({
                    "id": i + 1,
                    "state": 1,
                    "khuvuc": khuvuc,
                    "mode": mode,
                    "start_time": start_time,
                    "timeLength": timeLength
                })
            } else {
                rowDataJson.push({
                    "id": (i + 1),
                    "state": 0
                })
            }
        }
        return rowDataJson;
    }
    SendDailyDataRequest = () => {
        allowedSend = checkData();
        // console.log(allowedSend);
        if (allowedSend == 0) {
            $('#alert').removeClass("alert-success").addClass("alert-danger");
            $('#alert-text').text('Hãy thiết lập lại thông số');
            $('#alert').show();
            window.setTimeout(() => {
                $('#alert').hide();
            }, 3000);
        } else {
            let jsonData = getRowData();
            // stateRow1 = stateRow2 = stateRow3 = stateRow4 = stateRow5 = stateRow6 = 0;
            for (let i = 0; i < 6; i++) {
                khuvucArray.push(jsonData[i].khuvuc);
                modeArray.push(jsonData[i].mode);
                stateArray.push(jsonData[i].state);
                jsonData[i].state != 0 ? startTimeArray.push(jsonData[i].start_time) : startTimeArray.push(null)
                jsonData[i].state != 0 ? lengthArray.push(jsonData[i].timeLength) : lengthArray.push(null)
            }
            [mode1, mode2, mode3, mode4, mode5, mode6] = modeArray;
            [khuvuc1, khuvuc2, khuvuc3, khuvuc4, khuvuc5, khuvuc6] = khuvucArray;
            [startTime1, startTime2, startTime3, startTime4, startTime5, startTime6] = startTimeArray;
            [length1, length2, length3, length4, length5, length6] = lengthArray;
            [stateRow1, stateRow2, stateRow3, stateRow4, stateRow5, stateRow6] = stateArray;
        }

        let csrftoken = $("input[name=csrfmiddlewaretoken]").val();
        $.ajax({
            type: "POST",
            url: "http://" + window.location.host + "/set_daily",
            data: {
                csrfmiddlewaretoken: csrftoken,
                'start_time1': startTime1,
                'mode1': mode1,
                'khuvuc1': khuvuc1,
                'length1': length1,
                'stt1': stateRow1,

                'start_time2': startTime2,
                'mode2': mode2,
                'khuvuc2': khuvuc2,
                'length2': length2,
                'stt2': stateRow2,

                'start_time3': startTime3,
                'mode3': mode3,
                'khuvuc3': khuvuc3,
                'length3': length3,
                'stt3': stateRow3,

                'start_time4': startTime4,
                'mode4': mode4,
                'khuvuc4': khuvuc4,
                'length4': length4,
                'stt4': stateRow4,


                'start_time5': startTime5,
                'mode5': mode5,
                'khuvuc5': khuvuc5,
                'length5': length5,
                'stt5': stateRow5,

                'start_time6': startTime6,
                'mode6': mode6,
                'khuvuc6': khuvuc6,
                'length6': length6,
                'stt6': stateRow6
            },
            success: function (response) {
                console.log(response);
                $('#alert').removeClass("alert-danger").addClass("alert-success");
                $('#alert-text').text('Cài đặt thành công');
                $('#alert').show();
                window.setTimeout(() => {
                    $('#alert').hide();
                }, 3000);
                UpdateTable(response);
            }
        })
    }
    if (USING_MODE != 2) {
        CheckCheDo(USING_MODE, 2, SendDailyDataRequest)
    } else {
        SendDailyDataRequest();
    }

});

function UpdateHangNgay() {
    $.ajax({
        type: "GET",
        url: "http://" + window.location.host + "/set_daily",
        contentType: 'application/json',
        success: function (response) {
            document.getElementById('schedule').innerHTML = "";
            USING_MODE = response[0].sys_mode;
            response[0].sys_allow == 0 ? HideAllContent() : UnhideContent();
            UpdateTable(response[1]);
        }
    })
};
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
        messageData = JSON.parse(event.data)
        // if (messageData.model == "Daily") {
        //     console.log(messageData.data);
        //     UpdateTable(messageData.data);
        // }
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

$(document).ready(function () {
    UpdateHangNgay();
});
ConnectWebSocket();
