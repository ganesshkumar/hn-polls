make_clickable = function() {
   show_button();
   refresh_button();
}

show_button = function() {
    var poll_id = null;
    $('.show.button').unbind("click").bind("click", function(){
        poll_id = this.id.split("-")[0];

        show_button = $('#'+ poll_id +'-button')
        button_text = (show_button.text() == "+") ? "-" : "+";
        show_button.text(button_text);

        canvas = $('#' + poll_id + '-canvas');
        
        if (canvas.css('display') == 'none') {
            canvas.show()
            if (canvas.html() != "") {
                $('#' + poll_id + '-refresh').show();
                return;
            }
        }
        else {
            $('#' + poll_id + '-refresh').hide();
            canvas.hide();
            return;
        }

        show_button.text('·');
        var spinner = new Spinner(spinner_options).spin(show_button.get(0));
        render_graph(poll_id, show_button, button_text);
        return;
    });
}

refresh_button = function () {
    var poll_id = null;
    $('.refresh.button').unbind("click").bind("click", function(){
        poll_id = this.id.split("-")[0];
        refresh_button = $('#'+ poll_id +'-refresh');
        text = refresh_button.text();
        
        refresh_button.text('·');
        var spinner = new Spinner(spinner_options).spin(refresh_button.get(0));
        render_graph(poll_id, refresh_button, text);
    });
}

render_graph = function(poll_id, element, text) {
    canvas = $('#' + poll_id + '-canvas');
    $.getJSON($root_url + 'poll-detail', {
        poll_id: poll_id,
    }, function(data) {
        set_highchart(canvas, poll_id, data.result);
        $('#' + poll_id + '-refresh').show();
        element.text(text);
    });
}

set_highchart = function(element, poll_id, result) {
    element.highcharts({
        chart: {
            type: 'bar',
            backgroundColor: '#f6f6ef',
            height: 200 + result.labels.length * 20,
        },
        title: {
            text: result.title
        },
        subtitle: {
            text: ''
        },
        xAxis: {
            categories: result.labels,
            title: {
                text: null
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Number of votes',
                align: 'high'
            },
            labels: {
                overflow: 'justify'
            }
        },
        tooltip: {
            valueSuffix: ' votes'
        },
        plotOptions: {
            bar: {
                dataLabels: {
                    enabled: true
                }
            }
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'top',
            x: -40,
            y: 100,
            floating: true,
            borderWidth: 1,
            backgroundColor: '#FFFFFF',
            shadow: true
        },
        credits: {
            enabled: false
        },
        series: [{
            name: 'HN Votes',
            color: 'orange',
            data: result.votes
        }]
    });
}

var spinner_options = {
  lines: 7, // The number of lines to draw
  length: 4, // The length of each line
  width: 2, // The line thickness
  radius: 2, // The radius of the inner circle
  corners: 1, // Corner roundness (0..1)
  rotate: 0, // The rotation offset
  direction: 1, // 1: clockwise, -1: counterclockwise
  color: '#ff6600', // #rgb or #rrggbb or array of colors
  speed: 1, // Rounds per second
  trail: 60, // Afterglow percentage
  shadow: false, // Whether to render a shadow
  hwaccel: false, // Whether to use hardware acceleration
  className: 'spinner', // The CSS class to assign to the spinner
  zIndex: 2e9, // The z-index (defaults to 2000000000)
  top: 3, // Top position relative to parent in px
  left: 1 // Left position relative to parent in px
};