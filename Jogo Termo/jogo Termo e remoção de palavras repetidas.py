import random


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


dicionar = ['sagaz', 'negro', 'amago', 'exito', 'mexer', 'termo', 'senso', 'nobre', 'algoz', 'afeto', 'plena', 'etica', 'mutua',
            'sutil', 'tenue', 'vigor', 'aquem', 'audaz', 'porem', 'fazer', 'sanar', 'seçao', 'inato', 'assim', 'cerne', 'ideia',
            'desde', 'fosse', 'poder', 'moral', 'torpe', 'honra', 'muito', 'justo', 'anexo', 'futil', 'razao', 'quiça', 'etnia',
            'icone', 'sobre', 'tange', 'egide', 'lapso', 'mutuo', 'sonho', 'expor', 'haver', 'habil', 'amigo', 'tempo', 'pesar',
            'posse', 'avido', 'entao', 'boçal', 'ardil', 'coser', 'genro', 'corja', 'seara', 'dengo', 'prole', 'detem', 'causa',
            'dizer', 'tenaz', 'digno', 'dever', 'crivo', 'saber', 'obice', 'apice', 'ansia', 'brado', 'ceder', 'animo', 'gleba',
            'paria', 'graça', 'assaz', 'comum', 'atroz', 'culto', 'temor', 'sendo', 'mundo', 'censo', 'pauta', 'fugaz', 'denso',
            'cozer', 'valha', 'nenem', 'ainda', 'vicio', 'forte', 'reves', 'vulgo', 'estar', 'pudor', 'regra', 'dogma', 'louco',
            'banal', 'criar', 'pifio', 'impor', 'tenro', 'desse', 'apraz', 'jeito', 'reaça', 'ordem', 'round', 'atras', 'pedir',
            'saude', 'clava', 'viril', 'merce', 'usura', 'manso', 'juizo', 'sabio', 'ontem', 'servo', 'prosa', 'feliz', 'presa',
            'coisa', 'afago', 'fluir', 'falar', 'ebrio', 'cunho', 'forma', 'devir', 'meiga', 'vendo', 'serio', 'plato', 'guisa',
            'pleno', 'visar', 'temer', 'mesmo', 'cisma', 'limbo', 'bruma', 'magoa', 'acaso', 'puder', 'heroi', 'exodo', 'gerar',
            'obvio', 'afins', 'obter', 'valor', 'lugar', 'impio', 'matiz', 'praxe', 'crise', 'senil', 'havia', 'venia', 'certo',
            'fluxo', 'enfim', 'alibi', 'tedio', 'ritmo', 'posso', 'garbo', 'tomar', 'reter', 'pulha', 'parvo', 'uniao', 'valia',
            'grato', 'todos', 'vital', 'visao', 'favor', 'abrir', 'vivaz', 'laico', 'bravo', 'parco', 'prumo', 'facil', 'ameno',
            'genio', 'reles', 'obito', 'falso', 'possa', 'olhar', 'prime', 'levar', 'tecer', 'burro', 'selar', 'anelo', 'casta',
            'fator', 'citar', 'rogar', 'adiar', 'farsa', 'façam', 'ranço', 'achar', 'coeso', 'noçao', 'cisao', 'epico', 'legal',
            'cabal', 'morte', 'imune', 'sabia', 'sinto', 'nicho', 'fardo', 'falta', 'exato', 'ativo', 'gente', 'lavra', 'amplo',
            'força', 'ouvir', 'viver', 'brega', 'gesto', 'labor', 'dubio', 'revel', 'cesta', 'sonso', 'sesta', 'sulco', 'deter',
            'passo', 'leigo', 'tendo', 'unico', 'arduo', 'vemos', 'atuar', 'feixe', 'otica', 'rever', 'calma', 'ciume', 'igual',
            'toada', 'humor', 'debil', 'tende', 'sonsa', 'ideal', 'hiato', 'vacuo', 'pobre', 'ponto', 'ambos', 'claro', 'terno',
            'velho', 'remir', 'fusao', 'probo', 'outro', 'leito', 'senao', 'advem', 'doido', 'horda', 'carma', 'linda', 'marco',
            'jovem', 'inata', 'xeque', 'capaz', 'fonte', 'relva', 'ajuda', 'tenra', 'algum', 'caçar', 'velar', 'anuir', 'ficar',
            'noite', 'apoio', 'dorso', 'vimos', 'rigor', 'farao', 'serie', 'verso', 'botar', 'vazio', 'tanto', 'lider', 'prece',
            'cruel', 'terra', 'morar', 'ambas', 'moçao', 'frase', 'virus', 'peste', 'massa', 'entre', 'casto', 'coçar', 'pouco',
            'covil', 'coesa', 'fauna', 'faina', 'signo', 'sente', 'preso', 'furor', 'credo', 'docil', 'feito', 'lazer', 'minha',
            'vetor', 'arido', 'flora', 'raiva', 'aceso', 'ciclo', 'impar', 'maior', 'chata', 'torço', 'beata', 'vulto', 'brisa',
            'houve', 'trama', 'breve', 'papel', 'vasto', 'liame', 'setor', 'adeus', 'pegar', 'manha', 'salvo', 'senda', 'ardor',
            'seita', 'banzo', 'morro', 'pecha', 'atomo', 'prado', 'visse', 'reger', 'antro', 'blase', 'avaro', 'segue', 'livro',
            'nossa', 'ancia', 'comer', 'ocaso', 'plano', 'peixe', 'rezar', 'aureo', 'saiba', 'otimo', 'saida', 'alias', 'meses',
            'acima', 'sorte', 'chulo', 'junto', 'nunca', 'fitar', 'chuva', 'opçao', 'jazia', 'serao', 'mudar', 'fruir', 'pajem',
            'parar', 'bando', 'treta', 'fugir', 'motim', 'gerir', 'prazo', 'naçao', 'seria', 'carro', 'tosco', 'alude', 'leite',
            'sinha', 'norma', 'andar', 'epoca', 'grupo', 'brava', 'tenso', 'exame', 'arcar', 'rapaz', 'aviao', 'idolo', 'lenda',
            'venal', 'soldo', 'tirar', 'parte', 'virao', 'reino', 'campo', 'praga', 'malta', 'exijo', 'sumir', 'pompa', 'aonde',
            'logro', 'traga', 'vilao', 'fixar', 'preto', 'anais', 'voraz', 'corpo', 'antes', 'quase', 'solto', 'cheio', 'turva',
            'nodoa', 'agora', 'certa', 'copia', 'oasis', 'turba', 'alado', 'risco', 'apego', 'parva', 'filho', 'messe', 'indio',
            'grave', 'caixa', 'praia', 'estao', 'acesa', 'prova', 'verve', 'apelo', 'nivel', 'pardo', 'psico', 'texto', 'fenda',
            'ligar', 'trupe', 'retem', 'tocar', 'atrio', 'viria', 'lindo', 'dessa', 'alçar', 'ficha', 'navio', 'opaco', 'livre',
            'aurea', 'astro', 'supra', 'fraco', 'etico', 'afora', 'verba', 'faixa', 'elite', 'cioso', 'glosa', 'parca', 'conta',
            'autor', 'lidar', 'mente', 'firme', 'grata', 'tinha', 'verbo', 'calda', 'bater', 'prive', 'fatal', 'fatos', 'cousa',
            'oxala', 'reses', 'magia', 'junco', 'jirau', 'molho', 'irmao', 'turvo', 'macio', 'douto', 'deixa', 'torso', 'pagao',
            'salve', 'abriu', 'supor', 'pique', 'igneo', 'atual', 'asilo', 'light', 'rouca', 'festa', 'orfao', 'posto', 'caber',
            'extra', 'curso', 'besta', 'locus', 'ruina', 'sexta', 'judeu', 'paira', 'zelar', 'vezes', 'ereto', 'desta', 'finda',
            'sarça', 'video', 'radio', 'bioma', 'combo', 'feudo', 'agudo', 'tetra', 'facto', 'culpa', 'vinha', 'porta', 'menos',
            'urgia', 'vosso', 'longe', 'cutis', 'surja', 'advir', 'meigo', 'traço', 'bonus', 'autos', 'tento', 'super', 'sitio',
            'canon', 'cocho', 'drops', 'facho', 'rumor', 'museu', 'pilar', 'suave', 'clean', 'lasso', 'geral', 'amena', 'acola',
            'optar', 'medir', 'penta', 'turma', 'boato', 'pifia', 'açoes', 'chama', 'mosto', 'rubro', 'crime', 'letal', 'louça',
            'pacto', 'podio', 'ponha', 'lapis', 'cover', 'local', 'folga', 'nosso', 'cacho', 'hobby', 'hoste', 'aroma', 'vigia',
            'vetar', 'refem', 'finjo', 'drama', 'fazia', 'pasmo', 'açude', 'brabo', 'feroz', 'axila', 'rival', 'troça', 'movel',
            'mesma', 'monte', 'poema', 'golpe', 'ecoar', 'lesse', 'metie', 'riste', 'avida', 'plebe', 'forum', 'sucia', 'daqui',
            'liçao', 'pareo', 'coral', 'teste', 'forem', 'monge', 'aluno', 'clima', 'viram', 'carta', 'ebano', 'escol', 'macro',
            'poeta', 'venha', 'falha', 'legua', 'chato', 'sarau', 'farta', 'briga', 'cargo', 'cetro', 'atimo', 'ateia', 'passa',
            'fruto', 'tacha', 'perco', 'conto', 'plaga', 'calmo', 'idoso', 'plumo', 'busca', 'virar', 'piada', 'vento', 'roupa',
            'tarde', 'assar', 'chefe', 'arado', 'tribo', 'aviso', 'verde', 'surto', 'recem', 'grama', 'catre', 'seixo', 'traje',
            'impia', 'civil', 'ornar', 'deste', 'bruta', 'deram', 'saldo', 'arfar', 'fosso', 'vedar', 'trato', 'depor', 'troca',
            'beijo', 'nuvem', 'tiçao', 'corso', 'irado', 'porte', 'pasma', 'grota', 'canso', 'pedra', 'ambar', 'uteis', 'silvo',
            'cifra', 'bazar', 'gabar', 'regio', 'julia', 'segar', 'giria', 'vazao', 'casar', 'amado', 'pavor', 'tutor', 'laudo',
            'sosia', 'bruto', 'tiver', 'bença', 'troco', 'magna', 'perto', 'rural', 'vagar', 'molde', 'lesto', 'midia', 'tchau',
            'itens', 'unica', 'minar', 'nesse', 'artur', 'renda', 'odiar', 'manga', 'vadio', 'meche', 'fossa', 'sotao', 'clero',
            'jejum', 'inter', 'berro', 'feita', 'aviar', 'paiol', 'ileso', 'negar', 'largo', 'pomar', 'cinto', 'orgao', 'cenho',
            'lesao', 'pugna', 'canto', 'horto', 'visto', 'rocha', 'amiga', 'ruido', 'podar', 'pinho', 'inves', 'urdir', 'proto',
            'civel', 'bolsa', 'marca', 'ufano', 'vista', 'frota', 'mocho', 'vasta', 'densa', 'dubia', 'bulir', 'penso', 'piche',
            'umido', 'peita', 'jogar', 'culta', 'morfo', 'xucro', 'esgar', 'resto', 'mamae', 'cheia', 'close', 'linha', 'fazes',
            'apear', 'ubere', 'chula', 'demao', 'misto', 'narco', 'findo', 'monta', 'natal', 'manto', 'campa', 'stand', 'amada',
            'barao', 'fundo', 'agape', 'chaga', 'simio', 'mover', 'retro', 'jazer', 'venho', 'album', 'tenha', 'nessa', 'preço',
            'punha', 'sigla', 'cerca', 'seiva', 'sabor', 'calça', 'alamo', 'cosmo', 'firma', 'matar', 'rente', 'banto', 'louro',
            'polis', 'ferpa', 'salva', 'tumba', 'ceita', 'miope', 'coevo', 'barro', 'arroz', 'torna', 'verao', 'velha', 'sinta',
            'redor', 'volta', 'solta', 'enjoo', 'ousar', 'bolso', 'etapa', 'santo', 'audio', 'trago', 'zumbi', 'lousa', 'fugiu',
            'corar', 'letra', 'nesta', 'obtem', 'lutar', 'final', 'queda', 'cacto', 'mimar', 'baixa', 'troço', 'farol', 'reler',
            'fatuo', 'penca', 'veloz', 'vario', 'quite', 'nacar', 'longo', 'vazia', 'neste', 'burra', 'coroa', 'folha', 'mania',
            'farto', 'sugar', 'forro', 'staff', 'puido', 'refil', 'bedel', 'dança', 'justa', 'ultra', 'repor', 'viger', 'lucro',
            'subir', 'logos', 'passe', 'urgir', 'custo', 'sadio', 'chave', 'hifen', 'sexto', 'gueto', 'mimos', 'valer', 'mouro',
            'usual', 'socio', 'lento', 'cardo', 'salmo', 'versa', 'calor', 'desça', 'labil', 'redea', 'salto', 'corte', 'corta',
            'ferro', 'porra', 'corno', 'calvo', 'idola', 'morra', 'baixo', 'carne', 'diabo', 'trial', 'pular', 'morto', 'nasce',
            'adora', 'pisar', 'lesma', 'tinta', 'penis', 'minta', 'rugir', 'dorme', 'polir', 'poupa', 'polpa', 'roubo', 'rouba',
            'gospe', 'multa', 'corra', 'grego', 'trava', 'barra', 'braço', 'peido', 'corre', 'prima', 'porco', 'porto', 'polvo',
            'palmo', 'dente', 'adoro', 'fungo', 'praça', 'chega', 'tacar', 'balao', 'pavio', 'pavao', 'altar', 'caldo', 'chapa',
            'grilo', 'parto', 'panda', 'batao', 'torre', 'rosto', 'sento', 'balde', 'banco', 'funil', 'trevo', 'bomba', 'moeda',
            'ropao', 'corda', 'fruta', 'grana', 'forno', 'canta', 'briza', 'rodar', 'mosca', 'sauça', 'rosca', 'musgo', 'vidro',
            'areia', 'varal', 'canal', 'treze', 'cinco', 'circo', 'areal', 'pizza', 'testa', 'label', 'motor', 'treco', 'cauda',
            'tropa', 'perna', 'pinto', 'aguia', 'acido', 'errar', 'tumor', 'enfia', 'lente', 'duzia', 'dolar', 'droga', 'ecuar',
            'durma', 'dupla', 'mafia', 'duelo', 'duplo', 'durou', 'duque', 'dunas', 'torra', 'doida', 'golfe', 'dopar', 'dopam',
            'dopei', 'donos', 'domem', 'domar', 'domam', 'domei', 'cagar', 'docas', 'trema', 'ganso', 'disco', 'falou', 'bruxa',
            'devem', 'devei', 'deusa', 'vinho', 'delta', 'bloco', 'dedao', 'desce', 'dardo', 'fecha', 'fecho', 'danar', 'colon',
            'prego', 'chute', 'cesio', 'cesar', 'cilio', 'prata', 'cobre', 'cuspo', 'galho', 'cuspi', 'limão', 'curvo', 'corvo',
            'curva', 'curto', 'curti', 'gosma', 'curou', 'curar', 'curei', 'greve', 'cupom', 'cupim', 'prato', 'culpo', 'cuido',
            'cuida', 'cueca', 'colhe', 'tiara', 'cruza', 'croma', 'gnomo', 'creme', 'email', 'girar', 'criei', 'grita', 'krita',
            'grifo', 'grito', 'coito', 'polar', 'colar', 'colam', 'creio', 'coice', 'creia', 'torta', 'foice', 'cravo', 'coçei',
            'peira', 'bunda', 'cocha', 'freio', 'couro', 'marte', 'venus', 'putao', 'couve', 'coube', 'costa', 'manta', 'corto',
            'corri', 'raspa', 'broxa', 'emulo', 'emula', 'esimo', 'esima', 'ereis', 'epica', 'calha', 'calho', 'calhe', 'cales',
            'calem', 'calei', 'calca', 'calco', 'calce', 'calas', 'calar', 'calam', 'calai', 'caira', 'caiou', 'caies', 'caiem',
            'caiei', 'caido', 'caibo', 'caiba', 'caias', 'caiar', 'caiam', 'caiai', 'cague', 'cagou', 'cagas', 'cagam', 'cagai',
            'cafes', 'cacos', 'caces', 'cacem', 'cacei', 'cacas', 'cabra', 'cabos', 'cabia', 'cabes', 'cabem', 'cabei', 'buzio',
            'boers', 'boies', 'boiem', 'boias', 'boiam', 'bilis', 'bario', 'buxos', 'busto', 'busco', 'burla', 'burlo', 'burle',
            'burgo', 'bundo', 'bunde', 'bumbo', 'buliu', 'bulis', 'bulia', 'bules', 'bulbo', 'bulas', 'bulam', 'bujao', 'bufao',
            'bufou', 'bufes', 'bufem', 'bufei', 'bufas', 'bufar', 'bufam', 'bufai', 'bueno', 'bucho', 'bucha', 'bucal', 'bruxo',
            'brota', 'broto', 'brote', 'bromo', 'broca', 'broco', 'broas', 'brito', 'brita', 'brios', 'brins', 'brigo', 'brida',
            'breta', 'brejo', 'breca', 'breco', 'braça', 'brasa', 'brama', 'bramo', 'brami', 'brame', 'brada', 'brade', 'braba',
            'boxea', 'botao', 'botou', 'botes', 'botem', 'botei', 'botas', 'botam', 'botai', 'bosta', 'bossa', 'borra', 'borro',
            'borre', 'borda', 'bordo', 'borde', 'bones', 'bonde', 'bolao', 'bolou', 'bolos', 'bolha', 'boles', 'bolem', 'bolei',
            'boldo', 'bolas', 'bolar', 'bolam', 'bolai', 'boiou', 'boina', 'boiei', 'boiar', 'boiai', 'bodes', 'bodas', 'bocha',
            'bocas', 'bocal', 'bobos', 'bobea', 'bobas', 'boate', 'blusa', 'blefa', 'blefo', 'blefe', 'bisao', 'bispo', 'birra',
            'bique', 'bingo', 'bigas', 'biela', 'bicou', 'bicos', 'bicho', 'bicha', 'bicas', 'bicar', 'bicam', 'bicai', 'berço',
            'berra', 'berre', 'beque', 'benze', 'benzo', 'benzi', 'benza', 'benta', 'bemol', 'belos', 'belga', 'belas', 'beiço',
            'beira', 'beiro', 'beire', 'beija', 'beije', 'becos', 'becas', 'bebes', 'bebia', 'bebeu', 'beber', 'bebem', 'bebei',
            'bebas', 'bebam', 'beato', 'baias', 'baços', 'bauru', 'batom', 'batia', 'bateu', 'bates', 'batem', 'batel', 'batei',
            'batas', 'batam', 'basta', 'basto', 'baste', 'basea', 'bases', 'barre', 'bares', 'bardo', 'barco', 'barca', 'barba',
            'baque', 'banjo', 'baniu', 'banis', 'banir', 'bania', 'banha', 'banho', 'banhe', 'banes', 'banem', 'banda', 'banca',
            'bambu', 'bambo', 'bamba', 'balsa', 'baliu', 'balis', 'balir', 'balia', 'balea', 'bales', 'balem', 'balas', 'balam',
            'baiao', 'baixe', 'baita', 'baila', 'bailo', 'baile', 'bagos', 'bagas', 'bafos', 'bacia', 'babao', 'babas', 'babou',
            'babes', 'babem', 'babei', 'babar', 'babam', 'babai', 'aereo', 'aerea', 'azula', 'azulo', 'azule', 'azuis', 'azoto',
            'azias', 'azeda', 'azedo', 'azede', 'azara', 'azaro', 'azare', 'axial', 'avens', 'aviva', 'avivo', 'avive', 'avisa',
            'avise', 'avira', 'aviou', 'avimo', 'avies', 'avier', 'aviem', 'aviei', 'avias', 'aviam', 'aviai', 'avela', 'aveio',
            'aveia', 'avara', 'avais', 'autua', 'autuo', 'autue', 'auras', 'aulas', 'atens', 'atura', 'aturo', 'ature', 'atuou',
            'atuns', 'atues', 'atuem', 'atuei', 'atuas', 'atuam', 'atuai', 'atriz', 'atrai', 'atola', 'atolo', 'atole', 'atlas',
            'atiça', 'atiço', 'ativa', 'ative', 'atira', 'atiro', 'atire', 'atina', 'atino', 'atine', 'atido', 'atice', 'ateve',
            'ateus', 'atera', 'ateou', 'atemo', 'ateis', 'ateio', 'ateie', 'ateei', 'atear', 'ateai', 'atava', 'atara', 'atamo',
            'atais', 'atado', 'atada', 'ataca', 'ataco', 'assoo', 'assoa', 'assou', 'assoe', 'assis', 'assea', 'asses', 'assem',
            'assei', 'assas', 'assam', 'assai', 'aspas', 'asnos', 'asila', 'asile', 'artes', 'arria', 'arrio', 'arrie', 'arrea',
            'arque', 'arpoo', 'arpao', 'arpoa', 'arpoe', 'armou', 'armes', 'armem', 'armei', 'armas', 'armar', 'armam', 'armai',
            'argui', 'arguo', 'argua', 'arfou', 'arfes', 'arfem', 'arfei', 'arfas', 'arfam', 'arfai', 'arena', 'aremo', 'areja',
            'arejo', 'areje', 'areis', 'ardis', 'ardia', 'ardeu', 'ardes', 'arder', 'ardem', 'ardei', 'ardas', 'ardam', 'arcou',
            'arcos', 'arcas', 'arcam', 'arcai', 'araça', 'arava', 'arara', 'aramo', 'arame', 'arais', 'arada', 'apoie', 'apoia',
            'apura', 'apuro', 'apure', 'aptos', 'aptas', 'apolo', 'apita', 'apito', 'apite', 'apeou', 'apena', 'apeno', 'apene',
            'apela', 'apele', 'apeio', 'apeie', 'apeia', 'apega', 'apeei', 'apeai', 'apara', 'aparo', 'apare', 'apaga', 'apago',
            'aorta', 'anoes', 'aneis', 'anzol', 'anuis', 'anuia', 'anula', 'anulo', 'anule', 'anuiu', 'anuem', 'anuas', 'anuam',
            'anual', 'antao', 'antas', 'anota', 'anoto', 'anote', 'anjos', 'anima', 'anime', 'angra', 'anglo', 'anexa', 'anexe',
            'anela', 'anele', 'andou', 'andor', 'andes', 'andem', 'andei', 'andas', 'andam', 'andai', 'ancas', 'ampla', 'amola',
            'amolo', 'amole', 'amima', 'amimo', 'amime', 'amido', 'ameça', 'amemo', 'ameis', 'ameia', 'ameba', 'amava', 'amara',
            'amaro', 'amamo', 'amais', 'alçou', 'alças', 'alçam', 'alçai', 'alvos', 'alvor', 'alves', 'alvas', 'aluna', 'aluga',
            'alugo', 'aludo', 'aludi', 'aluda', 'altos', 'altea', 'altas', 'aloes', 'aloja', 'alojo', 'aloje', 'aloca', 'aloco',
            'almas', 'alisa', 'aliso', 'alise', 'aliou', 'alija', 'alijo', 'alije', 'alies', 'aliem', 'aliei', 'aliar', 'aliam',
            'aliai', 'alhos', 'alhea', 'algas', 'alema', 'alega', 'alego', 'aldea', 'alces', 'alcem', 'alcei', 'alaga', 'alago',
            'alada', 'ajudo', 'ajude', 'ajamo', 'ajais', 'aguça', 'aguço', 'aguou', 'agues', 'aguem', 'aguei', 'aguda', 'aguce',
            'aguas', 'aguar', 'aguam', 'aguai', 'agita', 'agito', 'agite', 'agira', 'agimo', 'agido', 'agias', 'agiam', 'aftas',
            'afros', 'aforo', 'afore', 'afoga', 'afogo', 'afofa', 'afofo', 'afofe', 'afoba', 'afobo', 'afobe', 'aflui', 'afluo',
            'aflua', 'afixa', 'afixo', 'afixe', 'afiro', 'afira', 'afiou', 'afina', 'afino', 'afine', 'afies', 'afiem', 'afiei',
            'afias', 'afiar', 'afiam', 'afiai', 'afeta', 'afete', 'aferi', 'afere', 'afega', 'afana', 'afano', 'afane', 'afaga',
            'advim', 'adula', 'adulo', 'adule', 'aduba', 'adubo', 'adube', 'adoça', 'adoço', 'adota', 'adoto', 'adote', 'adore',
            'adoce', 'adita', 'adito', 'adite', 'adira', 'adiro', 'adiou', 'adimo', 'adies', 'adiem', 'adiei', 'adido', 'adida',
            'adias', 'adiam', 'adiai', 'aderi', 'adere', 'adega', 'adaga', 'acusa', 'acuso', 'acuse', 'acuou', 'acues', 'acuem',
            'acuei', 'acudo', 'acudi', 'acuda', 'acuas', 'acuar', 'acuam', 'acuai', 'acode', 'achou', 'aches', 'achem', 'achei',
            'achas', 'acham', 'achai', 'aceto', 'acena', 'aceno', 'acene', 'acata', 'acato', 'acate', 'acaba', 'acabo', 'acabe',
            'abusa', 'abuso', 'abuse', 'abste', 'abris', 'abril', 'abria', 'abreu', 'abres', 'abrem', 'abras', 'abram', 'abono',
            'aboli', 'abole', 'ablui', 'abluo', 'ablua', 'abeto', 'abate', 'abato', 'abati', 'abata', 'abana', 'abano', 'abane',
            'abala', 'abalo', 'abale', 'abafa', 'abafo', 'abafe', 'eguas', 'anodo', 'azimo', 'atono', 'atona', 'arida', 'arias',
            'areas', 'ardua', 'arabe', 'agios', 'ageis', 'agata', 'acida', 'acaro', 'abaco', 'érico', 'érica', 'épiro', 'éfeso',
            'édipo', 'ávila', 'átila', 'estas', 'estai', 'esses', 'essas', 'esqui', 'espia', 'espio', 'espie', 'escoo', 'escoa',
            'escoe', 'ervas', 'errou', 'erros', 'erres', 'errem', 'errei', 'erras', 'erram', 'errai', 'erodo', 'erodi', 'erode',
            'eroda', 'ermos', 'eriça', 'eriço', 'erijo', 'erija', 'erigi', 'erige', 'erice', 'ergue', 'ergui', 'ergas', 'ergam',
            'ereta', 'envia', 'envio', 'envie', 'entoo', 'entra', 'entro', 'entoa', 'entoe', 'entes', 'enoja', 'enojo', 'enoje',
            'enjoa', 'enjoe', 'enfio', 'enfie', 'enche', 'encho', 'enchi', 'encha', 'emule', 'emito', 'emiti', 'emite', 'emita',
            'emana', 'emano', 'emane', 'elmos', 'elixo', 'elixi', 'elixe', 'eleva', 'elevo', 'eleve', 'elejo', 'eleja', 'elege',
            'elegi', 'ejeta', 'ejeto', 'ejete', 'eixos', 'eiras', 'educa', 'educo', 'edita', 'edito', 'edema', 'ecoou', 'ecoes',
            'ecoem', 'ecoei', 'ecoas', 'ecoam', 'ecoai', 'dalia', 'dutos', 'duros', 'durmo', 'dures', 'durem', 'durei', 'duras',
            'durar', 'duram', 'durai', 'dunga', 'dumas', 'dueto', 'duela', 'duele', 'ducha', 'dubla', 'dublo', 'duble', 'duais',
            'drogo', 'drena', 'dreno', 'drene', 'draga', 'drago', 'doias', 'doiam', 'douta', 'doura', 'douro', 'doure', 'dotou',
            'dotes', 'dotem', 'dotei', 'dotas', 'dotar', 'dotam', 'dotai', 'dosou', 'doses', 'dosem', 'dosei', 'dosas', 'dosar',
            'dosam', 'dosai', 'dormi', 'dores', 'dopou', 'dopes', 'dopem', 'dopas', 'dopai', 'donde', 'donas', 'domou', 'domes',
            'domas', 'domai', 'doera', 'doemo', 'doeis', 'dobra', 'dobro', 'dobre', 'doava', 'doara', 'doamo', 'doais', 'doado',
            'doada', 'dizia', 'dizes', 'dizem', 'dizei', 'divas', 'ditou', 'ditos', 'dites', 'ditem', 'ditei', 'ditas', 'ditar',
            'ditam', 'ditai', 'dista', 'disto', 'diste', 'disso', 'disse', 'dispo', 'disca', 'dirao', 'diras', 'diria', 'direi',
            'dique', 'diodo', 'dilui', 'diluo', 'dilua', 'digna', 'digne', 'digas', 'digam', 'dieta', 'dicas', 'devia', 'deveu',
            'deves', 'devas', 'devam', 'desço', 'despi', 'despe', 'desci', 'dermo', 'deres', 'derem', 'deras', 'depoe', 'depos',
            'depus', 'demos', 'deles', 'delas', 'deixo', 'deixe', 'deita', 'deito', 'deite', 'deduz', 'dedos', 'dedal', 'decai',
            'davas', 'davam', 'datou', 'dates', 'datem', 'datei', 'datas', 'datar', 'datam', 'datai', 'darao', 'daras', 'daria',
            'dares', 'darem', 'darei', 'danço', 'dante', 'danou', 'danos', 'danes', 'danem', 'danei', 'dando', 'dance', 'danas',
            'danam', 'danai', 'damos', 'damas', 'dados', 'dadas', 'curia', 'codea', 'cirio', 'celia', 'capua', 'cuica', 'custa',
            'custe', 'cuspa', 'curve', 'curte', 'curta', 'cursa', 'curse', 'cures', 'curem', 'curas', 'curam', 'curai', 'cunha',
            'cunhe', 'cumes', 'culpe', 'cujus', 'cujos', 'cujas', 'cuide', 'cuias', 'cucos', 'cucas', 'cubro', 'cubra', 'cubos',
            'cubas', 'creem', 'cruzo', 'cruze', 'cruas', 'cromo', 'crome', 'criva', 'crive', 'criou', 'crina', 'cries', 'criem',
            'crido', 'crias', 'criam', 'criai', 'crera', 'crema', 'cremo', 'crede', 'crava', 'crave', 'coibo', 'coibe', 'coiba',
            'coçou', 'coças', 'coçam', 'coçai', 'cozia', 'cozeu', 'cozes', 'cozem', 'cozei', 'cozas', 'cozam', 'coxos', 'coxim',
            'coxas', 'covas', 'cotou', 'cotes', 'cotem', 'cotei', 'cotas', 'cotar', 'cotam', 'cotai', 'cospe', 'cosia', 'coseu',
            'coses', 'cosem', 'cosei', 'cosas', 'cosam', 'coroo', 'corça', 'corro', 'corou', 'coros', 'coroe', 'cores', 'corem',
            'corei', 'coras', 'coram', 'corai', 'copos', 'copio', 'copie', 'copas', 'conte', 'conga', 'cones', 'conde', 'compo',
            'comia', 'comeu', 'comes', 'comem', 'comei', 'comas', 'comam', 'colou', 'colho', 'colhi', 'colha', 'coles', 'colem',
            'colei', 'colas', 'colai', 'coifa', 'coibi', 'cofre', 'coeva', 'coemo', 'coeis', 'cocos', 'coces', 'cocem', 'cocei',
            'cocal', 'cobra', 'cobro', 'cobri', 'coaxa', 'coaxo', 'coaxe', 'coava', 'coara', 'coamo', 'coajo', 'coaja', 'coais',
            'coagi', 'coage', 'coado', 'coada', 'clube', 'cloro', 'clone', 'clips', 'clara', 'clama', 'clamo', 'clame', 'civis',
            'citou', 'cites', 'citem', 'citei', 'citas', 'citam', 'citai', 'cisne', 'cismo', 'cisme', 'cisca', 'cisco', 'cipos',
            'ciosa', 'cinza', 'cinta', 'cinjo', 'cinja', 'cingi', 'cinge', 'cindo', 'cindi', 'cinde', 'cinda', 'cifro', 'cifre',
            'cidra', 'chuta', 'chuto', 'chupa', 'chupo', 'chupe', 'choça', 'chove', 'chovo', 'chovi', 'chova', 'chora', 'choro',
            'chore', 'choca', 'choco', 'chiou', 'chies', 'chiem', 'chiei', 'chias', 'chiar', 'chiam', 'chiai', 'chego', 'chefa',
            'checa', 'checo', 'chamo', 'chame', 'chale', 'chago', 'cetim', 'cesto', 'cessa', 'cesso', 'cesse', 'cervo', 'cerra',
            'cerro', 'cerre', 'cerol', 'cerni', 'cerda', 'cerco', 'ceras', 'cento', 'cenas', 'celta', 'celas', 'ceifa', 'ceifo',
            'ceife', 'ceies', 'ceiem', 'ceias', 'ceiam', 'cegue', 'cegou', 'cegos', 'cegas', 'cegar', 'cegam', 'cegai', 'ceemo',
            'ceeis', 'cedro', 'cedia', 'cedeu', 'cedes', 'cedem', 'cedei', 'cedas', 'cedam', 'ceava', 'ceara', 'ceamo', 'ceais',
            'ceado', 'caimo', 'caida', 'caçoo', 'caçao', 'caçoa', 'caçou', 'caçoe', 'caças', 'caçam', 'caçai', 'cavou', 'cavia',
            'cavio', 'cavie', 'caves', 'cavem', 'cavei', 'cavas', 'cavar', 'cavam', 'cavai', 'cauto', 'cauta', 'causo', 'cause',
            'caule', 'catou', 'cates', 'catem', 'catei', 'catas', 'catar', 'catam', 'catai', 'cassa', 'casso', 'casse', 'caspa',
            'casou', 'casos', 'cases', 'casem', 'casei', 'casco', 'casca', 'casas', 'casam', 'casal', 'casai', 'carao', 'carpi',
            'carpe', 'carpa', 'caros', 'carmo', 'carga', 'caras', 'capuz', 'caput', 'capta', 'capto', 'capte', 'capou', 'capim',
            'capes', 'capem', 'capei', 'capas', 'capar', 'capam', 'capai', 'cante', 'cansa', 'canse', 'canos', 'canoa', 'canja',
            'aanga', 'canaa', 'canas', 'camas', 'calço', 'calva', 'calou', 'calos', 'abade', 'trico', 'venda', 'noivo', 'pasta',
            'pente', 'frita', 'frito', 'fusca', 'palma', 'coita', 'madre', 'forca', 'porca', 'vocal', 'foque', 'poker', 'mirar',
            'vasou', 'poste', 'facao', 'torno', 'lixar', 'nitro', 'hotel', 'motel', 'fique', 'ficou', 'fasto', 'vapor', 'tampa',
            'tampo', 'magra', 'ziper', 'zurra', 'zurro', 'zurre', 'zuniu', 'zunis', 'zunir', 'zunia', 'zunes', 'zunem', 'zunas',
            'zunam', 'zumbo', 'zaria', 'zumbe', 'zumba', 'zonzo', 'zonza', 'zonas', 'zomba', 'zombo', 'zombe', 'souza', 'kazuo',
            'zinco', 'zerou', 'zeros', 'zeres', 'zerem', 'zerei', 'zeras', 'zerar', 'zeram', 'zerai', 'zelou', 'zeles', 'zelem',
            'zelei', 'zelas', 'zelam', 'zelai', 'zebra', 'zarpa', 'zarpo', 'zarpe', 'zanza', 'zanzo', 'zanze', 'zanga', 'zango',
            'zagas', 'vozes', 'vieza', 'vazou', 'vazes', 'vazem', 'vazei', 'vazas', 'vazar', 'vazam', 'vazai', 'traze', 'sirzo',
            'sirza', 'serzi', 'serze', 'seduz', 'rezou', 'rezes', 'rezem', 'rezei', 'rezas', 'rezam', 'rezai', 'refiz', 'refez',
            'refaz', 'reduz', 'preza', 'prezo', 'preze', 'petiz', 'pazes', 'nudez', 'nozes', 'nariz', 'mudez', 'luziu', 'luzis',
            'luzir', 'luzia', 'luzes', 'luzem', 'luzas', 'luzam', 'juiza', 'jazeu', 'jazes', 'jazem', 'jazei', 'jazas', 'jazam',
            'induz', 'guizo', 'gozou', 'gozos', 'gozes', 'gozem', 'gozei', 'gozas', 'gozar', 'gozam', 'gozai', 'gonzo', 'gazua',
            'fuzis', 'fuzil', 'urgiu', 'fizer', 'fezes', 'feraz', 'fazem', 'fazei', 'verga', 'vagir', 'grafa', 'grafo', 'grafe',
            'grade', 'gorro', 'urgis', 'gorou', 'gores', 'gorem', 'gorei', 'gordo', 'gorda', 'garoo', 'urges', 'urgem', 'ungir',
            'geram', 'gerai', 'gemer', 'gelar', 'geara', 'trigo', 'goras', 'gorar', 'goram', 'gorai', 'girou', 'giros', 'tigre',
            'surgi', 'surge', 'girai', 'gerou', 'germe', 'geriu', 'geris', 'garoa', 'sogro', 'sogra', 'sagra', 'sagro', 'gires',
            'girem', 'girei', 'giras', 'giram', 'garça', 'sagre', 'regua', 'geria', 'geres', 'gerem', 'gerei', 'geras', 'regia',
            'rusga', 'rugue', 'rugou', 'garra', 'garoe', 'garis', 'garfa', 'garfo', 'garfe', 'rugiu', 'rugis', 'rugia', 'ganir',
            'frigi', 'frige', 'ruges', 'rugem', 'rugas', 'rugar', 'fraga', 'rugam', 'rugai', 'rogue', 'rogou', 'rogos', 'rogas',
            'rogam', 'rogai', 'regue', 'regro', 'regre', 'regou', 'jorge', 'edgar', 'regeu', 'reges', 'braga', 'argos', 'argel',
            'regem', 'regei', 'regas', 'regar', 'gravo', 'grava', 'graus', 'grite', 'regam', 'regai', 'reagi', 'reage', 'graxo',
            'graxa', 'grudo', 'grude', 'gruda', 'rasga', 'rasgo', 'range', 'grifa', 'grega', 'graos', 'gruta', 'rangi', 'purga',
            'purgo', 'grila', 'grife', 'guris', 'guria', 'prega', 'gripe', 'grile', 'larga', 'lagar', 'pagar', 'orgia', 'guiar',
            'migra', 'magro', 'negra', 'mugir', 'logre', 'logra', 'legar', 'migro', 'migre', 'rufai', 'mofar', 'glifo', 'safar',
            'fuçar', 'orfas', 'trufa', 'sofre', 'sofro', 'sofri', 'sofra', 'safra', 'rufou', 'rufes', 'rufem', 'rufei', 'rufas',
            'rufar', 'rufam', 'rifou', 'rifle', 'rifes', 'rifem', 'rifei', 'rifas', 'rifar', 'rifam', 'rifai', 'pifar', 'infra',
            'furia', 'femur', 'feria', 'furao', 'furta', 'furto', 'furte', 'furou', 'furos', 'furna', 'fures', 'furem', 'furei',
            'furas', 'furar', 'furam', 'furai', 'fumar', 'fujir', 'fruis', 'fruia', 'fruiu', 'fruem', 'fruas', 'fruam', 'frite',
            'frisa', 'friso', 'frise', 'frios', 'frijo', 'frija', 'frias', 'frevo', 'freta', 'freto', 'frete', 'fresa', 'freso',
            'frese', 'freou', 'fremi', 'freme', 'freie', 'freia', 'freei', 'frear', 'freai', 'frade', 'fraca', 'forço', 'forra',
            'forre', 'foros', 'formo', 'forme', 'forja', 'forjo', 'forje', 'fores', 'force', 'foras', 'foram', 'focar', 'flori',
            'firmo', 'firas', 'firam', 'filar', 'fibra', 'fiara', 'ferve', 'fervo', 'fervi', 'ferva', 'ferra', 'ferre', 'feriu',
            'feris', 'ferir', 'feres', 'ferem', 'feras', 'feira', 'fedor', 'feder', 'febre', 'faras', 'farte', 'farra', 'farpa',
            'faros', 'faria', 'farei', 'farda', 'falir', 'chile', 'chico', 'chica', 'bahia', 'china', 'valho', 'unhas', 'tolhe',
            'tolho', 'tolhi', 'tolha', 'tocha', 'tenho', 'telha', 'talha', 'talho', 'talhe', 'tacho', 'tache', 'sonha', 'sonhe',
            'senha', 'sanha', 'rolha', 'ralha', 'ralho', 'ralhe', 'racha', 'racho', 'rache', 'punho', 'ponho', 'pinha', 'pilha',
            'pilho', 'pilhe', 'picha', 'picho', 'palha', 'olhou', 'olhos', 'olhes', 'olhem', 'olhei', 'olhas', 'olham', 'olhai',
            'ninho', 'molha', 'molhe', 'milho', 'milha', 'mecha', 'malha', 'malho', 'malhe', 'macho', 'linho', 'lhama', 'lenho',
            'lenha', 'junho', 'julho', 'incha', 'incho', 'inche', 'ilhou', 'ilhes', 'ilhem', 'ilhei', 'ilhas', 'ilhar', 'ilham',
            'ilhai', 'humus', 'himen', 'helio', 'hurra', 'hunos', 'hulha', 'horta', 'horas', 'honro', 'honre', 'homem', 'hinos',
            'hindu', 'hiena', 'herda', 'herdo', 'herde', 'heras', 'havei', 'hauri', 'haure', 'haste', 'harem', 'harpa', 'haras',
            'halos', 'hajas', 'hajam', 'ganha', 'ganho', 'ganhe', 'filha', 'ficho', 'fiche', 'feche', 'falho', 'falhe', 'wuhan',
            'hegel', 'haiti', 'delhi', 'dhaka', 'jogou', 'preve', 'pulga', 'tenta', 'lirio', 'merda', 'bacon', 'peito',
            'durex', 'ponta', 'ponte', 'pinta', 'sinal', 'garsa', 'salsa', 'pousa', 'pausa', 'pasto', 'treva', 'piano', 'picar'
            'exata', 'padre', 'trepa', 'apicu', 'afims', 'amita']


start = '\t(_ _ _ _ _)'
palavras = []

for k in dicionar:
    k = k.lower()
    if k not in palavras:
        palavras += [k]


print(colored(255, 0, 0, f'\nExiste {len(dicionar) - len(palavras)} palavras repetidas'))
print(f'mas elas não afetaram emi nada no jogo!\nExiste {len(palavras)} atualmente\n')
print(colored(0, 255, 100, '|---------Certo----------|'))
print(colored(255, 255, 0, '|Existe, mas lugar errado|'))
print(colored(200, 0, 200, '|-------Não Existe-------|\n'))

# escolhido = palavras[random.randint(0, len(palavras) - 1)]



special = ['á', 'à', 'â', 'ã', 'ä', 'é', 'è', 'ê', 'ë', 'í', 'ì', 'î', 'ï', 'ô', 'õ', 'ó', 'ò', 'ö', 'ú', 'ù', 'û', 'ü']
mode = ['solo()', 'dueto()', 'quarteto()', 'sair()']


def solo():
    escolhido = palavras[random.randint(0, len(palavras) - 1)]
    letras = []
    for letra in escolhido:
        letras += letra
    letras_c = []
    palavra_c = ''
    letras_falsa = ''
    letras_falsa_fix = []
    chance = 6

    while chance > 0:
        if palavra_c:
            print(f'\t({palavra_c})\n')
            print(f'Letras inexistentes:\n {letras_falsa}')
        else:
            print(start)

        while True:
            print(f'Você tem {chance} chances')
            chute = input('Digite uma palavra:')
            chute = chute.lower()
            letras_c = []
            for letra in chute:
                letras_c += letra
                letras_cc = letras_c

            for loop in range(len(letras_cc)):
                if letras_cc[loop] in special:
                    xyz = special.index(letras_cc[loop])
                    if xyz < 5:
                        letras_cc[loop] = 'a'
                    elif xyz < 9:
                        letras_cc[loop] = 'e'
                    elif xyz < 13:
                        letras_cc[loop] = 'i'
                    elif xyz < 18:
                        letras_cc[loop] = 'o'
                    else:
                        letras_cc[loop] = 'u'

            if chute in palavras:
                palavra_c = ''
                for loop in range(5):
                    if letras_cc[loop] == letras[loop]:
                        palavra_c += f'{colored(0, 255, 100, letras_c[loop])}'
                    elif letras_c[loop] in letras:
                        palavra_c += f'{colored(255, 255, 0, letras_c[loop])}'
                    else:
                        palavra_c += f'{colored(200, 0, 200, letras_c[loop])}'
                        if letras_c[loop] not in letras_falsa_fix:
                            letras_falsa += f'{colored(255, 65, 0, f"{letras_c[loop]},")}'
                            letras_falsa_fix += letras_c[loop]
                break

        if chute == escolhido:
            print('ACERTOU')
            print(palavra_c)
            break
        else:
            print('Errado!')
            chance -= 1

    if chance == 0:
        print('Você perdeu')
        print(f'A palavra era "{colored(255, 0, 0, escolhido)}"')


def dueto():
    letras = []
    letras_c = []
    palavra_c = ''
    letras_falsa = ''
    letras_falsa_fix = []
    chance = 10
    escolhido = []
    for loop in range(2):
        escolhido += [palavras[random.randint(0, len(palavras) - 1)]]
    print(escolhido)

    while chance > 0:
        if palavra_c:
            print(f'\t({palavra_c})\n')
            print(f'Letras inexistentes:\n {letras_falsa}')
        else:
            print(start)


def quarteto():
    letras = []
    letras_c = []
    palavra_c = ''
    letras_falsa = ''
    letras_falsa_fix = []
    chance = 12
    escolhido = []
    for loop in range(4):
        escolhido += [palavras[random.randint(0, len(palavras) - 1)]]
    print(escolhido)

    while chance > 0:
        if palavra_c:
            print(f'\t({palavra_c})\n')
            print(f'Letras inexistentes:\n {letras_falsa}')
        else:
            print(start)


def sair():
    desejo = input('Deseja ver a lista sem palavras repetidas? s ou n?')
    if desejo.lower() == 's':
        print(palavras)
    else:
        print('Espero que tenha se divertido!')


stop = 1
while stop == 1:
    modo = input('\t\t\tModos:\n(1)solo (2)dueto (3)quarteto (4)sair\nEscolha: ')
    for selecao in range(5):
        if modo == f'{selecao}':
            if modo == '4':
                stop = 0
            exec(mode[selecao - 1])
