import pyautogui
import time

# sua lista
acoes = [
    "A1UT34", "ABEV3", "ALZR11", "B1AM34", "B1SA34", "B5MB11", "BBFI11", "BBRC11",
    "BCWV39", "BDIF11", "BIDB11", "BIXC39", "BLPX39", "BOEF39", "BRCR11", "BRIM11",
    "BTRA11", "C1BL34", "C2RW34", "CBAV3", "CCME11", "CGAS3", "CLIN11", "CSAN3",
    "CXAG11", "DASA3", "DAYM11", "E1DU34", "E1QR34", "EALT3", "EGIE3", "EUCA4",
    "FAMB11", "FIGS11", "G1AR34", "G1DS34", "GMAT3", "HGCR11", "HSAF11", "IBMB34",
    "ICRI11", "KNIP11", "L1KQ34", "LVBI11", "LWSA3", "MCRE11", "MYPK3", "NCRI11",
    "O1KT34", "PABY11", "PACL11", "PETR3", "PETR4", "PGCO34", "PMAM3", "PPEI11",
    "PQAG11", "PTNT4", "RBRD11", "RBRL11", "RBRP11", "RECV3", "RNEW3", "RNEW4",
    "RNGO11", "SMRE11", "SNFF11", "T1AM34", "TOTS3", "TPIS3", "USIM3", "VCRI11",
    "VVCR11", "XPML11"
]

print("O script vai clicar em (129,162) para cada item da lista.")
print("Posicione o cursor e pressione Ctrl+C para parar a qualquer momento.\n")

time.sleep(3)  # tempo para você se preparar

for acao in acoes:
    input(f"Digite algo e pressione Enter para clicar para {acao}...")
    pyautogui.click(129, 162)
