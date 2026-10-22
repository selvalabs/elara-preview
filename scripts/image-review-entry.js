// Entrada da prévia de comparação: abrir nos cards sem interromper a navegação.
const section = document.getElementById('prova');
if (section && (!location.hash || location.hash === '#prova')) {
  history.replaceState(history.state, '', `${location.pathname}${location.search}#prova`);
  let active = true;
  const timers = [];
  function align() {
    if (!active) return;
    const header = document.getElementById('topbar');
    const top = section.getBoundingClientRect().top + scrollY - (header?.offsetHeight || 0);
    window.scrollTo({ top: Math.max(0, top), behavior: 'instant' });
  }
  function stop() {
    active = false;
    timers.forEach(clearTimeout);
    window.removeEventListener('elara:layout', align);
    for (const event of ['wheel', 'touchstart', 'pointerdown', 'keydown']) window.removeEventListener(event, stop);
  }
  for (const event of ['wheel', 'touchstart', 'pointerdown', 'keydown']) window.addEventListener(event, stop, { passive: true });
  window.addEventListener('elara:layout', align);
  const loaded = document.readyState === 'complete' ? Promise.resolve() : new Promise(resolve => window.addEventListener('load', resolve, { once: true }));
  Promise.all([loaded, document.fonts.ready]).then(() => {
    if (!active) return;
    requestAnimationFrame(() => requestAnimationFrame(align));
    timers.push(setTimeout(align, 300), setTimeout(align, 700), setTimeout(stop, 1500));
  });
}
