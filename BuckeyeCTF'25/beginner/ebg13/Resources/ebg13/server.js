import Fastify from 'fastify';
import * as cheerio from 'cheerio';

const FLAG = process.env.FLAG ?? "bctf{fake_flag}";

const INDEX_HTML = `
<!doctype html>
<html lang="en">

<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>ebj13</title>
  <link rel="stylesheet" href="https://unpkg.com/98.css" />
  <style>
    body {
      background: #008080;
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
      margin: 0;
    }

    .window {
      zoom: 1.5;
      width: 460px;
    }

    .window-body {
      text-align: center;
    }

    form {
      display: flex;
      justify-content: center;
      gap: 8px;
      flex-wrap: wrap;
      margin-top: 10px;
    }

    input[type="text"] {
      width: 300px;
    }

    .example-buttons {
      display: flex;
      justify-content: center;
      gap: 8px;
      margin-top: 12px;
    }
  </style>
</head>

<body>
  <div class="window" role="application">
    <div class="title-bar">
      <div class="title-bar-text">ebj13</div>
      <div class="title-bar-controls">
        <button aria-label="Minimize"></button>
        <button aria-label="Maximize"></button>
        <button aria-label="Close"></button>
      </div>
    </div>
    <div class="window-body">
      <p><strong>Enter URL</strong></p>

      <form action="/ebj13" method="get">
        <input type="text" name="url" placeholder="Enter a URL" id="urlInput" />
        <button type="submit" class="button">ebj13 it!</button>
      </form>

      <div class="example-buttons">
        <button class="button" type="button" onclick="urlInput.value = 'https://example.com'">example.com</button>
        <button class="button" type="button"
          onclick="urlInput.value = 'https://news.ycombinator.com'">news.ycombinator.com</button>
      </div>

      <p style="margin-top:10px;font-size:12px;">Paste a full URL (including https://)</p>
    </div>
  </div>
</body>

</html> 
`;

const fastify = Fastify({ logger: true });

function rot13(str) {
  return str.replace(/[a-zA-Z]/g, (c) =>
    String.fromCharCode(
      c.charCodeAt(0) + (c.toLowerCase() < 'n' ? 13 : -13)
    )
  );
}

function rot13TextNodes($, node) {
  $(node)
    .contents()
    .each((_, el) => {
      if (el.type === 'text') {
        el.data = rot13(el.data);
      } else {
        rot13TextNodes($, el);
      }
    });
}

fastify.get('/', async (req, reply) => {
  return reply.type('text/html').send(INDEX_HTML);
});

fastify.get('/ebj13', async (req, reply) => {
  const { url } = req.query;

  if (!url) {
    return reply.status(400).send('Missing ?url parameter');
  }

  try {
    const res = await fetch(url);
    const html = await res.text();

    const $ = cheerio.load(html);
    rot13TextNodes($, $.root());

    const modifiedHtml = $.html();

    reply.type('text/html').send(modifiedHtml);
  } catch (err) {
    reply.status(500).send(`Error fetching URL`);
  }
});

fastify.get('/admin', async (req, reply) => {
    if (req.ip === "127.0.0.1" || req.ip === "::1" || req.ip === "::ffff:127.0.0.1") {
      return reply.type('text/html').send(`Hello self! The flag is ${FLAG}.`)
    }

    return reply.type('text/html').send(`Hello ${req.ip}, I won't give you the flag!`)
})

fastify.listen({ port: 3000, host: '0.0.0.0' }, (err, address) => {
  if (err) throw err;
  console.log(`Server running at ${address}`);
});
