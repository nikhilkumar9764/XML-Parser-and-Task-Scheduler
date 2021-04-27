function geterror() {
    document.getElementById("result").innerHTML = "<p>There is no data to display for the requested operation</p>";
    $("#result").show();
}

function sendreq() {
    console.log("Button CLICK OKK!!");
}

function copyToClipboard(text) {
    var dummy = document.createElement("textarea");
    document.body.appendChild(dummy);

    dummy.value = text;
    dummy.select();
    document.execCommand("copy");
    document.body.removeChild(dummy);
}

function getselect() {
    var chckd = $("#sel-all").prop("checked");
    if (chckd === true) {
        $(':checkbox').each(function () {
            this.checked = true;
        });
    }
    else {
        $(':checkbox').each(function () {
            this.checked = false;
        });
    }
}

function getcheckbox() {
    let myval = "";
    let j = 5;
    let row_cnt = 0;
    $("#mytable tr").each(function (i) {
        if (row_cnt > 0) {
            var $chkbox = $(this).find('input[type="checkbox"]');
            if ($chkbox.length) {
                var status = $chkbox.prop('checked');
                if (status === true) {
                    var dat_source = document.getElementById(`${j}`).innerText;
                    var xx = $(this).find('textarea').val();
                    myval += "/*------"
                    myval += dat_source;
                    myval += "------*/"
                    myval += '\n';
                    myval += xx;
                    myval += '\n';
                    myval += '\n';
                }
            }
            j += 4;
        }
        ++row_cnt;
    })
    copyToClipboard(myval);
}

async function getlasttenaccess(did) {
    var Table = document.getElementById("mytable");
    $("#result").hide();
    let url = `/cockpit/LastTenAccessed?dashboardId=${did}`;
    var tbl = document.getElementById("mytable");
    fetch(url, {
        method: 'GET'
    }).then(async function (response) {
        var j1 = await response.json();
        Table.innerHTML = "";
        if (Object.keys(j1).length > 0 && j1.hasOwnProperty("Error") === false) {
            var row = tbl.insertRow();
            var cell1 = row.insertCell();
            var cell2 = row.insertCell();
            cell1.innerHTML = "<b>Login</b>";
            cell2.innerHTML = "<b>Name</b>";
            for (var key in j1) {
                let uid = key;
                let name = j1[key];
                var row = tbl.insertRow();
                var cell1 = row.insertCell();
                var cell2 = row.insertCell();
                cell1.innerHTML = uid;
                cell2.innerHTML = name;
            }
        }
        else {
            geterror();
        }
    })
        .catch(function (error) {
            document.getElementById("result").innerHTML = "<p>Some error occurred while trying to fetch data</p>";
            $("#result").show();
        })
}


async function getdashboarddetail(did) {
    var Table = document.getElementById("mytable");
    $("#result").hide();
    let url = `/cockpit/DashboardInfo?dashboardId=${did}`;
    var tbl = document.getElementById("mytable");
    fetch(url, {
        method: 'GET'
    }).then(async function (response) {
        var j1 = await response.json();
        Table.innerHTML = "";
        if (Object.keys(j1).length > 0 && typeof (j1['ContactPersonUserId']) !== 'undefined') {
            var row = tbl.insertRow();
            var cell1 = row.insertCell();
            var cell2 = row.insertCell();
            var cell3 = row.insertCell();
            var cell4 = row.insertCell();
            var cell5 = row.insertCell();
            var cell6 = row.insertCell();
            var cell7 = row.insertCell();
            var cell8 = row.insertCell();
            var cell9 = row.insertCell();
            var cell10 = row.insertCell();
            cell1.innerHTML = "<b>ContactPerson Id</b>";
            cell2.innerHTML = "<b>ContactPerson</b>";
            cell3.innerHTML = "<b>CreatedBy</b>";
            cell4.innerHTML = "<b>Created Date</b>";
            cell5.innerHTML = "<b>Dashboard ID</b>";
            cell6.innerHTML = "<b>Group Name</b>";
            cell7.innerHTML = "<b>Dashboard Name</b>";
            cell8.innerHTML = "<b>Updated By</b>";
            cell9.innerHTML = "<b>Updated Date</b>";
            cell10.innerHTML = "<b>Is Public</b>";

            var r1 = tbl.insertRow();
            var cell11 = r1.insertCell();
            var cell12 = r1.insertCell();
            var cell13 = r1.insertCell();
            var cell14 = r1.insertCell();
            var cell15 = r1.insertCell();
            var cell16 = r1.insertCell();
            var cell17 = r1.insertCell();
            var cell18 = r1.insertCell();
            var cell19 = r1.insertCell();
            var cell20 = r1.insertCell();

            cell11.innerHTML = j1['ContactPersonUserId'];
            cell12.innerHTML = j1['ContactPersonUserInfo'];
            cell13.innerHTML = j1['CreatedBy']
            cell14.innerHTML = j1['CreatedDate']
            cell15.innerHTML = j1['ID'];
            cell16.innerHTML = j1['GroupName'];
            cell17.innerHTML = j1['Name']
            cell18.innerHTML = j1['UpdatedBy']
            cell19.innerHTML = j1['UpdatedDate']
            cell20.innerHTML = j1['IsPublic']
        }
        else {
            geterror();
        }
    })
        .catch(function (error) {
            document.getElementById("result").innerHTML = "<p>Some error occurred while trying to fetch data</p>";
            $("#result").show();
        })
}


async function getdashboarddatasources(did) {
    var Table = document.getElementById("mytable");
    $("#result").hide();
    let url = `/cockpit/DataSourceInfo?dashboardId=${did}`;
    var tbl = document.getElementById("mytable");
    fetch(url, {
        method: 'GET'
    }).then(async function (response) {
        var j1 = await response.json();
        Table.innerHTML = "";
        if (Object.keys(j1).length > 0 && j1.hasOwnProperty("Error") === false) {
            var row = tbl.insertRow();
            var cell1 = row.insertCell();
            var cell2 = row.insertCell();
            cell1.innerHTML = "<b>Datasource</b>";
            cell2.innerHTML = "<b>Table Name</b>";
            for (var key in j1) {
                let uid = key;
                let lisa = j1[key];
                var row = tbl.insertRow();
                var cell1 = row.insertCell();
                var cell2 = row.insertCell();
                cell1.innerHTML = uid;
                for (let i = 0; i < lisa.length; i++) {
                    cell2.innerHTML += "[" + lisa[i] + "]";
                    if (i < lisa.length - 1) {
                        cell2.innerHTML += ',';
                    }
                }
            }
        }
        else {
            geterror();
        }
    })
        .catch(function (error) {
            document.getElementById("result").innerHTML = "<p>Some error occurred while trying to fetch data</p>";
            $("#result").show();
        })
}

async function getcustomquery(did) {
    var Table = document.getElementById("mytable");
    $("#result").hide();
    let url = `/cockpit/CustomQuery?dashboardId=${did}`;
    var tbl = document.getElementById("mytable");
    fetch(url, {
        method: 'GET'
    }).then(async function (response) {
        var j1 = await response.json();
        Table.innerHTML = "";
        if (Object.keys(j1).length > 0 && j1.hasOwnProperty("Error") === false) {
            var row = tbl.insertRow();
            var cell1 = row.insertCell();
            var cell2 = row.insertCell();
            var cell3 = row.insertCell();
            cell1.style.width = "15%";
            cell2.style.width = "35%";
            cell3.style.width = "50%";
            cell1.innerHTML = "<input type = 'checkbox' id = 'sel-all' onclick='getselect()'>";
            cell1.id = 1;
            cell2.innerHTML = "<b>Datasource</b>";
            cell2.id = 2;
            cell3.innerHTML = "<b>Custom Query</b>" + '<button type="button" id ="b11" class="btn btn-default pull-right" onclick = "getcheckbox()"><span class="glyphicon glyphicon-copy"></span>Copy</button>';
            cell3.id = 3;
            let j = 4;
            for (var key in j1) {
                let uid = key;
                let lisa = j1[key];
                for (let i = 0; i < lisa.length; i++) {
                    var row = tbl.insertRow();
                    var cell11 = row.insertCell();
                    var cell12 = row.insertCell();
                    var cell13 = row.insertCell();
                    cell11.id = j;
                    ++j;
                    cell12.id = j;
                    ++j;
                    cell13.id = j;
                    ++j;
                    cell11.style.width = "15%";
                    cell12.style.width = "35%";
                    cell13.style.width = "50%";
                    cell11.innerHTML = `<input type = 'checkbox'>`;
                    cell12.innerText = uid;
                    cell13.innerHTML += `<textarea style = 'width:100%;' id = '${j}'>` + lisa[i] + "</textarea>";
                    ++j;
                }
            }
        }
        else {
            geterror();
        }
    })
        .catch(function (error) {
            document.getElementById("result").innerHTML = "<p>Some error occurred while trying to fetch data</p>";
            $("#result").show();
        })
}


async function getIndexes(did) {
    var Table = document.getElementById("mytable");
    $("#result").hide();
    let url = `/cockpit/Indexes?dashboardId=${did}`;
    var tbl = document.getElementById("mytable");
    var aMap = {};
    fetch(url, {
        method: 'GET'
    }).then(async function (response) {
        var j1 = await response.text();
        Table.innerHTML = "";
        var mylist = JSON.parse(j1);
        for (let i = 0; i < mylist.length; i++) {
            aMap[mylist[i][0]] = aMap[mylist[i][0]] || [];
            aMap[mylist[i][0]].push(mylist[i][1]);
        }
        if (Object.keys(aMap).length > 0 && aMap.hasOwnProperty("Error") === false) {
            var row = tbl.insertRow();
            var cell1 = row.insertCell();
            var cell2 = row.insertCell();
            cell1.innerHTML = "<b>Datasource</b>";
            cell2.innerHTML = "<b>Columns used in relation and filters</b>";
            for (var key in aMap) {
                let uid = key;
                let lisa = aMap[key];
                var row = tbl.insertRow();
                var cell1 = row.insertCell();
                var cell2 = row.insertCell();
                cell1.innerHTML = uid;
                for (let i = 0; i < lisa.length; i++) {
                    cell2.innerHTML += "[" + lisa[i] + "]";
                    if (i < lisa.length - 1) {
                        cell2.innerHTML += ',';
                    }
                }
            }
        }
        else {
            geterror();
        }
    })
        .catch(function (error) {
            document.getElementById("result").innerHTML = "<p>Some error occurred while trying to fetch data</p>";
            $("#result").show();
        })
}

async function getqueryexec(did) {
    var Table = document.getElementById("mytable");
    $("#result").hide();
    let url = `/cockpit/CustomQueryExecutionTime?dashboardId=${did}`;
    var tbl = document.getElementById("mytable");
    fetch(url, {
        method: 'GET'
    }).then(async function (response) {
        var resp = await response.json();
        Table.innerHTML = "";
        var xx = document.getElementById('f1');
        if (typeof (xx) != 'undefined' && xx != null) {
            xx.remove();
        }
        if (Object.keys(resp).length > 0 && resp.hasOwnProperty("Error") === false) {
            var f = document.createElement("form");
            f.setAttribute('id', 'f1');
            f.setAttribute("method", "get");
            for (var k1 in resp) {
                let uid = k1;
                let vv = resp[k1];
                var one = vv.includes("(System.Int16)");
                var two = vv.includes("(System.Int32)");
                var three = vv.includes("(System.Int64)");
                var four = vv.includes("(System.String)");
                var five = vv.includes("(System.DateTime)");
                if (one === true || two === true || three === true) {
                    console.log("Entered here!!");
                    var lab = document.createElement("label");
                    lab.setAttribute("for", uid);
                    lab.innerText = `Enter value for ${uid} ?:`;
                    var inp = document.createElement("input");
                    inp.setAttribute("type", "number");
                    inp.setAttribute("id", uid);
                    inp.setAttribute("required", "");
                    var newLine = document.createElement('br');
                    f.appendChild(newLine);
                    f.appendChild(lab);
                    f.appendChild(inp);
                }
                else if (four === true) {
                    var lab = document.createElement("label");
                    lab.setAttribute("for", uid);
                    lab.innerText = `Enter value for ${uid} ?:`;
                    var inp = document.createElement("input");
                    inp.setAttribute("type", "text");
                    inp.setAttribute("id", uid);
                    inp.setAttribute("required", "");
                    var newLine = document.createElement('br');
                    f.appendChild(newLine);
                    f.appendChild(lab);
                    f.appendChild(inp);
                }
                else if (five === true) {
                    var lab = document.createElement("label");
                    lab.setAttribute("for", uid);
                    lab.innerText = `Enter value for ${uid} ?:`;
                    var inp = document.createElement("input");
                    inp.setAttribute("type", "date");
                    inp.setAttribute("id", uid);
                    inp.setAttribute("required", "");
                    var newLine = document.createElement('br');
                    f.appendChild(newLine);
                    f.appendChild(lab);
                    f.appendChild(inp);
                }
            }
            var newLine = document.createElement('br');
            f.appendChild(newLine);
            var btn = document.createElement("input");
            btn.setAttribute('type', "submit");
            btn.setAttribute('value', "Submit");
            btn.setAttribute('id', 'btx');
            btn.setAttribute('onclick', 'sendreq()');
            f.appendChild(btn);
            document.getElementsByTagName('body')[0].appendChild(f);
        }
    })
        .catch(function (error) {
            document.getElementById("result").innerHTML = "<p>Some error occurred while trying to fetch data</p>";
            $("#result").show();
        })
}


function getdetails() {
    let did = document.getElementById("dashboard_inp").value;
    let option_sel = document.getElementById("choice_inp").value;
    if (option_sel == "Get Last 10 Accessed") {
        getlasttenaccess(did);
    }
    else if (option_sel == "Get Dashboard Info") {
        getdashboarddetail(did);
    }
    else if (option_sel == "Get Dashboard DataSources") {
        getdashboarddatasources(did);
    }
    else if (option_sel == "Get Custom SQL") {
        getcustomquery(did);
    }
    else if (option_sel == "Get Columns used in Relation and Filters to create Indexes") {
        getIndexes(did);
    }
    else if (option_sel == "Get Query Execution Time") {
        getqueryexec(did);
    }
}