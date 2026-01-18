// const Base_URL = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@latest/v1/currencies" ;

// const dropdowns = document.querySelectorAll(".dropdown select ");
// const btn = document.querySelector("form button");
// const fromCurr = document.querySelector(".from select");
// const toCurr = document.querySelector(".to select");
//  const msg =  document.querySelector(".msg");
// let i = 0;
// for(let select of dropdowns){
//     for(currCode in countryList){
//         let newOption = document.createElement("option");
//         newOption.innerText = currCode ;
//         newOption.value = currCode;
//         if(select.name === "from" && currCode === "USD"){
//             newOption.selected = "selected";
//         } else if(select.name === "to" && currCode === "INR"){
//             newOption.selected = "selected";
//         }
//         select.append(newOption);

//         // console.log(code,countryList[code]);
// }
//  select.addEventListener("change",(evt) =>{
//        updateFlag(evt.target);     
//  });
//  }
// const updateFlag = (element)=> {
//       let currCode = element.value;   
//     //   console.log(currCode);

//       let countryCode = countryList[currCode];//IN ,EU
//       let newSrc = `https://flagsapi.com/${countryCode}/flat/64.png`;
//       let img = element.parentElement.querySelector('img');
//       img.src = newSrc;

// } ;

// btn.addEventListener("click",async(evt)=>{
//     evt.preventDefault();    
//     let amount = document.querySelector(".amount input");
//     let amtVal = amount.value;
//     if(amtVal === "" || amtVal < 1 ){
//         amtVal = 1;
//         amount.value ="1";
//     }
//     // console.log(fromCurr.value,toCurr.value);
//     // console.log(amtVal);
//     const URL = `${Base_URL}/${fromCurr.value.toLowerCase()}/${toCurr.value.toLowerCase()}.json`
//     let response = await fetch(URL);
//     let data = await response.json();
//     let rate = data[toCurr.value.toLowerCase()] ;
//     let finalAmount = amountVal * rate
//     msg.innerText = `${amtVal} ${fromCurr.value} = ${finalAmount} ${toCurr.value}` 
//     console.log(response);
//     console.log(data);
//     console.log(rate);

// });

// const Base_URL = "https://latest.currency-api.pages.dev/v1/currencies";

// const dropdowns = document.querySelectorAll(".dropdown select");
// const btn = document.querySelector("form button");
// const fromCurr = document.querySelector(".from select");
// const toCurr = document.querySelector(".to select");

// for (let select of dropdowns) {
//   for (let currCode in countryList) {
//     let newOption = document.createElement("option");
//     newOption.innerText = currCode;
//     newOption.value = currCode;

//     if (select.name === "from" && currCode === "USD") {
//       newOption.selected = true;
//     }
//     if (select.name === "to" && currCode === "INR") {
//       newOption.selected = true;
//     }

//     select.append(newOption);
//   }

//   select.addEventListener("change", (evt) => {
//     updateFlag(evt.target);
//   });
// }

// const updateFlag = (element) => {
//   let currCode = element.value;
//   let countryCode = countryList[currCode];
//   let img = element.parentElement.querySelector("img");
//   img.src = `https://flagsapi.com/${countryCode}/flat/64.png`;
// };

// btn.addEventListener("click", async (evt) => {
//   evt.preventDefault();

//   let amount = document.querySelector(".amount input");
//   let amtVal = amount.value || 1;

//   const URL = `${Base_URL}/${fromCurr.value.toLowerCase()}/${toCurr.value.toLowerCase()}.json`;

//   let response = await fetch(URL);
//   let data = await response.json();

//   let rate = data[toCurr.value.toLowerCase()];
//   let finalAmount = amtVal * rate;

//   document.querySelector(".msg").innerText =
//     `${amtVal} ${fromCurr.value} = ${finalAmount} ${toCurr.value}`;
// });

const Base_URL = "https://open.er-api.com/v6/latest";

const dropdowns = document.querySelectorAll(".dropdown select");
const btn = document.querySelector("form button");
const fromCurr = document.querySelector(".from select");
const toCurr = document.querySelector(".to select");

// Populate dropdowns
for (let select of dropdowns) {
  for (let currCode in countryList) {
    let option = document.createElement("option");
    option.innerText = currCode;
    option.value = currCode;

    if (select.name === "from" && currCode === "USD") {
      option.selected = true;
    }
    if (select.name === "to" && currCode === "INR") {
      option.selected = true;
    }

    select.append(option);
  }

  select.addEventListener("change", (evt) => {
    updateFlag(evt.target);
  });
}

const updateFlag = (element) => {
  let currCode = element.value;
  let countryCode = countryList[currCode];
  let img = element.parentElement.querySelector("img");
  img.src = `https://flagsapi.com/${countryCode}/flat/64.png`;
};

btn.addEventListener("click", async (evt) => {
  evt.preventDefault();

  let amount = document.querySelector(".amount input");
  let amtVal = amount.value || 1;

  try {
    let response = await fetch(`${Base_URL}/${fromCurr.value}`);
    let data = await response.json();

    let rate = data.rates[toCurr.value];
    let finalAmount = (amtVal * rate).toFixed(2);

    document.querySelector(".msg").innerText =
      `${amtVal} ${fromCurr.value} = ${finalAmount} ${toCurr.value}`;

  } catch (error) {
    document.querySelector(".msg").innerText =
      "Something went wrong!";
    console.error(error);
  }
});


