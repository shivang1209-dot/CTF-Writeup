const AUTH_TOKEN = 'trustfall-readonly';

const productTable = document.getElementById('product-table');
const detailCard = document.getElementById('detail-card');
const adminLink = document.getElementById('admin-link');
const adminStatus = document.getElementById('admin-status');

async function fetchJson(url, options = {}) {
  const response = await fetch(url, {
    credentials: 'same-origin',
    ...options,
    headers: {
      ...(options.headers || {}),
      Authorization: `Bearer ${AUTH_TOKEN}`
    }
  });

  if (!response.ok) {
    throw new Error(`Request failed with status ${response.status}`);
  }

  return response.json();
}

function renderProducts(products) {
  productTable.innerHTML = '';

  products.forEach((product) => {
    const row = document.createElement('tr');

    const skuCell = document.createElement('td');
    const skuLink = document.createElement('a');
    skuLink.href = `#${product.sku}`;
    skuLink.textContent = product.sku;
    skuLink.addEventListener('click', (event) => {
      event.preventDefault();
      loadProductDetails(product.sku);
    });
    skuCell.appendChild(skuLink);

    const nameCell = document.createElement('td');
    nameCell.textContent = product.name;

    const priceCell = document.createElement('td');
    priceCell.textContent = product.price ? `$${product.price.toFixed(2)}` : '—';

    const updatedByCell = document.createElement('td');
    updatedByCell.textContent =
      typeof product.updatedBy === 'number' ? product.updatedBy : 'unknown';

    row.appendChild(skuCell);
    row.appendChild(nameCell);
    row.appendChild(priceCell);
    row.appendChild(updatedByCell);

    productTable.appendChild(row);
  });
}

function renderProductDetails(product) {
  detailCard.innerHTML = '';

  const title = document.createElement('h3');
  title.textContent = product.name;

  const skuMeta = document.createElement('p');
  skuMeta.className = 'meta';
  skuMeta.textContent = `SKU: ${product.sku}`;

  const updatedMeta = document.createElement('p');
  updatedMeta.className = 'meta';
  const updatedByLabel =
    typeof product.updatedBy === 'number' ? product.updatedBy : 'unknown';
  updatedMeta.textContent = `Updated By: User ${updatedByLabel}`;

  const description = document.createElement('p');
  description.textContent = product.description || 'No description available.';

  detailCard.appendChild(title);
  detailCard.appendChild(skuMeta);
  detailCard.appendChild(updatedMeta);
  detailCard.appendChild(description);
}

function renderError(message) {
  detailCard.innerHTML = '';
  const error = document.createElement('p');
  error.className = 'placeholder';
  error.textContent = message;
  detailCard.appendChild(error);
}

async function loadProductDetails(sku) {
  try {
    const product = await fetchJson(`/api/products/${encodeURIComponent(sku)}`);
    renderProductDetails(product);
  } catch (error) {
    renderError('Unable to load product details.');
    // eslint-disable-next-line no-console
    console.error(error);
  }
}

async function bootstrap() {
  try {
    const products = await fetchJson('/api/products');
    renderProducts(products);
  } catch (error) {
    productTable.innerHTML = '';
    const row = document.createElement('tr');
    const cell = document.createElement('td');
    cell.colSpan = 4;
    cell.className = 'placeholder';
    cell.textContent = 'Catalog unavailable.';
    row.appendChild(cell);
    productTable.appendChild(row);
    // eslint-disable-next-line no-console
    console.error(error);
  }
}

function wireAdminLink() {
  if (!adminLink || !adminStatus) {
    return;
  }

  adminLink.addEventListener('click', async (event) => {
    event.preventDefault();
    adminStatus.className = 'admin-status';
    adminStatus.textContent = 'Checking admin privileges...';

    try {
      const response = await fetch('/admin', {
        credentials: 'same-origin',
        headers: { Authorization: `Bearer ${AUTH_TOKEN}` }
      });

      if (response.status === 403) {
        adminStatus.textContent =
          'Unauthorized: admin console restricted to leadership.';
      } else if (response.ok) {
        adminStatus.className = 'admin-status success';
        adminStatus.textContent = 'Admin console accessible.';
      } else {
        adminStatus.textContent = `Unexpected response: ${response.status}`;
      }
    } catch (error) {
      adminStatus.textContent = 'Unable to reach admin console.';
      // eslint-disable-next-line no-console
      console.error(error);
    }
  });
}

document.addEventListener('DOMContentLoaded', () => {
  bootstrap();
  wireAdminLink();
});