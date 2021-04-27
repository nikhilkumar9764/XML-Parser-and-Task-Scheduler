const puppeteer = require('puppeteer');

//const URL = 'https://ebam-dashboard.eu.airbus.corp/2A24/Cockpit/?mode=viewer&colorSchema=light&';


async function testDashboard(DashboardId, Timeout, URL) {
    let metrics;

    try {
        var IsErrorCodeRecived = false;
        let launchOptions = { headless: false, args: ['--start-maximized'] };

        var browser = await puppeteer.launch(launchOptions);
        var page = await browser.newPage();
        await page.setViewport({ width: 1366, height: 768 });
        console.log(DashboardId, URL);
        page.on('response', async response => {
            text3 = await response.status();
            console.log('HTTP Code : ', text3);
            if (text3 >= 500) {
                IsErrorCodeRecived = true;
            }
        });
        await page.goto(URL, { waitUntil: "networkidle0", timeout: Timeout });
        metrics = await page.metrics();
        var pagescrnsht = await page.screenshot({encoding : "base64"});

        await browser.close();
    }
    catch (error) {
        const pgscrnsht = await page.screenshot({encoding : "base64"});
        await browser.close();
        console.log("Here In The Error");
        console.log(error);
        return { "Error": "TimeOut Dashboard" + error.toString() , "image" : pgscrnsht };
    }
    if (IsErrorCodeRecived) return { "Error": "Internal Server Error", "image" : pagescrnsht };
    return { "metrics" : metrics , "image" : pagescrnsht};
}




module.exports = {
    testDashboard
};