<html lang="en">
<head>
    <meta charset="UTF-8">
    <title> Activity Selection</title>

</head>
<body>
    <h1> Hello, Please provide the name of the activity you would like to do?</h1>
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
            message.innerHTML = "Okay Great Choice You Will Be Doing " + userInput.value;  
        }
    </script>

    <table align="center"> 
    <tr> 
    <th>Snorkeling</th>
    <th>Water Sking</th>
   <th>The Spa</th>
      </tr>
    <tr>
    <td> 2 hours </td>
    <td> 1 hour</td>
    <td> 2 hours</td>
    </tr>
    <tr>
      <td> with food</td>
      <td> without food</td>
      <td> with food</td>
      </tr>
      <tr>
      <td> solo</td>
      <td> group</td>
      <td> solo</td>
      </tr>
      <tr>
        <td>shuttle from hotel </td>
        <td>no shuttle </td>
        <td>no shuttle </td>
      </tr>
      

</table>

</body>
</html>

<img  src="images/swim.jpg">