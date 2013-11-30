make_clickable = function() {
   show_button();
   refresh_button();
}

show_button = function() {
    var poll_id = null;
    $('.show.button').unbind("click").bind("click", function(){
        poll_id = this.id.split("-")[0];

        button_text = $('#'+ poll_id +'-button')
        button_text.text((button_text.text() == "+") ? "-" : "+");

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

        $.getJSON($root_url + 'poll-detail', {
            poll_id: poll_id,
        }, function(data) {
            set_highchart(canvas, poll_id, data.result);
            $('#' + poll_id + '-refresh').show();
        });
        return;
    });
}

refresh_button = function () {
    var poll_id = null;
    $('.refresh.button').unbind("click").bind("click", function(){
        poll_id = this.id.split("-")[0];
        canvas = $('#' + poll_id + '-canvas');

        $.getJSON($root_url + 'poll-detail', {
            poll_id: poll_id,
        }, function(data) {
            set_highchart(canvas, poll_id, data.result);
        });
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