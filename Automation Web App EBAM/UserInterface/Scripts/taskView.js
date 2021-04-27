var task_list = {};

function convertDate(secs) {
    let date = new Date(secs * 1000);
    return date.toString();
}


async function create_button(idx, ele, st) {
    console.log(idx, st);
    let x = document.createElement('button');
    var n1 = document.createElement('br');
    x.setAttribute('id', `${idx}`);
    console.log(task_list[idx]);
    x.innerHTML += task_list[idx]['TaskId'];
    x.innerHTML += '&nbsp;&nbsp;';
    x.innerHTML += task_list[idx]['TaskName'];
    x.innerHTML += '&nbsp;&nbsp;';
    x.innerHTML += task_list[idx]['Description'];
    x.innerHTML += '&nbsp;&nbsp;';
    x.innerHTML += convertDate(task_list[idx]['TaskLastRunTime']);
    x.setAttribute('style', 'font-size:60px');
    x.setAttribute('style', 'width:100%');
    x.setAttribute('style', 'margin-left:30px');
    if (st === 'red') {
        x.setAttribute('class', 'btn btn-danger btn-block');
    }
    else if (st === 'blue') {
        x.setAttribute('class', 'btn btn-primary btn-block');
    }
    else if (st === 'green') {
        x.setAttribute('class', 'btn btn-success btn-block');
    }
    x.setAttribute('onclick', `disp_content(${idx})`);
    ele.appendChild(x);
    ele.appendChild(n1);
}

async function get_tasks() {
    let ele = document.getElementById("tasks");
    let url = '/task/ShowTasks';
    fetch(url, {
        method: 'POST'
    }).then(async function (response) {
        response = await response.json();
        let state = '';
        response.forEach((vb) => {
            task_list[vb['TaskId']] = vb;
            console.log(vb);
            if (vb['TaskLastRunSuccessfully'] === -1) {
                state = 'red';
                create_button(vb["TaskId"], ele, state);
            }
            else if (vb['TaskLastRunSuccessfully'] === 0) {
                state = 'blue';
                create_button(vb["TaskId"], ele, state);
            }
            else if (vb['TaskLastRunSuccessfully'] === 1) {
                state = 'green';
                create_button(vb["TaskId"], ele, state);
            }
        });
    });
}

function appendImagetodiv(vb) {
    let ele = document.getElementById("taskresult");
    var image = new Image();
    image.src = "data:image/png;base64, " + vb["TaskResult"]["image"];
    ele.appendChild(image);
}

async function disp_content(task_id) {
    let url = '/task/Task';
    let ele = document.getElementById("taskresult");
    ele.innerHTML = "";
    let data = { "TaskId": task_id };
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    }).then(async function (response) {
        response = await response.json();
        console.log(response);
        response.forEach((vb) => {
            appendImagetodiv(vb);
            console.log(vb);
        });
    });



}


setTimeout(get_tasks, 2000);