import random
from supabase import create_client, Client

supabase_url = 'https://xoskahjpbroaqczrksvj.supabase.co'
supabase_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inhvc2thaGpwYnJvYXFjenJrc3ZqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDUzNjIzMDcsImV4cCI6MjA2MDkzODMwN30.cwL8rUkccYrxafczuaezVafP-h5j2F3H4CRAlOdxdzM'
supabase: Client = create_client(supabase_url, supabase_key)

casas=["Grifinória", "Corvinal", "Lufa-Lufa", "Sonserina"]
alunos = [
    # Grifinória
    "Harry Potter",
    "Hermione Granger",
    "Ron Weasley",
    "Neville Longbottom",
    "Ginny Weasley",
    "Parvati Patil",
    "Dean Thomas",
    "Seamus Finnigan",

    # Sonserina
    "Draco Malfoy",
    "Pansy Parkinson",
    "Blaise Zabini",
    "Theodore Nott",
    "Millicent Bulstrode",
    "Vincent Crabbe",
    "Gregory Goyle",
    "Daphne Greengrass",

    # Lufa-Lufa
    "Cedrico Diggory",
    "Nymphadora Tonks",
    "Hannah Abbott",
    "Ernie Macmillan",
    "Justin Finch-Fletchley",
    "Susan Bones",
    "Zacharias Smith",
    "Megan Jones",

    # Corvinal
    "Luna Lovegood",
    "Cho Chang",
    "Padma Patil",
    "Terry Boot",
    "Michael Corner",
    "Anthony Goldstein",
    "Roger Davies",
    "Marietta Edgecombe"
]
professores = [
    # Grifinória
    "Minerva McGonagall",
    "Rubeus Hagrid",
    "Remus Lupin",

    # Sonserina
    "Severus Snape",
    "Horace Slughorn",
    "Dolores Umbridge",

    # Lufa-Lufa
    "Pomona Sprout",
    "Silvanus Kettleburn",
    "Charity Burbage",

    # Corvinal
    "Filius Flitwick",
    "Aurora Sinistra",
    "Quirinus Quirrell"
]
pets_alunos = [
    "Coruja",      
    "Gato",        
    "Sapo",        
    "Rato",         
    "Fênix pequena",
    "Coruja-das-torres", 
    "Gato prateado", 
    "Coruja-das-neves", 
    "Dragão de estimação"
]
posicoes_jogador = [
    "Apanhador",     
    "Artilheiro",  
    "Batedor",       
    "Goleiro"   
]
locais = [
    "Salão Principal",
    "Sala Precisa",
    "Sala de Poções",
    "Sala de Transfiguração",
    "Sala de Defesa Contra as Artes das Trevas",
    "Biblioteca",
    "Salão Comunal da Grifinória",
    "Salão Comunal da Sonserina",
    "Salão Comunal da Corvinal",
    "Salão Comunal da Lufa-Lufa",
    "Escritório de Dumbledore",
    "Estufa de Herbologia",
    "Campo de Quadribol",
    "Enfermaria",
    "Banheiro dos Monitores",
    "Cozinha de Hogwarts",
    "Corredor do Terceiro Andar (proibido)",
    "Sala de Feitiços",
    "Torre de Astronomia",
    "MasMorras"
]
descricoes_lugares = [
    "Local das refeições, eventos e cerimônias com teto encantado.",
    "Aparece quando alguém precisa, muda conforme a necessidade mágica.",
    "Aula onde os alunos preparam poções com ingredientes perigosos.",
    "Onde aprendem a transformar objetos, pessoas e animais magicamente.",
    "Treinamento mágico para proteger contra maldições e criaturas perigosas.",
    "Repleta de livros mágicos, útil para estudos e pesquisas secretas.",
    "Aconchegante, com lareira e decoração vermelha, entrada por senha.",
    "Subterrâneo, com vista para o lago, cheio de tradição ambiciosa.",
    "Na torre, com enigmas para entrar e belas janelas arredondadas.",
    "Perto das cozinhas, acolhedor, cheio de plantas e conforto natural.",
    "Torre alta com escada espiral, repleta de instrumentos mágicos misteriosos.",
    "Contém plantas mágicas estudadas em aulas práticas com muito cuidado.",
    "Estádio com arquibancadas onde ocorrem emocionantes jogos estudantis voadores.",
    "Sala silenciosa onde Madame Pomfrey trata feridos e enfeitiçados.",
    "Luxuoso, com vitrais, banheira enorme e torneiras com espuma colorida.",
    "Elfos domésticos preparam refeições, escondida atrás de uma pintura.",
    "Esconde segredos perigosos e criaturas mágicas que guardam mistérios secretos.",
    "Sala usada para lançar feitiços, treinar habilidades e aprender encantamentos.",
    "Observatório alto usado para estudar estrelas, planetas e fenômenos astronômicos.",
    "Corredores frios e úmidos abaixo do castelo, escondem segredos sombrios."
]
materias = [
    "Herbologia",
    "Poções",
    "Transfiguração",
    "Defesa Contra as Artes das Trevas",
    "Feitiços"
]
professores = [
    "Minerva McGonagall",    
    "Severus Snape",          
    "Pomona Sprout",          
    "Filius Flitwick",        
    "Remus Lupin"           
]
eventos = [
    "Campeonato de Quadribol da Casa",
    "Treino do Time da Grifinória",
    "Festa de Vitória da Grifinória",
    "Planejamento da Armada de Dumbledore",
    "Celebração da Sonserina após o Torneio",
    "Reunião Secreta da Inquisidora",
    "Discussão sobre os Enigmas",
    "Estudo em Grupo da Corvinal",
    "Ritual de Amizade da Lufa-Lufa",
    "Celebração de Halloween da Lufa-Lufa",
    "Baile de Inverno",
    "Seleção das Casas pelo Chapéu Seletor",
    "Jantar de Boas-Vindas",
    "Anúncio do Torneio Tribruxo"
]
# Casas
resposta_casa = supabase.table("casa").select("id_casa","nome", "pontos", "time_quadribol").execute()
if len(resposta_casa.data) == 0:  # verificar se já existem casas no banco
    dados_casa = []
    for n in casas:
        pontos = random.randint(0, 500)
        time_quadribol = n
        dados_casa.append({"nome": n, "pontos": pontos, "time_quadribol": time_quadribol})
        print(n)

    supabase.table("casa").insert(dados_casa).execute()
    resposta_casa = supabase.table("casa").select("id_casa", "nome", "pontos", "time_quadribol").execute()
    print("Casas inseridas")

# Alunos
resposta_aluno = supabase.table("alunos").select("id","nome", "pet", "casa").execute()
if len(resposta_aluno.data) == 0:  # verificar se já existem alunos no banco
    dados_nome = []
    indice_aluno = 0 

    for n in casas:
        casa = resposta_casa.data[casas.index(n)]["id_casa"]
        print(f"Casa {n} → ID {casa}")
        for i in range(8):
            nome = alunos[indice_aluno]
            pets = random.choice(pets_alunos)
            dados_nome.append({"nome": nome, "pet": pets, "casa": casa})
            print(f"Inserindo: {nome}")
            indice_aluno += 1

    supabase.table("alunos").insert(dados_nome).execute()
    print("Alunos inseridos")

# Quadribol
resposta_quadribol = supabase.table("quadribol").select("nome", "casa").execute()
if len(resposta_quadribol.data) == 0: 
    dados_quadribol = []
    for n in casas:
        casa = resposta_casa.data[casas.index(n)]["nome"]
        casa_id = resposta_casa.data[casas.index(n)]["id_casa"]
        print(casa_id)
        dados_quadribol.append({"nome": casa, "casa": casa_id})

    supabase.table("quadribol").insert(dados_quadribol).execute()
    print("Times de quadribol inseridos")


# Alunos Quadribol
resposta_alunos_quadribol = supabase.table("alunos_quadribol").select("id","aluno_id","time_nome", "posicao_jogador").execute()
if len(resposta_alunos_quadribol.data) == 0: 
    dados_alunos_quadribol = []
    
    alunos_por_casa = {}
    for aluno in resposta_aluno.data:
        casa_id = aluno["casa"]
        if casa_id not in alunos_por_casa:
            alunos_por_casa[casa_id] = []
        alunos_por_casa[casa_id].append(aluno)

    for time in resposta_quadribol.data:
        casa_id = time["casa"]
        nome_time = time["nome"]

        if casa_id not in alunos_por_casa:
            continue 

        alunos_da_casa = alunos_por_casa[casa_id]
        contador = 0

        for aluno in alunos_da_casa:
            if contador >= 4:
                break

            posicao = random.choice(posicoes_jogador)
            dados_alunos_quadribol.append({
                "aluno_id": aluno["id"],
                "time_nome": nome_time,
                "posicao_jogador": posicao
            })
            contador += 1

    supabase.table("alunos_quadribol").insert(dados_alunos_quadribol).execute()
    print("Jogadores inseridos nos times de quadribol")
    
# Locais
resposta_locais = supabase.table("locais").select("id","nome","descricao").execute()
if len(resposta_locais.data) == 0: 
    dados_locais = []

    for i in range(len(locais)):
        nome = locais[i]
        descricao = descricoes_lugares[i]
        dados_locais.append({
            "nome": nome,
            "descricao": descricao
        })

    supabase.table("locais").insert(dados_locais).execute()
    print("Locais inseridos")

# Materias
resposta_materia = supabase.table("materia").select("id_materia","nome","local").execute()
if len(resposta_materia.data) == 0: 
    dados_materia = []
    
    resposta_locais = supabase.table("locais").select("id", "nome").execute()
    locais_no_banco = resposta_locais.data

    for local in locais_no_banco:
        nome_local = local["nome"]
        id_local = local["id"]

        if nome_local == "Sala de Feitiços":
            dados_materia.append({"nome": "Feitiços", "local": id_local})

        elif nome_local == "Estufa de Herbologia":
            dados_materia.append({"nome": "Herbologia", "local": id_local})

        elif nome_local == "Sala de Poções":
            dados_materia.append({"nome": "Poções", "local": id_local})

        elif nome_local == "Sala de Transfiguração":
            dados_materia.append({"nome": "Transfiguração", "local": id_local})

        elif nome_local == "Sala de Defesa Contra as Artes das Trevas":
            dados_materia.append({"nome": "Defesa Contra as Artes das Trevas", "local": id_local})

    supabase.table("materia").insert(dados_materia).execute()
    print("Matérias inseridas")
    
# Professores
resposta_professores = supabase.table("professores").select("id","nome","representa", "materia").execute()
if len(resposta_professores.data) == 0: 
    dados_professores = []

    casas_no_banco = resposta_casa.data
    materias_no_banco = resposta_materia.data

    for materia in materias_no_banco:
        nome_materia = materia["nome"]
        id_materia = materia["id_materia"]

        if nome_materia == "Transfiguração":
            for casa in casas_no_banco:
                if casa["nome"] == "Grifinória":
                    id_casa = casa["id_casa"]
                    dados_professores.append({
                        "nome": "Minerva McGonagall",
                        "representa": id_casa,
                        "materia": id_materia
                    })
                    break

        elif nome_materia == "Poções":
            for casa in casas_no_banco:
                if casa["nome"] == "Sonserina":
                    id_casa = casa["id_casa"]
                    dados_professores.append({
                        "nome": "Severus Snape",
                        "representa": id_casa,
                        "materia": id_materia
                    })
                    break

        elif nome_materia == "Herbologia":
            for casa in casas_no_banco:
                if casa["nome"] == "Lufa-Lufa":
                    id_casa = casa["id_casa"]
                    dados_professores.append({
                        "nome": "Pomona Sprout",
                        "representa": id_casa,
                        "materia": id_materia
                    })
                    break

        elif nome_materia == "Feitiços":
            for casa in casas_no_banco:
                if casa["nome"] == "Corvinal":
                    id_casa = casa["id_casa"]
                    dados_professores.append({
                        "nome": "Filius Flitwick",
                        "representa": id_casa,
                        "materia": id_materia
                    })
                    break

        elif nome_materia == "Defesa Contra as Artes das Trevas":
            dados_professores.append({
                "nome": "Remus Lupin",
                "representa": None,
                "materia": id_materia
            })

    supabase.table("professores").insert(dados_professores).execute()
    print("Professores inseridos")
    
# Leciona
resposta_leciona = supabase.table("leciona").select("id_materia", "professor", "alunos").execute()
if len(resposta_leciona.data) == 0: 
    dados_leciona = []
    
    professores_no_banco = resposta_professores.data
    alunos_no_banco = resposta_aluno.data
    ids_alunos = [aluno["id"] for aluno in alunos_no_banco]

    for prof in professores_no_banco:
        alunos_aleatorios = random.sample(ids_alunos, 10)

        for aluno_id in alunos_aleatorios:
            dados_leciona.append({
                "id_materia": prof["materia"],
                "professor": prof["id"],
                "alunos": aluno_id
            })

    supabase.table("leciona").insert(dados_leciona).execute()
    print("leciona inserido")

# Eventos
resposta_eventos = supabase.table("eventos").select("nome", "hora", "local").execute()
if len(resposta_eventos.data) == 0:
    dados_eventos = []

    locais_no_banco = resposta_locais.data

    for local in locais_no_banco:
        nome_local = local["nome"]
        id_local = local["id"]

        if nome_local == "Campo de Quadribol":
            dados_eventos.append({"nome": "Campeonato de Quadribol da Casa", "hora": "10:00", "local": id_local})
            dados_eventos.append({"nome": "Treino do Time da Grifinória", "hora": "15:00", "local": id_local})

        elif nome_local == "Salão Comunal da Grifinória":
            dados_eventos.append({"nome": "Festa de Vitória da Grifinória", "hora": "21:00", "local": id_local})
            dados_eventos.append({"nome": "Planejamento da Armada de Dumbledore", "hora": "18:00", "local": id_local})

        elif nome_local == "Salão Comunal da Sonserina":
            dados_eventos.append({"nome": "Celebração da Sonserina após o Torneio", "hora": "20:00", "local": id_local})
            dados_eventos.append({"nome": "Reunião Secreta da Inquisidora", "hora": "23:00", "local": id_local})

        elif nome_local == "Salão Comunal da Corvinal":
            dados_eventos.append({"nome": "Discussão sobre os Enigmas", "hora": "17:00", "local": id_local})
            dados_eventos.append({"nome": "Estudo em Grupo da Corvinal", "hora": "19:00", "local": id_local})

        elif nome_local == "Salão Comunal da Lufa-Lufa":
            dados_eventos.append({"nome": "Ritual de Amizade da Lufa-Lufa", "hora": "16:00", "local": id_local})
            dados_eventos.append({"nome": "Celebração de Halloween da Lufa-Lufa", "hora": "22:00", "local": id_local})
            
        elif nome_local == "Salão Principal":
            dados_eventos.append({"nome": "Baile de Inverno", "hora": "20:00", "local": id_local})
            dados_eventos.append({"nome": "Seleção das Casas pelo Chapéu Seletor", "hora": "19:00", "local": id_local})
            dados_eventos.append({"nome": "Jantar de Boas-Vindas", "hora": "18:00", "local": id_local})
            dados_eventos.append({"nome": "Anúncio do Torneio Tribruxo", "hora": "14:00", "local": id_local})

    supabase.table("eventos").insert(dados_eventos).execute()
    print("Eventos inseridos com sucesso")
    

# Participações em eventos
resposta_participa = supabase.table("participa_evento").select("professor", "aluno", "evento").execute()
if len(resposta_participa.data) == 0:
    dados_participa = []
    
    professores_no_banco = resposta_professores.data
    alunos_no_banco = resposta_aluno.data
    eventos_no_banco = resposta_eventos.data 

    for evento in eventos_no_banco:
        nome_evento = evento["nome"]

        prof = random.choice(professores_no_banco)
        alunos_aleatorios = random.sample(alunos_no_banco, 5)

        for aluno in alunos_aleatorios:
            dados_participa.append({
                "professor": prof["id"],
                "aluno": aluno["id"],
                "evento": nome_evento
            })

    supabase.table("participa_evento").insert(dados_participa).execute()
    print("Participações em eventos inseridas")
