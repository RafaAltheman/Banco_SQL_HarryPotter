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
    "Dragão de estimação (miniatura)"
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
resposta_aluno = supabase.table("alunos").select("nome", "pet", "casa").execute()
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