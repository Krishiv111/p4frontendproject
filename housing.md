<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title> Hotels Selection</title>

</head>
<body>
    <h1> Hello, Please provide the name of the hotel you would like to stay in?</h1>
    <input id="userInput"> 
    <button onclick="myFunction()"> Submit </button>
    <h1 id="message"></h1>
    <style>
        body {background-color:aliceblue; text-align: center; font-family: 'Times New Roman', Times, serif ;}
    </style>
    <script>
        function myFunction() {
            let userInput = document.querySelector("#userInput");
            let message = document.querySelector("#message");
            message.innerHTML = "Okay Great Choice You Will Be Staying At The >>>" + userInput.value;  
        }
    </script>

Garza Blanca Cancun | Grand Residences Rivera Cancun | Kempsi Hotel Cancun |
--| -- | -- |
9/10|9.6/10|9.0|
Internet| Internet|Internet|
Free Brekfast|No Free Brekfast|No Free Brekfast|
Free Parking|Free Parking|Free Parking|
Pool Included|Pool Included|Pool Included|
Room Service and Daily Cleaning|Room Service and Daily Cleaning|Room Service and Daily Cleaning|
No Airport Shuttle|Airport Shuttle|No Airport Shuttle|
610$/night|531$/night|500$/night|


</body>
</html>
