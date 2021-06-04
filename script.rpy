define jogador = Character("Maria", image="mariaDialogo")
define Luana = Character("Luana", image="luanaDialogo")
define Joao = Character("João", image="joaoDialogo")


image side joaoDialogo = "joao.png"
image side luanaDialogo = "luana.png"
image side mariaDialogo = "maria.png"

image person = "outraminazinha1-1.png"
image person2 = "outraminazinha1-2.png"

image bgPark = "praça.jpeg"
image bgStart = "bgPark.jpg"
image bgQuarto = "quarto.jpeg"
image bgRua = "ruasnoite.jpg"
image joaoImage = "menino.png"
image luanaImage = "senhora.png"
image  casaAssombrada = "sala.jpeg"
image porao = "porao.png"
label start:

    scene bgStart
    with dissolve

    play music "audio/theme.mp3"
    show person
    "Olá! Tudo bem? Posso te chamar de Maria?"
    menu:
        "Sim":
            jump Cena_inicio
        "Não":
            "Não? Bom, vou te chamar de Maria mesmo assim, porque eu quero."
            jump Cena_inicio

label Cena_inicio:
    scene bgPark
    with fade
    hide person

    show person2
    with dissolve
    "Maria, seu irmão está brincando ali perto do lago e você veio aqui no parque para ficar de olho nele.
    Eu sei que você não queria, que suas provas da escola estão bem aí,
    você está nervosa e tudo mais, mas a vida é assim. Você só tem um irmão,
    irmãos são preciosos e ninguém quer perdê-los por aí, lembre-se disso. A! cuidado com os patos, eles bicam."
    "..."
    menu:
        "Ei espera":
            "Que?"
            menu:
                "Qual é o nome dele?":
                    "Ah,sim! É João"
                    jump Cena_patos
        "Gente, mas não tem ninguém perto do lago":
            jump Cena_patos
    return
label Cena_patos:
    scene bgStart
    with fade

    show joaoImage
    with dissolve
    jogador "João?"
    Joao "OI MANA! CORRE AQUI! Olha esse pato louco hahaha"
    menu:
        "Garoto, para com isso, pato é um animal selvagem":
            jump Cena_patos_parte_2
        "Onde ?":
            jump Cena_patos_parte_2
    return

label Cena_patos_parte_2:
    scene bgStart
    with fade

    hide joaoImage

    show luanaImage
    with dissolve

    Luana "Meninos, longe dos patos. As pessoas jogam todo tipo de resto nesse lago,
    esses patos moram nele e... Maria, minha filha, que cara é essa?"
    jogador "Sono, tia."

    Luana "Deus me livre, parece quebranto. Olha filha,
    tudo demais é veneno, estudar é bom, mas dormir é essencial. Vamos para casa? Vem Joã... JOÃO MIGUEL, AQUI AGORA!"
    jogador "Eita tia, calma"

    "..."

    hide luanaImage

    show joaoImage
    with dissolve
    Joao "Que?"
    jogador "Vamos embora, vem. Tia Lu tá nervosa"

    hide joaoImage

    show luanaImage
    with dissolve
    Luana "João Miguel, quem era aquele homem"
    jogador "...O que é isso que você tá mastigando, irmão?"

    hide luanaImage

    show joaoImage
    with dissolve
    Joao "É meu amigo, tia. A gente conversa sempre aqui no parque, o filho dele vem aqui também. Às vezes ele compra sorvete para gente"
    jogador "Xô pato, xô..."

    hide joaoImage

    show luanaImage
    with dissolve
    Luana "João, nós não conhecemos esse homem e nem o filho dele. Não faça essa cara,
    são desconhecidos sim, pra mim e pra sua mãe. É perigoso. Agora venham pra casa os dois, andem"
    jogador "Ok ok"
    jump Cena_casa
    return

label Cena_casa:
    scene bgQuarto
    with dissolve
    "..."
    menu:
        "Dormir":
            "Tic tac tic tac tic tac tic…"
            jump Cena_dormindo
        "Dormir profundamente roncando bem alto":
            "Tic tac tic tac tic tac tic…"
            jump Cena_dormindo
    return
label Cena_dormindo:
    scene bgQuarto
    with fade
    jogador "Eita, ainda é madrugada. Cadê o João?"
    "..."
    jogador "João?"
    "..."
    menu:
        "Irmão? Cadê você?":
            "João?..."
            jump Cena_na_rua
        "Volta pra cama João, se mamãe descobrir que você tá acordado a essa hora...":
            "João?..."
            jump Cena_na_rua
    return
label Cena_na_rua:
    scene bgRua
    with fade

    stop music
    jogador "irmão?"
    "Algo estranho está perto do João"
    jump Cena_no_park
    return
label Cena_no_park:
    play music "audio/escape.ogg"
    jogador "João?.. Ei! Solta o meu irmão!"
    "..."
    "Desespero..."
    "..."
    jogador "Larga o meu irmão, volta aqui!"
    jump Cena_casa_assombrada
    return

label Cena_casa_assombrada:
    scene bgRua
    with fade
    "Meu Deus, e agora!"
    "..."
    menu:
        "Correr pra falar com minha mãe":
            show joaoImage
            with fade
            Joao "Maria... sgnif sgnif"
            "O que ?"
            jump Cena_entrar_na_casa
        "Correr pra ligar pra polícia":
            show joaoImage
            with fade
            Joao "Maria... sgnif sgnif"
            jump Cena_entrar_na_casa
        "Entrar nessa casa macabra atrás do João":
            jogador "Arrombar o basculante do porão e pular pra dentro"
            jump Cena_entrar_na_casa
    return

label Cena_entrar_na_casa:
    scene casaAssombrada
    with fade

    stop music
    play sound "audio/casa_song.ogg"
    "..."

    jogador "Que lugar horrível"
    menu:
        "Tatear os móveis ":
            jogador "ECA! Um rato"
            menu:
                "Continuar tateando os móveis":
                    jogador "Que é isso?... Uma lanterna? Uma lanterna!! Amém... Sem pilha"
                    menu:
                        "Continuar tateando os móveis aqui":
                            jogador "Um alicate...quebrado"
                            menu:
                                "Continuar tateando os móveis aqui":
                                    jogador "Um taco de golfe?... Uma vela?"
                                    jump Cena_porao
                                "Continuar tateando os móveis ali":
                                    jogador "Pilha? Será? Ai meu Deus, pilha! Pega a lanterna, Maria!"
                                    jump Cena_porao
                        "Continuar tateando os móveis ali":
                            jogador "Pilha? Será? Ai meu Deus, pilha! Pega a lanterna, Maria!"
                            jump Cena_porao
                "Tatear as paredes":
                    jogador "Um taco de golfe?... Uma vela?"
                    jogador "Acho que tem mais algo aqui perto"
                    "..."
                    jogador "Pilha? Será? Ai meu Deus, pilha! Pega a lanterna, Maria!"
                    jump Cena_porao
        "Tatear as paredes":
            jogador "Um taco de golfe?... Uma vela?"
            jogador "Acho que tem mais algo aqui perto"
            "..."
            jogador "Pilha? Será? Ai meu Deus, pilha! Pega a lanterna, Maria!"
            jump Cena_porao
    return

label Cena_porao:
    scene porao
    with dissolve
    "...Ruídos"
    "Que som estranho é esse?"
    "...medo"
    play sound "audio/song_susto.ogg"
    "AAAAhhhhh"
    "..."
    "O que foi isso!!"
    "Onde está meu irmão ????"
    "...Continua"
    return
