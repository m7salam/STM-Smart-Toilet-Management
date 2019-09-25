var refreshData = function () {
  $.ajax({
    url: 'http://127.0.0.1:8000/update-data',
    method: 'GET',
    data: {},
    success: function (data) {
      $('#sensor_data').html(data)
    },
    error: function (error) {
      console.log(error)
      console.log('error')
    }
  })
}

var totalSeconds = 10 // refresh every 5 seconds

setInterval(function () {
  refreshData()
}, totalSeconds * 1000)
