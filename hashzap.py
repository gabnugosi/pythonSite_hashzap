# Título: Hashzap
# Botão de iniciar chat
    # popup (janela na frente da tela)
    # Título: Bem vindo ao Hashzap
    # Campo de texto -> Escreva seu nome no chat
    #  Botão: Entrar no chat
        # Sumir com o título Hashzap
        # Sumir botão 'Iniciar chat'
        # Fechar a janela (popup)
        # Carregar o chat 
            # As mensagens que já foram enviadas
            # Campo: Digite sua mensagem
            # Botão de Enviar
# pip install flet 

import flet as ft

#criar a função principal do seu aplicativo 
def main(pagina):
    #criar todas as funcionalidades
    def entrar_chat(evento):
        pagina.remove(titulo_pagina)
        pagina.remove(botao_iniciar)
        popup_solicitacao_informacoes.open = False
        pagina.add(corpo_chat)
        pagina.add(linha_mensagem)
        mensagem = f'{campo_nome_usuario.value} entrou no chat'
        pagina.pubsub.send_all(mensagem)
        pagina.update()

    def iniciar_chat(evento):
        pagina.dialog = popup_solicitacao_informacoes
        popup_solicitacao_informacoes.open = True
        pagina.update()

    def enviar_mensagem(evento):       
        texto_mensagem = campo_mensagem.value
        nome_usuario = campo_nome_usuario.value
        mensagem = f'{nome_usuario}: {texto_mensagem}'
        pagina.pubsub.send_all(mensagem)
        campo_mensagem.value = ''
        pagina.update()

    def enviar_mensagem_tunel(mensagem):
        texto_chat = ft.Text(mensagem)
        corpo_chat.controls.append(texto_chat)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    # cria o elemento
    titulo_pagina = ft.Text('Hashzap')
    titulo_popup = ft.Text('Bem vindo ao Hashzap')
    campo_nome_usuario = ft.TextField(label='Escreva seu nome no chat')
    corpo_chat = ft.Column()
    campo_mensagem = ft.TextField(label='Digite sua mensagem') 
    
    botao_enviar_mensagem = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)
    
    linha_mensagem=ft.Row([campo_mensagem,botao_enviar_mensagem])
    
    botao_entrar_chat = ft.ElevatedButton('Entrar no chat', on_click=entrar_chat)
    popup_solicitacao_informacoes = ft.AlertDialog(title=titulo_popup,content=campo_nome_usuario,actions=[botao_entrar_chat])
    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=iniciar_chat)
    
    # adiciona o elemento na página
    pagina.add(titulo_pagina)
    pagina.add(botao_iniciar)

# rodar o aplicativo
ft.app(main, view=ft.WEB_BROWSER)