from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return '''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Geometric Gap</title>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" 
            integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
                    crossorigin="anonymous">
            <link rel="stylesheet" href="static/newcss.css" type="text/css">
            <style type="text/css">
                #calculator * {font-size: 16px;}
                #calculator table {border: solid 3px silver; border-spacing: 3px; background-color: #EEE; }
                #calculator table td {border-spacing: 3px;}
                input.display {width: 166px; text-align: right;}
                td.buttons {border-top: solid 1px silver;}	
                input[type= button] {width: 40px; height: 30px;}
            </style>
        </head>
        <body background="static/fon2.jpg">
            <table align = "center" width="100%" height="100%" border="0px" cellspacing="0" cellpadding="0">
                <tr>
                    <td height="150" width="13%"><a href="http://localhost:8080"><img src="static/1.png" width="250" 
                    height="170"></a></td>
                    <td><h2 class="funny-title section-title"> Бездна Геометрии </h2></td>
                </tr>
                <tr valign="top">
                    <td height="300"> 
                        <div class="category-wrap">
                            <h3>Теоремы</h3>
                            <ul class="drop_vert_menu">
                                <li><a href="http://localhost:8080/cheva">Чевы</a></li>
                                <li><a href="http://localhost:8080/cosines">Косинусов</a></li>
                                <li><a href="http://localhost:8080/sines">Синусов</a>
                                    <ul>
                                        <li><a href="http://localhost:8080/sines">Обычная</a></li>
                                        <li><a href="http://localhost:8080/sines_extended">Расширенная</a></li>
                                    </ul>
                                </li>
                                <li><a href="http://localhost:8080/menelaus">Менелая</a></li>
                                <li><a href="http://localhost:8080">Главная</a></li>
                            </ul>
                        </div> 
                    <form name="calc" id="calculator">
                        <table>
                            <tr>
                                <td>
                                    <input type="text" name="input" size="16" class="display">
                                </td>
                            </tr>
                            <tr>
                                <td class="buttons">
                                    <input type="button" name="one" value="1" OnClick="calc.input.value += '1'">
                                    <input type="button" name="two" value="2" OnClick="calc.input.value += '2'">
                                    <input type="button" name="three" value="3" OnClick="calc.input.value += '3'">
                                    <input type="button" name="add" value="+" OnClick="calc.input.value += '+'">
                                    <br>
                                    <input type="button" name="four" value="4" OnClick="calc.input.value += '4'">
                                    <input type="button" name="five" value="5" OnClick="calc.input.value += '5'">
                                    <input type="button" name="six" value="6" OnClick="calc.input.value += '6'">
                                    <input type="button" name="sub" value="-" OnClick="calc.input.value += '-'">
                                    <br>
                                    <input type="button" name="seven" value="7" OnClick="calc.input.value += '7'">
                                    <input type="button" name="eight" value="8" OnClick="calc.input.value += '8'">
                                    <input type="button" name="nine" value="9" OnClick="calc.input.value += '9'">
                                    <input type="button" name="mul" value="x" OnClick="calc.input.value += '*'">
                                    <br>
                                    <input type="button" name="clear" value="c" OnClick="calc.input.value = ''">
                                    <input type="button" name="zero" value="0" OnClick="calc.input.value += '0'">
                                    <input type="button" name="doit" value="=" OnClick="calc.input.value = 
                                    eval(calc.input.value)">
                                    <input type="button" name="div"  value="/" OnClick="calc.input.value += '/'">
                                </td>
                            </tr>
                        </table>
                    </form>
                    </td>
                    <td align='center'>
                        <div class="text">Геометрия является самым могущетсвенным средством для изощрения наших
                         умственных способностей и даёт нам возможность правильно мыслить и рассуждать. 
                        /Г.Галилей/</div>
                        <img src="static/3.png" height="500px" width="700px">
                    </td>    
                </tr>
            </table>
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" 
        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous">
        </script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" 
integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" 
integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
        </body>
    </html>
    '''


@app.route('/menelaus')
def menelaus():
    return '''
        <!DOCTYPE html>
        <html>   
            <head>
                <title>Geometric Gap</title>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="static/newcss.css" type="text/css">
                <style type="text/css">
                #calculator * {font-size: 16px;}
                #calculator table {border: solid 3px silver; border-spacing: 3px; background-color: #EEE; }
                #calculator table td {border-spacing: 3px;}
                input.display {width: 166px; text-align: right;}
                td.buttons {border-top: solid 1px silver;}	
                input[type= button] {width: 40px; height: 30px;}
            </style>
            </head>
            <body background="static/fon2.jpg">
                <table align = "center" width="100%" height="100%" border="0px" cellspacing="0" cellpadding="0">
                    <tr>
                        <td height="150" width="13%"><a href="http://localhost:8080"><img src="static/1.png" width="250"
                         height="170"></a></td>
                        <td><h2 class="funny-title section-title"> Бездна Геометрии </h2></td>
                    </tr>
                    <tr valign="top">
                        <td> 
                            <div class="category-wrap">
                                <h3>Теоремы</h3>
                                <ul class="drop_vert_menu">
                                    <li><a href="http://localhost:8080/cheva">Чевы</a></li>
                                    <li><a href="http://localhost:8080/cosines">Косинусов</a></li>
                                    <li><a href="http://localhost:8080/sines">Синусов</a>
                                        <ul>
                                            <li><a href="http://localhost:8080/sines">Обычная</a></li>
                                            <li><a href="http://localhost:8080/sines_extended">Расширенная</a></li>
                                        </ul>
                                    </li>
                                    <li><a href="http://localhost:8080/menelaus" style="background: #87CEFA;">Менелая
                                    </a></li>
                                    <li><a href="http://localhost:8080">Главная</a></li>
                                </ul>
                            </div> 
                            <form name="calc" id="calculator">
                        <table>
                            <tr>
                                <td>
                                    <input type="text" name="input" size="16" class="display">
                                </td>
                            </tr>
                            <tr>
                                <td class="buttons">
                                    <input type="button" name="one" value="1" OnClick="calc.input.value += '1'">
                                    <input type="button" name="two" value="2" OnClick="calc.input.value += '2'">
                                    <input type="button" name="three" value="3" OnClick="calc.input.value += '3'">
                                    <input type="button" name="add" value="+" OnClick="calc.input.value += '+'">
                                    <br>
                                    <input type="button" name="four" value="4" OnClick="calc.input.value += '4'">
                                    <input type="button" name="five" value="5" OnClick="calc.input.value += '5'">
                                    <input type="button" name="six" value="6" OnClick="calc.input.value += '6'">
                                    <input type="button" name="sub" value="-" OnClick="calc.input.value += '-'">
                                    <br>
                                    <input type="button" name="seven" value="7" OnClick="calc.input.value += '7'">
                                    <input type="button" name="eight" value="8" OnClick="calc.input.value += '8'">
                                    <input type="button" name="nine" value="9" OnClick="calc.input.value += '9'">
                                    <input type="button" name="mul" value="x" OnClick="calc.input.value += '*'">
                                    <br>
                                    <input type="button" name="clear" value="c" OnClick="calc.input.value = ''">
                                    <input type="button" name="zero" value="0" OnClick="calc.input.value += '0'">
                                    <input type="button" name="doit" value="=" OnClick="calc.input.value =
                                     eval(calc.input.value)">
                                    <input type="button" name="div"  value="/" OnClick="calc.input.value += '/'">
                                </td>
                            </tr>
                        </table>
                    </form>
                        </td>
                        <td align='center' colspan="2"> 
                            <div style="width: 50%;border-radius: 10px; opacity: 0.8; background: whitesmoke; font-size:
                             20px; font-family: FontAwesome;">
                                <p style ="font-family: Bradley Hand, cursive;">Рассмотрим произвольный треугольник ABC
                                 и некую прямую l, которая пересекает две стороны нашего треугольника внутренним образом
                                  и одну — на продолжении. Обозначим точки пересечения M, N, K. </p>
                                <p style ="font-family: Bradley Hand, cursive;">Тогда выполняется следующее соотношение:
                                 (AM / MB) * (BN / NC) * (CK / KA) = 1</p>
                                <p>Д.п. CT||AB, причем a⋂CT = T. </p>
                                <p>Рассмотрим △CTK и △AMK:</p>
                                <p>∠K – общий, ∠TCK = ∠MAK как соответственные при параллельных прямых CT и AB =></p>
                                <p>△CTK подобен △AMK по I признаку подобия => </p>
                                <p>AM / CT = AK / CK => CT = (AM * CK) / AK (1)</p>
                                <p>Рассмотрим △NTC и △BMN:</p>
                                <p>∠TNC = ∠BNM как вертикальные, ∠BMN = ∠NTC как накрест лежащие при параллельных
                                 прямых AB и CT =></p>
                                <p>△NTC подобен △BMN по I признаку подобия =></p>
                                <p>BM / CT = BN / CN => CT = (BM * CN) / BN (2)</p>
                                <p>Приравняем правые части равенств (1) и (2):</p>
                                <p>(AM * CK) / AK = (BM * CN) / BN</p>
                                <p>AM * CK * BN = BM * CN * AK</p>
                                <p>(AM * CK * BN) / (BM * CN * AK) = 1</p>
                                <p>(AM / MB) * (BN / NC) * (CK / KA) = 1;</p>
                                <p>Теорема доказана.</p>
                            </div>
                        </td>    
                    </tr>
                    <tr>
                        <td> </td>
                        <td align="center"><div style="width: 50%;border-radius: 10px; opacity: 0.8; background:
                         whitesmoke; font-size: 20px; font-family: FontAwesome;
                                 height: 350px;">
                                <p><img src="static/me.png" width="400" height="250"></p> 
                            </div>
                        </td>
                    </tr>        
                </table>        
            </body>
        </html>
    '''


@app.route('/cheva')
def cheva():
    return '''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Geometric Gap</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="static/newcss.css" type="text/css">
            <style type="text/css">
                #calculator * {font-size: 16px;}
                #calculator table {border: solid 3px silver; border-spacing: 3px; background-color: #EEE; }
                #calculator table td {border-spacing: 3px;}
                input.display {width: 166px; text-align: right;}
                td.buttons {border-top: solid 1px silver;}	
                input[type= button] {width: 40px; height: 30px;}
            </style>
        </head>
        <body background="static/fon2.jpg">
            <table align = "center" width="100%" height="100%" border="0px" cellspacing="0" cellpadding="0">
                <tr>
                    <td height="150" width="13%"><a href="http://localhost:8080"><img src="static/1.png" width="250"
                     height="170"></a></td>
                    <td><h2 class="funny-title section-title"> Бездна Геометрии </h2></td>
                </tr>
                <tr valign="top">
                    <td> 
                        <div class="category-wrap">
                            <h3>Теоремы</h3>
                            <ul class="drop_vert_menu">
                                <li><a href="http://localhost:8080/cheva" style="background: #87CEFA;">Чевы</a></li>
                                <li><a href="http://localhost:8080/cosines">Косинусов</a></li>
                                <li><a href="http://localhost:8080/sines">Синусов</a>
                                    <ul>
                                        <li><a href="http://localhost:8080/sines">Обычная</a></li>
                                        <li><a href="http://localhost:8080/sines_extended">Расширенная</a></li>
                                    </ul>
                                </li>
                                <li><a href="http://localhost:8080/menelaus">Менелая</a></li>
                                <li><a href="http://localhost:8080">Главная</a></li>
                            </ul>
                        </div> 
                    <form name="calc" id="calculator">
                        <table>
                            <tr>
                                <td>
                                    <input type="text" name="input" size="16" class="display">
                                </td>
                            </tr>
                            <tr>
                                <td class="buttons">
                                    <input type="button" name="one" value="1" OnClick="calc.input.value += '1'">
                                    <input type="button" name="two" value="2" OnClick="calc.input.value += '2'">
                                    <input type="button" name="three" value="3" OnClick="calc.input.value += '3'">
                                    <input type="button" name="add" value="+" OnClick="calc.input.value += '+'">
                                    <br>
                                    <input type="button" name="four" value="4" OnClick="calc.input.value += '4'">
                                    <input type="button" name="five" value="5" OnClick="calc.input.value += '5'">
                                    <input type="button" name="six" value="6" OnClick="calc.input.value += '6'">
                                    <input type="button" name="sub" value="-" OnClick="calc.input.value += '-'">
                                    <br>
                                    <input type="button" name="seven" value="7" OnClick="calc.input.value += '7'">
                                    <input type="button" name="eight" value="8" OnClick="calc.input.value += '8'">
                                    <input type="button" name="nine" value="9" OnClick="calc.input.value += '9'">
                                    <input type="button" name="mul" value="x" OnClick="calc.input.value += '*'">
                                    <br>
                                    <input type="button" name="clear" value="c" OnClick="calc.input.value = ''">
                                    <input type="button" name="zero" value="0" OnClick="calc.input.value += '0'">
                                    <input type="button" name="doit" value="=" OnClick="calc.input.value = 
                                    eval(calc.input.value)">
                                    <input type="button" name="div"  value="/" OnClick="calc.input.value += '/'">
                                </td>
                            </tr>
                        </table>
                    </form>
                    </td>
                    <td align='center' colspan="2"> 
                        <div style="width: 50%;border-radius: 10px; opacity: 0.8; background: whitesmoke; font-size:
                         20px; font-family: FontAwesome;">
                            <p style ="font-family: Bradley Hand, cursive;">Пусть точки A1, B1, C1 лежат на сторонах 
                            треугольника BC, AC и AB соответственно. Пусть отрезки AA1, BB1, CC1 пересекаются в одной 
                            точке O. Тогда:</p>
                            <p style ="font-family: Bradley Hand, cursive;">(AC1 / C1B) * (BA1 / A1C) * (CB1 / B1A) = 1
                            </p>
                            <p>Д.п. Через точки А и С проведём прямые a и b такие, что a||b||BB1, </p>
                            <p>а также продолжим отрезок СС1 за точку С1 до пересечения с прямой a в точке М, 
                            отрезок АА1 за точку А1 до пересечения с прямой b в точке Е.</p>
                            <p>Рассмотрим △AMC1 и △BOC1:</p>
                            <p>∠MC1A = ∠BC1O как вертикальные, ∠AMC1 = ∠BOC1 как накрест лежащие при параллельных 
                            прямых a и ВВ1 =></p>
                            <p>△AMC1 подобен △BOC1 по I признаку подобия =></p>
                            <p>AC1 / C1B = AM / BO;</p>
                            <p>Рассмотрим △BOA1 и △CEA1:</p>
                            <p>∠BA1O = ∠EA1C как вертикальные, ∠BOA1 = ∠CEA1 как накрест лежащие при параллельных 
                            прямых b и BB1 =></p>
                            <p>△BOA1 подобен △CEA1 по I признаку подобия =></p>
                            <p>BA1 / A1C = BO / EC;</p>
                            <p>Рассмотрим △AEC и △AOB1:</p>
                            <p>∠A – общий, ∠AOB1 = ∠AEC как соответственные при параллельных прямых ВВ1 и b =></p>
                            <p>△AEC подобен △AOB1 по I признаку подобия =></p>
                            <p>AB1 / AC = OB1 / EC; (1)</p>
                            <p>Рассмотрим △AMC и △B1OC:</p>
                            <p>∠C – общий, ∠COB1 = ∠CMA как соответственные при параллельных прямых BB1 и a =></p>
                            <p>△AMC подобен △B1OC по I признаку подобия =></p>
                            <p>B1C / AC = OB1 / AM; (2) </p>
                            <p>Поделим (2) на (1):</p>
                            <p>B1C / AB1 = EC / AM; </p>
                            <p>Получаем: (AC1 / C1B) * (BA1 / A1C) * (CB1 / B1A) = (AM / BO) * (BO / EC) * (EC / AM)
                             = 1;</p>
                            <p>Теорема доказана.</p>
                        </div>
                    </td>    
                </tr>
                <tr>
                    <td> </td>
                    <td align="center"><div style="width: 50%;border-radius: 10px; opacity: 0.8; background: whitesmoke;
                     font-size: 20px; font-family: FontAwesomel;
                             height: 350px;">
                            <p><img src="static/che.png" width="400" height="250"></p> 
                        </div>
                    </td>
                </tr>
            </table>
        </body>
    </html>
    '''


@app.route('/cosines')
def cosines():
    return '''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Geometric Gap</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="static/newcss.css" type="text/css">
            <style type="text/css">
                #calculator * {font-size: 16px;}
                #calculator table {border: solid 3px silver; border-spacing: 3px; background-color: #EEE; }
                #calculator table td {border-spacing: 3px;}
                input.display {width: 166px; text-align: right;}
                td.buttons {border-top: solid 1px silver;}	
                input[type= button] {width: 40px; height: 30px;}
            </style>
        </head>
        <body background="static/fon2.jpg">
            <table align = "center" width="100%" height="100%" border="0px" cellspacing="0" cellpadding="0">
                <tr>
                    <td height="150" width="13%"><a href="http://localhost:8080"><img src="static/1.png" width="250" 
                    height="170"></a></td>
                    <td><h2 class="funny-title section-title"> Бездна Геометрии </h2></td>
                </tr>
                <tr valign="top">
                    <td> 
                        <div class="category-wrap">
                            <h3>Теоремы</h3>
                            <ul class="drop_vert_menu">
                                <li><a href="http://localhost:8080/cheva">Чевы</a></li>
                                <li><a href="http://localhost:8080/cosines" style="background: #87CEFA;">Косинусов</a>
                                </li>
                                <li><a href="http://localhost:8080/sines">Синусов</a>
                                    <ul>
                                        <li><a href="http://localhost:8080/sines">Обычная</a></li>
                                        <li><a href="http://localhost:8080/sines_extended">Расширенная</a></li>
                                    </ul>
                                </li>
                                <li><a href="http://localhost:8080/menelaus">Менелая</a></li>
                                <li><a href="http://localhost:8080">Главная</a></li>
                            </ul>
                        </div> 
                    <form name="calc" id="calculator">
                        <table>
                            <tr>
                                <td>
                                    <input type="text" name="input" size="16" class="display">
                                </td>
                            </tr>
                            <tr>
                                <td class="buttons">
                                    <input type="button" name="one" value="1" OnClick="calc.input.value += '1'">
                                    <input type="button" name="two" value="2" OnClick="calc.input.value += '2'">
                                    <input type="button" name="three" value="3" OnClick="calc.input.value += '3'">
                                    <input type="button" name="add" value="+" OnClick="calc.input.value += '+'">
                                    <br>
                                    <input type="button" name="four" value="4" OnClick="calc.input.value += '4'">
                                    <input type="button" name="five" value="5" OnClick="calc.input.value += '5'">
                                    <input type="button" name="six" value="6" OnClick="calc.input.value += '6'">
                                    <input type="button" name="sub" value="-" OnClick="calc.input.value += '-'">
                                    <br>
                                    <input type="button" name="seven" value="7" OnClick="calc.input.value += '7'">
                                    <input type="button" name="eight" value="8" OnClick="calc.input.value += '8'">
                                    <input type="button" name="nine" value="9" OnClick="calc.input.value += '9'">
                                    <input type="button" name="mul" value="x" OnClick="calc.input.value += '*'">
                                    <br>
                                    <input type="button" name="clear" value="c" OnClick="calc.input.value = ''">
                                    <input type="button" name="zero" value="0" OnClick="calc.input.value += '0'">
                                    <input type="button" name="doit" value="=" OnClick="calc.input.value = 
                                    eval(calc.input.value)">
                                    <input type="button" name="div"  value="/" OnClick="calc.input.value += '/'">
                                </td>
                            </tr>
                        </table>
                    </form>
                    </td>
                    <td align='center' colspan="2"> 
                        <div style="width: 50%;border-radius: 10px; opacity: 0.8; background: whitesmoke; font-size:
                         20px; font-family: FontAwesome;">
                            <p style ="font-family: Bradley Hand, cursive;"> Для плоского треугольника, у которого
                             стороны a, b, c и угол α, который противолежит стороне a,справедливо соотношение: </p>
                            <p style ="font-family: Bradley Hand, cursive;">a2 = b2 + c2 – 2bc cosα. </p>
                            <p>Обозначим ∠С за α;</p>
                            <p>Поместим △ABC в систему координат так, что вершина А попала в начало координат, и
                             сторона AC наложилась на луч Ox .</p>
                            <p>Тогда A(0, 0), C(0, b).</p>
                            <p>Выразим координаты точки В через длину отрезка AB и тригонометрические функции угла α:
                            </p>
                            <p>B(с * cos α, c * sin α), т.к. :</p>
                            <p>Д.п. ВН - высота. В △ABH AB – гипотенуза => AH = c * cos α, BH = c * sin α,</p>
                            <p>но AH и ВН – расстояния от осей координат =></p>
                            <p>длина отрезка АН – абсцисса точки В, а длина отрезка ВН – ордината точки В;</p>
                            <p>Выразим длину отрезка BC через координаты его вершин:</p>
                            <p>ВС = √(𝑐∗cos𝛼−𝑏)2+𝑐2∗ 𝑠𝑖𝑛2𝛼 = √𝑐2 ∗𝑐𝑜𝑠2𝛼−2∗𝑏∗𝑐∗cos𝛼+𝑏2+𝑐2∗𝑠𝑖𝑛2
                             𝛼 =√𝑐2∗(𝑠𝑖𝑛2 𝛼+𝑐𝑜𝑠2 𝛼)+𝑏2−2∗𝑏∗𝑐∗cos𝛼;</p>
                            <p>Но из основного тригонометрического тождества следует, что sin2 α + cos2 α = 1 =></p>
                            <p>BC = √𝑐2+𝑏2−2∗𝑏∗𝑐∗cos𝛼 =></p>
                            <p>BC2 = c2 + b2 – 2 * b * c * cos α;</p>
                            <p>Теорема доказана.</p>
                        </div>
                    </td>    
                </tr>
                <tr>
                    <td> </td>
                    <td align="center"><div style="width: 50%;border-radius: 10px; opacity: 0.8; background: whitesmoke;
                     font-size: 20px; font-family: FontAwesome;
                             height: 350px;">
                            <p><img src="static/co.png" width="350" height="250"></p> 
                        </div>
                    </td>
                </tr>
            </table>
        </body>
    </html>
    '''


@app.route('/sines')
def sines():
    return '''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Geometric Gap</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="static/newcss.css" type="text/css">
           <style type="text/css">
                #calculator * {font-size: 16px;}
                #calculator table {border: solid 3px silver; border-spacing: 3px; background-color: #EEE; }
                #calculator table td {border-spacing: 3px;}
                input.display {width: 166px; text-align: right;}
                td.buttons {border-top: solid 1px silver;}	
                input[type= button] {width: 40px; height: 30px;}
            </style>
        </head>
        <body background="static/fon2.jpg">
            <table align = "center" width="100%" height="100%" border="0px" cellspacing="0" cellpadding="0">
                <tr>
                    <td height="150" width="13%"><a href="http://localhost:8080"><img src="static/1.png" width="250"
                     height="170"></a></td>
                    <td><h2 class="funny-title section-title"> Бездна Геометрии </h2></td>
                </tr>
                <tr valign="top">
                    <td> 
                        <div class="category-wrap">
                            <h3>Теоремы</h3>
                            <ul class="drop_vert_menu">
                                <li><a href="http://localhost:8080/cheva">Чевы</a></li>
                                <li><a href="http://localhost:8080/cosines">Косинусов</a></li>
                                <li><a href="http://localhost:8080/sines" style="background: #87CEFA;">Синусов</a>
                                    <ul>
                                        <li><a href="http://localhost:8080/sines">Обычная</a></li>
                                        <li><a href="http://localhost:8080/sines_extended">Расширенная</a></li>
                                    </ul>
                                </li>
                                <li><a href="http://localhost:8080/menelaus">Менелая</a></li>
                                <li><a href="http://localhost:8080">Главная</a></li>
                            </ul>
                        </div> 
                    <form name="calc" id="calculator">
                        <table>
                            <tr>
                                <td>
                                    <input type="text" name="input" size="16" class="display">
                                </td>
                            </tr>
                            <tr>
                                <td class="buttons">
                                    <input type="button" name="one" value="1" OnClick="calc.input.value += '1'">
                                    <input type="button" name="two" value="2" OnClick="calc.input.value += '2'">
                                    <input type="button" name="three" value="3" OnClick="calc.input.value += '3'">
                                    <input type="button" name="add" value="+" OnClick="calc.input.value += '+'">
                                    <br>
                                    <input type="button" name="four" value="4" OnClick="calc.input.value += '4'">
                                    <input type="button" name="five" value="5" OnClick="calc.input.value += '5'">
                                    <input type="button" name="six" value="6" OnClick="calc.input.value += '6'">
                                    <input type="button" name="sub" value="-" OnClick="calc.input.value += '-'">
                                    <br>
                                    <input type="button" name="seven" value="7" OnClick="calc.input.value += '7'">
                                    <input type="button" name="eight" value="8" OnClick="calc.input.value += '8'">
                                    <input type="button" name="nine" value="9" OnClick="calc.input.value += '9'">
                                    <input type="button" name="mul" value="x" OnClick="calc.input.value += '*'">
                                    <br>
                                    <input type="button" name="clear" value="c" OnClick="calc.input.value = ''">
                                    <input type="button" name="zero" value="0" OnClick="calc.input.value += '0'">
                                    <input type="button" name="doit" value="=" OnClick="calc.input.value =
                                     eval(calc.input.value)">
                                    <input type="button" name="div"  value="/" OnClick="calc.input.value += '/'">
                                </td>
                            </tr>
                        </table>
                    </form>
                    </td>
                    <td align='center' colspan="2"> 
                        <div style="width: 50%;border-radius: 10px; opacity: 0.8; background: whitesmoke; font-size:
                         20px; font-family: FontAwesome;">
                            <p style ="font-family: Bradley Hand, cursive;">Теорема Синусов</p>
                            <p style ="font-family: Bradley Hand, cursive;">Стороны треугольника пропорциональны 
                            синусам противолежащих углов.</p>
                            <p>Распишем площадь <span class="trig">△ABC</span> через формулу площади через две стороны 
                            и угол между ними тремя разными способами: </p>
                            <p>S(<span class="trig">△ABC</span>) = 0,5 * <span class="red">a</span> * <span
                            class="green">b</span> * <span class="brown">sin∠C</span>, S(<span class="trig">△ABC</span>)
                             = 0,5 * <span class="red">a</span> * <span class="brown">c</span> * <span class="green">sin∠B</span>, S(<span class="trig">△ABC</span>) = 0,5 * <span class="green">b</span> * <span class="brown">c</span> * <span class="red">sin∠A</span>;</p>
                            <p>Приравняем правые части равенств:</p>
                            <p>0,5 * <span class="red">a</span> * <span class="green">b</span> * <span class="brown">
                            sin∠C</span> = 0,5 * <span class="red">a</span> * <span class="brown">c</span> * 
                            <span class="green">sin∠B</span> = 0,5 * <span class="green">b</span> * <span class="brown">
                            c</span> * <span class="red">sin∠A</span>;</p>
                            <p>Поделим каждое выражение на 0,5 * <span class="red">a</span> * <span class="green">
                            b</span> * <span class="brown">c</span>: </p>
                            <p><span class="red">sin∠A</span> / <span class="red">a</span> = <span class="green">sin∠B
                            </span> / <span class="green">b</span> = <span class="brown">sin∠C</span> / 
                            <span class="brown">c</span>; </p>
                            <p>Теорема доказана.</p>
                        </div>
                    </td>    
                </tr>
                <tr>
                    <td> </td>
                    <td align="center"><div style="width: 50%;border-radius: 10px; opacity: 0.8; background: 
                    whitesmoke; font-size: 20px; font-family: FontAwesome;
                             height: 350px;">
                            <p><img src="static/triug.png" width="320" height="250"></p>
                        </div>
                    </td>
                </tr>
            </table>
        </body>
    </html>
    '''


@app.route('/sines_extended')
def sines_extended():
    return '''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Geometric Gap</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="static/newcss.css" type="text/css">
            <style type="text/css">
                #calculator * {font-size: 16px;}
                #calculator table {border: solid 3px silver; border-spacing: 3px; background-color: #EEE; }
                #calculator table td {border-spacing: 3px;}
                input.display {width: 166px; text-align: right;}
                td.buttons {border-top: solid 1px silver;}	
                input[type= button] {width: 40px; height: 30px;}
            </style>
        </head>
        <body background="static/fon2.jpg">
            <table align = "center" width="100%" height="100%" border="0px" cellspacing="0" cellpadding="0">
                <tr>
                    <td height="150" width="13%"><a href="http://localhost:8080"><img src="static/1.png" width="250" 
                    height="170"></a></td>
                    <td><h2 class="funny-title section-title"> Бездна Геометрии </h2></td>
                </tr>
                <tr valign="top">
                    <td> 
                        <div class="category-wrap">
                            <h3>Теоремы</h3>
                            <ul class="drop_vert_menu">
                                <li><a href="http://localhost:8080/cheva">Чевы</a></li>
                                <li><a href="http://localhost:8080/cosines">Косинусов</a></li>
                                <li><a href="http://localhost:8080/sines" style="background: #87CEFA;">Синусов</a>
                                    <ul>
                                        <li><a href="http://localhost:8080/sines">Обычная</a></li>
                                        <li><a href="http://localhost:8080/sines_extended">Расширенная</a></li>
                                    </ul>
                                </li>
                                <li><a href="http://localhost:8080/menelaus">Менелая</a></li>
                                <li><a href="http://localhost:8080">Главная</a></li>
                            </ul>
                        </div> 
                       <form name="calc" id="calculator">
                        <table>
                            <tr>
                                <td>
                                    <input type="text" name="input" size="16" class="display">
                                </td>
                            </tr>
                            <tr>
                                <td class="buttons">
                                    <input type="button" name="one" value="1" OnClick="calc.input.value += '1'">
                                    <input type="button" name="two" value="2" OnClick="calc.input.value += '2'">
                                    <input type="button" name="three" value="3" OnClick="calc.input.value += '3'">
                                    <input type="button" name="add" value="+" OnClick="calc.input.value += '+'">
                                    <br>
                                    <input type="button" name="four" value="4" OnClick="calc.input.value += '4'">
                                    <input type="button" name="five" value="5" OnClick="calc.input.value += '5'">
                                    <input type="button" name="six" value="6" OnClick="calc.input.value += '6'">
                                    <input type="button" name="sub" value="-" OnClick="calc.input.value += '-'">
                                    <br>
                                    <input type="button" name="seven" value="7" OnClick="calc.input.value += '7'">
                                    <input type="button" name="eight" value="8" OnClick="calc.input.value += '8'">
                                    <input type="button" name="nine" value="9" OnClick="calc.input.value += '9'">
                                    <input type="button" name="mul" value="x" OnClick="calc.input.value += '*'">
                                    <br>
                                    <input type="button" name="clear" value="c" OnClick="calc.input.value = ''">
                                    <input type="button" name="zero" value="0" OnClick="calc.input.value += '0'">
                                    <input type="button" name="doit" value="=" OnClick="calc.input.value = 
                                    eval(calc.input.value)">
                                    <input type="button" name="div"  value="/" OnClick="calc.input.value += '/'">
                                </td>
                            </tr>
                        </table>
                    </form>
                    </td>
                    <td align='center'> 
                        <div style="width: 50%;border-radius: 10px; opacity: 0.8; background: whitesmoke; font-size:
                         20px; font-family: FontAwesome;">
                            <p style ="font-family: Bradley Hand, cursive;">a / sin∠A = b / sin∠B = c / sin∠C = 2R </p>
                            <p style ="font-family: Bradley Hand, cursive;">где a, b, c — стороны треугольника, , 
                            β, γ — противолежащие этим сторонам углы, а R — радиус окружности, которая описана вокруг
                             треугольника.</p>
                            <p>Д. п. Опишем данный треугольник, а также построим диаметр СG.</p>
                            <p>В △BCG ∠CBG = 90⁰, т.к. лежит против диаметра =></p>
                            <p>BC = sin∠BGC * CG = sin∠BCG * 2R ;</p>
                            <p>Т.к. ∠BGC и ∠BAC(∠A) опираются на одну и ту же дугу ∪BC, то эти углы равны =></p>
                            <p>sin∠A = sin∠BGC => BC = sin∠A * 2R. По <a href="http://localhost:8080/sines">обычной 
                            теорме синусов</a></p>
                            <p>sin∠A / a = sin∠B / b = sin∠C / c, то и a / sin∠A = b / sin∠B = c / sin∠C,</p>
                            <p>но a / sin∠A = (2R * sin∠A) / sin∠A = 2R =></p>
                            <p>a / sin∠A = b / sin∠B = c / sin∠C = 2R</p>
                        </div>
                    </td>    
                </tr>
                <tr>
                    <td> </td>
                    <td align="center"><div style="width: 50%;border-radius: 10px; opacity: 0.8; background: whitesmoke;
                     font-size: 20px; font-family: FontAwesome;
                             height: 350px;">
                            <p><img src="static/ras.png" width="250" height="250"></p> 
                        </div>
                    </td>
                </tr>
            </table>
        </body>
    </html>
    '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
