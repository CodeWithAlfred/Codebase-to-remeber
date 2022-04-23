const setBg = () => {
  const randomColor = Math.floor(Math.random()*16777215).toString(16);
  document.body.style.backgroundColor = "#" + randomColor;
  document.getElementById('container').style.color = `#${randomColor}`;
  document.getElementById('container').innerHTML = `Color value is #${randomColor}`;
}
setInterval(setBg, 2000)
setBg();