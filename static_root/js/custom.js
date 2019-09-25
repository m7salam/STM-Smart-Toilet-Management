var refreshData = function () {
  $.ajax({
    url: 'http://127.0.0.1:8000/api/data-tissue/',
    method: 'GET',
    data: {},
    success: function (data) {
      $('#sensor_data_tissue').replaceWith($('#sensor_data_tissue', data))
    },
    error: function (error) {
      console.log(error)
      console.log('error')
    }
  })
}

var totalSeconds = 5 // refresh every 5 seconds

setInterval(function () {
  refreshData()
}, totalSeconds * 1000)
