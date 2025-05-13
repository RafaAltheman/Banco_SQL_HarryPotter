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
SELECT a.nome AS aluno, aq.posicao_jogador, aq.time_nome
FROM alunos_quadribol aq
JOIN alunos a ON aq.aluno_id = a.id
WHERE aq.posicao_jogador = 'Apanhador';
*/

/* 3. Listar os eventos que ocorreram no Salão Principal, os professores e os alunos que participam */
/*
SELECT 
  e.nome AS evento,
  p.nome AS professor,
  a.nome AS aluno
FROM eventos e
JOIN locais l ON e.local = l.id
JOIN participa_evento pe ON pe.evento = e.nome
JOIN professores p ON pe.professor = p.id
JOIN alunos a ON pe.aluno = a.id
WHERE l.nome = 'Salão Principal';
*/

/* 4. Qual aluno teve qual materia em qual local */
/*
SELECT 
  a.nome AS aluno,
  m.nome AS materia,
  l.nome AS local
FROM leciona lec
JOIN alunos a ON lec.alunos = a.id
JOIN materia m ON lec.id_materia = m.id_materia
JOIN locais l ON m.local = l.id;
*/

/* 5. Alunos que têm o mesmo pet e jogam na mesma posição */
/*
SELECT 
  a1.nome AS aluno1,
  a2.nome AS aluno2,
  a1.pet,
  aq1.posicao_jogador
FROM alunos a1
JOIN alunos a2 ON a1.pet = a2.pet AND a1.id < a2.id
JOIN alunos_quadribol aq1 ON a1.id = aq1.aluno_id
JOIN alunos_quadribol aq2 ON a2.id = aq2.aluno_id
WHERE aq1.posicao_jogador = aq2.posicao_jogador;
*/

/* 6. Professores que participaram dos mesmos eventos que seus alunos */
/*
SELECT DISTINCT 
  prof.nome AS professor,
  al.nome AS aluno,
  ev.nome AS evento
FROM participa_evento pe
JOIN professores prof ON pe.professor = prof.id
JOIN alunos al ON pe.aluno = al.id
JOIN eventos ev ON pe.evento = ev.nome
JOIN leciona l ON l.professor = prof.id AND l.alunos = al.id
WHERE EXISTS (
  SELECT 1
  FROM participa_evento pe2
  WHERE pe2.professor = pe.professor 
    AND pe2.aluno = pe.aluno
    AND pe2.evento = pe.evento
);
*/

/* 7. Listar os alunos que não jogam quadribol e de qual casa eles são */
/*
SELECT
  a.nome AS alunos,
  c.nome AS casa
FROM alunos a
JOIN casa c ON a.casa = c.id_casa
WHERE a.id NOT IN (
  SELECT aluno_id FROM alunos_quadribol
);
*/

/* 8. Listar os professores que representam um casa e qual casa eles representam. Os que não são representantes, substituir por 'nenhum' */
/*
SELECT 
  p.nome AS professor,
  COALESCE(c.nome, 'nenhum') AS casa
FROM professores p 
LEFT JOIN casa c ON p.representa = c.id_casa;
*/

/* 9.Para cada casa, liste o aluno que mais participou de eventos, sua quantidade de participações e as matérias que ele teve, com o local dessas matérias */
/*
SELECT 
  c.nome AS casa,
  a.nome AS aluno,
  COUNT(pe.evento) AS participacoes,
  m.nome AS materia,
  l.nome AS local
FROM alunos a
JOIN casa c ON a.casa = c.id_casa
LEFT JOIN participa_evento pe ON pe.aluno = a.id
LEFT JOIN leciona lec ON lec.alunos = a.id
LEFT JOIN materia m ON lec.id_materia = m.id_materia
LEFT JOIN locais l ON m.local = l.id
GROUP BY c.nome, a.nome, m.nome, l.nome
ORDER BY c.nome, participacoes;
*/

/* 10. Mostrar a quantidade de alunos de cada casa e a quantidade de alunos de cada casa que jogam quadribol */
/*
SELECT 
  c.nome AS casa,
  COUNT(a.id) AS total_alunos,
  COUNT(aq.aluno_id) AS alunos_quadribol
FROM casa c
LEFT JOIN alunos a ON a.casa = c.id_casa
LEFT JOIN alunos_quadribol aq ON aq.aluno_id = a.id
GROUP BY c.nome;
*/
