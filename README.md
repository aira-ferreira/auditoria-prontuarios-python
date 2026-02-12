Auditoria de Prontuários: Tratamento e Automação

Este projeto apresenta um fluxo completo de tratamento de dados e auditoria automatizada para registros de atendimentos, combinando a agilidade do Power Query para ETL e a robustez do Python para validações complexas.

Etapa 1: Tratamento e Validação (Power Query)
Antes da automação, os dados brutos passam por um processo de higienização no Power Query. O foco aqui é a integridade estrutural da base.

As etapas documentadas no arquivo base_auditoria_power_query incluem:

Padronização de Tipos: Ajuste de datas, textos e campos numéricos.

Normalização Textual: Tratamento de cases e remoção de espaços extras para evitar duplicidade por erro de digitação.

Qualidade de Dados: Identificação de campos obrigatórios vazios e remoção de registros inconsistentes.


Nota: Para visualizar o passo a passo detalhado da transformação, abra o editor do Power Query no arquivo Excel disponibilizado.


Regras de Auditoria Aplicadas

A inteligência do projeto reside na aplicação de 13 regras críticas para garantir a conformidade dos prontuários:

Categoria	Regras de Validação
Consistência Logística	
• Sucesso no contato "Sim" com presença "Faltou"

• Sucesso no contato "Não" com presença "Compareceu"

• Atendimento lançado retroativamente (Data Criação > Data Atendimento)

Qualidade da Escrita	
• Evoluções com menos de 50 caracteres

• Evoluções idênticas para pacientes diferentes

• Evoluções diferentes para o mesmo paciente no mesmo dia

Integridade de Cadastro	
• CPF igual associado a nomes diferentes

Automação da Auditoria com Python

Nesta etapa, o Python é utilizado para transformar as regras de negócio em um motor de auditoria de alta performance, garantindo que grandes volumes de dados sejam verificados em segundos.

Diferenciais da Implementação
Vetorização de Dados: Utilização da biblioteca pandas para aplicar regras de validação em blocos, garantindo maior velocidade em comparação a loops tradicionais.

Centralização da Lógica: Todas as 13 regras de auditoria são processadas em um único script, facilitando manutenções futuras.

Rastreabilidade: O script gera um diagnóstico detalhado por linha, permitindo que a equipe operacional identifique exatamente qual regra foi violada.

Nota: Para visualizar do resultado, abra a planilha disponibilizada atendimento_auditoria_auditado.


Próxima etapa será incluir o Dashboard para visualização dos resultados encontrados.
