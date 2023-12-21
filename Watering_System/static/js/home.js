function HideAllContent() {
    $("#Sys_info").addClass("disabledbutton");
    $("#Sys_info").find('input').each(function () {
        $(this).prop('disabled', true);
    });
}

function UnhideContent() {
    $("#Sys_info").removeClass("disabledbutton");
    $("#Sys_info").find('input').each(function () {
        $(this).prop('disabled', false);
    });
}

function ChangeGauge(idGauge, value, idInput) {
    value = (value == '' || value == null) ? 0 : value;
    var Needle, arc, arcEndRad, arcStartRad, barWidth, chart, chartInset, degToRad, el, endPadRad, height, i, margin, needle, numSections, padRad, percToDeg, percToRad, percent, radius, ref, sectionIndx, sectionPerc, startPadRad, svg, totalPercent, width;

    percent = value / 100;

    barWidth = 40;

    numSections = 3;

    // / 2 for HALF circle
    sectionPerc = 1 / numSections / 2;

    padRad = 0.05;

    chartInset = 10;

    // start at 270deg
    totalPercent = .75;

    el = d3.select('#' + idGauge);

    margin = {
        top: 0,
        right: 25,
        bottom: 0,
        left: 5
    };

    width = el[0][0].offsetWidth - margin.left - margin.right;

    height = width;

    radius = Math.min(width, height) / 2;

    percToDeg = function (perc) {
        return perc * 360;
    };

    percToRad = function (perc) {
        return degToRad(percToDeg(perc));
    };

    degToRad = function (deg) {
        return deg * Math.PI / 180;
    };

    svg = el.append('svg').attr('width', width + margin.left + margin.right).attr('height', height + margin.top + margin.bottom);

    chart = svg.append('g').attr('transform', `translate(${(width + margin.left) / 2}, ${(height + margin.top) / 2})`);

    // build gauge bg
    for (sectionIndx = i = 1, ref = numSections;
        (1 <= ref ? i <= ref : i >= ref); sectionIndx = 1 <= ref ? ++i : --i) {
        arcStartRad = percToRad(totalPercent);
        arcEndRad = arcStartRad + percToRad(sectionPerc);
        totalPercent += sectionPerc;
        startPadRad = sectionIndx === 0 ? 0 : padRad / 2;
        endPadRad = sectionIndx === numSections ? 0 : padRad / 2;
        arc = d3.svg.arc().outerRadius(radius - chartInset).innerRadius(radius - chartInset - barWidth).startAngle(arcStartRad + startPadRad).endAngle(arcEndRad - endPadRad);
        chart.append('path').attr('class', `arc chart-color${sectionIndx}`).attr('d', arc);
    }

    Needle = class Needle {
        constructor(len, radius1) {
            this.len = len;
            this.radius = radius1;
        }

        drawOn(el, perc) {
            el.append('circle').attr('class', 'needle-center').attr('cx', 0).attr('cy', 0).attr('r', this.radius);
            return el.append('path').attr('class', idGauge).attr('d', this.mkCmd(perc));
        }

        animateOn(el, perc) {
            var self;
            self = this;
            return el.transition().delay(500).ease('elastic').duration(3000).selectAll('.' + idGauge).tween('progress', function () {
                return function (percentOfPercent) {
                    var progress;
                    progress = percentOfPercent * perc;
                    return d3.select(this).attr('d', self.mkCmd(progress));
                };
            });
        }

        mkCmd(perc) {
            var centerX, centerY, leftX, leftY, rightX, rightY, thetaRad, topX, topY;
            thetaRad = percToRad(perc / 2); // half circle
            centerX = 0;
            centerY = 0;
            topX = centerX - this.len * Math.cos(thetaRad);
            topY = centerY - this.len * Math.sin(thetaRad);
            leftX = centerX - this.radius * Math.cos(thetaRad - Math.PI / 2);
            leftY = centerY - this.radius * Math.sin(thetaRad - Math.PI / 2);
            rightX = centerX - this.radius * Math.cos(thetaRad + Math.PI / 2);
            rightY = centerY - this.radius * Math.sin(thetaRad + Math.PI / 2);
            return `M ${leftX} ${leftY} L ${topX} ${topY} L ${rightX} ${rightY}`;
        }

    };

    needle = new Needle(50, 15);

    needle.drawOn(chart, 0);

    needle.animateOn(chart, percent);

    let input = document.getElementById(idInput);
    input.addEventListener('keyup', function () {
        let valueInput = input.value;
        needle.animateOn(chart, valueInput / 100);
    });
}

var USING_MODE;
const csrftoken = $("input[name=csrfmiddlewaretoken]").val();

function ToggleTimeRow(idInput, idButton) {
    $("#" + idInput).toggleClass("disabletime");
    $("#" + idInput).prop('disabled', $("#" + idInput).hasClass("disabletime"));
}

function ToogleCard(idCard, idButton) {
    $("#" + idCard).toggleClass("disablecard");
    $("#" + idCard).find('input').each(function () {
        $(this).prop('disabled', $("#" + idCard).hasClass("disablecard"));
    });
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

function UpdateThongTinHeThong() {
    $.ajax({
        type: "GET",
        url: "http://" + window.location.host + "/request/datajson/tu-dong-data",
        // context: document.body,
        contentType: 'application/json',
        success: function (response) {
            USING_MODE = response[0].sys_mode;
            response[0].sys_allow == 0 ? HideAllContent() : UnhideContent();
            // response[1]
            let listIDStateKV1 = ['kv1_check_l1', 'kv1_check_l2', 'kv1_check_l3', 'kv1_check_l4', 'kv1_check_l5', 'kv1_check_l6'];
            let listIDStateKV3 = ['kv3_check_l1', 'kv3_check_l2', 'kv3_check_l3', 'kv3_check_l4', 'kv3_check_l5', 'kv3_check_l6'];
            let listIDTimeKV1 = ['kv1_time1', 'kv1_time2', 'kv1_time3', 'kv1_time4', 'kv1_time5', 'kv1_time6'];
            let listIDTimeKV3 = ['kv3_time1', 'kv3_time2', 'kv3_time3', 'kv3_time4', 'kv3_time5', 'kv3_time6'];
            let listIDHumidMinKV1 = ['kv1_range_min_1', 'kv1_range_min_2', 'kv1_range_min_3', 'kv1_range_min_4', 'kv1_range_min_5', 'kv1_range_min_6']
            let listIDHumidMinKV3 = ['kv3_range_min_1', 'kv3_range_min_2', 'kv3_range_min_3', 'kv3_range_min_4', 'kv3_range_min_5', 'kv3_range_min_6']
            let listIDHumidMaxKV1 = ['kv1_range_max_1', 'kv1_range_max_2', 'kv1_range_max_3', 'kv1_range_max_4', 'kv1_range_max_5', 'kv1_range_max_6']
            let listIDHumidMaxKV3 = ['kv3_range_max_1', 'kv3_range_max_2', 'kv3_range_max_3', 'kv3_range_max_4', 'kv3_range_max_5', 'kv3_range_max_6']
            let listLengthKV1 = ['kv1_length1', 'kv1_length2', 'kv1_length3', 'kv1_length4', 'kv1_length5', 'kv1_length6'];
            let listLengthKV3 = ['kv3_length1', 'kv3_length2', 'kv3_length3', 'kv3_length4', 'kv3_length5', 'kv3_length6'];

            for (let i = 0; i < 6; i++) {
                $("#" + listIDStateKV1[i]).prop("checked", response[2][i].state == 1 ? true : false);
                if (response[2][i].state != 1) {
                    $("#" + listIDTimeKV1[i]).addClass('disabletime');
                    $("#" + listIDTimeKV1[i]).prop('disabled', true);
                }
                $("#" + listIDStateKV3[i]).prop("checked", response[2][i + 6].state == 1 ? true : false);
                if (response[2][i + 6].state != 1) {
                    $("#" + listIDTimeKV3[i]).addClass('disabletime');
                    $("#" + listIDTimeKV3[i]).prop('disabled', true);
                }
                $("#" + listIDTimeKV1[i]).val(response[2][i].time_start);
                $("#" + listIDTimeKV3[i]).val(response[2][i + 6].time_start);
                $("#" + listIDHumidMinKV1[i]).val(response[3][i].humid_min);
                $("#" + listIDHumidMinKV3[i]).val(response[3][i + 6].humid_min);
                $("#" + listIDHumidMaxKV1[i]).val(response[3][i].humid_max);
                $("#" + listIDHumidMaxKV3[i]).val(response[3][i + 6].humid_max);
                $("#" + listLengthKV1[i]).val(response[3][i].time_length);
                $("#" + listLengthKV3[i]).val(response[3][i + 6].time_length);
            }
            ChangeGauge('gauge1', response[4].desire_humidity, 'kv1_humid');
            ChangeGauge('gauge3', response[6].desire_humidity, 'kv3_humid');
            $("#kv1_humid").val(response[4].desire_humidity);
            $("#kv3_humid").val(response[6].desire_humidity);
            $("#phun_suong_kv12").prop("checked", response[1].phun_suong == 1 ? true : false);
            $("#phun_suong_kv34").prop("checked", response[1].phun_suong == 1 ? true : false);
            $("#nho_giot_kv12").prop("checked", response[4].nho_giot == 1 || response[5].nho_giot == 1 ? true : false);
            $("#nho_giot_kv34").prop("checked", response[6].nho_giot == 1 || response[7].nho_giot == 1 ? true : false);
            if (response[4].state_td == 0) {
                $('#kv1_check').prop('checked', false);
                $('#card_kv1_content').addClass("disablecard");
                $('#card_kv1_content').find('input').each(function () {
                    $(this).prop('disabled', $('#card_kv1_content').hasClass("disablecard"));
                });
            } else {
                $('#kv1_check').prop('checked', true);
                $('#card_kv1_content').removeClass("disablecard");
                $('#card_kv1_content').find('input').each(function () {
                    $(this).prop('disabled', $('#card_kv1_content').hasClass("disablecard"));
                });
            }
            if (response[6].state_td == 0) {
                $('#kv3_check').prop('checked', false);
                $('#card_kv3_content').addClass("disablecard");
                $('#card_kv3_content').find('input').each(function () {
                    $(this).prop('disabled', $('#card_kv3_content').hasClass("disablecard"));
                });
            } else {
                $('#kv3_check').prop('checked', true);
                $('#card_kv3_content').removeClass("disablecard");
                $('#card_kv3_content').find('input').each(function () {
                    $(this).prop('disabled', $('#card_kv3_content').hasClass("disablecard"));
                });
            }
            $("#phunmua").find('input').each(function () {
                $(this).prop('disabled', true);
            });
        }
    });
}

function CheckFormData(formID, kv) {
    let check1, check2, check3, check4 = true;
    let listHumidMinMaxKv1 = {
        1: ['kv1_range_min_1', 'kv1_range_max_1'],
        2: ['kv1_range_min_2', 'kv1_range_max_2'],
        3: ['kv1_range_min_3', 'kv1_range_max_3'],
        4: ['kv1_range_min_4', 'kv1_range_max_4'],
        5: ['kv1_range_min_5', 'kv1_range_max_5'],
        6: ['kv1_range_min_6', 'kv1_range_max_6'],
    };
    let listHumidMinMaxKv3 = {
        1: ['kv3_range_min_1', 'kv3_range_max_1'],
        2: ['kv3_range_min_2', 'kv3_range_max_2'],
        3: ['kv3_range_min_3', 'kv3_range_max_3'],
        4: ['kv3_range_min_4', 'kv3_range_max_4'],
        5: ['kv3_range_min_5', 'kv3_range_max_5'],
        6: ['kv3_range_min_6', 'kv3_range_max_6'],
    };
    let listData;
    listData = (kv == 1) ? listHumidMinMaxKv1 : listHumidMinMaxKv3;
    let kvID = (kv == 1) ? 'kv1_humid' : 'kv3_humid';
    let humidValue = $('#' + kvID).val();
    if (humidValue > 100 || humidValue < 0 || humidValue == '') {
        check1 = false;
    }
    for (id in listData) {
        let humid_min = $('#' + listData[id][0]).val();
        let humid_max = $('#' + listData[id][1]).val();
        if (humid_max <= humid_min ||
            humid_min < 0 ||
            humid_max < 0 ||
            humid_min > 100 ||
            humid_max > 100 ||
            humid_min == '' ||
            humid_max == '') {
            check2 = false;
        }
    }
    $("#" + formID).find('.col-sm-3 >input').each(function () {
        if (this.value == '' && ($(this).hasClass('disabletime')) == false) {
            check3 = false;
        }
    });
    $("#" + formID).find('.col-sm-5 >table>tbody>tr>td>input').each(function () {
        if (this.value == '' || parseInt(this.value) < 0 || ($(this).hasClass('timelenght') == false && parseInt(this.value) > 100)) {
            check4 = false;
        }
    });
    let check = (check1 == false || check2 == false || check3 == false || check4 == false) ? false : true;
    return check;
}

function FillArrayData(ArrayData, ListID, typeInput) {
    for (i in ListID) {
        let id = ListID[i];
        let value;
        if (typeInput == 'checkbox') {
            value = ($('#' + id).prop("checked") == true) ? 1 : 0;
        }
        if (typeInput == "number") {
            value = $('#' + id).val();
        }
        ArrayData.push(value);
    }
    return ArrayData;
}

function SendFormDataRequest(formID, alertID, kv) {
    function SendRequest() {
        checkKVID = (kv == 'kv1') ? 1 : 3;
        let checkInput = CheckFormData(formID, checkKVID);
        let checkKV = $("#" + kv + "_check").prop("checked");
        if (checkInput == false && checkKV == true) {
            $('#' + alertID).removeClass("alert-success").removeClass("alert-warning").addClass("alert-danger");
            $('#' + alertID + '-text').text('Hãy kiểm tra lại thông số cài đặt');
            $('#' + alertID).show();
            window.setTimeout(() => {
                $('#' + alertID).hide();
            }, 3000);
            return;
        } else if (checkKV == false) {
            $.ajax({
                type: "POST",
                url: "http://" + window.location.host + "/request/datajson/tu-dong",
                data: {
                    csrfmiddlewaretoken: csrftoken,
                    'kv': kv,
                    'state': 0,
                    'type': 'update_khu_vuc_state',
                },
                success: function (response) {
                    $('#' + alertID).removeClass("alert-danger").removeClass("alert-success").addClass("alert-warning");
                    $('#' + alertID + '-text').text('Khu vực đã tạm ngừng');
                    $('#' + alertID).show();
                    window.setTimeout(() => {
                        $('#' + alertID).hide();
                    }, 3000);
                }
            });
        } else {
            let stateArray = [];
            let timeArray = [];
            let humidMinArray = [];
            let humidMaxArray = [];
            let timelenghtArray = [];
            let humidValue;
            let state1, state2, state3, state4, state5, state6;
            let time1, time2, time3, time4, time5, time6;
            let humidMin1, humidMin2, humidMin3, humidMin4, humidMin5, humidMin6;
            let humidMax1, humidMax2, humidMax3, humidMax4, humidMax5, humidMax6;
            let length1, length2, length3, length4, length5, length6;
            let listStateID = [
                kv + '_check_l1',
                kv + '_check_l2',
                kv + '_check_l3',
                kv + '_check_l4',
                kv + '_check_l5',
                kv + '_check_l6',
            ];
            let listTimeID = [
                kv + '_time1',
                kv + '_time2',
                kv + '_time3',
                kv + '_time4',
                kv + '_time5',
                kv + '_time6',
            ];
            let listHumidMinID = [
                kv + '_range_min_1',
                kv + '_range_min_2',
                kv + '_range_min_3',
                kv + '_range_min_4',
                kv + '_range_min_5',
                kv + '_range_min_6',
            ];
            let listHumidMaxID = [
                kv + '_range_max_1',
                kv + '_range_max_2',
                kv + '_range_max_3',
                kv + '_range_max_4',
                kv + '_range_max_5',
                kv + '_range_max_6',
            ];
            let listTimeLengthID = [
                kv + '_length1',
                kv + '_length2',
                kv + '_length3',
                kv + '_length4',
                kv + '_length5',
                kv + '_length6',
            ];

            stateArray = FillArrayData(stateArray, listStateID, 'checkbox');
            timeArray = FillArrayData(timeArray, listTimeID, 'number');
            humidMinArray = FillArrayData(humidMinArray, listHumidMinID, 'number');
            humidMaxArray = FillArrayData(humidMaxArray, listHumidMaxID, 'number');
            timelenghtArray = FillArrayData(timelenghtArray, listTimeLengthID, 'number');

            humidValue = $('#' + kv + '_humid').val();
            [state1, state2, state3, state4, state5, state6] = stateArray;
            [time1, time2, time3, time4, time5, time6] = timeArray;
            [humidMin1, humidMin2, humidMin3, humidMin4, humidMin5, humidMin6] = humidMinArray;
            [humidMax1, humidMax2, humidMax3, humidMax4, humidMax5, humidMax6] = humidMaxArray;
            [length1, length2, length3, length4, length5, length6] = timelenghtArray;
            $.ajax({
                type: "POST",
                url: "http://" + window.location.host + "/request/datajson/tu-dong",
                data: {
                    csrfmiddlewaretoken: csrftoken,
                    'type': 'update_data_tu_dong',
                    'kv': kv,
                    'desire_humidity': humidValue,

                    'time_1': time1,
                    'time_2': time2,
                    'time_3': time3,
                    'time_4': time4,
                    'time_5': time5,
                    'time_6': time6,

                    'min_1': humidMin1,
                    'min_2': humidMin2,
                    'min_3': humidMin3,
                    'min_4': humidMin4,
                    'min_5': humidMin5,
                    'min_6': humidMin6,

                    'state_1': state1,
                    'state_2': state2,
                    'state_3': state3,
                    'state_4': state4,
                    'state_5': state5,
                    'state_6': state6,

                    'max_1': humidMax1,
                    'max_2': humidMax2,
                    'max_3': humidMax3,
                    'max_4': humidMax4,
                    'max_5': humidMax5,
                    'max_6': humidMax6,

                    'length_1': length1,
                    'length_2': length2,
                    'length_3': length3,
                    'length_4': length4,
                    'length_5': length5,
                    'length_6': length6,
                },
                success: function (response) {
                    $('#' + alertID).removeClass("alert-danger").removeClass("alert-warning").addClass("alert-success");
                    $('#' + alertID + '-text').text('Cài đặt thành công');
                    $('#' + alertID).show();
                    window.setTimeout(() => {
                        $('#' + alertID).hide();
                    }, 3000);
                }
            });
        }
    }
    if (USING_MODE != 1) {
        CheckCheDo(USING_MODE, 1, SendRequest)
    } else {
        SendRequest();
    }
};

function SendButtonRequest(buttonID, typeRequest) {
    $("#" + buttonID).prop('checked', !$("#" + buttonID).prop('checked'));
    SendRequest = () => {
        let value;
        let state;
        state = ($("#" + buttonID).prop("checked") == true) ? false : true;
        value = ($("#" + buttonID).prop("checked") == true) ? 0 : 1;
        var csrftoken = $("input[name=csrfmiddlewaretoken]").val();
        $.ajax({
            type: "POST",
            url: "http://" + window.location.host + "/request/datajson/tu-dong",
            data: {
                csrfmiddlewaretoken: csrftoken,
                'value': value,
                'type': typeRequest
            },
            success: function (response) {
                $("#" + buttonID).prop('checked', state);
            }
        });
    }
    if (USING_MODE != 1) {
        CheckCheDo(USING_MODE, 1, SendRequest);

    } else {
        SendRequest();
    }
}

$('#kv1_check').on('click', function () {
    ToogleCard('card_kv1_content', 'kv1-humid-submit');
})
$('#kv3_check').on('click', function () {
    ToogleCard('card_kv3_content', 'kv3-humid-submit');
})

let listTimeID = {
    'kv1_check_l1': 'kv1_time1',
    'kv1_check_l2': 'kv1_time2',
    'kv1_check_l3': 'kv1_time3',
    'kv1_check_l4': 'kv1_time4',
    'kv1_check_l5': 'kv1_time5',
    'kv1_check_l6': 'kv1_time6',
    'kv3_check_l1': 'kv3_time1',
    'kv3_check_l2': 'kv3_time2',
    'kv3_check_l3': 'kv3_time3',
    'kv3_check_l4': 'kv3_time4',
    'kv3_check_l5': 'kv3_time5',
    'kv3_check_l6': 'kv3_time6',
};
for (let id in listTimeID) {
    $('#' + id).on('change', function () {
        ToggleTimeRow(listTimeID[id], id);
    });
}

//send max and min humid kv 1 to server
$("#kv1-humid-submit").on('click', function () {
    SendFormDataRequest('card_kv1_content', 'kv1-humid-alert', 'kv1');
});



//send max and min humid kv 3 to server
$("#kv3-humid-submit").on('click', function () {
    SendFormDataRequest('card_kv3_content', 'kv3-humid-alert', 'kv3');
});




$("#phun_suong_kv12").on('change', function (e) {
    SendButtonRequest('phun_suong_kv12', 'ps');
});



//send max and min humid kv 2 to server
$("#phun_suong_kv34").on('change', function (e) {
    SendButtonRequest('phun_suong_kv34', 'ps');
});

$("#nho_giot_kv12").on('change', function (e) {
    SendButtonRequest('nho_giot_kv12', 'ng_12');
});

$("#nho_giot_kv34").on('change', function (e) {
    SendButtonRequest('nho_giot_kv34', 'ng_34');
});

UpdateGeneralInfo = (message) => {
    $("#phun_suong_kv12").prop("checked", message.phun_suong == 1 ? true : false);
    $("#phun_suong_kv34").prop("checked", message.phun_suong == 1 ? true : false);
    console.log('update by websocket');
}
UpdateInvidualAreaInfo = (message, idArea) => {
    if (idArea < 3) {
        $("#nho_giot_kv12").prop("checked", message.nho_giot == 1 ? true : false);
    } else {
        $("#nho_giot_kv34").prop("checked", message.nho_giot == 1 ? true : false);
    }
}
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
// socket
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
        if (messageData.model == "AreaInfo") {
            UpdateInvidualAreaInfo(messageData, messageData.kv);
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
UpdateThongTinHeThong();
// $(document).ready(function () {

// });
