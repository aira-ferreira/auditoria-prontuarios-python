# Auditoria de Prontuários Eletrônicos

Este projeto apresenta uma pipeline de auditoria de prontuários clínicos com foco na identificação de inconsistências, melhoria da qualidade dos registros e detecção de padrões atípicos em dados de atendimento.

O fluxo do projeto inclui:

- Tratamento e padronização dos dados
- Aplicação de regras de auditoria
- Automação da validação com Power Query e Python
- Análise e visualização dos resultados em Power BI

O objetivo é demonstrar como técnicas de análise de dados podem apoiar processos de auditoria assistencial, governança de dados e melhoria da qualidade dos registros clínicos.

---

# 🔎 Tratamento e Validação no Power Query

Antes da automação em Python, os dados passaram por um processo de tratamento e validação no Power Query, com foco em padronização, qualidade dos dados e aplicação inicial das regras de auditoria.

As principais etapas realizadas foram:

- Importação e organização da base de atendimentos
- Padronização dos tipos de dados (datas, textos e campos categóricos)
- Normalização de textos para evitar inconsistências de escrita
- Verificação de campos obrigatórios e identificação de preenchimento incompleto
- Aplicação de regras de auditoria relacionadas à presença, sucesso no contato e evolução do atendimento
- Identificação de registros duplicados e inconsistentes
- Geração de colunas auxiliares para apoio à auditoria

Arquivo com as etapas realizadas no Power Query:

[Base tratada no Power Query](base_auditoria_power_query.xlsx)

---

# 📋 Regras de Auditoria Aplicadas

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

Essas regras simulam verificações realizadas em auditorias de qualidade de prontuários clínicos.

---

# ⚙️ Automação da Auditoria em Python

Após o tratamento inicial no Power Query, foi desenvolvido um script em Python para automatizar a auditoria dos atendimentos.

O script executa as seguintes etapas:

- Leitura da base tratada em Excel
- Padronização e validação adicional de campos
- Aplicação automática de todas as regras de auditoria definidas
- Identificação e marcação dos registros com inconsistências
- Geração de colunas de erro e motivo da auditoria
- Exportação da base final auditada em Excel

O objetivo da automação é garantir:

- Reprodutibilidade
- Escalabilidade
- Padronização do processo de auditoria

Isso reduz significativamente a necessidade de validações manuais.

Script utilizado:

[Script de auditoria em Python](python/auditoria_prontuarios.py)

---

# 📊 Dashboard de Auditoria

Após a execução das regras de auditoria, os dados foram analisados em um dashboard desenvolvido no Power BI.

O dashboard permite acompanhar indicadores importantes da qualidade dos prontuários, como:

- Total de atendimentos auditados
- Total de registros com erro
- Taxa de erro
- Score de gravidade dos erros
- Ranking de profissionais com maior incidência de inconsistências
- Evolução temporal dos erros
- Distribuição dos tipos de erro

Planilha final com os dados auditados:

[Base final auditada](atendimento_auditoria_auditado.xlsx)

Dashboard utilizado na análise: 

![Uploading Dashboard - portifólio.png…]()


---

# 🧠 Insights da Auditoria

A análise exploratória da base auditada permitiu identificar padrões relevantes relacionados à qualidade do preenchimento dos prontuários.

## 1. Concentração de erros por profissional

Foi possível identificar que determinados profissionais apresentam maior incidência de inconsistências nos registros clínicos.

Esse comportamento pode indicar:

- Necessidade de treinamento sobre preenchimento de prontuários
- Falta de padronização na escrita da evolução clínica
- Sobrecarga de atendimentos

---

## 2. Tipos de erro mais frequentes

A classificação dos erros revelou que alguns tipos de inconsistência ocorrem com maior frequência, como:

- Erros de presença
- Evoluções clínicas insuficientes ou inconsistentes
- Registros duplicados
- CPF associado a pacientes diferentes

---

## 3. Evolução clínica com baixa qualidade textual

Um número relevante de registros apresentou evoluções com menos de 50 caracteres.

Esse comportamento pode indicar:

- Registros clínicos superficiais
- Falta de detalhamento do atendimento
- Possível preenchimento automático ou padronizado

---

## 4. Possíveis indícios de inconsistência ou fraude

A auditoria também identificou situações que podem indicar comportamento atípico nos registros, como:

- Evoluções idênticas para pacientes diferentes
- Mesma evolução utilizada em múltiplos atendimentos
- CPF associado a mais de um paciente

---

## 5. Tendência temporal dos erros

A análise temporal mostrou variação no volume de erros ao longo dos meses auditados.

Essa análise permite monitorar melhorias no processo de registro clínico.

---

# 🏥 Potenciais Aplicações

Este projeto pode ser utilizado em ambientes de saúde para:

- Monitoramento de qualidade de prontuários eletrônicos
- Identificação de inconsistências em registros clínicos
- Apoio a processos de auditoria assistencial
- Detecção de padrões atípicos em dados clínicos
- Apoio à governança e qualidade de dados em saúde

---

# 🛠 Tecnologias Utilizadas

- Power Query
- Python
- Pandas
- Excel
- Power BI

---

# 📁 Estrutura do Projeto

```text
auditoria_prontuarios
│
├ data
│
├ prints_power_query
│
├ python
│   └ auditoria_prontuarios.py
│
├ prints_dashboard
│
└ README.md

---

Observação:
Este repositório não inclui dados reais por motivos de privacidade e conformidade com a LGPD.
