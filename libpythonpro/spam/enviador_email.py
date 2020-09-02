class Enviador:

    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalido(f'O Email do remetente é inválido: {remetente}')
        return remetente


class EmailInvalido(Exception):
    pass