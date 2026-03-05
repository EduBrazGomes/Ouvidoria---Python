📣 Sistema de Ouvidoria - Python & MySQL
Este repositório contém um sistema de Ouvidoria desenvolvido para facilitar a gestão de manifestações (sugestões, reclamações ou elogios) de usuários. O projeto utiliza a linguagem Python integrada ao banco de dados MySQL para garantir o armazenamento persistente e seguro das informações.

🎯 Objetivo do Projeto
Oferecer uma interface de linha de comando (CLI) simples e eficiente para que administradores possam gerenciar o ciclo de vida de manifestações. O sistema resolve o problema de organização de feedbacks, substituindo processos manuais por um registro digital estruturado e seguro.

🛠️ Tecnologias Utilizadas
Python 3: Linguagem principal para a lógica do sistema.

MySQL: Banco de dados relacional para persistência de dados.

mysql-connector-python: Driver para conexão entre Python e MySQL.

🧠 Conceitos Aplicados
Modularização: Código organizado em diferentes arquivos/módulos.

Tratamento de Exceções: Robustez no manuseio de erros de conexão.

Segurança: Uso de prepared statements para prevenir ataques de SQL Injection.

🚀 Funcionalidades Principais
O sistema opera através de um menu interativo com as seguintes operações:

📌 Listagem de Manifestações: Exibe todas as mensagens cadastradas no banco de dados.

📌 Pesquisa por Código: Localiza rapidamente uma manifestação específica através de seu ID único.

📌 Adicionar Nova Manifestação: Insere novos feedbacks diretamente no sistema.

📌 Contador de Registros: Exibe a quantidade total de manifestações armazenadas.

📌 Remoção de Manifestação: Exclui registros utilizando o código de identificação.

