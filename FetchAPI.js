/*
fetch JavaScript ka built-in function hota hai jo server / API se data mangane (HTTP request) ke kaam aata hai 🌐
Simple words me:
fetch = internet se data laana
fetch kya karta hai?
Server ko request bhejta hai (GET, POST, etc.)
Response deta hai Promise ke form me
Mostly APIs se JSON data lene ke liye use hota hai
AJAX->Asyncronous Javascript and XML
 */


let p = fetch("https://goweather.herokuapp.com/weather/Ny") 
p.then((response) => {
    console.log(response.status);//200
    console.log(response.ok); // true
    // console.log(response.headers);
    // console.log(Request.header); ye hum pass krte h apnui request ke sath
    // console.log(response.text()); ye run hone ke baad data json me nhi aaega string me convert ho jaata h
     return response.json() // convert string responsse to json
}).then((response)=>{
      console.log(response);
}  )  

// let p = fetch("https://goweather.herokuapp.com/weather/Ny");

// p.then((response) => {
//     return response.json();
// }).then((data) => {
//     console.log(data);
// });
