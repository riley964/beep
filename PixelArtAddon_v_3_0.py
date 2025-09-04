<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Beep Counter</title>
</head>
<body>
  <h1>Beep Counter</h1>
  <p id="count">Beep count: 0</p>
  <p id="message"></p>

  <script>
    let beepCount = 0;
    const triggerInterval = 1000; // every 1000 beeps

    function beep() {
      beepCount++;
      document.getElementById("count").textContent = "Beep count: " + beepCount;

      if (beepCount % triggerInterval === 0) {
        document.getElementById("message").textContent = "Special message triggered!";
      }
    }

    // pretend we beep every 100ms
    setInterval(beep, 100);
  </script>
</body>
</html>