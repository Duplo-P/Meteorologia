import tkinter as tk
import requests as rq 

janela = tk.Tk()
janela.title("Informações Meteorológica")
janela.geometry("600x400")
janela.resizable( False, False)
fontes = ("verdana", 12)

#Funções
def pegar_dados(cidade: str):
    chave_API = "58f5d3f893621ea2078657cd523e52bb"
    lang = "pt"
    ls = [lbl_resutado_1,lbl_resutado_2,lbl_pressao_1,lbl_vento_1]
    texto = "Dados Não Encontrado"

    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_API}&units=metric&lang={lang} "
        resposta = rq.get(url)
        for i in ls:
            i["fg"] = "green"
        dados = resposta.json()
        lbl_resutado_1["text"] = f'{dados["main"]["temp"]} ̣CELSO'
        lbl_resutado_2["text"] = f'{dados["main"]["humidity"]}%'
        lbl_pressao_1["text"] = f'{dados["main"]["pressure"]} Pa'
        lbl_vento_1["text"] = f'{dados["wind"]["speed"]} m/s'
  

    except:
        for i in ls:
            i["fg"] = "red"
            i["text"] = texto




lb_principal = tk.Label(janela,font = ("verdana", 20, "bold"), text = "NOTIFICAÇÃO")
lb_principal.pack(pady = 30)

lb_info = tk.Label(janela, text = "Insira aqui o nome da Cidade:")
lb_info.pack()

en_cidade = tk.Entry(janela, width = 50)
en_cidade.pack()

    
btb_buscar = tk.Button(janela,bg = "pink", fg = "green", font = ("verdana", 14, "bold"),command = lambda: pegar_dados(en_cidade.get()), text = "BUSCAR")
btb_buscar.pack(pady = 20)

frm_1 = tk.Frame(janela)
#Temperatura
lbl_temperatura = tk.Label(frm_1, font =fontes, text = "Temperatura")
lbl_temperatura.grid(row = 0, column = 0)
lbl_resutado_1 = tk.Label(frm_1)
lbl_resutado_1.grid(row = 1, column = 0  )

#Velocidade do vento
lbl_vento = tk.Label(frm_1,font =fontes, text = "Velocidade do Vento")
lbl_vento.grid(row = 2, column = 0)
lbl_vento_1 = tk.Label(frm_1)
lbl_vento_1.grid(row = 3, column = 0)

#Umidade
lbl_umidade = tk.Label(frm_1,font =fontes, text = "Humidade")
lbl_umidade.grid(row = 0, column = 1, padx = 20)
lbl_resutado_2 = tk.Label(frm_1)
lbl_resutado_2.grid(row = 1, column = 1, padx = 20 )

#Umidade
lbl_pressao = tk.Label(frm_1,font =fontes, text = "Pressão")
lbl_pressao.grid(row = 2, column = 1, padx = 20)
lbl_pressao_1 = tk.Label(frm_1)
lbl_pressao_1.grid(row = 3, column = 1, padx = 20 )

frm_1.pack()



janela.mainloop()