$('input').on('click', function (event) {
  event.preventDefault();
});

function UpdateSystem(message) {
  var systemMode = {
    '0': "Chưa thiết lập",
    '1': "Tự động",
    '2': "Hằng ngày",
    '3': "Bằng tay"
  };
  let length = 4;
  for (let index = 0; index < length; index++) {
    if (index == message.sys_mode) {
      $('#sys_mode').text(systemMode[index]);
    }
  }
}

function CheckCheDoTuoi(khu_vuc, gia_tri_ng) {
  const KHUVUC = [1, 2, 3, 4]
  for (let index of KHUVUC) {
    if (index == khu_vuc) {
      $("#kv" + index + "_ng_status").prop("checked", gia_tri_ng == 1 ? true : false);
      return;
    }
  }
};

function AddAreaInfo(dataArray) {
  $("#temperature_data").text((dataArray.temp || 'N/A ') + "°C");
  $("#light_data").text((dataArray.light || 'N/A ') + " LUX");
  $("#cool_ps").text(dataArray.cool_ps == 1 ? 'ON' : 'OFF');
  $("#cool_stt").text((dataArray.cool_sys == 1 || dataArray.fan == 1) ? 'ON' : 'OFF');
  $("#pump2_status").text(dataArray.pump == 1 ? 'ON' : 'OFF');
  $("#tank_data").text(dataArray.tank == 1 ? 'Đầy' : 'Cạn');
  $("#air-humid").text((dataArray.air_humid || 'N/A') + "%");
  for (let i = 0; i < 5; i++) {
    $("#kv" + (i + 1) + "_ps_status").prop("checked", dataArray.phun_suong == 1 ? true : false);
  }
}

function AddWaterSystemInfoOFEachAreaInfo(KhuVuc, dataArray) {
  $('#kv' + KhuVuc + '_humid_data_display').text((dataArray.humid || ' ') + "%");
  CheckCheDoTuoi(KhuVuc, dataArray.nho_giot);
}

function GetThongTin() {
  $.ajax({
    type: "GET",
    url: "http://" + window.location.host + "/request/datajson/general",
    // context: document.body,
    contentType: 'application/json',
    success: function (response) {
      console.log(response);
      //response[0]
      var systemMode = {
        '0': "OFFLINE",
        '1': "Tự động",
        '2': "Hằng ngày",
        '3': "Bằng tay"
      };
      let length = 4;
      for (let index = 0; index < length; index++) {
        if (index == response[0].sys_mode) {
          $('#sys_mode').text(systemMode[index]);
        }
        AddWaterSystemInfoOFEachAreaInfo(index + 1, response[index + 2]);
      }
      AddAreaInfo(response[1]);
    }
  });

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
    console.log(JSON.parse(event.data));
    messageData = JSON.parse(event.data)
    if (messageData.model == "General") {
      AddAreaInfo(messageData);
    }
    if (messageData.model == "AreaInfo") {
      AddWaterSystemInfoOFEachAreaInfo(messageData.kv, messageData);
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
GetThongTin();
ConnectWebSocket();
