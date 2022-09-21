ESG:
var port = process.env.PORT || 8000;

Server.listen(port, function() {
    console.log("App is running on port "+ port);
});
ES6:
const port = process.env.PORT || 8000;

Server.listen(port, () => {
    console.log("App is running on port "+ port)
});
