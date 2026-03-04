# Ouvidoria - Python
Sistema de Ouvidoria em Python com MySQL Este repositório contém um sistema de Ouvidoria desenvolvido para facilitar a gestão de manifestações (sugestões, reclamações ou elogios) de usuários. O projeto utiliza a linguagem Python integrada a um banco de dados relacional (MySQL) para garantir que as informações sejam armazenadas de forma persistente e segura. 

🎯 Objetivo do Projeto: O principal objetivo deste projeto é oferecer uma interface de linha de comando (CLI) simples e eficiente onde um administrador ou atendente possa gerenciar o ciclo de vida de manifestações enviadas por clientes. Ele resolve o problema de organização de feedbacks, substituindo anotações manuais por um registro digital estruturado.

🛠️ Tecnologias Utilizadas:
📌 Python 3: Linguagem principal para a lógica do sistema.  
📌 MySQL: Banco de dados relacional para armazenamento dos dados. 
📌 mysql-connector-python: Biblioteca para realizar a ponte entre o código Python e o banco de dados.
📌 Conceitos de Programação: Modularização (divisão do código em diferentes arquivos), tratamento de exceções e uso de prepared statements para segurança contra ataques de SQL Injection.

🚀 Funcionalidades Principais

O sistema é operado através de um menu interativo com as seguintes opções: 
📌 Listagem de Manifestações: Exibe todas as mensagens cadastradas no banco de dados.
📌 Pesquisa por Código: Localiza rapidamente uma manifestação específica através de seu ID único. 
📌 Adicionar Nova Manifestação: Permite a inserção de novos feedbacks diretamente no sistema.  
📌 Contador de Registros: Exibe a quantidade total de manifestações armazenadas até o momento.
📌 Remoção de Manifestação: Exclui registros do banco de dados utilizando o código de identificação.

📂 Estrutura do Código
O projeto está dividido em três módulos para facilitar a manutenção: 
📌 Menu.py: O ponto de entrada do programa. Gerencia a interface com o usuário e o fluxo do menu.  
📌 Ouvidoria.py: Contém as regras de negócio e a lógica das funções (listar, adicionar, remover).  
📌 operacoesbd.py: Módulo genérico de infraestrutura que lida diretamente com os comandos SQL (Conexão, Select, Insert, Delete).
