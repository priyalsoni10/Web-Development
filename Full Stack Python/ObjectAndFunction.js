let Human ={
    Eyes :2 ,
    Hands : 2,
    Legs : 2 
}
let P1 = {
    Name : "Bob",
    Age :  21 ,
    Job : "Developer",
    ...Human //(...) Spread operator or rest operator
}
console.log(P1);//{ Name: 'Bob', Age: 21, Job: 'Developer', Eyes: 2, Hands: 2, Legs: 2 }
