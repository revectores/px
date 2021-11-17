function build_type_tree(types) {
    let root = {};
    const max_depth = 3;
    for (depth = 1; depth <= max_depth; depth++) {
        for (const k in types) {
            let parents = types[k].type_path.split('/');
            parents.pop();
            if (parents.length + 1 === depth) {
                let parent = root;
                parents.forEach(t => parent = parent[t]);
                parent[types[k].id] = {};
            }
        }
    }
    return root;
}


function compute_durations(logs) {
    durations = {}
    logs.forEach(log => {
        if (!(log.type in durations)) durations[log.type] = 0;
        durations[log.type] += (log.end - log.start) / 1000;
    });
    return durations;
}


function build_data_tree(durations, types, root) {
    return make_node(durations, types, root, '');
}


function make_node(durations, types, root, id) {
    let children = [];
    let node_duration = (id in durations) ? durations[id]: 0;
    for (child_id in root) {
        let child_node = make_node(durations, types, root[child_id], child_id);
        children.push(child_node);
        node_duration += child_node["value"];
    }

    return {
        "name": id === '' ? 'Total' : types[id].name,
        "children": children,
        "value": node_duration,
        "itemStyle": {
            "opacity": node_duration ? 1 : 0.3,
        }
    }
}


function get_tree_chart(logs, types, date_range) {
    let root = build_type_tree(types);
    let durations = compute_durations(logs);
    let data_root = build_data_tree(durations, types, root);
    let data = data_root;

    let option = {
        tooltip: {
            trigger: 'item',
            triggerOn: 'mousemove'
        },
        // title: {
        //     text: 'Interval Types Hierarchy',
        //     left: 'center'
        // },
        series: [
            {
                type: 'tree',
                id: 0,
                name: 'tree1',
                data: [data],

                top: '10%',
                bottom: '10%',
                left: '15%',
                right: '15%',

                symbolSize: 7,

                // edgeShape: 'polyline',
                edgeForkPosition: '63%',
                initialTreeDepth: 3,

                lineStyle: {
                    width: 2
                },

                label: {
                    backgroundColor: '#fff',
                    position: 'left',
                    verticalAlign: 'middle',
                    align: 'right',
                    formatter: function(node){
                        return node.value ? `${node.name} ${seconds_to_hms(node.value)}`: node.name;
                    }
                },

                leaves: {
                    label: {
                        position: 'right',
                        verticalAlign: 'middle',
                        align: 'left',
                        formatter: function(node){
                            return node.value ? `${node.name} ${seconds_to_hms(node.value)}`: node.name;
                        }
                    },
                },

                expandAndCollapse: true,
                animationDuration: 550,
                animationDurationUpdate: 750
            }
        ]
    };

    return option;
}
