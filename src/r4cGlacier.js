const { R6StatAPI} = require("r6statapi");
require('dotenv').config({path: "../.env"});
const api = new R6StatAPI();
const email = process.env.EMAIL;
const password = process.env.PASSWORD;
const host = process.env.DB_HOST;
const user = process.env.DB_USER;
const cron = require("node-cron");
const mysql = require("mysql2/promise");
const ITEM_ID = "f619eb19-de6e-4dcd-96eb-08b45f80fe64";

const pool = mysql.createPool({
    host: host,
    user: user,
    password: password,
    database: "R6Marketplace",
});


async function getPriceData() {
        try{
        await api.login(email, password);
        const details = await api.getItemDetails(ITEM_ID);
        const lastSalePrice = details.marktetData.lastSoldAt.price;
        const timestamp = details.marktetData.lastSoldAt.performedAt;
        const formatTime = new Date(timestamp).toISOString().slice(0, 19).replace('T', ' ');
        const lowestSalePrice = details.marktetData.sellStats.lowestPrice;
        console.log("Lowest Current Price:", lowestSalePrice);
        console.log("Last Sale Price:", lastSalePrice);
        console.log("Last Sold At:", formatTime);
    }
    catch (error){
        console.log("Error:", error);
    }
    }
getPriceData();

