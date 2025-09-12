<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Current Date Info</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      padding-top: 100px;
      background-color: #f0f0f0;
    }
    .date-box {
      background-color: #fff;
      padding: 30px;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
      display: inline-block;
    }
    h1 {
      margin-bottom: 20px;
    }
  </style>
</head>
<body>

  <div class="date-box">
    <h1> Today's Date Info</h1>
    <p id="date"></p>
    <p id="month"></p>
    <p id="year"></p>
    <p id="day"></p>
  </div>

  <script>
    const now = new Date();

    const days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    const months = [
      "January", "February", "March", "April", "May", "June",
      "July", "August", "September", "October", "November", "December"
    ];

    document.getElementById("date").textContent = `Date: ${now.getDate()}`;
    document.getElementById("month").textContent = `Month: ${months[now.getMonth()]}`;
    document.getElementById("year").textContent = `Year: ${now.getFullYear()}`;
    document.getElementById("day").textContent = `Day: ${days[now.getDay()]}`;
  </script>

</body>
</html>
