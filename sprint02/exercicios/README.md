## Exercício 1

 Exportar o resultado da query que obtém os 10 livros mais caros para um arquivo CSV
Utilizar a ; como separador
Respeitar a sequência de colunasPágina com os exercícios da sprint 02
```
SELECT 
	livro.cod AS CodLivro,
	livro.titulo AS "Título",
	autor.codautor AS CodAutor, 
	autor.nome AS Nome, 
	livro.valor AS Valor, 
	editora.codeditora AS CodEditora, 
	editora.nome AS NomeEditora  
FROM livro 
JOIN autor 
ON livro.autor = autor.codautor 
JOIN editora 
ON livro.editora = editora.codeditora 
ORDER BY valor 
DESC LIMIT 10
```

## Exercício 2

Exportar o resultado da query que obtém as 5 editoras com maior quantidade de livros na biblioteca para um arquivo CSV
Utilizar | como separador
Respeitar a sequência de colunas
```
SELECT 
	editora.codeditora AS CodEditora,
	editora.nome AS NomeEditora,
	COUNT(livro.editora) AS QuantidadeLivros
FROM livro
JOIN editora 
ON livro.editora = editora.codeditora
GROUP BY NomeEditora
LIMIT 5
```
