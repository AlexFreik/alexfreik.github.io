var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
const Http = new XMLHttpRequest();
const url='https://www.googleapis.com/drive/v2/files?q="1p6avfXtLQBAImA9teTjIBW1GYTSsOpsL"+in+parents&key={apiKey}';
Http.open("GET", url);
Http.send();

Http.onreadystatechange = (e) => {
  console.log(Http.responseText)
}
