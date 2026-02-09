import pandas as pd
import unicodedata
import os

# =====================================================
# LOCALIZAÇÃO ROBUSTA DO ARQUIVO
# =====================================================

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

POSSIVEIS_CAMINHOS = [
    SCRIPT_DIR,
    os.path.dirname(SCRIPT_DIR),
    os.path.dirname(os.path.dirname(SCRIPT_DIR))
]

ARQ_ENTRADA = None

for pasta in POSSIVEIS_CAMINHOS:
    candidato = os.path.join(pasta, "atendimentos_auditoria.xlsx")
    if os.path.exists(candidato):
        ARQ_ENTRADA = candidato
        break

if ARQ_ENTRADA is None:
    raise FileNotFoundError(
        "❌ Arquivo 'atendimentos_auditoria.xlsx' não encontrado."
    )

ARQ_SAIDA = os.path.join(
    os.path.dirname(ARQ_ENTRADA),
    "atendimento_auditoria_auditado.xlsx"
)

print("\n==============================")
print("🔍 INÍCIO DA AUDITORIA")
print("==============================")
print(f"📂 Arquivo: {ARQ_ENTRADA}\n")

# =====================================================
# FUNÇÕES AUXILIARES
# =====================================================

def normalizar_texto(texto):
    if pd.isna(texto):
        return None
    texto = str(texto).strip().lower()
    texto = unicodedata.normalize("NFKD", texto)
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    return texto

def erro(condicao):
    return "Erro" if condicao else "OK"

# =====================================================
# LEITURA DO EXCEL
# =====================================================

df = pd.read_excel(ARQ_ENTRADA)
print(f"📄 Total de registros analisados: {len(df)}")

# =====================================================
# NORMALIZAÇÕES
# =====================================================

df["cpf"] = df["cpf"].astype(str).str.replace(r"\D", "", regex=True)

df["nome_norm"]     = df["nome"].apply(normalizar_texto)
df["presenca_norm"] = df["presenca"].apply(normalizar_texto)
df["sucesso_norm"]  = df["sucesso_contato"].apply(normalizar_texto)
df["status_norm"]   = df["status"].apply(normalizar_texto)

df["evolucao_limpa"] = df["evolucao"].apply(normalizar_texto)
df["evolucao_qtd"]   = df["evolucao"].fillna("").astype(str).str.len()

df["data_criacao"]     = pd.to_datetime(df["data_criacao"], errors="coerce")
df["data_atendimento"] = pd.to_datetime(df["data_atendimento"], errors="coerce")

# =====================================================
# REGRAS DE AUDITORIA
# =====================================================

print("\n📋 APLICANDO REGRAS DE AUDITORIA...\n")

df["erro_evolucao_curta"] = (
    (df["evolucao"].notna()) & (df["evolucao_qtd"] < 50)
).apply(erro)

df["erro_sucesso_sim_faltou"] = (
    (df["sucesso_norm"] == "sim") &
    (df["presenca_norm"] == "faltou")
).apply(erro)

df["erro_sucesso_nao_compareceu"] = (
    (df["sucesso_norm"] == "nao") &
    (df["presenca_norm"] == "compareceu")
).apply(erro)

df["erro_data"] = (
    df["data_criacao"] > df["data_atendimento"]
).apply(erro)

campos_obrigatorios = [
    "data_atendimento",
    "nome",
    "cpf",
    "presenca",
    "sucesso_contato",
    "evolucao"
]

df["erro_campo_obrigatorio_vazio"] = (
    df[campos_obrigatorios].isna().any(axis=1)
).apply(erro)

cpf_nome = df.groupby("cpf")["nome_norm"].nunique()
cpf_invalidos = cpf_nome[cpf_nome > 1].index
df["erro_cpf_duplicado"] = df["cpf"].isin(cpf_invalidos).apply(erro)

evo_cpf = (
    df[df["evolucao_limpa"].notna()]
    .groupby("evolucao_limpa")["cpf"]
    .nunique()
)
evo_invalidas = evo_cpf[evo_cpf > 1].index
df["erro_evolucao_igual_pacientes_diferentes"] = (
    df["evolucao_limpa"].isin(evo_invalidas)
).apply(erro)

df["erro_evolucao_duplicada"] = (
    df.groupby(
        ["nome_norm", "cpf", "evolucao_limpa", "data_atendimento"]
    ).transform("size") > 1
).apply(erro)

df["erro_presenca_em_branco"] = df["presenca"].isna().apply(erro)
df["erro_sucesso_em_branco"]  = df["sucesso_contato"].isna().apply(erro)

df["erro_sucesso_incoerente"] = (
    ((df["presenca_norm"] == "faltou") & (df["sucesso_norm"] == "sim")) |
    ((df["presenca_norm"] == "compareceu") & (df["sucesso_norm"] == "nao"))
).apply(erro)

if "encaminhamento" in df.columns:
    df["erro_status_inativo_sem_encaminhamento"] = (
        (df["status_norm"] == "inativo") &
        (df["encaminhamento"].isna())
    ).apply(erro)
else:
    df["erro_status_inativo_sem_encaminhamento"] = "OK"

# =====================================================
# AUDITORIA DETALHADA NO CONSOLE
# =====================================================

colunas_erro = [c for c in df.columns if c.startswith("erro_")]

print("\n🔎 AUDITORIA DETALHADA POR REGRA:")
for col in colunas_erro:
    qtd = (df[col] == "Erro").sum()
    print(f" - {col}: {qtd}")

df["possui_erro"] = df[colunas_erro].eq("Erro").any(axis=1)

total_erros = df["possui_erro"].sum()

print("\n==============================")
print("📊 RESUMO FINAL DA AUDITORIA")
print("==============================")
print(f"❌ Registros com erro : {total_erros}")
print(f"✅ Registros OK       : {len(df) - total_erros}")

# =====================================================
# EXPORTAÇÃO
# =====================================================

df.to_excel(ARQ_SAIDA, index=False)

print("\n📁 Arquivo exportado:")
print(ARQ_SAIDA)
print("\n==============================")
print("✅ FIM DA AUDITORIA")
print("==============================")

