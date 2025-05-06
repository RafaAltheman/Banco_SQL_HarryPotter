CREATE TABLE IF NOT EXISTS casa (
  id_casa serial PRIMARY KEY,
  nome text,
  pontos int,
  time_quadribol text
);

CREATE TABLE IF NOT EXISTS alunos (
  id serial PRIMARY KEY,
  nome text,
  pet text,
  casa int,
  FOREIGN KEY (casa) REFERENCES casa(id_casa)
);

CREATE TABLE IF NOT EXISTS quadribol (
  nome text PRIMARY KEY,
  casa int,
  FOREIGN KEY (casa) REFERENCES casa(id_casa)
);

CREATE TABLE IF NOT EXISTS alunos_quadribol (
  id serial PRIMARY KEY,
  aluno_id int,
  time_nome text,
  posicao_jogador text,
  FOREIGN KEY (aluno_id) REFERENCES alunos(id),
  FOREIGN KEY (time_nome) REFERENCES quadribol(nome)
);

CREATE TABLE IF NOT EXISTS locais
(
  id serial PRIMARY KEY,
  nome text,
  descricao text
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

/*  QUERIES  */

/* 1. Mostrar as casas em ordem de pontuação */
/*
SELECT nome, pontos FROM casa
ORDER BY pontos
*/

/* 2. Listar os apanhadores de cada time de quadribol */
/*
SELECT aluno_id, posicao_jogador FROM alunos_quadribol
WHERE posicao_jogador = 'Apanhador'
*/

/* 3. Listar os eventos que ocorreram no Salão Principal, os professores e os alunos que participam  */
/*
SELECT e.nome AS evento, p.nome AS professor, a.nome AS aluno
FROM eventos e
JOIN locais l ON e.local = l.id
JOIN participa_evento pe ON pe.evento = e.nome
JOIN professores p ON pe.professor = p.id
JOIN alunos a ON pe.aluno = a.id
WHERE l.nome = 'Salão Principal';
*/

/*4. Alunos que têm o mesmo pet e jogam na mesma posição*/
SELECT n.nome AS alunos, pj.posicao_jogador AS alunos_quadribol
JOIN alunos n ON n.nome = posicao.posicao_jogador 
WHERE n.id IN (
  SELECT aluno_id FROM alunos_quadribol
);

  

/*5.  Professores que participaram dos mesmos eventos que seus alunos */

/* 6. Listar os alunos que não jogam quadribol e de qual casa eles são */
/*
SELECT a.nome AS alunos, c.nome AS casa
FROM alunos a
JOIN casa c ON a.casa = c.id_casa
WHERE a.id NOT IN (
  SELECT aluno_id FROM alunos_quadribol
);
*/
/* 7. Listar os professores que representam um casa e de qual casa eles são e os que não são representantes, substituir por 'nenhum' */
/* 8. Qual aluno teve qual materia em qual local */
/* 9. Aluno com mais participações em eventos e os nomes desses eventos */
/* 10. Mostrar a quantidade de alunos de cada casa e a quantidade de alunos de cada casa que jogam quadribol */
