document.getElementById("condition-check-btn").addEventListener("click", function() {
    var a = parseInt(document.getElementById("inputA").value);
    var b = parseInt(document.getElementById("inputB").value);
    var c = parseInt(document.getElementById("inputC").value);
    var d = parseInt(document.getElementById("inputD").value);
    
    var resultText = "";

    if (a < b) {
        if (c > d) {
            resultText = "Condition a < b and c > d is true";
        } else if (c == d) {
            resultText = "Condition a < b and c == d is true";
        } else {
            resultText = "Condition a < b and c < d is true";
        }
    } else if (a == b) {
        if (c > d) {
            resultText = "Condition a == b and c > d is true";
        } else if (c == d) {
            resultText = "Condition a == b and c == d is true";
        } else {
            resultText = "Condition a == b and c < d is true";
        }
    } else {
        resultText = "Condition a > b";
    }

    // Update the result div with the result
    document.getElementById("result").innerText = resultText;
});
