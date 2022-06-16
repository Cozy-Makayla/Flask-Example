

let myName = 'Kayla';
const date = Date()

function printName(myName) {
    console.log(`${myName}`);
}

function messageHider() {
    let element = document.getElementById("message-box");
    element.classList.toggle("hidden");
}

function displayDate() {
    document.getElementById("date").innerHTML = Date();
}
