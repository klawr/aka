const hash = window.location.hash;
if (hash) {
    document.getElementById('links').style.display = 'none';
    const text = document.createElement('h1');
    const a = document.getElementById(hash);
    text.innerHTML = `You are being redirected to: ${a.href}`;
    document.body.appendChild(text);
    setTimeout(() => { a.click(); }, 3000);
}
