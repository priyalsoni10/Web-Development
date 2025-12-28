let Human ={
    Eyes :2 ,
    Hands : 2,
    Legs : 2 
}
// Spread operator
let P1 = {
    Name : "Bob",
    Age :  21 ,
    Job : "Developer",
    // Spread operator: Existing object/array ke elements ko copy karke naya object/array me daalna.
    // Rest Operator: Function me ya destructuring me baki ke elements/properties ko ek variable me collect karna.
    ...Human // isme human dobara bnaya h (...) Spread operator or rest operator kehte h but but yha spread operator use hua h
}
console.log(P1);//{ Name: 'Bob', Age: 21, Job: 'Developer', Eyes: 2, Hands: 2, Legs: 2 }
console.log('---------------------');  
// Rest operator
function sum(a, b, ...rest) {
  console.log(rest); // baaki arguments ka array
}
sum(1, 2, 3, 4); // [3, 4] baki bacche element ka naya array
console.log('---------------------');  
let { Name, ...others } = { Name: "Bob", Age: 21, Job: "Dev" };
console.log(others); // { Age: 21, Job: 'Dev' }
console.log('----------------------');

let p ={
    Name : "Bob",
    Age :  21 ,
    Job : "Developer",
    // prototype : Human -> hr object me prototype hota h or hr prototype me object hi rkh skte h  isko prototypal chainning
    __proto__ : Human // ye inheritance h yha (...) nhi lgaya h isleye vo spread nhi hua h 

}
// p.__proto__ = Human //ye inheritance h ye extend keya hua data magne pr hi dekhata
console.log(p); // { Name: 'Bob', Age: 21, Job: 'Developer' }
console.log(p.Eyes); // 2 -> jo share ho gya h vo magne pr print hoga nhi to p only print hoga 
console.log(p.__proto__); // { Eyes: 2, Hands: 2, Legs: 2 }
console.log('----------------------')

let p2 = {
    Name: "Ajay",
    Age: 23
}
let x2 = p2 // jo p2 me h vo x2 me bhi h or x2 me change krenge to p2 me bhi ho jaega
console.log(x2.Name);// Ajay
console.log(x2.Age); // 23 
p2.Age = 24 ;
console.log(x2.Age); // 24
Object.freeze(p2) // object change nhi ho skta h ab
p2.Age = 25 ;
console.log(x2.Age); // 24
let y = p2
console.log(y); // { Name: 'Ajay', Age: 24 }
y.Age = 25;
console.log(y.Age); // 24  ye change nhi ho skta
console.log('------------------------');

//  global object jo this naam ke variable/propeerty me hota h
console.log(this);// {} ->node pr  khali object but browser ke  console me khali nhi rhta h window nam ka object me (html ,css or  basic javascript compilation process,browser contol access like camera,location etc  )





