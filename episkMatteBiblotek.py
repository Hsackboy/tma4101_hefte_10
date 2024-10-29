from math import ceil, floor


def integralMidpunkt(a: float, b: float, n: int, f, absolute: bool) -> float:
    """Finner integralet med midpunktstillnærming

    Args:
        a (float): start
        b (float): slutt
        n (int): antall iterasjoner
        f (function): funksjonen som integreres
        absolute (bool): Bestemmer om du skal ha integralet eller arealet av grafen

    Returns:
        float: returnerer integralet eller arealet av grafen
    """

    dx = (b - a) / n
    s = 0
    if absolute == True:
        for i in range(1, n + 1):
            m = a + (i - 0.5) * dx
            s += abs(f(m) * dx)
    else:
        for i in range(1, n + 1):
            m = a + (i - 0.5) * dx
            s += f(m) * dx
    return s


def integralTrapes(a: float, b: float, n: int, f, absolute: bool) -> float:
    """Finner integralet med trapesmetoden

    Args:
        a (float): start
        b (float): slutt
        n (int): antall iterasjoner
        f (function): funksjonen som integreres
        absolute (bool): Bestemmer om du skal ha integralet eller arealet av grafen

    Returns:
        float: returnerer integralet eller arealet av grafen
    """
    dx = (b - a) / n
    s = f(a) + f(b)
    if absolute == True:
        for i in range(1, n):
            x_i = a + i * dx
            s += abs(2 * f(x_i))
        s *= dx / 2
    else:
        for i in range(1, n):
            x_i = a + i * dx
            s += 2 * f(x_i)
        s *= dx / 2
    return s


def integralLeft(a: float, b: float, n: int, f, absolute: bool) -> float:
    """Finner integralet med venstretillnærming

    Args:
        a (float): start
        b (float): slutt
        n (int): antall iterasjoner
        f (function): funksjonen som integreres
        absolute (bool): Bestemmer om du skal ha integralet eller arealet av grafen

    Returns:
        float: returnerer integralet eller arealet av grafen
    """
    dx = (b - a) / n
    s = 0
    if absolute == True:
        for i in range(1, n + 1):
            x_i = a + (i - 1) * dx
            s += abs(f(x_i) * dx)
    else:
        for i in range(1, n + 1):
            x_i = a + (i - 1) * dx
            s += f(x_i) * dx
    return s


def integralRight(a: float, b: float, n: int, f, absolute: bool) -> float:
    """Finner integralet med høyretillnærming

    Args:
        a (float): start
        b (float): slutt
        n (int): antall iterasjoner
        f (function): funksjonen som integreres
        absolute (bool): Bestemmer om du skal ha integralet eller arealet av grafen

    Returns:
        float: returnerer integralet eller arealet av grafen
    """
    dx = (b - a) / n
    s = 0
    if absolute == True:
        for i in range(1, n + 1):
            x_i = a + i * dx
            s += abs(f(x_i) * dx)
    else:
        for i in range(1, n + 1):
            x_i = a + i * dx
            s += f(x_i) * dx
    return s


def integralRightList(x: list, f: list) -> float:
    """finner integralet basert på en liste med verdier og høyretillnærming

    Args:
        x (list): x verdier
        f (list): f(x) verdier

    Returns:
        float: retunerer integralet
    """
    s = 0
    dx = x[1] - x[0]
    for i in range(1, len(f)):
        s += dx * f[i]
    return s


def integralLeftList(x: list, f: list) -> float:
    """finner integralet basert på en liste med verdier og venstretillnærming

    Args:
        x (list): x verdier
        f (list): f(x) verdier

    Returns:
        float: retunerer integralet
    """
    dx = x[1] - x[0]
    s = 0
    for i in range(len(f) - 1):
        s += dx * f[i]
    return s


def integralEpisk(a: float, b: float, n: int, f, absolute: bool) -> float:
    """kombinerer alle fire integreringsmetodene ved å ta gjennomsnittet av de

    Args:
        a (float): start
        b (float): slutt
        n (int): antall iterasjoner
        f (function): funksjonen som integreres
        absolute (bool): Bestemmer om du skal ha integralet eller arealet av grafen

    Returns:
        float: returnerer integralet eller arealet av grafen
    """
    i = 0
    i += integralMidpunkt(a, b, n, f, absolute)
    i += integralRight(a, b, n, f, absolute)
    i += integralLeft(a, b, n, f, absolute)
    i += integralTrapes(a, b, n, f, absolute)
    return i / 4


def integralLikning(
    a: float, end: float, dx: float, f, absolute: bool, nIIntegral: int
):
    """Advarsel! funker ikke så bra
        Finner når integralet er lik en verdi og returnerer den (b)


    Args:
        a (float): startverdi
        end (float): integral verdi
        dx (float): steg størrelse anbefalt ca 10**-3
        f (_type_): funksjon
        absolute (bool): bestemmer om man bruker arealet eller integralet
        nIIntegral (int): antall iterasjoner i integralet

    Returns:
        _type_: _description_
    """
    s = 0
    b = dx
    # a = 0
    while s <= end:
        s = integralEpisk(a, b, nIIntegral, f, absolute)
        b += dx
    return b


def andrePolySolve(a: float, b: float, c: float, target: float) -> list:
    """løser andregraslikninger

    Args:
        a (float): x^2
        b (float): x
        c (float): konstantledd
        target (float): hvilket tall polynomet er lik

    Returns:
        list: retunerer løsningen som liste
    """
    print(f"a={a},b={b},c={c},taget={target}")
    returnList = []
    if target > 0:
        c -= target
    if target < 0:
        c += target

    try:
        returnList.append((-b + sqrT((-b) ** 2 - 4 * a * c)) / (2 * a))
    except:
        pass
        # print("nei", end="")

    try:
        returnList.append((-b - sqrT((-b) ** 2 - 4 * a * c)) / (2 * a))
    except:
        pass
        # print("nei", end="")

    return sorted(returnList)


def faktoriser(tall: int) -> list:
    """faktoriserer tallet

    Args:
        tall (int): tallet som skal faktoriseres

    Returns:
        list: liste med faktorer
    """
    fractionList = []
    noMoreFractions = False
    tall = int(tall)
    while noMoreFractions == False:
        # print("c")
        noMoreFractions = True
        for i in range(2, tall):
            # print(i)
            if tall / i == int(tall / i):
                fractionList.append(i)
                tall = int(tall / i)
                noMoreFractions = False
                break
    fractionList.append(tall)
    return fractionList


def makeFraction(answer, roundAmount):  # ikke bruk
    """Ikke bruk!!!!!

    Args:
        answer (_type_): _description_
        roundAmount (_type_): _description_

    Returns:
        _type_: _description_
    """
    top = round(answer, roundAmount)
    bottom = 1
    # print(top)
    # print(bottom)
    while top != int(top):
        # print("a")
        top *= 10
        bottom *= 10
    # print("b")
    # print(top)
    # print(bottom)
    topFaktor = faktoriser(top)
    bottomFaktor = faktoriser(bottom)
    topFaktorAfter = []
    # print(f"top ={topFaktor} \nbottom ={bottomFaktor}")
    for value in topFaktor:
        if value in bottomFaktor:
            bottomFaktor.pop(bottomFaktor.index(value))
        else:
            topFaktorAfter.append(value)

    top = 1
    bottom = 1
    for value in topFaktorAfter:
        top *= value
    for value in bottomFaktor:
        bottom *= value
    return f"{top}/{bottom}"


def averageIntegral(a: float, b: float, n: int, f) -> float:
    """finner gjennomsnittsverdien av integralet

    Args:
        a (float): startverdi
        b (float): sluttverdi
        n (int): interasjsoner
        f (funksjon): funksjon

    Returns:
        float: gjennomsnittsverdi av integral
    """
    integral = integralEpisk(a, b, n, f, False)
    average = (1 / (b - a)) * integral
    return average


def fakultet(x: int) -> int:
    """finner fakultet til et tall (2!,3! osv)

    Args:
        x (int): tallet som det skal finne fakultet til

    Returns:
        int: fakulteten av tallet
    """
    fakultetVerdi = 1
    for i in range(1, x + 1):
        fakultetVerdi *= i
    return fakultetVerdi


def spimplifyFraction(top: int, bottom: int) -> list:
    """forenkler en brøk

    Args:
        top (int): teller
        bottom (int): nevner

    Returns:
        list: liste over ny brøk [0]=top [1]=bot
    """
    isNegative = False
    if top < 0:
        top = abs(top)
        isNegative = not isNegative
    if bottom < 0:
        bottom = abs(bottom)
        isNegative = not isNegative

    topFactors = faktoriser(top)
    newFactorTop = []
    bottomFactors = faktoriser(bottom)

    for factor in topFactors:
        if factor in bottomFactors:
            bottomFactors.remove(factor)
        else:
            newFactorTop.append(factor)

    newTop = 1
    for factor in newFactorTop:
        newTop *= factor

    newBot = 1
    for factor in bottomFactors:
        newBot *= factor

    if isNegative:
        return [newTop * -1, newBot]
    return [newTop, newBot]


def spimplifyFractionP(top: int, bottom: int) -> None:
    """forenkler en brøk og skirver ut i Konsoll

    Args:
        top (int): teller
        bottom (int): nevner

    """
    isNegative = False
    if top < 0:
        top = abs(top)
        isNegative = not isNegative
    if bottom < 0:
        bottom = abs(bottom)
        isNegative = not isNegative

    topFactors = faktoriser(top)
    newFactorTop = []
    bottomFactors = faktoriser(bottom)

    for factor in topFactors:
        if factor in bottomFactors:
            bottomFactors.remove(factor)
        else:
            newFactorTop.append(factor)

    newTop = 1
    for factor in newFactorTop:
        newTop *= factor

    newBot = 1
    for factor in bottomFactors:
        newBot *= factor

    if isNegative:
        print([newTop * -1, newBot])
    else:
        print([newTop, newBot])


def eInXVal(x: float, n: int) -> float:
    """Beregner verdien for e opphøyd i x

    Args:
        x (float): x verdi som e opphøyes i
        n (int): antall iterasjoner (bestemmer nøyaktighet)

    Returns:
        float: beregnet verdi for e opphøyd i x
    """
    eValue = 1
    for i in range(1, n):
        eValue += (x**i) / fakultet(i)
    return eValue


def toRad(angel: float, fraction=False):
    """gjør vinkel om til radian

    Args:
        angel (float):vinkel
        fraction (bool, optional): retunerer som brøk, Advarsel! inneholder ikke pi noe som også egentlig skal væremed i teller. Defaults to False.

    Returns:
        _type_: radian
    """
    if fraction == True:
        return spimplifyFraction(angel, 180)
    return (angel / 180) * pi


def toRadP(angel: float, fraction=False) -> None:
    """gjør vinkel om til radian og skriver det ut

    Args:
        angel (float):vinkel
        fraction (bool, optional): retunerer som brøk, Advarsel! inneholder ikke pi noe som også egentlig skal væremed i teller. Defaults to False.
    """
    if fraction == True:
        print(spimplifyFraction(angel, 180))
    else:
        print((angel / 180) * pi)


def toAngel(rad: float) -> float:
    """gjør radian til vinkel

    Args:
        rad (float): radian

    Returns:
        float: vinkel
    """
    return (rad / pi) * 180


def toAngelP(rad: float) -> None:
    """gjør radian til vinkel og skriver den ut

    Args:
        rad (float): radian
    """
    print((rad / pi) * 180)


def sqrT(
    n, accuracy=10**-10, stop=1000
) -> float:  # bruker stor T i navet slik at det ikke blir kluss med math bibloteket
    """beregner verdi for kvadratrot

    Args:
        n (float): tallet som skal kvadratrotes
        accuracy (_type_, optional): hvor nøyaktig før man stopper. Defaults to 10**-10.
        stop (int, optional): antall iterasjoner hvis det ikke kommer en løsning. Defaults to 1000.

    Returns:
        float: kvadratrot av n
    """
    old_x = n
    for i in range(stop):
        new_x = (1 / 2) * (old_x + (n / old_x))
        if abs(new_x - old_x) < accuracy:
            break
        old_x = new_x
    return new_x


def compareAccuracy(num1: float, num2: float, inPercent=False):
    """sammenlikner 2 tall på antall siffer som er rett

    Args:
        num1 (float): nummer 1
        num2 (float): nummer 2
        inPercent (bool, optional): retunrerer forskjellen i prosent. Defaults to False.

    Returns:
        float or string: returnerer en string eller float som forteller nøyaktigheten
    """
    (*num1,) = str(num1)
    (*num2,) = str(num2)

    numberOfRight = 0

    num1Length = len(num1)
    num2Length = len(num2)

    lengthToUse = num1Length
    longest = num2Length
    if num1Length > num2Length:
        lengthToUse = num2Length
        longest = num1Length

    for i in range(lengthToUse):
        if num1[i] == num2[i]:
            numberOfRight += 1
        else:
            break

    if inPercent == True:
        if num1Length > num2Length or num1Length < num2Length:
            return (numberOfRight / longest) * 100
        return (numberOfRight / num1Length) * 100

    if num1Length > num2Length or num1Length < num2Length:
        return f"{numberOfRight}/{longest}"
    return f"{numberOfRight}/{num1Length}"


def coS(
    x: float, degrees=True, accuracy=10**-17, stop=1000
) -> float:  # Taylor Series
    """beregner verdi for cos(x)

    Args:
        x (float): tall som skal beregenes cos på
        degrees (bool, optional): grader eller radianer. Defaults to True.
        accuracy (_type_, optional): nøyakktighet for stopp. Defaults to 10**-17.
        stop (int, optional): antall iterasjoner hvis det ikke kommer en løsning. Defaults to 1000.

    Returns:
        float: verdi for cos(x)
    """
    if degrees == True:
        x = toRad(x)

    old_x = 0
    new_x = 0
    for i in range(0, stop):
        new_x += (((-1) ** i) * (x ** (2 * i))) / (fakultet(2 * i))
        if abs(new_x - old_x) < accuracy:
            # print("accuracy reached")
            break
        old_x = new_x
    return new_x


def siN(x: float, degrees=True, accuracy=10**-18, stop=1000) -> float:
    """beregner verdi for sin(x)

    Args:
        x (float): tall som skal beregenes cos på
        degrees (bool, optional): grader eller radianer. Defaults to True.
        accuracy (_type_, optional): nøyakktighet for stopp. Defaults to 10**-18.
        stop (int, optional): antall iterasjoner hvis det ikke kommer en løsning. Defaults to 1000.

    Returns:
        float: verdi for cos(x)
    """
    if degrees == True:
        x = toRad(x)

    old_x = x
    new_x = x
    for i in range(1, stop):
        new_x += ((-1) ** i) * ((x ** (3 + 2 * (i - 1))) / fakultet(3 + 2 * (i - 1)))
        if abs(new_x - old_x) < accuracy:
            # print("accuracy reached")
            break
        old_x = new_x
    return new_x


def finnKvadrantOgOmlop(x:float, degrees=True)->None:
    """finner kvandrant og omløp til vinkel x

    Args:
        x (float): vinkel
        degrees (bool, optional): bestemmer om vinkel skrives inn som vinkel. Defaults to True.
    """
    if degrees is False:
        x = toAngel(x)
    omlop = ceil(x/360)
    kvadrant = floor(((x-0.1)-(floor(x/360)*360))/90)+1
    if kvadrant==0:
        kvadrant=1
    print(f"vinkelen {x} er i omløp {omlop} og i kvadrant {kvadrant}")

def derivert(x:float,f, delta_x=1E-8)->float:
    """deriverer funksjon f

    Args:
        x (float): x verdi for derivasjon
        f (_type_): Funksjon
        delta_x (_type_, optional): bestemmer nøyaktighet til derivasjonen. Defaults to 1E-8.

    Returns:
        float: deriverte av f for en verdi av x
    """
    return (f(x+delta_x)-f(x))/delta_x
    

e = eInXVal(1, 1000)  # definerer verdi for e opphøyd i 1
pi = 3.14159265359  # definerer verdi for pi. (Hentet fra geogebra)

# oldAcc = 0
# newAcc = oldAcc

# for acc in range(5,30):
#     summen = 0
#     runder =0
#     accToUse = 10**-acc

#     for i in range(1,3600):
#         summen+= compareAccuracy(coS(i/10,accuracy=accToUse,stop=10**100),m.cos(m.radians(i/10)),True)
#         runder+=1
#     newAcc=summen/runder
#     # print(f"summen={summen}, runder={runder} sammen= {summen/runder}")
#     print(f"nøyaktighet= {newAcc} % , accToUse={accToUse}, diffOldNewAcc ={compareAccuracy(newAcc,oldAcc,True)}")
#     oldAcc = newAcc
#     print("done")
