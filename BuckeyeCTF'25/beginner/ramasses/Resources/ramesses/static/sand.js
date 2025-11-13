(function () {
  const canvas = document.getElementById("sand-canvas");
  if (!canvas) return;
  const ctx = canvas.getContext("2d");

  let width = 0;
  let height = 0;
  let DPR = Math.max(1, window.devicePixelRatio || 1);

  function resize() {
    DPR = Math.max(1, window.devicePixelRatio || 1);
    width = canvas.clientWidth || window.innerWidth;
    height = canvas.clientHeight || window.innerHeight;
    canvas.width = Math.floor(width * DPR);
    canvas.height = Math.floor(height * DPR);
    canvas.style.width = width + "px";
    canvas.style.height = height + "px";
    ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
  }

  window.addEventListener("resize", resize);
  window.addEventListener("orientationchange", resize);
  resize();

  function rand(min, max) {
    return Math.random() * (max - min) + min;
  }

  const colors = ["#d6b887", "#d3ae79", "#cfa66b", "#e5c07b", "#b89562"];

  const BASE = Math.min(
    400,
    Math.max(120, Math.floor((width * height) / 30000))
  );
  const PARTICLE_COUNT = Math.round(BASE);

  const particles = new Array(PARTICLE_COUNT).fill(0).map(() => {
    const size = rand(0.6, 3.8);
    return {
      x: rand(0, width),
      y: rand(0, height),
      size: size,
      speed: rand(20, 140) * (size / 2),
      drift: rand(-0.4, 0.4),
      wobble: rand(0.8, 3.0),
      hue: colors[Math.floor(rand(0, colors.length))],
      opacity: rand(0.5, 0.95),
      angle: rand(0, Math.PI * 2),
    };
  });

  let last = performance.now();

  function step(now) {
    const dt = Math.min(64, now - last) / 1000;
    last = now;

    ctx.clearRect(0, 0, width, height);

    for (let i = 0; i < particles.length; i++) {
      const p = particles[i];

      p.y += p.speed * dt * 0.12;

      p.angle += p.wobble * dt * 0.7;
      p.x += Math.sin(p.angle) * (p.drift + 0.2 * dt);

      if (p.y > height + 10) {
        p.y = -10 - rand(0, 100);
        p.x = rand(0, width);
      }
      if (p.x < -20) p.x = width + 20;
      if (p.x > width + 20) p.x = -20;

      ctx.beginPath();
      ctx.fillStyle = p.hue;
      ctx.globalAlpha = p.opacity * (0.8 + 0.2 * Math.sin(p.angle * 0.5));

      const w = p.size;
      const h = p.size * (0.6 + Math.abs(Math.sin(p.angle)) * 0.8);
      ctx.ellipse(p.x, p.y, w, h, p.angle, 0, Math.PI * 2);
      ctx.fill();
    }

    ctx.globalAlpha = 1;
    requestAnimationFrame(step);
  }

  last = performance.now();
  requestAnimationFrame(step);

  window._sand = {
    reduce: function (factor) {
      const keep = Math.max(16, Math.floor(particles.length * factor));
      particles.length = keep;
    },
  };
})();
