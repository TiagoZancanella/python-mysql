drop database if exists super_empresa;
create database super_empresa;
use super_empresa;

create table produtos(
    id int primary key auto_increment,
    nome varchar(50)
);


create table clientes(
    id int primary key auto_increment,
    nome varchar(50),
    cpf varchar(14)
);



CREATE TABLE fornecedor (
    id INT PRIMARY KEY AUTO_INCREMENT,
    razao_social VARCHAR(50),
    cnpj VARCHAR(18),
    nome_fantasia VARCHAR(50),
    valor_faturado DECIMAL(15,2),
    quantidade_colaboradores INT
);