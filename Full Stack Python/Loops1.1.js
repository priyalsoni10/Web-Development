let num = [3,5,11,2,7,8];
for(let i=0;i<num.length;i++){ //f traditional for loop(classical for loop)(index based loop)
   console.log(num[i]);
}
// forEach loop ->For-each loop ek aisa loop hota hai jo automatically array ya object ke elements ko ek-ek karke read karta hai.
//Isme aapko index manage nahi karna padta.
console.log("----------------");    
num.forEach((element) =>{
    console.log(element);

}
)
console.log("----------------"); 
num.forEach((element)=>{
    console.log(element * element);
})

// Array.form loop -> creates array from string or other iterable objects
let name = "JavaScript";
let arr = Array.from(name);
console.log(arr);
console.log("----------------");  

// For of loop -> For-off loop bhi for-each loop ki tarah hi hota hai jo iterable objects ke elements ko read karta hai.
// for...of ka use array, string, maps, sets jaise iterable cheezo ke values ko read karne ke liye hota hai
//Object par directly nahi chal sakta.
for(let element of name){
    console.log(element);
} 
console.log("----------------"); 
for (let i of num){
    console.log(i);
}
console.log("----------------");
let str = "RAM"; // string example
for (let ch of str) {
    console.log(ch); // R A M (each character on a new line)
}
console.log("----------------");
let array = [10, 20, 30]; // array example
for (let value of array) {
    console.log(value); // 10 20 30 (each number on a new line)
    }
console.log("----------------");
let arr1 = ["apple", "banana", "mango"];// array example

for (let [index, value] of arr1.entries()) {
    console.log(index, value);
}
console.log("----------------");
let mp = new Map([
    ["name", "Ravi"], // map example (key-value pairs)
    ["age", 20]
]);
for (let [key, value] of mp) {
    console.log(key, value);
}
console.log("----------------");
let st = new Set([1, 2, 3]); //  set example (unique values only)

for (let val of st) {
    console.log(val);
}
console.log("----------------");
let nums = [[1, 2], [3, 4]]; // nested array example

for (let pair of nums) {
    console.log(pair);
}
console.log("----------------");


// For in loop -> For-in loop ka use object ke properties ko read karne ke liye hota hai.
//Object ke keys ya array ke INDEX ko read karta hai
//Values lane ke liye: object[key]

let person = {
    name: "Amit",
    age: 25,
    city: "Delhi"
}; // for object

for (let key in person) {
    //console.log(key); // keys: name, age, city
    //console.log(person[key]); // values: Amit, 25, Delhi

    console.log(key, person[key]); // key-value pairs
}
console.log("----------------");

let fruits = ["apple", "banana", "mango"]; // for array

for (let index in fruits) {
    console.log(index, fruits[index]);// array index-value pairs
}
console.log("----------------");
let str1 = "ABC";
for (let index in str) {
    console.log(index, str1[index]); // string index-value pairs
}
console.log("----------------");
let student = {
    name: "Rahul",
    marks: { math: 90, sci: 85 }
};
for (let key in student) {
    console.log(key, student[key]);
}
console.log("----------------");

let users = [
    {id: 1, name: "Rohan"},
    {id: 2, name: "Mohan"}
];// array of objects

for (let index in users) {
    console.log(index, users[index].name);
}
console.log("----------------");
/// Object 
let student1 = {
    name: "Rahul",
    age: 20,
    city: "Delhi"
}; // object h jo internally key-value pairs ka collection hota hai JO DICTIONAYR KI TARAH KAAM KRTA HAI

/*
Object JavaScript ka sabse important data type hota hai.
Isme hum key–value pair ke form me data store karte hain.
Isme hum kisi bhi data type ka value store kar sakte hain, jaise ki string, number, array, function, aur even dusra object bhi.
Object internally ek dictionary ki tarah kaam karta hai:
Har key ko ek memory location milti hai
Key se uski value access hoti hai
Aap new key add kar sakte ho
Purani key update ho sakti hai
Keys unique hoti hain (duplicate key nahi hoti)
*/

let student2 = {
    name: "Rahul",
    age: 20,
    city: "Delhi"
};
console.log(student2.name);   // Rahul
console.log(student2.age);    // 20
console.log(student2.city);   // Delhi
console.log(student["city"]);   // Delhi  jb key string ya special character("hello".city ,full-name,full name ,123val or variable me store ho) me ho to dot se access nhi kr skte
console.log("----------------");

console.log("hello".length);//5 ye work krega kyuonki property h length string ki
//console.log("hello".city); //undefined ye nhi krega kyuonki aisi koi property nhi h string me
console.log("----------------");
student2.gender = "male"; // Adding new key-value pair
console.log(student2);
student2.age = 21; // Updating existing key-value pair
console.log(student2);
console.log("----------------");
delete student2.city;
console.log(student2); // Deleting key-value pair
console.log("----------------");
let user = {
    name: "Rohan",
    address: {
        city: "Indore",
        pin: 452001
    }
}; //object ke andar object (nested object)

console.log(user.address.city);  // Indore
for (let key in user) {
    console.log(key, user[key]);
}
console.log("----------------");
 let num2 = [1,2,3,4,5];
 for(let item of num2){
    console.log(item); // elements dega
}
console.log("----------------");
for(let i in num){
    console.log(i); // index dega

}





