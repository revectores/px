function render_item(params, api) {
    let category_index = api.value(0);
    let start = api.coord([api.value(1), category_index]);
    let end = api.coord([api.value(2), category_index]);
    let height = api.size([0, 1])[1] * 0.6;

    let shape = echarts.graphic.clipRectByRect({
        x: start[0],
        y: start[1] - height / 2,
        width: end[0] - start[0],
        height: height
    }, {
        x: params.coordSys.x,
        y: params.coordSys.y,
        width: params.coordSys.width,
        height: params.coordSys.height
    });

    return shape && {
        type: 'rect',
        shape: shape,
        style: api.style()
    };
}


function extract_top_typeid(type_path){
    return type_path.split('/')[0];
}


function create_date_gantt_option(logs, types, range){
    let date_gantt_option = create_gantt_option(logs, types);
    date_gantt_option.xAxis = {
        min: range.start,
        max: range.end,
        type: 'time',
        scale: true,
        axisLabel: {
            /*
            formatter: function (val) {
                return val
            }
            */
        },    
    }
    // date_intervals_gantt_option.title.text = `Intervals in ${date_format(range.start)}`

    return date_gantt_option;
}


function create_gantt_option(logs, types) {
    let data = [];
    let types_arr = Object.values(types);
    let top_names = [];
    let typeid2seq = {}
    let y_seq = 0;
    for (const tid in types) {
        if (types[tid].depth === 1) {
            top_names.push(types[tid].name);
            typeid2seq[tid] = y_seq;
            y_seq += 1;
        }
    }

    logs.forEach(function(log){
        let type = types[log.type];
        let top_typeid = extract_top_typeid(type.type_path);
        let top_typename = typeid2seq[top_typeid];

        data.push({
            name: type.name_path,
            comment: log.comment,
            value: [
                top_typename,
                log.start,
                log.end,
            ],
            itemStyle: {
                normal: {
                    color: type.color
                }
            }
        })
    });

    option = {
        tooltip: {
            formatter: function (log){
                [_, log.start, log.end] = log.value;
                let total_seconds = (log.end - log.start) / 1000;
                let duration_string = seconds_to_hms(total_seconds);
                let start_clock = log.start.toLocaleTimeString('en-GB');
                let end_clock = log.end.toLocaleTimeString('en-GB');
                return `${log.marker}${log.name}: ${start_clock}~${end_clock} (${duration_string})`;
            }
        },
        // title: {
        //     text: 'Intervals',
        //     left: 'center'
        // },
        dataZoom: [{
            type: 'slider',
            filterMode: 'weakFilter',
            showDataShadow: false,
            top: 400,
            height: 10,
            borderColor: 'transparent',
            backgroundColor: '#e2e2e2',
            handleIcon: 'M10.7,11.9H9.3c-4.9,0.3-8.8,4.4-8.8,9.4c0,5,3.9,9.1,8.8,9.4h1.3c4.9-0.3,8.8-4.4,8.8-9.4C19.5,16.3,15.6,12.2,10.7,11.9z M13.3,24.4H6.7v-1.2h6.6z M13.3,22H6.7v-1.2h6.6z M13.3,19.6H6.7v-1.2h6.6z', // jshint ignore:line
            handleSize: 20,
            handleStyle: {
                shadowBlur: 6,
                shadowOffsetX: 1,
                shadowOffsetY: 2,
                shadowColor: '#aaa'
            },
            labelFormatter: ''
        }, {
            type: 'inside',
            filterMode: 'weakFilter'
        }],
        grid: {
            height: 300
        },
        yAxis: {
            data: top_names
        },
        series: [{
            type: 'custom',
            renderItem: render_item,
            itemStyle: {
                opacity: 0.8
            },
            encode: {
                x: [1, 2],
                y: 0
            },
            data: data
        }]
    };

    return option;
}