function raiseError(msg) {
    var exist = document.getElementById("alx");
    if (typeof exist !== "undefined" && exist !== null) {
        exist.remove();
    }
    var ft = document.getElementById("fp");
    var pp = document.createElement("p");
    pp.setAttribute("class", "alert alert-warning");
    pp.innerText = msg;
    pp.setAttribute("id", "alx");
    ft.appendChild(pp);
    document.getElementsByTagName("body")[0].appendChild(ft);
}

function sendreq(tsksel) {

    let check = $("#isonce").prop("checked");
    if (
        $("#did").val() === "" ||
        $("#durl").val() === "" ||
        $("#tout").val() === "" ||
        $("#desc").val() === "" ||
        (
            check === false &&
            $("#interv").val() === ""
        )
    ) {
        console.log("fnkfsdjk\n");
        msg = "Please fill in the required fields\n";
        raiseError(msg);
    } else {
        let vv = document.getElementById("interv").value;
        if (check === false && vv < 10) {
            console.log("sdhsfkd\n");
            msg = "Enter interval time of running to be >=10 minutes\n";
            raiseError(msg);
        } 
        else {
            var ft = document.getElementById("alx");
            if (typeof ft !== "undefined" && ft !== null)
             {
                ft.remove();
             }
            let v1 = $("#did").val();
            let v2 = $("#durl").val();
            let v3 = $("#tout").val();
            let v4 = parseInt($("#interv").val());
            let decrip = $("#desc").val();
            let onlyonce = 0;
            if (check === true) {
                onlyonce = 1;
                v4 = 123;
            }
            console.log(v4 * 60);
            va = {
                "DashboardId": v1,
                "DashboardUrl": v2,
                "TimeOut": v3 * 1000 * 60,
                "Description": decrip,
                "OnlyOnce": onlyonce,
                "Interval": v4 * 60,
            };
            data = { "TaskType": "DashboardTest", "Arg": va };
            console.log(data);
            fetch("/task/AddTask", {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            }).then(async function (resp) {
                console.log(resp);
                resp_final = await resp.json();
                alert(JSON.stringify(resp_final));
            });
        }
        }
}

function send_del_req() {
    if ($("#did").val() === "") {
        let msg = "Please fill in the required fields\n";
        raiseError(msg);
    }
    else {
        let task_id = parseInt($("#did").val());
        data = { "TaskId": task_id };
        console.log(data);
        fetch("/task/DeleteTask", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        }).then(async function (resp) {
            resp_final = await resp.json();
            alert(JSON.stringify(resp_final));
        });


    }



}
function chckboxchange() {
    var ptp = $("#isonce").prop("checked");
    console.log(ptp);
    var one = document.getElementById("interv");
    var two = document.getElementById("lablint");
    if (ptp === true) {
        one.disabled = true;
    } else {
        one.disabled = false;
        // var newLine = document.createElement('br');
        // var lab3 = document.createElement("label");
        // var ff = document.getElementById("fp");
        // lab3.setAttribute("id","lablint");
        // lab3.innerText = `Enter the interval of running the task ? :`;
        // var interval_dur = document.createElement("input");
        // interval_dur.setAttribute('type',"number");
        // interval_dur.setAttribute("id","interv");
        // ff.appendChild(lab3);
        // ff.appendChild(interval_dur);
        // document.getElementsByTagName('body')[0].appendChild(ff);
    }
}

function addtask(mytasksel) {
    var exist = document.getElementById("fp");
    if (typeof exist !== "undefined" && exist !== null) {
        exist.remove();
    }
    var ff = document.createElement("form");
    ff.setAttribute("id", "fp");
    var lab = document.createElement("label");
    lab.setAttribute("for", "did");
    lab.setAttribute("style", "font-size:medium");
    lab.innerText = `Enter the dashboard id?:`;
    var inp = document.createElement("input");
    inp.setAttribute("type", "number");
    inp.setAttribute("id", "did");
    inp.setAttribute("required", "");

    var lab1 = document.createElement("label");
    lab1.setAttribute("for", "durl");
    lab1.setAttribute("style", "font-size:medium");
    lab1.innerText = `Enter the dashboard URL correctly?:`;
    var inpurl = document.createElement("input");
    inpurl.setAttribute("type", "text");
    inpurl.setAttribute("id", "durl");
    inpurl.setAttribute("required", "");

    var lab6 = document.createElement("label");
    lab6.setAttribute("for", "desc");
    lab6.setAttribute("style", "font-size:medium");
    lab6.innerText = `Enter the Description?:`;
    var inpdesc = document.createElement("input");
    inpdesc.setAttribute("type", "text");
    inpdesc.setAttribute("id", "desc");
    inpdesc.setAttribute("required", "");

    var lab4 = document.createElement("label");
    lab4.setAttribute("for", "tout");
    lab4.setAttribute("style", "font-size:medium");
    lab4.innerText = `Enter the expected timeout of the task in seconds?:`;
    var taskout = document.createElement("input");
    taskout.setAttribute("type", "number");
    taskout.setAttribute("id", "tout");
    taskout.setAttribute("required", "");

    var lab2 = document.createElement("label");
    lab2.setAttribute("for", "isonce");
    lab2.setAttribute("style", "font-size:medium");
    lab2.innerText = `Run the task once?:`;
    var chckbox = document.createElement("input");
    chckbox.setAttribute("type", "checkbox");
    chckbox.setAttribute("id", "isonce");
    chckbox.setAttribute("onclick", "chckboxchange()");

    var lab3 = document.createElement("label");
    lab3.setAttribute("id", "lablint");
    lab3.setAttribute("style", "font-size:medium");
    lab3.innerText = `Enter the interval of running the task ? :`;
    var interval_dur = document.createElement("input");
    interval_dur.setAttribute("type", "number");
    interval_dur.setAttribute("id", "interv");
    interval_dur.setAttribute("required", "");

    var btn = document.createElement("input");
    btn.setAttribute("type", "button");
    btn.setAttribute("value", "Submit");
    btn.setAttribute("class", "btn btn-success");
    btn.setAttribute("id", "btx");
    btn.setAttribute("onclick", 'sendreq("' + mytasksel + '")');

    var n1 = document.createElement("br");
    var n2 = document.createElement("br");
    var n3 = document.createElement("br");
    var n4 = document.createElement("br");
    var n5 = document.createElement("br");
    var n6 = document.createElement("br");
    var n7 = document.createElement("br");
    var n8 = document.createElement("br");
    var n9 = document.createElement("br");
    var n10 = document.createElement("br");
    var n11 = document.createElement("br");
    var n12 = document.createElement("br");
    ff.appendChild(n1);
    ff.appendChild(lab);
    ff.appendChild(inp);
    ff.appendChild(n2);
    ff.appendChild(n6);
    ff.appendChild(lab1);
    ff.appendChild(inpurl);
    ff.appendChild(n3);
    ff.appendChild(n7);
    ff.appendChild(lab6);
    ff.appendChild(inpdesc);
    ff.appendChild(n11);
    ff.appendChild(n12);
    ff.appendChild(lab4);
    ff.appendChild(taskout);
    ff.appendChild(n9);
    ff.appendChild(n10);
    ff.appendChild(lab2);
    ff.appendChild(chckbox);
    ff.appendChild(n4);
    ff.appendChild(n8);
    ff.appendChild(lab3);
    ff.appendChild(interval_dur);
    ff.appendChild(n5);
    ff.appendChild(btn);
    document.getElementsByTagName("body")[0].appendChild(ff);
}

function updatetask(mytasksel) { }

function deletetask(mytasksel) {
    var exist = document.getElementById("fp");
    if (typeof exist !== "undefined" && exist !== null) {
        exist.remove();
    }
    var ff = document.createElement("form");
    ff.setAttribute("id", "fp");
    var lab = document.createElement("label");
    lab.setAttribute("for", "did");
    lab.setAttribute("style", "font-size:medium");
    lab.innerText = `Enter the task id?:`;
    var inp = document.createElement("input");
    inp.setAttribute("type", "number");
    inp.setAttribute("id", "did");
    inp.setAttribute("required", "");

    var btn = document.createElement("input");
    btn.setAttribute("type", "button");
    btn.setAttribute("value", "Delete");
    btn.setAttribute("class", "btn btn-danger");
    btn.setAttribute("id", "btx");
    btn.setAttribute("onclick", 'send_del_req("' + mytasksel + '")');

    var n1 = document.createElement("br");
    var n2 = document.createElement("br");
    var n3 = document.createElement("br");

    ff.appendChild(n1);
    ff.appendChild(lab);
    ff.appendChild(inp);
    ff.appendChild(n2);
    ff.appendChild(n3);
    ff.appendChild(btn);
    document.getElementsByTagName("body")[0].appendChild(ff);
}

function taskaction() {
    let task_sel = document.getElementById("task_inp").value;
    if (task_sel == "Dashboard Performance Testing") {
        let tsk = "DashboardTest";
        let option_sel = document.getElementById("choice_inp").value;
        if (option_sel == "Add a task to perform") {
            addtask(tsk);
        } else if (option_sel == "Update an existing task") {
            updatetask(tsk);
        } else if (option_sel == "Delete a task") {
            deletetask(tsk);
        }
    }
}