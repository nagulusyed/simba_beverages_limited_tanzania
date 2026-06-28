const CACHE_NAME = 'simba-v1';
const SHELL = ['/', '/index.html', '/images/sbl-logo.png', '/images/hero-bottle.png'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE_NAME).then(c => c.addAll(SHELL)));
});

self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  const url = new URL(e.request.url);
  // Don't cache analytics, whatsapp links, formspree, etc.
  if (url.origin !== location.origin) return;

  e.respondWith(
    caches.match(e.request).then(cached => {
      const networked = fetch(e.request).then(res => {
        const cacheCopy = res.clone();
        caches.open(CACHE_NAME).then(c => c.put(e.request, cacheCopy));
        return res;
      }).catch(() => cached);
      return cached || networked;
    })
  );
});
