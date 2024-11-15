const { R6StatAPI} = require("r6statapi");
require('dotenv').config({path: "../.env"});
const api = new R6StatAPI();
const email = process.env.EMAIL;
const password = process.env.PASSWORD;
const username = process.env.USERNAME;
const platform = process.env.PLATFORM;

async function getPriceData(itemID) {
    try{
        const token = await api.login(email, password);
        const details = await api.getItemDetails("f619eb19-de6e-4dcd-96eb-08b45f80fe64");
        console.log("Lowest Current Price:", details.marktetData.sellStats.lowestPrice);
    }
    catch (error){
        console.log("Error:", error);
    }
}

const ID = "0d2ae42d-4c27-4cb7-af6c-2099062302bb";
getPriceData(ID);