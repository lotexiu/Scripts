import os.path
import random
import time
for nao_toque in range(1):
    for configuracao_do_jogo in range(1):

        gameover = 1000 # é a quantidade de monstros, quando chegar no ultímo, o jogo acaba.

        # Configuração do jogador
        level = 0 # Seu nível inícial do jogo. (aumentar irá deixar o jogo mais dificil)
        hp_total = 100 # vida inicial do jogador.
        mp_total = 100 # mana inicial do jogador.
        skillpoints = 0  # pontos de habilidade (você ganha com o tempo)
        skilldmg = 0  # pontos de dano (você ganha com o tempo)
        skillhp = 0  # pontos de vida (você ganha com o tempo)
        skillmp = 0  # pontos de mana (você ganha com o tempo)
        skillint = 0  # pontos de inteligencia (Dano do ataque especial) (você ganha com o tempo)
        doll_hp = 50 # vida do boneco
        money = 0 # quantidade de ouro
        accdmg = 0 # Precisão do ataque skill point

        # monstros e eventos (para adicionar monstros crie: mons_nome (nome = bioma) = [35, 60, 72, 78, 80, 84, 90, 96, 100]
        # os três ultimos são possiveis eventos (então não mexa) 1 = 1% de chance 100 = 100% chance
        mons = [35, 60, 72, 78, 82, 84, 91, 94, 100]
        nome_alipu = ['Slime', 'Kobold', 'Espectro', 'Goblin com baixa autoestima', 'Golem', 'Tarrasque', 'nada', 'Baú', 'Negociador']
        # tukta
        nome_tukta = ['Goblin', 'Esqueleto', 'Kruthik', 'Fada', 'Gnog', 'Devorador de Almas', 'nada', 'Baú', 'Negociador']
        # videlia
        nome_videlia = ['zumbi', 'Aranha Saltimorte ', 'Guardião', 'Morte', 'Papirus', 'Urso Coruja', 'nada', 'Baú']
        # hyter
        nome_hyter = ['Dr. Zoidberg.', 'Espirito', 'Elemental de fogo', 'gogolta', 'Beholder', 'Beelzebub', 'nada', 'Baú']
        nome_mons = [nome_alipu, nome_tukta, nome_videlia, nome_hyter]
        info_regiao = ['alipu', 'tukta', 'videlia', 'hyter']
        # Configuração de item no inventário

        # itens do jogador (O funcionamento é o mesmo do drop)
        itens = [0, 0, 0, 0, 0, 0]
        # cajado: item para classe mago (consegue do negociador)
        # greatsword: item para classe tank (consegue do negociador)
        # adagas: item para classe assassino (consegue do negociador)
        # anel de cura: item para todas as classes (consegue do negociador)
        # Boneco:  Item ajudante.. (consegue do negociador)
        # armadura leve: diminui o dano recebido (-2)
    # Configurção que não podem ser alteradas!
    exp = 0
    hp_atual = hp_total
    mp_atual = mp_total
    lvlup = 1 # Confidencial
    mortos = 0 # fala de quantos você matou
    luta = 0 # fala de quantas lutas que voce teve
    fugiu = 0 # fala de quantos você fugiu
    kms = 0 # quilometros percorrido
    cp = [40, 100, 100, 100, 80, 40]
    regiao_local = 0
    mons_local = nome_alipu

    txt_compra1 = ['Quer alguma coisa? ', '1.Anel de cura.', '2.Adagas venenosas.', '3.Espada leve.',
                   '4.Cajado do abismo.', '5.Boneco', '6.Armadura Leve', '7.Sair']
    txt_compra2 = ['Quer alguma coisa? ', '1.Amuleto Sagrado.', '2.Adagas de aço.', '3.Espada Pesada.',
                   '4.Nucleo para cajado.', '5.Boneco', '6.Armadura Pesada', '7.Sair']
    txt_compra3 = ['Lamento, mas nao tenho nada para vender', '7.Sair']
    txt_compra4 = ['Lamento, mas nao tenho nada para vender', '7.Sair']
    negociante_txt = [txt_compra1, txt_compra2, txt_compra3, txt_compra4]

print('Antes de começarmos')
print('1.Novo')
if os.path.isfile('save.py'):
    print('2.Carregar')
pergunta = int(input('Escolha:'))
if pergunta == 1:
    neg_local = txt_compra1
    name = input('Seu nome. :')
    nome_boneco = input('Fale um nome de um acompanhante. :')

    print('Escolha uma classe.')
    print('1.Assassíno (Mais dano no principal)')
    print('2.Tank (Mais vida)')
    print('3.Mago (Mais dano no especial)')
    for bug in range(100):
        classe = int(input('Numero da Classe: '))
        if classe == 1:
            spdmg = 10
            bonus_sp = 3
            bonus = 5
            dmg = 10
            hp_total = 80
            break
        elif classe == 2:
            spdmg = 10
            bonus_sp = 3
            hp_total = 200
            bonus = 3
            dmg = 5
            break
        elif classe == 3:
            spdmg = 10
            bonus_sp = 5
            bonus = 3
            dmg = 5
            break
        else:
            print('Erro na seleção. Tente novamente!')

elif pergunta == 2:
    import save

    name = save.name
    nome_boneco = save.nome_boneco
    level = save.level
    hp_total = save.hp_total
    mp_total = save.mp_total
    skillpoints = save.skillpoints
    skilldmg = save.skilldmg
    skillhp = save.skillhp
    skillmp = save.skillmp
    skillint = save.skillint
    money = save.money
    itens = save.itens
    mortos = save.mortos
    luta = save.luta
    fugiu = save.fugiu
    kms = save.kms
    regiao_local = save.regiao_local
    ty = save.ty
    mons_local = nome_mons[ty]
    neg_local = negociante_txt[ty]
    spdmg = save.spdmg
    bonus_sp = save.bonus_sp
    bonus = save.bonus
    dmg = save.dmg
    classe = save.classe
    exp = save.exp
    lvlup = save.lvlup
    accdmg = save.accdmg

for caixas_de_texto in range(1):
        for negociador1_txt in range(1):
            adeus = ['Adeus, espero que não encontremos de novo.', 'Adeus, foi bom fazer negocios com você.',
                     'Se alguem perguntar sobre mim, fale que não conheçe',
                     'Adeus estranho que incomoda a minha vida, mas que me ajuda a ganhar dinheiro.']
            ola = ['Olá estranho qual eu não sei o nome', ('Olá', name, 'como você vai?'),
                   'Olá estranho que me faz rico.', 'Você de novo?',
                   'Você ainda esta vivo?', 'Olá estranho fedorento.']

            txt_con = ['Este item custa']
        for morte1_txt in range(1):
            morte_txt = ['Você morreu.', 'Você morreu de forma elegante.', 'Você morreu de forma estúpida.',
                         'Você foi amassado', 'Você morreu por ataques psicológicos', 'Você morreu de medo']
            morte_enemigo = ['Você o matou', 'Enemigo derrotado.', 'Você matou ele de forma covarde',
                             'Enemigo teve um infarto.', 'Enemigo morreu de cansaço', 'Enemigo morreu de tédio',
                             'O enemigo morreu por causa do seu mal cheiro.']

#
time.sleep(1)
print('Você está saindo de', info_regiao[regiao_local])
time.sleep(1)
for jogo in range(gameover):
    # sistema de morte
    if hp_atual <= 0:
        break
    if hp_atual > 0:
        for lado in range(100):
            ty = 0
            distancia = random.randint(10, 17)
            kms = kms + distancia
            if kms >= 100:
                kms = kms - 100
                regiao = random.randint(0, len(info_regiao) - 1)
                for regiao_loop in range(100):
                    if regiao == ty:
                        if regiao_local == ty:
                            ty = ty + 1
                        regiao_local = ty
                        mons_local = nome_mons[ty]
                        neg_local = negociante_txt[ty]
                        print('Você chegou numa nova região', info_regiao[ty])
                        break
                    else:
                        ty = ty + 1
            else:
                qt = 0
                kb = mons[qt]
                kv = 0

                esquerda = random.randint(1, mons[-1])  # Entre X e Y
                for test in range(100):
                    if esquerda <= kb:
                        es_valor = kv
                        break
                    else:
                        qt = qt + 1
                        kv = kv + 1
                        kb = mons[qt]

                qt = 0
                kv = 0
                if (regiao_local > 1) and (es_valor == 8):
                    es_valor = es_valor - 1
                for test in range(100):
                    if es_valor == kv:
                        mons[qt] = mons[qt] - 9
                        qt = 0
                        for test in range(100):
                            if qt == 9:  # 1 acima da ultima porcentagem
                                break
                            else:
                                mons[qt] = mons[qt] + 1
                                qt = qt + 1
                        break
                    else:
                        qt = qt + 1
                        kv = kv + 1
                        kb = mons[qt]
                qt = 0
                kb = mons[qt]
                kv = 0
                direita = random.randint(1, mons[-1])  # Entre X e Y

                for test in range(100):
                    if direita <= kb:
                        di_valor = kv
                        break
                    else:
                        qt = qt + 1
                        kv = kv + 1
                        kb = mons[qt]

                qt = 0
                kv = 0
                if (regiao_local > 1) and (di_valor == 8):
                    di_valor = di_valor - 1
                for test in range(100):
                    if di_valor == kv:
                        mons[qt] = mons[qt] - 9
                        qt = 0
                        for test in range(100):
                            if qt == 9:  # 1 acima da ultima porcentagem
                                break
                            else:
                                mons[qt] = mons[qt] + 1
                                qt = qt + 1
                        break
                    else:
                        qt = qt + 1
                        kv = kv + 1
                        kb = mons[qt]
            break
        print('Você andou', distancia, 'km')
        time.sleep(1)
        print('E surge dois caminhos.')
        time.sleep(1)
        print('A esquerda tem:', mons_local[es_valor], '| A direita tem:', mons_local[di_valor])
        time.sleep(1)
        print('Qual caminho você deseja?')
        time.sleep(1)
        for escolha in range(100):
            pergunta = input('(1)Esquerda ou (2)Direita?')
            print('')
            if pergunta == '1':
                valor = es_valor
                break
            elif pergunta == '2':
                valor = di_valor
                break
            elif pergunta != '':
                print('erro na escolha')
        if valor == 6:
            time.sleep(0.5)
            print('Você passa pelo caminho sem nada')
            time.sleep(0.5)
        elif valor == 8:
            time.sleep(0.5)
            print('Você se aproxima dessa negociador desconhecido')
            time.sleep(0.5)
            print('E ele lhe oferece coisas em troca de itens.')
            print('')
            time.sleep(0.5)
            for trocador in range(100):
                ng = 0
                hgg = 1
                gold = 0
                randoms = random.randint(0, 5)
                print(ola[randoms])
                for negociador in neg_local:
                    print(negociador)
                    time.sleep(0.4)
                print('Ouro:', money)
                pergunta = int(input('Escolha um item.'))
                print('')
                if pergunta == 7:
                    randoms = random.randint(0, 3)
                    print(adeus[randoms])
                    break
                elif pergunta < 7:
                    for test in range(100):
                        if pergunta == hgg:
                            print(txt_con[0], cp[gold], 'ouros.')
                            pergunta = input('Deseja Compra-lo? s ou n?')
                            if (pergunta == 's') and (money < gold):
                                print('Não tem o suficiente')
                                break
                            elif pergunta == 's':
                                itens[gold] = itens[gold] + 1
                                money = money - cp[gold]
                            elif pergunta == 'n':
                                print('ok')
                                break
                        else:
                            hgg = hgg + 1
                            gold = gold + 1
        elif valor == 7:
            print('Você vê um báu e decide se aproximar')
            time.sleep(0.5)
            mimico = random.randint(1, 2)
            if mimico < 2:
                print('Vê que é um báu velho de ouro')
            else:
                print('Vê que é um báu velho de ferro.')
            time.sleep(0.5)
            pergunta = input('Deseja Abri-lo? s ou n? ')
            print('')
            if pergunta == 'n':
                print('Você decide não abrir e continua em frente.')
            elif pergunta == 's':
                if mimico < 2:
                    print('Você ficou preso no baú vivo')
                    less_money = int(money * 0.2)
                    less_hp = int(hp_total * 0.2)
                    print('Baú - Se você me pagar o dobro de', less_money)
                    print('Eu não roubarei 20% de sua vida')
                    for lose_money in range(100):
                        pergunta = input('Pagar? s ou n?')
                        if pergunta == 'n':
                            money = money - less_money
                            hp_total = hp_total - less_hp
                            print('voce perdeu', less_money * 2, ' ouros e', less_hp * 2, 'de vida.')
                            break
                        elif (pergunta == 's') and money > 6:
                            money = money - less_money * 2
                            print('voce perdeu', less_money * 2, ' ouros.')
                            break
                        else:
                            print('você está vazio')
                else:
                    gold_box = random.randint(1, 100)
                    money = money + gold_box
                    print('Você achou', gold_box, 'ouros.')
        elif valor <= 5:
            val = 0
            power_ene = 0
            for monstros in range(100):
                if valor == val:
                    hp_enemie = power_ene + 20 * lvlup
                    xp_enemie = power_ene + 10 * lvlup
                    break
                else:
                    val = val + 1
                    power_ene = power_ene + 20

            doll_battle = 0
            luta = luta + 1
            hp_atual = hp_total + (skillhp * 10) + (10 * itens[0])
            mp_atual = mp_total + (skillmp * 10)

            print('monstro', luta)

            for sistema_de_batalha in range(100):
                for luta1_txt in range(1):
                    luta_txt = ['', mons_local[val], ('Vida do monstro:', hp_enemie), '', ('Vida:', hp_atual, '| Mana:', mp_atual, '| Level:', level,)]

                act_bar = '1.Ataque  2.Ataque Especial '
                act_bar2 = '3.Jogar Boneco '
                act_bar3 = '4.Fugir   :'
                tyclas = 1
                reg_player = hp_total * 0.01
                for loop in range(100):
                    if classe == tyclas:
                        sp_dmg = spdmg + (skillint * bonus_sp) + (itens[tyclas] * 10)
                        dmg_player = dmg + (skilldmg * bonus) + (itens[tyclas] * 10)
                        break
                    else:
                        tyclas = tyclas + 1

                if hp_atual <= 0:
                    break
                elif hp_enemie <= 0:
                    break
                elif (hp_atual >= 1) and (hp_enemie >= 1):
                    time.sleep(0.5)
                    txt = 0
                    for luta_info in luta_txt:
                        print(luta_info)
                    if itens[4] > 0:
                        print('A vida atual %s é %s' % (nome_boneco, doll_hp))
                        ataque = int(input('1.Ataque  2.Ataque Especial  3.Jogar Boneco  4.Fugir   :'))
                    else:
                        ataque = int(input('1.Ataque  2.Ataque Especial  4.Fugir   :'))
                    print('')

                    if (ataque == 3) and (itens[4] > 0):
                        print('você jogou o boneco')
                        itens[4] = itens[4] - 1
                        doll_battle = doll_battle + 1
                    elif (ataque == 3) and (itens[4] <= 0):
                        print('Você não tem boneco')
                    if ataque == 4:
                        EscapeChance = random.randint(1, 10)
                        if EscapeChance >= 4:
                            print('Você escapou')
                            fugiu = fugiu + 1
                            break
                        else:
                            print('Falhou!')
                    atk = 1
                    pk = [dmg_player, sp_dmg]
                    manapk = 0
                    atkV = 0
                    attackchance = random.randint(1, 25)
                    for loop_atk in range(2):
                        if ataque > 2:
                            break
                        elif (ataque == 2) and (mp_atual < 20):
                            print('Não tem mana o suficiente!')
                            break
                        elif ataque == atk:
                            if attackchance > 8 - accdmg:
                                hp_enemie = hp_enemie - pk[atkV]
                                mp_atual = mp_atual - manapk
                                print('dano causado', pk[atkV])
                                break
                            else:
                                print('Falha no ataque')
                                mp_atual = mp_atual - manapk
                                break
                        else:
                            atk = atk + 1
                            atkV = atkV + 1
                            manapk = 20

                    attackchance = random.randint(1, 10)
                    if (attackchance >= 8 - accdmg) and (hp_enemie > 0):  # monstros
                        enemie_dmg = random.randint(5, 10)
                        enemie_dmg = enemie_dmg * lvlup + (power_ene // 3)
                        if (doll_battle > 0) and (doll_hp > 0):
                            doll_hp = doll_hp - enemie_dmg
                            print(nome_boneco, 'recebeu o dano!')
                            if doll_hp <= 0:
                                print('Boneco', '(', nome_boneco, ')', 'morreu!')
                        else:
                            hp_atual = hp_atual - enemie_dmg
                            print('Dano Recebido!', enemie_dmg)
                    elif (attackchance <= 3) and (hp_enemie > 0):
                        print('O Monstro Errou!')
            if hp_enemie <= 0:
                time.sleep(1)
                m_e = random.randint(0, 6)
                print(morte_enemigo[m_e])
                money_random = random.randint(5, 30)
                money = money + money_random
                print('')
                print('Você obteve', money_random, 'ouros.')
                print('Xp Coletado:', exp, '| Xp Necessário para subir de level:', 20 * lvlup)
                print('Agora você tem %s ouros!' % money)
                print('')
                exp = exp + xp_enemie
                mortos = mortos + 1
                time.sleep(1)
            diag = input('Aperte "Enter" para continuar')

            for skillloop in range(100):
                if exp >= 20 * lvlup:
                    exp = exp - (20 * lvlup)
                    level, lvlup = level + 1, lvlup + 1
                    skillpoints = skillpoints + 3
                    time.sleep(1)
                    print('Você Subiu de Nivel!!')
                    print('+3 SkillPoints!')
                    time.sleep(1)
                else:
                    break
            if skillpoints > 0:
                for bug in range(100):
                    diag = input('Você tem Skillpoints! Deseja gasta-los?(s) ou (n): ')
                    if diag == 'n':
                        time.sleep(0.5)
                        print('ok')
                        break
                    elif (diag == 's') and (skillpoints > 0):
                        for skills in range(skillpoints):
                            time.sleep(0.5)
                            print('')
                            print('Em qual delas você quer melhorá-las?')
                            print('skillpoints', skillpoints)
                            print('1.Dano', skilldmg)
                            print('2.Vida', skillhp)
                            print('3.Mana', skillmp)
                            print('4.Ataque Especial', skillint)
                            print('5.Precisão Do ataque', accdmg)
                            for bug in range(100):
                                diag = input('Numero da Habilidade:')
                                if diag == '1':
                                    skilldmg = skilldmg + 1
                                    skillpoints = skillpoints - 1
                                    break
                                elif diag == '2':
                                    skillhp = skillhp + 1
                                    skillpoints = skillpoints - 1
                                    break
                                elif diag == '3':
                                    skillmp = skillmp + 1
                                    skillpoints = skillpoints - 1
                                    break
                                elif diag == '4':
                                    skillint = skillint + 1
                                    skillpoints = skillpoints - 1
                                    break
                                elif diag == '5':
                                    accdmg += + 1
                                    skillpoints += - 1
                                    break
                                elif diag != '':
                                    print('Falha na escolha da habilidade.')
                        break
                    else:
                        print('Erro na escolha.')
        print('')
        pergunta_save = input('Opá, antes de continuar, deseja salvar? s ou n?')
        if pergunta_save == 's':
            savetest = open('save.py', "w")
            savetest.write("name = '%s'\r" % name)
            savetest.write("nome_boneco = '%s'\r" % nome_boneco)
            savetest.write("level = %d\r" % level)
            savetest.write("hp_total = %d\r" % hp_total)
            savetest.write("mp_total = %d\r" % mp_total)
            savetest.write("skillpoints = %d\r" % skillpoints)
            savetest.write("skilldmg = %d\r" % skilldmg)
            savetest.write("skillhp = %d\r" % skillhp)
            savetest.write("skillmp = %d\r" % skillmp)
            savetest.write("skillint = %d\r" % skillint)
            savetest.write("itens = [%d, %d, %d, %d, %d, %d]\r" % (itens[0], itens[1], itens[2], itens[3], itens[4], itens[5]))
            savetest.write("mortos = %d\r" % mortos)
            savetest.write("luta = %d\r" % luta)
            savetest.write("fugiu = %d\r" % fugiu)
            savetest.write("kms = %d\r" % kms)
            savetest.write("regiao_local = %d\r" % regiao_local)
            savetest.write("ty = %d\r" % ty)
            savetest.write("exp = %d\r" % exp)
            savetest.write("spdmg = %d\r" % spdmg)
            savetest.write("bonus_sp = %d\r" % bonus_sp)
            savetest.write("bonus = %d\r" % bonus)
            savetest.write("dmg = %d\r" % dmg)
            savetest.write("classe = %d\r" % classe)
            savetest.write("money = %d\r" % money)
            savetest.write("lvlup = %d\r" % lvlup)
            savetest.write("accdmg = %d\r" % accdmg)

            print('Estado Salvo')
            savetest.close()
        else:
            print('ok')

        time.sleep(1)
        print('Após a luta')
        time.sleep(1)
        print('')

time.sleep(1)
if hp_atual <= 0:
    print('Você morreu!')
print('Fim de jogo')
time.sleep(0.5)
print('Você derrotou:', mortos, 'monstros.')
time.sleep(0.5)
print('Voce fugiu de', fugiu, 'monstros.')
time.sleep(0.5)
print('Você chegou até o Level:', level)