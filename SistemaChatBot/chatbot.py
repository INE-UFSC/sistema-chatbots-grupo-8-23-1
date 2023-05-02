class SistemaChatBot:
    def __init__(self, lista_bots):
        self.__lista_bots = lista_bots
        self.__bot: Bot = None

    def escolhe_bot(self):
        print("Escolha um Bot: (1) Feliz, (2) Triste, (3) Zangado")
        bot_num = int(input())
        self.__bot = self.__lista_bots[bot_num-1]
        self.mostra_comandos_bot()

    def mostra_comandos_bot(self):
        self.__bot.mostra_comandos()
    def le_envia_comando(self, comando):
        self.__bot.executa_comando(comando)

    def inicio(self):
        self.escolhe_bot()
        comando = int(input("Coloque aqui o comando\n"))
        while comando != -1:
            self.mostra_comandos_bot()
            self.le_envia_comando(comando)
            if comando == 3:self.escolhe_bot()
            comando = int(input("Coloque aqui o comando"))


class Bot:
    def __init__(self, nome, comandos):
        self.__nome = nome
        self.comandos = comandos

    def executa_comando(self, comando: int):
        if comando == 1:
            self.apresentacao()
        elif comando == 2:
            self.boas_vindas()
        elif comando == 3:
            self.despedida()
        else:
            self.executa_gen(comando)

    def executa_gen(self, valor):
        result = self.comandos[valor]
        self.generic_speech(result)

    def apresentacao(self, string):
        self.generic_speech(string)

    def boas_vindas(self, string):
        self.generic_speech(string)

    def despedida(self, string):
        self.generic_speech(string)

    def generic_speech(self, string):
        print(f"{self.__nome}: {string}")
        
    def mostra_comandos(self):
        print("1) Introducao\n2)Boas Vindas\n3)Despedida")
        for n, commands in self.comandos:
            print("{}")


class BotFeliz(Bot):
    def __init__(self, comandos):
        super().__init__("Feliz", comandos)

    def apresentacao(self):
        super().apresentacao("Eu sou um Yoda Feliz")

    def boas_vindas(self):
        super().boas_vindas("Sou Feliz")

    def despedida(self):
        super().despedida("Tchau!!!")


class BotTriste(Bot):
    def __init__(self, comandos):
        super().__init__("Triste", comandos)

    def apresentacao(self):
        super().apresentacao("Eu sou um Yoda Bad Vibes")

    def boas_vindas(self):
        super().boas_vindas("Sou manso")

    def despedida(self):
        super().despedida("Tchau triste!!!")


class BotZangado(Bot):
    def __init__(self, comandos):
        super().__init__("Zangado", comandos)

    def apresentacao(self):
        super().apresentacao("Ok")

    def boas_vindas(self):
        super().boas_vindas("Sua mãe precisa de receita pra fazer gelo")

    def despedida(self):
        super().despedida("Passas-te da data de validade")


def main():
    novo = SistemaChatBot([BotFeliz({}), BotTriste({}), BotZangado({})])
    novo.inicio()


if __name__ == "__main__":
    main()
