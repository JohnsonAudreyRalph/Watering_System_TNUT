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

moment.locale('vi');
// $('#customdate1').daterangepicker();
// $('#customdate2').daterangepicker();

var chart = document.getElementById('myChart').getContext('2d');
var AreaChart = document.getElementById('AreaChart').getContext('2d');

let months = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10 ',
    '11',
    '12',
];
let days = [];
for (let i = 1; i <= 31; i++) {
    days.push(i);
}
let Chart1 = new Chart();
let Chart2 = new Chart();
// let Areachart = new Chart(AreaChart, config);


function DrawChart1(chartData, labels, xAxisName, labelDataSet, colorCode) {
    Chart1.destroy();
    let data = {
        labels: labels,
        datasets: [{
            label: labelDataSet,
            data: chartData,
            fill: false,
            borderColor: colorCode,
            tension: 0.1,
            borderWidth: 4
        }]
    };
    let config = {
        type: 'line',
        data: data,
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    display: true,
                    title: {
                        display: true,
                        text: xAxisName,
                        color: 'rgba(4, 4, 4, 1)',
                        font: {
                            family: 'Comic Sans MS',
                            weight: 'bold',
                        },
                        padding: {
                            top: 5,
                            left: 0,
                            right: 0,
                            bottom: 5
                        }
                    }
                },
                y: {
                    beginAtZero: true,
                }
            },
        },
    };
    Chart1 = new Chart(chart, config);
    Chart.defaults.font.size = 14;
}

function DrawChart2(chartData, labels, xAxisName, labelDataSet, colorCode) {
    Chart2.destroy();
    let data = {
        labels: labels,
        datasets: [{
            label: labelDataSet,
            data: chartData,
            fill: false,
            borderColor: colorCode,
            tension: 0.1,
            borderWidth: 4
        }]
    };
    let config = {
        type: 'line',
        data: data,
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    display: true,
                    title: {
                        display: true,
                        text: xAxisName,
                        color: 'rgba(4, 4, 4, 1)',
                        font: {
                            family: 'Comic Sans MS',
                            weight: 'bold',
                        },
                        padding: {
                            top: 5,
                            left: 0,
                            right: 0,
                            bottom: 5
                        }
                    }
                },
                y: {
                    beginAtZero: true,
                }
            },
        },
    };
    Chart2 = new Chart(AreaChart, config);
    Chart.defaults.font.size = 14;
}

function UpdateChart1(dataName) {
    $.ajax({
        type: "GET",
        // url: "http://" + window.location.host + "/request/datajson/chart-data",
        contentType: 'application/json',
        data: {
            'name': dataName
        },
        success: function (response) {
            dataKey = Object.keys(response[0])[0];
            if (response == null){

            }
            if (dataKey == 'temp__avg') {
                try {
                    chartData = []
                    for (var i in response)
                        chartData.push(response[i].temp__avg);
                    DrawChart1(chartData, months, 'Tháng', 'Nhiệt độ', '#F01616');
                    UnhideContent();
                } catch (error) {
                    console.log(error);
                }
            } else if (dataKey == 'light__avg') {
                try {
                    chartData = []
                    for (var i in response)
                        chartData.push(response[i].light__avg);
                    DrawChart1(chartData, months, 'Tháng', 'Ánh sáng', '#CF8F04');
                    UnhideContent();
                } catch (error) {
                    console.log(error);
                }
            } else if (dataKey == 'air_humid__avg') {
                try {
                    chartData = []
                    for (var i in response)
                        chartData.push(response[i].air_humid__avg);
                    DrawChart1(chartData, months, 'Tháng', 'Độ ẩm không khí', '#0F79DD');
                    UnhideContent();
                } catch (error) {
                    console.log(error);
                }
            }
        }
    });
}

function UpdateChart1Daily(dataName, month) {
    $.ajax({
        type: "GET",
        // url: "http://" + window.location.host + "/request/datajson/chart-data-daily",
        contentType: 'application/json',
        data: {
            'name': dataName,
            'month': month
        },
        success: function (response) {
            dataKey = Object.keys(response[0])[0];
            if (dataKey == 'temp__avg') {
                try {
                    chartData = []
                    for (var i in response)
                        chartData.push(response[i].temp__avg);
                    DrawChart1(chartData, days, 'Tháng ' + month, 'Nhiệt độ', '#F01616');
                    UnhideContent();
                } catch (error) {
                    console.log(error);
                }
            } else if (dataKey == 'light__avg') {
                try {
                    chartData = []
                    for (var i in response)
                        chartData.push(response[i].light__avg);
                    DrawChart1(chartData, days, 'Tháng ' + month, 'Ánh sáng', '#CF8F04');
                    UnhideContent();
                } catch (error) {
                    console.log(error);
                }
            } else if (dataKey == 'air_humid__avg') {
                try {
                    chartData = []
                    for (var i in response)
                        chartData.push(response[i].air_humid__avg);
                    DrawChart1(chartData, days, 'Tháng ' + month, 'Độ ẩm không khí', '#0F79DD');
                    UnhideContent();
                } catch (error) {
                    console.log(error);
                }
            }
        }
    });
};

function UpdateChart2(kv_id) {
    $.ajax({
        type: "GET",
        // url: "http://" + window.location.host + "/request/datajson/chart-area-data",
        contentType: 'application/json',
        data: {
            'kv': kv_id
        },
        success: function (response) {
            console.log(response);
            dataKey = Object.keys(response[0])[0];
            try {
                chartData = []
                for (var i in response)
                    chartData.push(response[i].humid__avg);
                DrawChart2(chartData, months, 'Tháng', 'Độ ẩm đất', '#23364b');
                UnhideContent();
            } catch (error) {
                console.log(error);
            }
        }
    });
};

function UpdateChart2Daily(kv, month) {
    $.ajax({
        type: "GET",
        // url: "http://" + window.location.host + "/request/datajson/chart-area-data-daily",
        contentType: 'application/json',
        data: {
            'kv': kv,
            'month': month
        },
        success: function (response) {
            console.log(response);
            dataKey = Object.keys(response[0])[0];
            chartData = []
            for (var i in response)
                chartData.push(response[i].humid__avg);
            DrawChart2(chartData, days, 'Tháng ' + month, 'Độ ẩm đất', '#23364b');
            UnhideContent();

        }
    });
};

HideAllContent();
$(document).ready(function () {
    UpdateChart1('temp');
    UpdateChart2(1);
});

$('#temp').on('click', function () {
    HideAllContent();
    $('#temp').addClass('active-btn');
    $('#light').removeClass('active-btn');
    $('#air_humid').removeClass('active-btn');
    if ($('#year1').hasClass('active-btn') == true) {
        UpdateChart1('temp');
    } else {
        let month = $('#list-months1').find('.active-option')[0].text;
        UpdateChart1Daily('temp', month);
    }
});

$('#light').on('click', function () {
    HideAllContent();
    $('#light').addClass('active-btn');
    $('#temp').removeClass('active-btn');
    $('#air_humid').removeClass('active-btn');
    if ($('#year1').hasClass('active-btn') == true) {
        UpdateChart1('light');
    } else {
        let month = $('#list-months1').find('.active-option')[0].text;
        UpdateChart1Daily('light', month);
    }
});

$('#air_humid').on('click', function () {
    HideAllContent();
    $('#air_humid').addClass('active-btn');
    $('#temp').removeClass('active-btn');
    $('#light').removeClass('active-btn');
    if ($('#year1').hasClass('active-btn') == true) {
        UpdateChart1('air_humid');
    } else {
        let month = $('#list-months1').find('.active-option')[0].text;
        UpdateChart1Daily('air_humid', month);
    }
});
$('#list-months1 > a').on('click', function () {
    HideAllContent();
    // console.log(this.text);
    $('#list-months1 > a').removeClass('active-option');
    $('#year1').removeClass('active-btn');
    $('#dropdownMenuButton').addClass('active-btn');
    $('#dropdownMenuButton').html('Tháng ' + this.text);
    $(this).addClass('active-option');
    let month = this.text;
    let listBtnID = ['temp', 'light', 'air_humid'];
    for (let id in listBtnID) {
        if ($('#' + listBtnID[id]).hasClass('active-btn') == true) {
            UpdateChart1Daily(listBtnID[id], month);
        }
    }
});

$('#year1').on('click', function () {
    HideAllContent();
    $('#list-months1 > a').removeClass('active-option');
    $('#year1').addClass('active-btn');
    $('#dropdownMenuButton').removeClass('active-btn');
    $('#dropdownMenuButton').html('Chọn tháng');
    let listBtnID = ['temp', 'light', 'air_humid'];
    for (let id in listBtnID) {
        if ($('#' + listBtnID[id]).hasClass('active-btn') == true) {
            UpdateChart1(listBtnID[id]);
        }
    }
});

$('#year2').on('click', function () {
    HideAllContent();
    $('#list-months2 > a').removeClass('active-option');
    $('#year2').addClass('active-btn');
    $('#dropdownMenuButton2').removeClass('active-btn');
    $('#dropdownMenuButton2').html('Chọn tháng');
    let listBtnID = {
        'kv1_btn': 1,
        'kv2_btn': 2,
        'kv3_btn': 3,
        'kv4_btn': 4
    };
    for (let id in listBtnID) {
        if ($('#' + id).hasClass('active-btn') == true) {
            UpdateChart2(listBtnID[id]);
        }
    }
});

$('#kv1_btn').on('click', function () {
    HideAllContent();
    $('#kv1_btn').addClass('active-btn');
    $('#kv2_btn').removeClass('active-btn');
    $('#kv3_btn').removeClass('active-btn');
    $('#kv4_btn').removeClass('active-btn');
    if ($('#year2').hasClass('active-btn') == true) {
        UpdateChart2(1);
    } else {
        let month = $('#list-months2').find('.active-option')[0].text;
        UpdateChart2Daily(1, month);
    }
});

$('#kv2_btn').on('click', function () {
    HideAllContent();
    $('#kv2_btn').addClass('active-btn');
    $('#kv1_btn').removeClass('active-btn');
    $('#kv3_btn').removeClass('active-btn');
    $('#kv4_btn').removeClass('active-btn');
    if ($('#year2').hasClass('active-btn') == true) {
        UpdateChart2(2);
    } else {
        let month = $('#list-months2').find('.active-option')[0].text;
        UpdateChart2Daily(2, month);
    }
});

$('#kv3_btn').on('click', function () {
    HideAllContent();
    $('#kv3_btn').addClass('active-btn');
    $('#kv2_btn').removeClass('active-btn');
    $('#kv1_btn').removeClass('active-btn');
    $('#kv4_btn').removeClass('active-btn');
    if ($('#year2').hasClass('active-btn') == true) {
        UpdateChart2(3);
    } else {
        let month = $('#list-months2').find('.active-option')[0].text;
        UpdateChart2Daily(3, month);
    }
});

$('#kv4_btn').on('click', function () {
    HideAllContent();
    $('#kv4_btn').addClass('active-btn');
    $('#kv2_btn').removeClass('active-btn');
    $('#kv3_btn').removeClass('active-btn');
    $('#kv1_btn').removeClass('active-btn');
    if ($('#year2').hasClass('active-btn') == true) {
        UpdateChart2(4);
    } else {
        let month = $('#list-months2').find('.active-option')[0].text;
        UpdateChart2Daily(4, month);
    }
});

$('#list-months2 > a').on('click', function () {
    HideAllContent();
    // console.log(this.text);
    $('#list-months2 > a').removeClass('active-option');
    $('#year2').removeClass('active-btn');
    $('#dropdownMenuButton2').addClass('active-btn');
    $('#dropdownMenuButton2').html('Tháng ' + this.text);
    $(this).addClass('active-option');
    let month = this.text;
    let listBtnID = {
        'kv1_btn': 1,
        'kv2_btn': 2,
        'kv3_btn': 3,
        'kv4_btn': 4
    };
    for (let id in listBtnID) {
        if ($('#' + id).hasClass('active-btn') == true) {
            UpdateChart2Daily(listBtnID[id], month);
        }
    }
});