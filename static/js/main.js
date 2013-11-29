make_clickable = function() {
    poll_id = null
    $('.clickable').unbind("click").bind("click", function(){
        poll_id = this.id.split("-")[0];

        $.getJSON($root_url + 'poll-detail', {
            poll_id: poll_id,
        }, function(data) {
            window.result = data.result;
            var canvas = document.getElementById(poll_id + "-canvas");
            canvas.style.display = "block";
            options = {
              scaleOverlay : true,
              scaleOverride : true,
              scaleStartValue : 0,
              scaleSteps : 11,
              scaleStepWidth : (Math.max.apply(Math, data.result.datasets.data)/10)
            }
            new Chart(canvas.getContext("2d")).Bar(data.result);
        });
        return false;
    })
}