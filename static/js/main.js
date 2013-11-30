make_clickable = function() {
    poll_id = null
    $('.clickable').unbind("click").bind("click", function(){
        poll_id = this.id.split("-")[0];

        canvas = $('#' + poll_id + '-canvas');
            if (canvas.css('display') == 'none')
                canvas.show();
            else {
                canvas.hide();
                return; 
            }

        $.getJSON($root_url + 'poll-detail', {
            poll_id: poll_id,
        }, function(data) {
            window.result = data.result;
            result = data.result;

            //Code for highchart.js
            canvas.highcharts({
            chart: {
                type: 'bar',
                height: 200 + result.labels.length * 20
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

        });
        return false;
    })
}