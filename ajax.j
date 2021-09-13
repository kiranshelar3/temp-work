
// localStorage.setItem('["name":"test34","salary":"173","age":"23"]' )
// console.log(localStorage.getItem("salary"))


let fetchbtn = document.getElementById('fetchid');
fetchbtn.addEventListener('click', buttonclickhandler)

// function making 

function buttonclickhandler() {

    // instantiating the object 

    const xhr = new XMLHttpRequest();

    // open the object with assynchronous request=true(non-blocking)
    xhr.open('GET', 'https://jsonplaceholder.typicode.com/todos/1', true);


    xhr.onload = function () {
        if (this.status === 200) {

            console.log(this.responseText)
        }
        else {
            console.error("some error occured.")
        }
    }
    // sending the request 
    xhr.send()

}

let pstbtn = document.getElementById('backupid');
pstbtn.addEventListener('click', buttonclickhandler2)


function buttonclickhandler2() {
    
    // obj creation 
    const xhr1 = new XMLHttpRequest();
    
    // post request 
    xhr1.open('POST', 'http://dummy.restapiexample.com/api/v1/create', true);
    xhr1.getResponseHeader('content-type', 'application/json');

    xhr1.onload = function () {
        if (this.status === 200) {
            console.log(this.responseText)
        }
        else {
            console.error("error occured")
        }
    }

    para = '{"name":"test34","salary":"173","age":"23"} ';
    xhr1.send(para)

}

let popbtn = document.getElementById('popbtid');
popbtn.addEventListener('click', buttonclickhandler3)

function buttonclickhandler3(){
    console.log('you clicked in populate')

    const xhr3 = new XMLHttpRequest();

    xhr3.open('GET','http://dummy.restapiexample.com/api/v1/employees',true);

    xhr3.onload = function(){
        if(this.status ==200){
            let obj = JSON.parse(this.responseText);
            console.log(obj)
            let list = document.getElementById('list');
            str = "";
            for(key in obj)
            {
                str += `<li> ${obj[key].employee_name}</li>`;
            }  
            list.innerHTML = str;

        }
        else{
            console.log("error occurred")
        }
    }
    xhr3.send();
}