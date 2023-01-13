<html lang="en">
<head>
    <meta charset="UTF-8">
    <title> Car Rental Selection</title>

</head>
<body>
    <h1> Hello, Please provide the name of the model of car you would like to rent.</h1>
    <input id="userInput"> 
    <button onclick="myFunction()"> Select </button>
    <h1 id="message"></h1>
    <style>
          body {background-color:aliceblue; text-align: center; font-family: 'Times New Roman', Times, serif ;}
    </style>
    <script>
        function myFunction() {
            let userInput = document.querySelector("#userInput");
            let message = document.querySelector("#message");
            message.innerHTML = "Great Choice You Will Be Driving A " + userInput.value;
        }
    </script>
    <table align="center"> 
    <tr> 
    <th>Toyota Corolla</th>
    <th>Chevrolet Camaro</th>
    <th>Aston Martin Vantage</th>
      </tr>
    <tr>
    <td> 5 Seats</td>
    <td> 4 Seats</td>
    <td> 2 Seats</td>
    </tr>
    <tr>
      <td> 0-60 (7.8 Seconds)</td>
      <td> 0-60 (3.5 Seconds)</td>
      <td> 0-60 (4.4 Seconds)</td>
      </tr>
      <tr>
      <td> Yes-Apple Car Play</td>
      <td> Yes-Apple Car Play</td>
      <td> No-Apple Car Play</td>
      </tr>
      <tr>
        <td>Yes-Safety Features</td>
        <td>Yes-Safety Features </td>
        <td>Yes-Safety Features </td>
      </tr>
      <tr>
        <td> Automatic</td>
        <td> Automatic and Manual</td>
        <td> Automatic</td>
      </tr>
      <tr>
        <td> 150$/day</td>
        <td> 175$/day</td>
        <td> 210$/day</td>
      </tr>

</table>

</body>
</html>

# Cars Below
-------------
<div class="row"> <!--- make a new row -->
  <!-- each column is one-third of width -->
  <div class="column"> Toyota Corolla
    <img src="/images/toyota.jpg" alt="toyota" style="width:100%">
  </div>
   <div class="column"> Chevrolet Camaro
    <img src="/images/chevy.png" alt="chevy" style="width:100%">
  </div>
   <div class="column"> Aston Martin Vantage
    <img src="/images/aston.jpg" alt="aston" style="width:100%">
  </div>
</div>

<!-- bundle exec jekyll serve -H 0.0.0.0 -P 4001 -->