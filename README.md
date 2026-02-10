
 **Auditoria de Prontuários**

Script em Python para auditar registros de atendimentos com regras como:
- evolução < 50 caracteres
- incoerência entre presença e sucesso no contato
- CPF duplicado para nomes diferentes
- evolução igual entre pacientes diferentes
- campos obrigatórios vazios
- status inativo sem encaminhamento 
- evolução duplicada para o mesmo paciente

 Como usar
1. Coloque o arquivo `atendimentos_auditoria.xlsx` na mesma pasta do script.
2. Abra o arquivo em Python e rode
3. O arquivo de saída será gerado como: atendimento_auditoria_auditado.xlsx

** Observação: este repositório não inclui dados reais por privacidade (LGPD)**

