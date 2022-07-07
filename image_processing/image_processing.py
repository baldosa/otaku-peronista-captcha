import sys
import base64
import json
import cv2
import requests
import numpy as np

from urllib.request import urlopen
def url_to_image(url, readFlag=cv2.IMREAD_COLOR):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, readFlag)

    # return the image
    return image

def remove_white_background(img, dest):
        
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    th, threshed = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

    ## (2) Morph-op to remove noise
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11,11))
    morphed = cv2.morphologyEx(threshed, cv2.MORPH_CLOSE, kernel)

    ## (3) Find the max-area contour
    cnts = cv2.findContours(morphed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    cnt = sorted(cnts, key=cv2.contourArea)[-1]

    ## (4) Crop and save it
    x,y,w,h = cv2.boundingRect(cnt)
    dst = img[y:y+h, x:x+w]
    cv2.imwrite(dest, dst)
    # retval, buffer_img= cv2.imencode('.jpg', dst)
    # return base64.b64encode(buffer_img)

otaku_links = {
  "000": ["https://i.imgur.com/ESKluJL.png", "https://i.imgur.com/N6p6Cvy.png"],
  "001": ["https://i.imgur.com/x08Q6HC.png", "https://i.imgur.com/XLRChNI.png"],
  "002": ["https://i.imgur.com/8uU3lGk.png", "https://i.imgur.com/96L4Ycj.png"],
  "003": ["https://i.imgur.com/gaNKySj.png", "https://i.imgur.com/UJU9VIT.png"],
  "004": ["https://i.imgur.com/rlgbqAL.png", "https://i.imgur.com/KTwQs5S.png"],
  "005": ["https://i.imgur.com/RjIz3Ai.png", "https://i.imgur.com/xIRdgd8.png"],
  "006": ["https://i.imgur.com/TKquqEN.png", "https://i.imgur.com/0e7oFPm.png"],
  "007": ["https://i.imgur.com/MHcsGtq.png", "https://i.imgur.com/W1kwYTM.png"],
  "008": ["https://i.imgur.com/AkkQGPY.png", "https://i.imgur.com/xWifE5w.png"],
  "009": ["https://i.imgur.com/Hv3PQky.png", "https://i.imgur.com/GaOeZTq.png"],
  "010": ["https://i.imgur.com/XHb4bZD.png", "https://i.imgur.com/1hIjjqo.png"],
  "011": ["https://i.imgur.com/9MaORLW.png", "https://i.imgur.com/FIfU5QI.png"],
  "012": ["https://i.imgur.com/4uS9TF7.png", "https://i.imgur.com/M4FOUO2.png"],
  "013": ["https://i.imgur.com/Te9DnQK.png", "https://i.imgur.com/uc5ewc3.png"],
  "014": ["https://i.imgur.com/2fXXW8c.png", "https://i.imgur.com/9Bp9eJN.png"],
  "015": ["https://i.imgur.com/oBrd0II.png", "https://i.imgur.com/cc9lp1O.png"],
  "016": ["https://i.imgur.com/Grl5CI8.png", "https://i.imgur.com/zd2T3kX.png"],
  "017": ["https://i.imgur.com/x9bbmc3.png", "https://i.imgur.com/tJPGfLZ.png"],
  "018": ["https://i.imgur.com/B9xIOlo.png", "https://i.imgur.com/A73gTW0.png"],
  "019": ["https://i.imgur.com/rPhElEz.png", "https://i.imgur.com/CULDWUq.png"],
  "020": ["https://i.imgur.com/7tegHvj.png", "https://i.imgur.com/RHEHuIz.png"],
  "021": ["https://i.imgur.com/QEiP3OX.png", "https://i.imgur.com/gBFXwlq.png"],
  "022": ["https://i.imgur.com/9IgLPS6.png", "https://i.imgur.com/qPAyCqJ.png"],
  "023": ["https://i.imgur.com/kbtqxMl.png", "https://i.imgur.com/nY0YLwP.png"],
  "024": ["https://i.imgur.com/GdiGm9a.png", "https://i.imgur.com/W9zH0Hi.png"],
  "025": ["https://i.imgur.com/QFcOMBM.png", "https://i.imgur.com/nolUYpQ.png"],
  "026": ["https://i.imgur.com/mrUFQNV.png", "https://i.imgur.com/DWvoxoH.png"],
  "027": ["https://i.imgur.com/sk4AwWg.png", "https://i.imgur.com/3qrk8mF.png"],
  "028": ["https://i.imgur.com/nqepjli.png", "https://i.imgur.com/forVeRB.png"],
  "029": ["https://i.imgur.com/DSJFb0O.png", "https://i.imgur.com/mOEtuHK.png"],
  "030": ["https://i.imgur.com/I0M4PW2.png", "https://i.imgur.com/MrJd92P.png"],
  "031": ["https://i.imgur.com/cllIwg6.png", "https://i.imgur.com/HNuC6pP.png"],
  "032": ["https://i.imgur.com/1GmGHwR.png", "https://i.imgur.com/shQzOUc.png"],
  "033": ["https://i.imgur.com/zJhGAGT.png", "https://i.imgur.com/RQ8Cd0G.png"],
  "034": ["https://i.imgur.com/IDZJUv6.png", "https://i.imgur.com/WCcj4TY.png"],
  "035": ["https://i.imgur.com/tE4fV1H.png", "https://i.imgur.com/Cbrx07f.png"],
  "036": ["https://i.imgur.com/q75Ghps.png", "https://i.imgur.com/sxZ9kRP.png"],
  "037": ["https://i.imgur.com/XSmtvOb.png", "https://i.imgur.com/qtTgBsr.png"],
  "038": ["https://i.imgur.com/WNmZnYo.png", "https://i.imgur.com/jR50iTW.png"],
  "039": ["https://i.imgur.com/bfiUwPh.png", "https://i.imgur.com/eTQtp6W.png"],
  "040": ["https://i.imgur.com/SNS4vMr.png", "https://i.imgur.com/bcad9pH.png"],
  "041": ["https://i.imgur.com/y4NGs1D.png", "https://i.imgur.com/P3wxD2Y.png"],
  "042": ["https://i.imgur.com/WxVLPH8.png", "https://i.imgur.com/gdQJ9Q4.png"],
  "043": ["https://i.imgur.com/Oyy7T6H.png", "https://i.imgur.com/lmwYWc4.png"],
  "044": ["https://i.imgur.com/d8HGvho.png", "https://i.imgur.com/lvuWWTK.png"],
  "045": ["https://i.imgur.com/FYEz1Ni.png", "https://i.imgur.com/KFPa811.png"],
  "046": ["https://i.imgur.com/AnjpHVH.png", "https://i.imgur.com/3u0JFp8.png"],
  "047": ["https://i.imgur.com/y1pe8RY.png", "https://i.imgur.com/OpQGBDw.png"],
  "048": ["https://i.imgur.com/YLwocCN.png", "https://i.imgur.com/WpyJwjn.png"],
  "049": ["https://i.imgur.com/EkdgnxS.png", "https://i.imgur.com/G8ovpJp.png"],
  "050": ["https://i.imgur.com/Fh9m1e5.png", "https://i.imgur.com/ioUTJCI.png"],
  "051": ["https://i.imgur.com/S7K6Oi1.png", "https://i.imgur.com/4I0CsuZ.png"],
  "052": ["https://i.imgur.com/MI8q9b5.png", "https://i.imgur.com/1A78F8M.png"],
  "053": ["https://i.imgur.com/ViEztJJ.png", "https://i.imgur.com/Sem1eCg.png"],
  "054": ["https://i.imgur.com/DfwWK1R.png", "https://i.imgur.com/IQzjVRH.png"],
  "055": ["https://i.imgur.com/LySYxGz.png", "https://i.imgur.com/prxQ0gS.png"],
  "056": ["https://i.imgur.com/31xrPRM.png", "https://i.imgur.com/ZHKbc2G.png"],
  "057": ["https://i.imgur.com/hHN2dLC.png", "https://i.imgur.com/Rf2FQqU.png"],
  "058": ["https://i.imgur.com/Lj2hUqz.png", "https://i.imgur.com/27fQKg7.png"],
  "059": ["https://i.imgur.com/HwQGu7v.png", "https://i.imgur.com/NRImGOJ.png"],
  "060": ["https://i.imgur.com/Du4yKDe.png", "https://i.imgur.com/Pr4LEC7.png"],
  "061": ["https://i.imgur.com/xZDwAwl.png", "https://i.imgur.com/IdhBv8o.png"],
  "062": ["https://i.imgur.com/w6p49Xs.png", "https://i.imgur.com/GF3C81M.png"],
  "063": ["https://i.imgur.com/VLLOuGm.png", "https://i.imgur.com/0nvc6EB.png"],
  "064": ["https://i.imgur.com/wXAoH4D.png", "https://i.imgur.com/LlySQJ7.png"],
  "065": ["https://i.imgur.com/MCTFiFo.png", "https://i.imgur.com/UGoygKv.png"],
  "066": ["https://i.imgur.com/EDjkkwp.png", "https://i.imgur.com/6vj4KR2.png"],
  "067": ["https://i.imgur.com/R9t6ugF.png", "https://i.imgur.com/s5aub6J.png"],
  "068": ["https://i.imgur.com/EU08oiN.png", "https://i.imgur.com/j9whREB.png"],
  "069": ["https://i.imgur.com/yQ1YRL5.png", "https://i.imgur.com/ntRWyCm.png"],
  "070": ["https://i.imgur.com/f6LlAM2.png", "https://i.imgur.com/qNLcTLx.png"],
  "071": ["https://i.imgur.com/GPFDrwB.png", "https://i.imgur.com/yHVqUii.png"],
  "072": ["https://i.imgur.com/f836T7Z.png", "https://i.imgur.com/2Ro3Xy7.png"],
  "073": ["https://i.imgur.com/d3uX35Q.png", "https://i.imgur.com/0OFRLvT.png"],
  "074": ["https://i.imgur.com/CTVdLTv.png", "https://i.imgur.com/mnC3O9B.png"],
  "075": ["https://i.imgur.com/merEn8u.png", "https://i.imgur.com/8oAUQBO.png"],
  "076": ["https://i.imgur.com/sBYKtjM.png", "https://i.imgur.com/C3KZcCz.png"],
  "077": ["https://i.imgur.com/HzrVSTK.png", "https://i.imgur.com/CVSk04L.png"],
  "078": ["https://i.imgur.com/l7ykoJP.png", "https://i.imgur.com/5A0dEdo.png"],
  "079": ["https://i.imgur.com/B8P1mRe.png", "https://i.imgur.com/1In7L3C.png"],
  "080": ["https://i.imgur.com/2Xxfm0J.png", "https://i.imgur.com/3VJOeTb.png"]
}

peronista_links = {
  "000": ["https://i.imgur.com/Io2xP5s.png", "https://i.imgur.com/tKFsfX8.png"],
  "001": ["https://i.imgur.com/tuJz9JR.png", "https://i.imgur.com/sxwCSgC.png"],
  "002": ["https://i.imgur.com/RXwubbC.png", "https://i.imgur.com/lQVx7GZ.png"],
  "003": ["https://i.imgur.com/PwulXNL.png", "https://i.imgur.com/4dIUWP7.png"],
  "004": ["https://i.imgur.com/v3CrMBw.png", "https://i.imgur.com/V1N8Ool.png"],
  "005": ["https://i.imgur.com/Oy6OV1p.png", "https://i.imgur.com/pVpUb1O.png"],
  "006": ["https://i.imgur.com/bTzvZZc.png", "https://i.imgur.com/kDUuWzJ.png"],
  "007": ["https://i.imgur.com/GO8Q61Z.png", "https://i.imgur.com/Yku3AW4.png"],
  "008": ["https://i.imgur.com/w8dgJjL.png", "https://i.imgur.com/8pVV3RK.png"],
  "009": ["https://i.imgur.com/vpoK52l.png", "https://i.imgur.com/lEcX2LT.png"],
  "010": ["https://i.imgur.com/MMnY464.png", "https://i.imgur.com/Vkrfwrm.png"],
  "011": ["https://i.imgur.com/MyHXsrY.png", "https://i.imgur.com/PLpPBOk.png"],
  "012": ["https://i.imgur.com/Bl0uZCR.png", "https://i.imgur.com/CAbfLfe.png"],
  "013": ["https://i.imgur.com/oy9nZrW.png", "https://i.imgur.com/J28pW3K.png"],
  "014": ["https://i.imgur.com/QFch33B.png", "https://i.imgur.com/Bqr8RUU.png"],
  "015": ["https://i.imgur.com/T1W67NZ.png", "https://i.imgur.com/pZKqwvA.png"],
  "016": ["https://i.imgur.com/SmnUbAy.png", "https://i.imgur.com/VZN8t8h.png"],
  "017": ["https://i.imgur.com/tSosuvz.png", "https://i.imgur.com/zAqdUZH.png"],
  "018": ["https://i.imgur.com/Lm4ZbT7.png", "https://i.imgur.com/YwmSPjt.png"],
  "019": ["https://i.imgur.com/MAtxyU9.png", "https://i.imgur.com/v8PysPS.png"],
  "020": ["https://i.imgur.com/PV31YL2.png", "https://i.imgur.com/AdNSKF2.png"],
  "021": ["https://i.imgur.com/x5wld2q.png", "https://i.imgur.com/yd1gmdf.png"],
  "022": ["https://i.imgur.com/zIu0rfj.png", "https://i.imgur.com/BduyXpd.png"],
  "023": ["https://i.imgur.com/sc8wKkx.png", "https://i.imgur.com/hGheLCj.png"],
  "024": ["https://i.imgur.com/aTTtoah.png", "https://i.imgur.com/1URkH8T.png"],
  "025": ["https://i.imgur.com/2RhGFyo.png", "https://i.imgur.com/8dh3WwD.png"],
  "026": ["https://i.imgur.com/911ezxf.png", "https://i.imgur.com/DpOLsGP.png"],
  "027": ["https://i.imgur.com/PMzmrde.png", "https://i.imgur.com/uzK0HMZ.png"],
  "028": ["https://i.imgur.com/Vv9OeV8.png", "https://i.imgur.com/FJ0kOKq.png"],
  "029": ["https://i.imgur.com/cGFPmju.png", "https://i.imgur.com/BHxM5Qe.png"],
  "030": ["https://i.imgur.com/8YKaCBP.png", "https://i.imgur.com/halN7iC.png"],
  "031": ["https://i.imgur.com/N3KusGR.png", "https://i.imgur.com/MztNQji.png"],
  "032": ["https://i.imgur.com/SobdclW.png", "https://i.imgur.com/MS37VET.png"],
  "033": ["https://i.imgur.com/UfWO9wx.png", "https://i.imgur.com/G57VrNR.png"],
  "034": ["https://i.imgur.com/7vFyyGP.png", "https://i.imgur.com/odKgerR.png"],
  "035": ["https://i.imgur.com/hdgjzFQ.png", "https://i.imgur.com/R2HU6Pr.png"],
  "036": ["https://i.imgur.com/nJBH2wV.png", "https://i.imgur.com/kl3vG6b.png"],
  "037": ["https://i.imgur.com/yhOeaKY.png", "https://i.imgur.com/VPlrWLN.png"],
  "038": ["https://i.imgur.com/U6gZf2a.png", "https://i.imgur.com/5VaiYv4.png"],
  "039": ["https://i.imgur.com/wG70SnH.png", "https://i.imgur.com/FQOQAww.png"],
  "040": ["https://i.imgur.com/S9igFu6.png", "https://i.imgur.com/zc53vKm.png"],
  "041": ["https://i.imgur.com/PgD4J3u.png", "https://i.imgur.com/jNOT6mK.png"],
  "042": ["https://i.imgur.com/HrJMT7s.png", "https://i.imgur.com/f3MliKc.png"],
  "043": ["https://i.imgur.com/EdQdnXu.png", "https://i.imgur.com/DXr1cpD.png"],
  "044": ["https://i.imgur.com/IE5YObQ.png", "https://i.imgur.com/tNgN7Nc.png"],
  "045": ["https://i.imgur.com/wYuZttI.png", "https://i.imgur.com/PVEc93L.png"],
  "046": ["https://i.imgur.com/FXRhdZB.png", "https://i.imgur.com/XiRogEh.png"],
  "047": ["https://i.imgur.com/HOdtTde.png", "https://i.imgur.com/kEq92lX.png"],
  "048": ["https://i.imgur.com/ohcGSzJ.png", "https://i.imgur.com/r48V0Ua.png"],
  "049": ["https://i.imgur.com/vArNH5U.png", "https://i.imgur.com/t83sYWG.png"],
  "050": ["https://i.imgur.com/Yzkdz3G.png", "https://i.imgur.com/01ukRpP.png"],
  "051": ["https://i.imgur.com/qCNXOmI.png", "https://i.imgur.com/RezIGO4.png"],
  "052": ["https://i.imgur.com/XkVXH9r.png", "https://i.imgur.com/130kRnb.png"],
  "053": ["https://i.imgur.com/Qi2gBka.png", "https://i.imgur.com/if05xa9.png"],
  "054": ["https://i.imgur.com/4wAipTt.png", "https://i.imgur.com/2WtPfqD.png"],
  "055": ["https://i.imgur.com/IGIqu0Y.png", "https://i.imgur.com/w1fXcfs.png"],
  "056": ["https://i.imgur.com/7Pk74N0.png", "https://i.imgur.com/OF9gX3Q.png"],
  "057": ["https://i.imgur.com/OlqpKe6.png", "https://i.imgur.com/av1Jyfd.png"],
  "058": ["https://i.imgur.com/zdNlGYs.png", "https://i.imgur.com/4nvJq2H.png"],
  "059": ["https://i.imgur.com/qEtoVXz.png", "https://i.imgur.com/y31SmGo.png"],
  "060": ["https://i.imgur.com/uVZNFJJ.png", "https://i.imgur.com/8YDJv6z.png"],
  "061": ["https://i.imgur.com/pFcuCuk.png", "https://i.imgur.com/AJLvFfq.png"],
  "062": ["https://i.imgur.com/E7xVc6K.png", "https://i.imgur.com/rgphjJJ.png"],
  "063": ["https://i.imgur.com/KOoNNTO.png", "https://i.imgur.com/faq2x4T.png"],
  "064": ["https://i.imgur.com/HweonkO.png", "https://i.imgur.com/uJ6xMGR.png"],
  "065": ["https://i.imgur.com/lmpHVsx.png", "https://i.imgur.com/qpj2rqJ.png"],
  "066": ["https://i.imgur.com/hemDhwA.png", "https://i.imgur.com/wZxVzmZ.png"],
  "067": ["https://i.imgur.com/UpSvZHJ.png", "https://i.imgur.com/MO6GDfA.png"],
  "068": ["https://i.imgur.com/zqw3z42.png", "https://i.imgur.com/svVZQ8e.png"],
  "069": ["https://i.imgur.com/KV9vvFK.png", "https://i.imgur.com/E5dUkB8.png"],
  "070": ["https://i.imgur.com/sXD7Z6W.png", "https://i.imgur.com/okyEvJV.png"],
  "071": ["https://i.imgur.com/E2cd96Q.png", "https://i.imgur.com/hfz6MAu.png"],
  "072": ["https://i.imgur.com/Xekv1Qm.png", "https://i.imgur.com/0gYjALF.png"],
  "073": ["https://i.imgur.com/OfR8iiy.png", "https://i.imgur.com/PlLTmE1.png"],
  "074": ["https://i.imgur.com/zpkVsu8.png", "https://i.imgur.com/PoVUJGu.png"],
  "075": ["https://i.imgur.com/NompMKa.png", "https://i.imgur.com/4yZlX8Z.png"],
  "076": ["https://i.imgur.com/7cnbGn6.png", "https://i.imgur.com/6GQoqYV.png"],
  "077": ["https://i.imgur.com/UlgX03u.png", "https://i.imgur.com/mscnHxO.png"],
  "078": ["https://i.imgur.com/SiaSyA6.png", "https://i.imgur.com/rvT2u70.png"],
  "079": ["https://i.imgur.com/2RF86JH.png", "https://i.imgur.com/dVNSvUS.png"],
  "080": ["https://i.imgur.com/CCtrO1n.png", "https://i.imgur.com/Cg4VVYi.png"]
}


if __name__ == '__main__':
    images = []
    for k in otaku_links.keys():
        remove_white_background(url_to_image(otaku_links[k][0]), f'../images/{otaku_links[k][0].rsplit("/", 1)[1]}')
        images.append({
            'image': f"./images/{otaku_links[k][0].rsplit('/', 1)[1]}",
            'result': 'o',
            'id': otaku_links[k][0].rsplit('/', 1)[1].replace('.png', ''),
        })
    for k in peronista_links.keys():
        remove_white_background(url_to_image(peronista_links[k][0]), f'../images/{peronista_links[k][0].rsplit("/", 1)[1]}')
        images.append({
            'image': f"./images/{peronista_links[k][0].rsplit('/', 1)[1]}",
            'result': 'p',
            'id': peronista_links[k][0].rsplit('/', 1)[1].replace('.png', ''),
        })
    with open('../images/images.json', 'w') as file:
        json.dump(images, file)
