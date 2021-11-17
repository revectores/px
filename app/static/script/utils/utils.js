function leading_zero(string){
    if (typeof(string) !== "string") string = string.toString();
    return string.length < 2 ? '0' + string : string;
}


function seconds_to_hms(seconds){
    let hour   = Math.floor(seconds / 3600);
    let minute = Math.floor(seconds % 3600 / 60);
    let second = seconds % 60;

    hour   = leading_zero(hour);
    minute = leading_zero(minute);
    second = leading_zero(second);

    duration_string = `${hour}h ${minute}m ${second}s`;
    return duration_string;
}


function date_format(date){
    let year  = date.getFullYear();
    let month = leading_zero(date.getMonth() + 1);
    let date_  = date.getDate();
    return `${year}-${month}-${date_}`;
}


function add_type_path(types){
    // if (Object.keys(types).length === 0) return;

    for (let [typeid, type] of Object.entries(types)) {
        let cur_type = Object.assign({}, type);
        let path_stack = [];
        while (cur_type !== undefined) {
            path_stack.push(cur_type.id);
            cur_type = types[cur_type.parent];
        }
        type.type_path = '';
        while (path_stack.length) {
            type.type_path += path_stack.pop();
            if (path_stack.length >= 1){
                type.type_path += '/';
            }
        }
    }
    return types
}


function add_paths(types){
    types = add_type_path(types);
    for (let [typeid, type] of Object.entries(types)) {
        name_path = '';
        type.type_path.split('/').forEach((id) => {
            name_path += types[id].name + '/'
        });
        type.name_path = name_path.substr(0, name_path.length - 1);
    }
    return types;
}
