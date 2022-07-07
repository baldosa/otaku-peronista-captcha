console.log('loaded captcha :-)')

function getRandomImage() {
  return fetch('https://captcha.meme.ar/captcha')
    .then(response => response.json())
    .then(data => data)
    .catch(error => console.log(error));
}

async function loadCaptcha() {
  // get random image
  const imgData = await getRandomImage()
  imgSrc = await `data:image/jpeg;base64,${imgData.image}`
  
  const captchaModal = document.querySelector('#op-captcha-modal')
  captchaModal.style.visibility = 'visible'
  captchaModal.innerHTML = ''
  captchaModal.setAttribute('class', 'op-captcha-card')

  const modalCard = `
    <div id="op-captcha-modal-content">
      <img id="op-captcha-img" src="${imgSrc}">
      <footer>
            <button id="op-captcha-otaku" class="op-captcha-bg-otaku">Otaku</button>
            <button id="op-captcha-peronista" class="op-captcha-bg-peronista">Peronista</button>
        <input id="op-captcha-uuid" value="${imgData.uuid}" type="hidden">
      </footer>
    <div>
  `
  captchaModal.innerHTML += modalCard
  const otakuBtn = document.querySelector('#op-captcha-otaku')
  const peronistaBtn = document.querySelector('#op-captcha-peronista')
  

  otakuBtn.addEventListener('click', function () {
    validateCaptcha(imgData.id, 'o', imgData.uuid)
  });
  

  peronistaBtn.addEventListener('click', function () {
    validateCaptcha(imgData.id, 'p', imgData.uuid)
  });

}


async function validateCaptcha(imgId, option, uuid) {
  await fetch('https://captcha.meme.ar/captcha/check', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ imgId: imgId, option: option, uuid: uuid })
  })
    .then((res) => res.json())
    .then((res) => {
      if (res.status) {
        const newCard = `
          <div id="op-card" class="op-captcha-card">
            <img id="op-captcha-checkbox" src="data:image/svg+xml;base64,PHN2ZyB2ZXJzaW9uPSIxLjEiIGNsYXNzPSJoYXMtc29saWQgIiB2aWV3Qm94PSIwIDAgMzYgMzYiIHByZXNlcnZlQXNwZWN0UmF0aW89InhNaWRZTWlkIG1lZXQiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIGZvY3VzYWJsZT0iZmFsc2UiIHJvbGU9ImltZyIgd2lkdGg9IjM1IiBoZWlnaHQ9IjM1IiBmaWxsPSIjMTNlNzc5Ij48cGF0aCBjbGFzcz0iY2xyLWktb3V0bGluZSBjbHItaS1vdXRsaW5lLXBhdGgtMSIgZD0iTTE4LDZBMTIsMTIsMCwxLDAsMzAsMTgsMTIsMTIsMCwwLDAsMTgsNlptMCwyMkExMCwxMCwwLDEsMSwyOCwxOCwxMCwxMCwwLDAsMSwxOCwyOFoiLz48cGF0aCBjbGFzcz0iY2xyLWktb3V0bGluZSBjbHItaS1vdXRsaW5lLXBhdGgtMiIgZD0iTTE2LjM0LDIzLjc0bC01LTVhMSwxLDAsMCwxLDEuNDEtMS40MWwzLjU5LDMuNTksNi43OC02Ljc4YTEsMSwwLDAsMSwxLjQxLDEuNDFaIi8+PHBhdGggY2xhc3M9ImNsci1pLXNvbGlkIGNsci1pLXNvbGlkLXBhdGgtMSIgZD0iTTMwLDE4QTEyLDEyLDAsMSwxLDE4LDYsMTIsMTIsMCwwLDEsMzAsMThabS00Ljc3LTIuMTZhMS40LDEuNCwwLDAsMC0yLTJsLTYuNzcsNi43N0wxMywxNy4xNmExLjQsMS40LDAsMCwwLTIsMmw1LjQ1LDUuNDVaIiBzdHlsZT0iZGlzcGxheTpub25lIi8+PC9zdmc+">
            <label for="op-captcha-checkbox">Ganaste</label>
            <div id="op-captcha-modal"></div>
          </div>
        `
        const opCard = document.querySelector('#op-captcha')
        opCard.innerHTML = newCard
        localStorage.setItem('op-captcha-validator', JSON.stringify(res));

      } else {
        loadCaptcha()
      }
    })
    .catch((err) => {
      console.log(err)
    })
}

function generateCaptcha() {
  const captchaDiv = document.querySelector('#op-captcha')

  const card = `
    <div id="op-card" class="op-captcha-card">
      <input type="checkbox" id="op-captcha-checkbox">
      <label for="op-captcha-checkbox">Resolver captcha</label>
      <div id="op-captcha-modal"></div>
    </div>
  `
  captchaDiv.innerHTML = card

  const checkBox = document.querySelector('#op-captcha-checkbox')

  checkBox.addEventListener('click', () => {
    checkBox.disabled = true
    loadCaptcha()
  });

}

generateCaptcha()