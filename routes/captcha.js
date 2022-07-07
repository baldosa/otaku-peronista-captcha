const { v4: uuidv4 } = require('uuid');
const crypto = require('crypto');

var express = require('express'); 
const fs = require('fs');

var router = express.Router();

const imagesFile = fs.readFileSync('./images/images.json');
const images = JSON.parse(imagesFile);


function base64_encode(file) {
  // read binary data
  var bitmap = fs.readFileSync(file);
  // convert binary data to base64 encoded string
  return new Buffer.from(bitmap).toString('base64');
}
async function genHash(password) {
  return new Promise((resolve, reject) => {
    const salt = crypto.randomBytes(8).toString("hex")

    crypto.scrypt(password, salt, 64, (err, derivedKey) => {
      if (err) reject(err);
      resolve(salt + ":" + derivedKey.toString('hex'))
    });
  })
}

async function verifyHash(password, hash) {
  return new Promise((resolve, reject) => {
    const [salt, key] = hash.split(":")
    crypto.scrypt(password, salt, 64, (err, derivedKey) => {
      if (err) reject(err);
      resolve(key == derivedKey.toString('hex'))
    });
  })
}

/* GET captcha. */
router.get('/', function(req, res, next) {
  const randomImg = images[Math.floor(Math.random() * images.length)]
  res.send({
    'image': base64_encode(randomImg.image),
    'id': randomImg.id,
    'uuid': uuidv4()
  })

});

/* POST check captcha. */
router.post('/check', async function (req, res, next) {

  const data = `${req.body.imgId}${req.body.formId}${req.body.option}`;

  const img = images.filter((el) => {
    return el.id === req.body.imgId
  })
  if (img[0].result === req.body.option) {
    res.send({
      status: true,
      validator: await genHash(data),
      imgId: req.body.imgId,
      option: req.body.option,
    });
  } else {
    res.send({
      status: false
    });
  }
});

/* POST validate captcha. */
router.post('/validate', async function (req, res, next) {
  const data = `${req.body.imgId}${req.body.formId}${req.body.option}`;

  const val = await verifyHash(data, req.body.validator)
  if (val) {
    res.send({
      valid: true
    });
  } else {
    res.send({
      valid: false
    });
  }
});

module.exports = router;
