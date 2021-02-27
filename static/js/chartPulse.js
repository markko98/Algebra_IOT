$.ajax({
    url: "http://pavliskomiot2021.westeurope.cloudapp.azure.com:80/api/telemetry/measurement",
    data: {
        "DeviceId": '1',
        "SensorName": "pulse", 
        "dateFrom": "2021-02-01",
        "dateTo": "2022-02-25"
    },
    cache: false,
    type: "GET",
    success: function (response) {
        values = [];
        captions = [];
        for (var i = 0; i < response.length; i++) {
            captions[i] = response[i]["CreatedOn"];
            values[i] = response[i]["SensorValue"];
        }
 
        var ctx = document.getElementById("Mychart");
        var mychart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: captions,
                datasets: [
                    {
                        data: values,
                        label: "Pulse",
                        borderColor: "#FF0000",
                        fill: false
                    },
                ]
            }
        });
    },
    error: function (xhr) {
        console.log("Ajax error!");
        console.log(xhr);
    }
});