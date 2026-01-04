//Simple loop
for (let i=0;i<5 ;i++){
    for(let j=0;j<5;j++)  {
        for(let k = 0; k<2; k++){
            console.log(i,j,k)
        }
        console.log("\n")
    }  
    console.log("\n")
} 
// Table 2 to 20
for(let i = 2;i<=20;i++){
    for(let j=1;j<=10;j++){
        console.log(`${i} x ${j} = ${i*j}`)
    }
    console.log("------------------------------")
}
 // Simple Pattern
star =""
for(let i=0;i<5;i++){
   for(let j=0;j<5;j++){
    star+="* "
 }
star+="\n"
console.log("----------------");
}
console.log(star);

 //Right triangle
 let n = 5; 
 let star1 =""
for(let i=0;i<n;i++){
   for(let j=0;j<=i;j++){
    star1+="* "
 }
star1+="\n"
}
console.log(star1)
console.log("----------------");

// Reverse Right triangle
 let n1 = 5; 
 let star2 =""
for(let i=0; i<n1 ;i++){
   for(let j=i ;j<=n1 ;j++){
    star2+="* "
 }
star2+="\n";
}
console.log(star2);
console.log("----------------");

//Triangle
let n2 = 5; 
 let star3 =""
for(let i=0; i<n2 ;i++){
   for(let j=0 ;j<=i ;j++){
    star3+="* "
 }
star3+="\n";
}
for(let i=0; i<n2 ;i++){
   for(let j=i ;j<=n2 ;j++){
    star3+="* "
 }
star3+="\n";
}
console.log(star3);
console.log("----------------"); 
//Triangle
let n4 = 5; 
 let star4 =""
for(let i=0; i < n4 ;i++){
   for(let j=i ;j<n4 ; j++){
    star4+=" "
 }
   for(let k=0 ;k<=i ;k++){
    star4+="* "
 }
star4+="\n";
}
console.log(star4);

// InvertedTriangle
let n5 = 5; 
let star5 =""
for(let i=0; i <= n5;i++){
   for(let j=0 ;j<=i ; j++){
    star5+=" "
 }
   for(let k=i ;k<=n ;k++){
    star5+="* "
 }
star5+="\n";
}
console.log(star5);
