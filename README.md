# Auditoria de Prontuários

## Tratamento e Validação no Power Query

Antes da automação em Python, os dados passaram por um processo de tratamento e validação no Power Query, com foco em padronização, qualidade dos dados e aplicação inicial das regras de auditoria.

As principais etapas realizadas foram:

- Importação e organização da base de atendimentos
- Padronização dos tipos de dados (datas, textos e campos categóricos)
- Normalização de textos para evitar inconsistências de escrita
- Verificação de campos obrigatórios e identificação de preenchimento incompleto
- Aplicação de regras de auditoria relacionadas à presença, sucesso no contato e evolução do atendimento
- Identificação de registros duplicados e inconsistentes
- Geração de colunas auxiliares para apoio à auditoria

Os prints das etapas realizadas no Power Query estão disponíveis na pasta `prints_power_query`.

---

## Regras de Auditoria Aplicadas

O processo de auditoria de prontuários utiliza regras para validação de consistência, qualidade do preenchimento e identificação de possíveis falhas nos registros.

As regras aplicadas são:

1. Evolução com menos de 50 caracteres  
2. Sucesso no contato = "Sim" e presença = "Faltou"  
3. Sucesso no contato = "Não" e presença = "Compareceu"  
4. Atendimento lançado posteriormente (data de criação maior que a data de atendimento)  
5. Linha em branco (campos obrigatórios não preenchidos)  
6. CPF igual associado a pacientes diferentes  
7. Evolução idêntica para pacientes diferentes  
8. Evolução diferente para o mesmo paciente no mesmo dia  
9. Registro duplicado (mesmo CPF, mesma data de atendimento e mesma evolução)  
10. Presença não preenchida  
11. Sucesso no contato não preenchido  
12. Evolução preenchida com presença não preenchida  
13. Registro com status inativo sem encaminhamento  

---

## Automação da Auditoria em Python

Após o tratamento inicial no Power Query, foi desenvolvido um script em Python para automatizar a auditoria dos atendimentos.

O script executa as seguintes etapas:

- Leitura da base tratada em Excel
- Padronização e validação adicional de campos
- Aplicação automática de todas as regras de auditoria definidas
- Identificação e marcação dos registros com inconsistências
- Geração de colunas de erro e motivo da auditoria
- Exportação da base final auditada em Excel

O objetivo da automação é garantir reprodutibilidade, escalabilidade e padronização do processo de auditoria, reduzindo a necessidade de validações manuais.

---

## Como usar

1. Coloque o arquivo `atendimentos_auditoria.xlsx` na mesma pasta do script.
2. Abra o script em Python e execute.
3. O arquivo de saída será gerado como `atendimento_auditoria_auditado.xlsx`.

---

**Observação:** este repositório não inclui dados reais por motivos de privacidade e conformidade com a LGPD.


