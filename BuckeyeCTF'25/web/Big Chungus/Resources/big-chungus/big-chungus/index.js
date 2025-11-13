import express from "express";

const app = express();

app.get("/", (req, res) => {
  if (!req.query.username) {
    res.send(`
<!DOCTYPE html>
<html>
<head>
  <title>NO CHUNGUS</title>
  <style>
    body {
      font-family: Comic Sans MS;
      background: linear-gradient(45deg, #ff0000, #00ff00, #0000ff);
      animation: rainbow 2s infinite;
      text-align: center;
      padding: 50px;
    }
    @keyframes rainbow {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }
    h1 { font-size: 100px; color: white; text-shadow: 5px 5px black; }
    img { width: 300px; border: 10px solid yellow; animation: spin 1s infinite; }
    @keyframes spin {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }
    .marquee {
      font-size: 50px;
      color: lime;
      animation: marquee 3s linear infinite;
    }
  </style>
</head>
<body>
  <h1>NO CHUNGUS DETECTED</h1>
  <div class="marquee">⚠️ WARNING: NO CHUNGUS FOUND ⚠️</div>
  <img src="https://i.imgflip.com/aaxz3e.jpg" alt="NO CHUNGUS" onerror="this.src='data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22%3E%3Ctext x=%220%22 y=%2215%22 font-size=%2220%22%3ENO CHUNGUS%3C/text%3E%3C/svg%3E'">
  <p style="font-size: 30px; color: red;">😢 WHERE IS CHUNGUS? 😢</p>
  <form method="GET">
    <input type="text" name="username" placeholder="Enter username..." style="font-size: 20px; padding: 10px;">
    <button type="submit" style="font-size: 20px; padding: 10px;">CHECK CHUNGUS</button>
  </form>
</body>
</html>
    `);
    return;
  }

  if (req.query.username.length > 0xB16_C4A6A5) {
    res.send(`
<!DOCTYPE html>
<html>
<head>
  <title>BIG CHUNGUS!!!</title>
  <style>
    body {
      font-family: Impact, Arial Black;
      background: repeating-linear-gradient(45deg, #ff0000, #ff0000 10px, #ffff00 10px, #ffff00 20px);
      text-align: center;
      padding: 20px;
      animation: shake 0.5s infinite;
    }
    @keyframes shake {
      0%, 100% { transform: translate(0, 0); }
      25% { transform: translate(-10px, 10px); }
      75% { transform: translate(10px, -10px); }
    }
    h1 {
      font-size: 150px;
      color: #ff00ff;
      text-shadow: 10px 10px 0px #00ffff, 20px 20px 0px #ffff00;
      animation: pulse 0.3s infinite;
    }
    @keyframes pulse {
      0%, 100% { transform: scale(1); }
      50% { transform: scale(1.1); }
    }
    img {
      width: 500px;
      border: 20px dashed lime;
      animation: zoom 0.5s infinite alternate;
    }
    @keyframes zoom {
      from { transform: scale(1); }
      to { transform: scale(1.2); }
    }
    .username { font-size: 40px; color: white; background: black; padding: 10px; }
    .blink { animation: blink 0.5s infinite; }
    @keyframes blink {
      0%, 50% { opacity: 1; }
      51%, 100% { opacity: 0; }
    }
  </style>
</head>
<body>
  <h1>BIG CHUNGUS!!!</h1>
  <div class="username blink">Welcome, ${req.query.username}!</div>
  <img src="https://purepng.com/public/uploads/large/big-chungus-jkg.png" alt="BIG CHUNGUS" onerror="this.src='data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22%3E%3Ctext x=%220%22 y=%2215%22 font-size=%2220%22%3EBIG CHUNGUS%3C/text%3E%3C/svg%3E'">
  <p style="font-size: 50px; color: white; background: red; padding: 20px;">🎉 YOU FOUND THE BIGGEST CHUNGUS! 🎉</p>
  <p style="font-size: 30px; color: lime;">FLAG: ${
    process.env.FLAG || "FLAG_NOT_SET"
  }</p>
  <marquee style="font-size: 60px; color: yellow;">BIG CHUNGUS IS HERE BIG CHUNGUS IS HERE BIG CHUNGUS IS HERE</marquee>
  <form method="GET">
    <input type="text" name="username" placeholder="Enter username..." style="font-size: 20px; padding: 10px;">
    <button type="submit" style="font-size: 20px; padding: 10px;">CHECK CHUNGUS</button>
  </form>
</body>
</html>
    `);
    return;
  }

  res.send(`
<!DOCTYPE html>
<html>
<head>
  <title>little chungus - so very sad</title>
  <style>
    body {
      font-family: 'Times New Roman', serif;
      background: linear-gradient(to bottom, #1a1a2e, #16213e, #0f3460);
      text-align: center;
      padding: 30px;
      color: #e0e0e0;
      position: relative;
      overflow: hidden;
      min-height: 100vh;
    }
    .rain {
      position: absolute;
      width: 100%;
      height: 100%;
      top: 0;
      left: 0;
      pointer-events: none;
      z-index: 0;
    }
    .drop {
      position: absolute;
      width: 2px;
      height: 50px;
      background: rgba(150, 200, 255, 0.5);
      animation: fall linear infinite;
      animation-duration: var(--duration);
      animation-delay: var(--delay);
      left: var(--left);
      top: -50px;
    }
    @keyframes fall {
      to {
        top: 100vh;
        opacity: 0;
      }
    }
    .content {
      position: relative;
      z-index: 1;
    }
    h1 {
      font-size: 80px;
      color: #a0a0a0;
      text-shadow: 3px 3px 10px rgba(0,0,0,0.8);
      animation: fadeInOut 3s ease-in-out infinite;
      margin: 20px 0;
    }
    @keyframes fadeInOut {
      0%, 100% { opacity: 0.5; }
      50% { opacity: 1; }
    }
    h2 {
      font-size: 40px;
      color: #888;
      margin: 30px 0;
      font-style: italic;
    }
    .username {
      font-size: 28px;
      color: #bbb;
      margin: 30px 0;
      padding: 15px;
      background: rgba(0,0,0,0.3);
      border-left: 5px solid #555;
    }
    img {
      width: 250px;
      border: 5px solid #555;
      opacity: 0.7;
      filter: grayscale(70%);
      animation: shrink 2s ease-in-out infinite;
      margin: 20px 0;
    }
    @keyframes shrink {
      0%, 100% { transform: scale(1); }
      50% { transform: scale(0.95); }
    }
    .sad-message {
      font-size: 24px;
      color: #999;
      margin: 30px 20px;
      line-height: 1.8;
      font-style: italic;
    }
    .tears {
      font-size: 60px;
      animation: cry 1s ease-in-out infinite;
      margin: 20px 0;
    }
    @keyframes cry {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(10px); }
    }
    form {
      margin-top: 40px;
      padding: 20px;
      background: rgba(0,0,0,0.4);
      border-radius: 10px;
      display: inline-block;
    }
    input, button {
      font-size: 18px;
      padding: 10px;
      background: #2a2a3e;
      color: #ddd;
      border: 1px solid #555;
    }
  </style>
</head>
<body>
  <div class="rain" id="rain"></div>
  <div class="content">
    <div class="tears">😢 💧 😭</div>
    <h1>little chungus</h1>
    <h2>so very, very little...</h2>
    <div class="username">Welcome, ${req.query.username}...</div>
    <img src="https://images.steamusercontent.com/ugc/943958709953537755/556C9BC26D0E7261242A75A13AF865DA892DFEBC/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false" alt="little chungus" onerror="this.src='data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22%3E%3Ctext x=%220%22 y=%2215%22 font-size=%2220%22%3Elittle chungus%3C/text%3E%3C/svg%3E'">
    <div class="sad-message">
      <p>😢 It is truly a tragedy... The chungus is so very, very little...</p>
      <p>💔 Why must the chungus suffer so? Why must it be so small?</p>
      <p>🌧️ The universe weeps for this tiny chungus...</p>
      <p>😞 One day, perhaps, the chungus will grow... but today is not that day...</p>
      <p>💧 We can only hope... and dream... of a BIGGER chungus...</p>
    </div>
    <form method="GET">
      <input type="text" name="username" placeholder="Try again... maybe...">
      <button type="submit">Search for Hope</button>
    </form>
  </div>
  <script>
    const rain = document.getElementById('rain');
    for (let i = 0; i < 50; i++) {
      const drop = document.createElement('div');
      drop.className = 'drop';
      drop.style.setProperty('--left', Math.random() * 100 + '%');
      drop.style.setProperty('--duration', (Math.random() * 2 + 1) + 's');
      drop.style.setProperty('--delay', Math.random() * 2 + 's');
      rain.appendChild(drop);
    }
  </script>
</body>
</html>
  `);
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});
