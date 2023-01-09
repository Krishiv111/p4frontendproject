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
        body {background-color:rgb(40, 23, 117); text-align: center; font-family: 'Times New Roman', Times, serif ;}
    </style>
    <script>
        function myFunction() {
            let userInput = document.querySelector("#userInput");
            let message = document.querySelector("#message");
            message.innerHTML = "Okay Great Choice You Will Be Staying At The >>>" + userInput.value;  
        }
    </script>
    <table align="center"> 
    <tr> 
    <th>Garza Blanca Cancun</th>
    <th>Grand Residences Rivera Cancun</th>
   <th>Kempsi Hotel Cancun</th>
      </tr>
    <tr>
    <td> Free Internet</td>
    <td> Free Internet</td>
    <td> Free Internet</td>
    </tr>
    <tr>
      <td> Free Breakfast</td>
      <td> NO Free Breakfast</td>
      <td> NO Free Breakfast</td>
      </tr>
      <tr>
      <td> Pool Included</td>
      <td> Pool Included</td>
      <td> Pool Included</td>
      </tr>
      <tr>
        <td>Room Service and Daily Cleaning </td>
        <td>Room Service and Daily Cleaning </td>
        <td>Room Service and Daily Cleaning </td>
      </tr>
      <tr>
        <td> No Airport Shuttle</td>
        <td> Yes Airport Shuttle</td>
        <td> No Airport Shuttle</td>
      </tr>
      <tr>
        <td> 610$/night</td>
        <td> 531$/night</td>
        <td> 500$/night</td>
      </tr>

</table>

</body>
</html>

<img  src="images/trail.jpg">
