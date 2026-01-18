// API -> Application programming interface
// AJAX -> Asynchronous javascript and XML(XML replace to json -> AJAJ)
// JSON -> Javascript object Notation
// jSon ()-> return a second promise that resolves with the result of parsing the response body text as JSON(Input is json,outtput is js object)
const URL = "https://api.thedogapi.com/v1";
const factPara = document.querySelector("#fact");
const btn = document.querySelector("#btn");

promise1 = fetch(URL);
console.log(promise1);
console.log("Getting data....");
const getFacts = async () =>{
    let response = await fetch(URL);
    console.log(response);// get request h -> json data
    console.log(response.status);//200 mtlb request okk h 
    let data = await response.json();
    factPara.innerText = data.service
    console.log(data);
    // console.log(data[0]); mere case me undefined h kyunki ek hi row h data me
    console.log(data.env); // production
}
btn.addEventListener("click",getFacts);

function getFact(){
    fetch(URL).then((response) =>{
        return response.json();
    }).then((data)=>{
        console.log(data);
         console.log(data.env); // production
    })
}
console.log("-------------------");

//Request and Response
// HTTP->Hyper text transfer protocol
// Responsestatus code
// HTTP response headers also contain detail about the response such as content type HTTP status code etc

/*
HTTP requests (methods) client (browser / app) aur server ke beech data bhejne–lene ke rules hote hain.
GET, POST, PUT, DELETE, PATCH sab HTTP methods hain.
1. GET Request
 Data lene ke liye (read only)
Server se data fetch karta hai
Database me koi change nahi karta
Real life:Amazon pe product list dekhna
POST Request
Naya data create karne ke liye
Server me new record add karta hai
Data body me bheja jata hai
Real life: Signup / Register form submit
PUT Request
Poora data update karne ke liye
Existing data ko completely replace karta hai
Real life: Profile edit (name, email, age sab change)
PATCH Request
Partial update ke liye
Sirf selected fields update karta hai
Real life: Sirf mobile number update
DELETE Request
Data delete karne ke liye
Server se record remove karta hai
Real life:  Account delete / Cart item remove
*/

