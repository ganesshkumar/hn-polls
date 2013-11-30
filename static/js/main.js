make_clickable = function() {
    poll_id = null
    $('.clickable').unbind("click").bind("click", function(){
        poll_id = this.id.split("-")[0];

        $.getJSON($root_url + 'poll-detail', {
            poll_id: poll_id,
        }, function(data) {
            window.result = data.result;
            result = data.result;
            
            //Code for highchart.js
            canvas = $('#' + poll_id + '-canvas');
            canvas.show()
            canvas.highcharts({
            chart: {
                type: 'bar'
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
                data: result.votes
            }]
        });

        });
        return false;
    })
}