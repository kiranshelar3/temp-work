
let fetchbtn = document.getElementById('fetchid');
fetchbtn.addEventListener('click', buttonclickhandler)


function buttonclickhandler() {

    const xhr = new XMLHttpRequest();

    xhr.open('GET', 'random.txt', true);

}
xhr.onload = function () {
    if (this.status === 200) {

        console.log(this.responseText)
    }
    else {
        console.error("some error occured.")
    }
}
xhr.send()


