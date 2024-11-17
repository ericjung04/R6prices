const { R6StatAPI} = require("r6statapi");
require('dotenv').config({path: "../.env"});
const api = new R6StatAPI();
const email = process.env.EMAIL;
const dbpassword = process.env.DB_PASSWORD;
const apipassword = process.env.API_PASSWORD;
const host = process.env.DB_HOST;
const user = process.env.DB_USER;
const cron = require("node-cron");
const mysql = require("mysql2/promise");
const ITEM_ID = "f619eb19-de6e-4dcd-96eb-08b45f80fe64";

const pool = mysql.createPool({
    host: host,
    user: user,
    password: dbpassword,
    database: "R6Marketplace",
});


async function getPriceData() {
        try{
        await api.login(email, apipassword);
        const details = await api.getItemDetails(ITEM_ID);
        const lastSalePrice = details.marktetData.lastSoldAt.price;
        const timestamp = details.marktetData.lastSoldAt.performedAt;
        const formatTime = new Date(timestamp).toISOString().slice(0, 19).replace('T', ' ');
        const lowestSalePrice = details.marktetData.sellStats.lowestPrice;
        console.log("Lowest Current Price:", lowestSalePrice);
        console.log("Last Sale Price:", lastSalePrice);
        console.log("Last Sold At:", formatTime);
        return [formatTime, lastSalePrice];
        }

        catch (error){
            console.log("Error:", error);
        }
    }


async function recordSale(itemID, soldAt, price)
{
    try{
        const [rows] = await pool.query(
            "SELECT * FROM prices WHERE item_id = ? AND sold_at = ?",
          [itemID, soldAt]  
        );

        if (rows.length > 0)
        {
            console.log("No new sales.");
            return;
        }

        await pool.query(
            "INSERT INTO prices (item_id, sold_at, price) VALUES (?, ?, ?)",
            [itemID, soldAt, price]          
        );
        console.log("New Sale at:", timestamp);
    }

    catch (error){
        console.log("Error Adding Sale:", error);
    }
}

async function getAndRecordSale()
{
    try {
        let [x, y] = await getPriceData();
        await recordSale(ITEM_ID, x, y);
    } 
    
    catch (error) {
        console.log(error);
    }
}

cron.schedule("*/30 * * * *", async () => {
    console.log("Checking Prices");
    await getAndRecordSale();
});