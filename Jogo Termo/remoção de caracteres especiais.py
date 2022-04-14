def correcao():
    palavras2 = []

    palavras = ['vinho', 'vinha', 'venho', 'venha', 'velho', 'velha', 'valho', 'valha', 'unhas', 'tolhê', 'tolho', 'tolhi', 'tolhe', 'tolha', 'tocha', 'tinha',
                'tenho', 'tenha', 'telha', 'talhá', 'talho', 'talhe', 'talha', 'tachá', 'tacho', 'tache', 'tacha', 'sonhá', 'sonho', 'sonhe', 'sonha', 'senha',
                'sanha', 'rolha', 'rocha', 'ralhá', 'ralho', 'ralhe', 'ralha', 'rachá', 'racho', 'rache', 'racha', 'punho', 'punha', 'ponho', 'ponha', 'pinho',
                'pinha', 'pilhá', 'pilho', 'pilhe', 'pilha', 'pichá', 'picho', 'piche', 'picha', 'palha', 'olhou', 'olhos', 'olhes', 'olhem', 'olhei', 'olhas',
                'olhar', 'olham', 'olhai', 'ninho', 'nicho', 'molhá', 'molho', 'molhe', 'molha', 'minha', 'milho', 'milha', 'mecha', 'manhã', 'manha', 'malhá',
                'malho', 'malhe', 'malha', 'macho', 'linho', 'linha', 'lhama', 'lenho', 'lenha', 'junho', 'julho', 'inchá', 'incho', 'inche', 'incha', 'ilhou',
                'ilhes', 'ilhem', 'ilhei', 'ilhas', 'ilhar', 'ilham', 'ilhai', 'húmus', 'hímen', 'hífen', 'hélio', 'hábil', 'hurra', 'hunos', 'humor', 'hulha',
                'houve', 'hotel', 'horto', 'horta', 'horda', 'horas', 'honrá', 'honro', 'honre', 'honra', 'homem', 'hinos', 'hindu', 'hiena', 'hiato', 'herói',
                'herdá', 'herdo', 'herde', 'herda', 'heras', 'havia', 'haver', 'havei', 'hauri', 'haure', 'haste', 'harém', 'harpa', 'haras', 'halos', 'hajas',
                'hajam', 'ganhá', 'ganho', 'ganhe', 'ganha', 'galho', 'folha', 'filha', 'fichá', 'ficho', 'fiche', 'ficha', 'fechá', 'fecho', 'feche', 'fecha',
                'falhá', 'falho', 'falhe', 'falha', 'facho', 'enchê', 'encho', 'enchi', 'enche', 'encha', 'ducha', 'cunhá', 'cunho', 'cunhe', 'cunha', 'colhê',
                'colho', 'colhi', 'colhe', 'colha', 'cocho', 'chuva', 'chutá', 'chuto', 'chute', 'chuta', 'chupá', 'chupo', 'chupe', 'chupa', 'choça', 'chovê',
                'chovo', 'chovi', 'chove', 'chova', 'chorá', 'choro', 'chore', 'chora', 'chocá', 'choco', 'choca', 'chiou', 'chies', 'chiem', 'chiei', 'chias',
                'chiar', 'chiam', 'chiai', 'cheio', 'cheia', 'chegá', 'chego', 'chega', 'chefe', 'chefa', 'checá', 'checo', 'checa', 'chave', 'chato', 'chata',
                'chapa', 'chamá', 'chamo', 'chame', 'chama', 'chalé', 'chale', 'chagá', 'chago', 'chaga', 'calhá', 'calho', 'calhe', 'calha', 'cacho', 'bucho',
                'bucha', 'bolha', 'bocha', 'bicho', 'bicha', 'banhá', 'banho', 'banhe', 'banha', 'alhos', 'alheá', 'achou', 'aches', 'achem', 'achei', 'achas',
                'achar', 'acham', 'achai', 'Wuhan', 'Hegel', 'Haiti', 'Filho', 'Délhi', 'Dhaka', 'Delhi', 'China', 'Chile', 'Chico', 'Chica', 'Bahia',]

    special = ['á', 'à', 'â', 'ã', 'ä', 'é', 'è', 'ê', 'ë', 'í', 'ì', 'î', 'ï', 'ô', 'õ', 'ó', 'ò', 'ö', 'ú', 'ù', 'û', 'ü']
    letras = ''

    for k in palavras:
        xt = ''
        for letra in k:
            if letra in special:
                xyz = special.index(letra)
                if xyz < 5:
                    xt += 'a'
                elif xyz < 9:
                    xt += 'e'
                elif xyz < 13:
                    xt += 'i'
                elif xyz < 18:
                    xt += 'o'
                else:
                    xt += 'u'
            else:
                xt += letra

        palavras2 += [xt]

    print(palavras2)

correcao()