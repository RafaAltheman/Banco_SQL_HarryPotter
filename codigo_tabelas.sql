CREATE TABLE IF NOT EXISTS quadribol
(
  nome text PRIMARY KEY,
  posicao_jogador text,
  jogadores int,
  FOREIGN KEY (jogadores) REFERENCES alunos(id)
);

CREATE TABLE IF NOT EXISTS casa
(
  id_casa serial PRIMARY KEY,
  nome text,
  pontos int,
  time_quadribol text,
  FOREIGN KEY (time_quadribol) REFERENCES quadribol(nome)
);

CREATE TABLE IF NOT EXISTS alunos
(
  id serial PRIMARY KEY,
  nome text,
  PET text,
  casa int,
  FOREIGN KEY (casa) REFERENCES casa(id_casa)
);

CREATE TABLE IF NOT EXISTS locais
(
  id serial PRIMARY KEY,
  nome text
);

CREATE TABLE IF NOT EXISTS materia
(
  id_materia serial PRIMARY KEY,
  nome text,
  local int,
  FOREIGN KEY (local) REFERENCES locais(id)
);

CREATE TABLE IF NOT EXISTS professores
(
  id serial PRIMARY KEY,
  nome text,
  representa int,
  FOREIGN KEY (representa) REFERENCES casa(id_casa)
);

CREATE TABLE IF NOT EXISTS leciona
(
  id_materia int,
  professor int,
  alunos int,
  FOREIGN KEY (id_materia) REFERENCES materia(id_materia),
  FOREIGN KEY (professor) REFERENCES professores(id),
  FOREIGN KEY (alunos) REFERENCES alunos(id)
);

CREATE TABLE IF NOT EXISTS eventos
(
  nome text PRIMARY KEY,
  hora text,
  local int,
  FOREIGN KEY (local) REFERENCES locais(id)
);

CREATE TABLE IF NOT EXISTS participa_evento
(
  professor int,
  aluno int,
  evento text,
  FOREIGN KEY (professor) REFERENCES professores(id),
  FOREIGN KEY (aluno) REFERENCES alunos(id),
  FOREIGN KEY (evento) REFERENCES eventos(nome)
);
