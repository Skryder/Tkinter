
//const baseApiUrl = "127.0.0.1:8000/";

async function docsista_api_get(apiUrl) {
    return await fetch(apiUrl, {
        method: "GET"
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log('Data gotten:', data);
    })
    .catch(error => {
        console.error('Error getting data:', error);
        
    });
}

async function docsista_api_getHTML(apiUrl) {
    return await fetch(apiUrl, {
        method: "GET"
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        //console.log("response: " + response.text())
        return response.text();
    })
    .then(data => {
        return data;
    })
    .catch(error => {
        console.error('Error getting data:', error);
    });
}

async function docsista_api_post(apiUrl, input) {
    return await fetch(apiUrl, {
        method: "POST",
        body: JSON.stringify({"Message": input}),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    })
    .then(response => {
        if (!response.ok) {
            console.log("failed: Input is: " +  input)
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        console.log("Print post");
        return response.json();
    })
    .then(data => {
        console.log("Print postlog");
        console.log('Data posted:', data);
    })
    .catch(error => {
        console.error('Error posting data:', error);
        
    });
}

const contentContainer = document.getElementById('content-container');

async function parseFromClipboard() {
    console.log("Print 2");
    apiUrl = "post-cmts-output/";
    const clipboardText = await navigator.clipboard.readText();
    await docsista_api_post(apiUrl, clipboardText);
    console.log("Print 3");
}

async function getModel() {
    apiUrl = "get-model";
    console.log(await docsista_api_get(apiUrl));
}

async function getReadableStats() {
    console.log("Print 5");
    apiUrl = "get-readable";
    output = await docsista_api_getHTML(apiUrl);
    console.log("Print 6");
    console.log("Output: " + output);
    return output;

}

function embedHTML(input) {
    console.log("Print 7");
    contentContainer.innerHTML = input;
}

async function cmtsBtnClicked() {
    console.log("Print 1");
    const thing = await parseFromClipboard(); //read in the data
    console.log("Print 4");
    const html = await getReadableStats(); // get back the raw HTML
    console.log("html: " + html);
    embedHTML(html);
}

