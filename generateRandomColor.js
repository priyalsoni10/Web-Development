// // Generate random color  
//  const randomColor = function(){
//     const hex = "0123456789ABCDEF"
//     let color = '#';
//     for(let i = 0; i<6 ; i++) {
//        color += hex[(Math.floor(Math.random()* 16))]
//     }
//     return color;
//  };
// //  console.log(randomColor);
// //  console.log(Math.random()*10);
// //  console.log(Math.floor(Math.random()*16));
// let intervalId;
// const startChangingColor = function(){
//    if(!intervalId){
//        intervalId =  setInterval(changeBgColor,1000);
//    }    
//        function changeBgColor(){
//            document.body.style.backgroundColor = randomColor();
//    }
// };
// const stopChangingColor = function(){
//   clearInterval(intervalId);
//   intervalId = null;
// } ;
// document.querySelector('#start').addEventListener('click', startChangingColor);
// document.querySelector('#stop').addEventListener('click', stopChangingColor);


// let intervalId;

// const randomColor = function () {
//   const hex = "0123456789ABCDEF";
//   let color = "#";
//   for (let i = 0; i < 6; i++) {
//     color += hex[Math.floor(Math.random() * 16)];
//   }
//   return color;
// };

// const startChangingColor = function () {
//   if (!intervalId) {
//     intervalId = setInterval(() => {
//       document.body.style.backgroundColor = randomColor();
//     }, 1000);
//   }
// };

// const stopChangingColor = function () {
//   clearInterval(intervalId);
//   intervalId = null;
// };

// document.querySelector('#start').addEventListener('click', startChangingColor);
// document.querySelector('#stop').addEventListener('click', stopChangingColor);


// const buttons = document.querySelectorAll('.button');

// buttons.forEach((button) => {
//   button.addEventListener('click', (e) => {
//     document.body.style.backgroundColor = e.target.id;
//   });
// });

// Generate random color
const randomColor = function () {
  const hex = "0123456789ABCDEF";
  let color = "#";

  for (let i = 0; i < 6; i++) {
    color += hex[Math.floor(Math.random() * 16)];
  }
  return color;
};

let intervalId = null;

const startChangingColor = function () {
  if (intervalId === null) {
    intervalId = setInterval(() => {
      document.body.style.backgroundColor = randomColor();
    }, 1000);
  }
};

const stopChangingColor = function () {
  clearInterval(intervalId);
  intervalId = null;
};

document.querySelector("#start").addEventListener("click", startChangingColor);
document.querySelector("#stop").addEventListener("click", stopChangingColor);
