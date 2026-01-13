// Promises ->Promises in javascript
//  Promise kya hota hai?
// Promise ek aisa object hai jo future me hone wale kaam ka result represent karta hai
//  ya to kaam complete hoga (resolve)
//  ya fail hoga (reject)

//  Mostly use hota hai:
// API calls
// File reading
// Timers
// Async operations

//  Promise ke 3 states
// 1 Pending - kaam chal raha hai
// 2 Fulfilled - kaam successfully ho gaya
// 3 Rejected - error aa gaya

// Promises creation
const promiseOne = new Promise(function(resolve , reject){ // ye callback leta h
    // Do an async task
    //DB calls, cryptography ,network
    setTimeout(function(){
        console.log('Async task is complete');
        resolve()
    },1000)
})  // instance(object) mil jaata  h(ES6 me introduce hua h) blue bird or queue phle use hota tha
promiseOne.then(function(){ //ye function automatically ek argument receive krtah jo bhi kaam settimeout function se hua h values return krta h
    console.log("Promise Consumed");
}) // directly connect  to resolve

console.log('------------------------');

new Promise(function(resolve,reject){
    setTimeout(function(){
        console.log("Async task 2");
        resolve()
    },1000)
}).then(function(){
    console.log("Async 2 resolve");
})

console.log('------------------------');

const promiseThree = new Promise(function(resolve,reject){
    setTimeout(function(){
        resolve({username:"Abc",email: "Abc@gmail.com" })
    },1000)
})
promiseThree.then(function(user){// Promise consume krte h
    console.log(user);// { username: 'Abc', email: 'Abc@gmail.com' }
})

console.log('------------------------');

const promisefour =  new Promise(function(resolve,reject){
    setTimeout(function(){
        // let error = true
        let error = false
        if(!error){
            resolve({username:"Priyal",Password:"123"})
        }
        else{
            reject('ERROR : Something went wrong')
        }

    },1000)
})
// promisefour.then().catch()// promise consume krna
promisefour.then((user)=>{
      console.log(user); //{ username: 'Priyal', Password: '123' }
      return user.username;
}).then((username)=>{ //call back hell chainning
    console.log(username);// Priyal
    
}).catch(function(error){
    console.log(error);//ERROR : Something went wrong(if error true)
}).finally(()=>{
    console.log("The promise is either resolve or reject!");
})
console.log("-----------------------");
/**
avaScript by default synchronous hota hai
Matlab:
Ek kaam khatam → phir doosra kaam
Agar koi kaam time leta hai (API call, file read, DB query), to pura program ruk jata hai 😵
Async / Await asynchronous code ko synchronous jaisa likhne ka tareeka hai 💡
 async kya karta hai?
Function ko asynchronous bana deta hai
Automatically Promise return karta hai 
await kya karta hai?

Promise ke complete hone ka wait karta hai

Result milne ke baad next line chalata hai
await sirf async function ke andar kaam karta hai
**/

const promiseFive = new Promise(function(resolve,reject){
    setTimeout(function(){
       let error = true
        if(!error){
            resolve({username:"JavaScript",Password:"123"})
        }
        else{
            reject('ERROR : JS went wrong')
        }

    },1000)
});

async function consumePromiseFive() {
    try{
    const response = await promiseFive
    console.log(response);
    }catch(error){
        console.log(error);
    }
    
}
consumePromiseFive();

async function getAllUsers() {
    try{
        const response = await  fetch('https://jsonplaceholder.typicode.com/users')
        console.log(response); // string format me aayega data
        const data =  response.json()
         console.log(data);
    }catch(error){
      console.log("Error:",error);
    }
    
}
getAllUsers()

fetch('https://jsonplaceholder.typicode.com/users').then((response)=>{
    return response.json()
}).then((data)=>{ // ek then khatam hone ke baad hi dusra then start hoga
    console.log(data);
})
.catch((error)=>console.log(error))



