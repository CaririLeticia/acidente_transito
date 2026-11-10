from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
RAW = RAIZ / "data" / "raw"
PROCESSED = RAIZ / "data" / "processed"
FIGURAS = RAIZ / "figuras"

ARQ_BRUTO = PROCESSED / "01_bruto.parquet"
ARQ_LIMPO = PROCESSED / "02_limpo.parquet"

# caixa aproximada de Fortaleza, usada pra descartar coordenada errada
LAT_MIN, LAT_MAX = -4.00, -3.68
LON_MIN, LON_MAX = -38.70, -38.40

DIAS_SEMANA = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
VEICULOS = ["AUTOMOVEL", "ONIBUS", "BICICLETA", "CAMINHAO", "MICROONIBUS",
            "CICLOMOTOR", "MOTOCICLETA", "TRACAOANIMAL", "TREM"]
