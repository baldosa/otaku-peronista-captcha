  Otaku o peronista, un captcha   

![](public/logo.png)

### Otaku o Peronista Captcha.

Robando la idea de [un tuit](https://twitter.com/nachoinventado/status/1463289179022966790?s=21) y las imagenes de [¿Otaku o Peronista?](https://otakuoperonista.com/) un captcha que te hace distinguir si la ✌️ la está haciendo un otaku o un peronista para validar que sos un humano. Probablemente no lo seas o probablemente este captcha tenga cero sentido.

#### ¿Cómo se usa?

*   Agregás el css en el head de tu página
    
        <link rel="stylesheet" href="https://captcha.meme.ar/css/captcha.css">
    
*   Un div con el id "op-captcha"
    
        <div id="op-captcha"></div>
    
*   Y este js al final
    
        <script src="https://captcha.meme.ar/javascripts/captcha.js"></script>
    

Una vez que el humano demostró ser humano, se guarda en el localstorage con un JSON con nombre op-captcha-validator que podés validar mandando en el body de un POST a https://captcha.meme.ar/captcha/validate

Mirate un [demo](https://captcha.meme.ar/demo.html)

[🐛 Reportar error o quejarse fuerte](https://github.com/baldosa/otaku-peronista-captcha)

##### Hecho con amor a los memes usando la [Chota](https://jenil.github.io/chota/)