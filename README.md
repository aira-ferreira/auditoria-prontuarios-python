Auditoria Automatizada de Prontuários Clínicos

Este projeto implementa um pipeline completa de tratamento, validação e auditoria automatizada de registros clínicos, combinando Power Query (ETL estrutural) e Python (motor de validação de regras de negócio).

O objetivo é garantir integridade, conformidade e prevenção de inconsistências que impactam faturamento e qualidade assistencial.

Problema de Negócio

Empresas de saúde mental frequentemente enfrentam:

Inconsistências no preenchimento de prontuários

Registros duplicados

Falhas na classificação de presença

Evoluções padronizadas indevidamente

Erros que impactam faturamento e a qualidade.

O processo manual é lento, sujeito a erro humano e difícil de escalar.

Este projeto automatiza a auditoria e reduz drasticamente o tempo de verificação.

Arquitetura do Pipeline

Base bruta (Excel)
   
Power Query (Tratamento estrutural e padronização)
            
Base tratada
            
Base auditada com flags de erro
            
Dashboard analítico (próxima etapa)

Python (tratamento e análise automatizados)
              
Base auditada com flag de erros

Etapa - Tratamento e Validação Estrutural (Power Query)

Antes da aplicação das regras de auditoria, os dados passam por um processo de higienização estrutural no Power Query.

O arquivo base_auditoria_power_query.xlsx, disponível neste repositório, contém todas as etapas documentadas e pode ser aberto para visualização completa do processo.

Transformações realizadas:
- Padronização de Tipos

Conversão correta de datas

Ajuste de campos numéricos

Tratamento de textos inconsistentes

- Normalização Textual

Padronização de maiúsculas/minúsculas

Remoção de espaços extras

Correção de inconsistências que poderiam gerar falsos duplicados

- Qualidade de Dados

Identificação de campos obrigatórios vazios

Remoção de registros estruturalmente inválidos

Verificação de CPFs com formatação incorreta


Etapa em Python

A segunda etapa transforma regras de negócio em validações automatizadas de alta performance utilizando Python + Pandas.

O script processa grandes volumes de dados em segundos e gera diagnóstico detalhado por registro.

Regras de Auditoria Aplicadas

O projeto implementa 13 regras críticas organizadas por categoria:

Consistência Logística

Sucesso no contato "Sim" com presença "Faltou"

Sucesso no contato "Não" com presença "Compareceu"

Atendimento lançado retroativamente (Data Criação > Data Atendimento)

Status inativo sem encaminhamento adequado

Evolução com menos de 50 caracteres

Evolução idêntica para pacientes diferentes

Evolução idêntica para o mesmo paciente em dias diferentes

Evolução diferente para o mesmo paciente no mesmo dia

Integridade Cadastral

CPF igual associado a nomes diferentes

Duplicidade por combinação CPF + Data + Evolução

Campos obrigatórios vazios

Coerência de Classificação


⚙ Diferenciais Técnicos

-Processamento vetorizado com Pandas (alta performance)

- Uso de Regex para identificação semântica de padrões textuais

- Normalização de texto antes das validações

- Centralização das regras em único script

- Auditoria detalhada por linha

- Log no console com resumo dos erros encontrados

- Exportação automática da base auditada



Estrutura do Repositório
auditoria_prontuarios_python
│
├── base_auditoria_power_query.xlsx
├── atendimentos_auditoria.xlsx
├── auditoria_script.py
├── auditoria_resultado_detalhado.xlsx
└── README.md

Stack Utilizada

Excel

Power Query

Python

Pandas

Regex

Git / GitHub


Resultados

Redução significativa do tempo de auditoria manual

Padronização das validações

Rastreabilidade por regra violada

Base pronta para construção de dashboard gerencial

Próxima Etapa

Implementação de dashboard analítico para:

Identificar padrões recorrentes de erro
Monitorar evolução da qualidade do preenchimento ao longo do tempo

Observação

Os arquivos base_auditoria_power_query e atendimento_auditoria_auditado disponibilizados no repositório permite visualizar todo o processo de transformação estrutural aplicado em Power Query e Python.
